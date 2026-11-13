"""
Minimal client for the datos.gov.co (Socrata) API.

Public datasets need no user or password: that is what kept the old code from connecting. An app
token only raises the rate limit; it is read from the environment variable SOCRATA_APP_TOKEN or from
config.json -> api -> app_token, and the client works without it.

Aggregations (count, avg, group by) run on the server, so a query returns one row per municipality
and year instead of millions of individual records.
"""
import json
import os
import time
from pathlib import Path

import pandas as pd
import requests

DOMAIN = "https://www.datos.gov.co"
PAGE_SIZE = 50000


def app_token(config_file: str = "config.json"):
    token = os.environ.get("SOCRATA_APP_TOKEN")
    if token:
        return token
    path = Path(config_file)
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8")).get("api", {}).get("app_token") or None
        except (ValueError, AttributeError):
            return None
    return None


def _metadata(dataset: str) -> dict:
    response = requests.get(f"{DOMAIN}/api/views/{dataset}.json", timeout=120)
    response.raise_for_status()
    return response.json()


def dataset_description(dataset: str) -> str:
    return _metadata(dataset).get("description") or ""


def dataset_columns(dataset: str) -> list:
    return [c["fieldName"] for c in _metadata(dataset).get("columns", [])]


def query(dataset: str, select: str, where: str = None, group: str = None, order: str = None,
          token: str = None, retries: int = 3) -> pd.DataFrame:
    """
    Runs a SoQL query against a dataset and returns every page as one DataFrame.

    `order` is required for stable paging; when absent it defaults to `group`.
    """
    params = {"$select": select, "$limit": PAGE_SIZE}
    if where:
        params["$where"] = where
    if group:
        params["$group"] = group
    order = order or group
    if order:
        params["$order"] = order
    headers = {"X-App-Token": token} if token else {}

    rows, offset = [], 0
    while True:
        params["$offset"] = offset
        for attempt in range(retries):
            response = requests.get(f"{DOMAIN}/resource/{dataset}.json", params=params, headers=headers, timeout=300)
            if response.status_code == 200:
                break
            if response.status_code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(f"{dataset}: HTTP {response.status_code}: {response.text[:300]}")
        page = response.json()
        rows.extend(page)
        if len(page) < PAGE_SIZE:
            return pd.DataFrame(rows)
        offset += PAGE_SIZE
