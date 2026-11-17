"""
Violence index by the Human Development Index method (UNDP): each component is normalised between
fixed goalposts and the components are combined with a geometric mean.

- Goalposts are fixed over the whole panel, so a value means the same in every year: the lower
  goalpost is 0 and the upper one is the 99th percentile of the rate, so one tiny municipality with an
  extreme year does not compress everybody else. Values above it are capped at 1.
- A geometric mean is not defined with a zero component, and many municipalities have zero cases of
  something in a year. As UNDP does with zero values in the Gender Inequality Index, components are
  floored at a small minimum (0.001) before the mean.

Higher = more violence.
"""
import numpy as np
import pandas as pd

FLOOR = 0.001


def goalposts(panel: pd.DataFrame, components: list, quantile: float = 0.99) -> dict:
    return {c: float(panel[c].quantile(quantile)) for c in components}


def dimension_index(panel: pd.DataFrame, components: list, upper: dict) -> pd.Series:
    normalised = pd.DataFrame({
        c: (panel[c] / upper[c]).clip(lower=0, upper=1) if upper[c] > 0 else 0.0 for c in components
    }, index=panel.index)
    complete = normalised.notna().all(axis=1)
    index = np.exp(np.log(normalised.clip(lower=FLOOR)).mean(axis=1))
    return index.where(complete)
