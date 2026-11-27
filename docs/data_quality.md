# Data quality

Written by `python -m panel.quality` from `RelationsAndConclusions.DataQualityFlags`; the rules of each source
are at the top of `panel/quality.py`. Nothing in the source tables is changed.

| Kind | Meaning | What to do with the value |
|---|---|---|
| error | a value the measure does not allow | leave it out |
| missing | no value, for a known reason | nothing to use |
| inconsistent | the source contradicts itself | use with the note in mind |
| break | a jump between years larger than the thing can make | do not read it as change |
| small_base | atypical only because few people stand behind it | use the smoothed value (`SmoothedValues`) |
| extreme | atypical after weighing its base: a real case | keep it |

## DANE

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| Census2018Municipal | dep_child_labour | 0 | 0 | 0 | 0 | 0 | 1 |
| Census2018Municipal | dep_critical_overcrowding | 0 | 0 | 0 | 0 | 0 | 3 |
| Census2018Municipal | dep_dependency_rate | 0 | 0 | 0 | 0 | 0 | 6 |
| Census2018Municipal | dep_early_childhood_care_barriers | 0 | 0 | 0 | 0 | 0 | 8 |
| Census2018Municipal | dep_health_access_barriers | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | dep_illiteracy | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | dep_inadequate_excreta_disposal | 0 | 0 | 0 | 0 | 0 | 8 |
| Census2018Municipal | dep_informal_work | 0 | 0 | 0 | 0 | 0 | 5 |
| Census2018Municipal | dep_low_educational_attainment | 0 | 0 | 0 | 0 | 0 | 5 |
| Census2018Municipal | dep_no_health_insurance | 0 | 0 | 0 | 0 | 0 | 13 |
| Census2018Municipal | dep_no_improved_water | 0 | 0 | 0 | 0 | 0 | 9 |
| Census2018Municipal | dep_school_non_attendance | 0 | 0 | 0 | 0 | 0 | 1 |
| Census2018Municipal | dwellings_occupied | 0 | 0 | 25 | 0 | 0 | 2 |
| Census2018Municipal | ipm | 0 | 0 | 0 | 0 | 0 | 4 |
| Census2018Municipal | ipm_vs_nbi | 0 | 0 | 0 | 0 | 0 | 3 |
| Census2018Municipal | nbi | 0 | 0 | 0 | 0 | 0 | 18 |
| Census2018Municipal | nbi_economic_dependency | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | nbi_misery | 0 | 0 | 0 | 0 | 0 | 14 |
| Census2018Municipal | nbi_overcrowding | 0 | 0 | 0 | 0 | 0 | 3 |
| Census2018Municipal | nbi_school_non_attendance | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | nbi_services | 0 | 0 | 0 | 0 | 0 | 18 |
| Census2018Municipal | share_electricity | 0 | 0 | 14 | 0 | 0 | 10 |
| Census2018Municipal | share_garbage | 0 | 0 | 0 | 0 | 0 | 13 |
| Census2018Municipal | share_gas | 0 | 0 | 0 | 0 | 0 | 30 |
| Census2018Municipal | share_internet | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | share_no_electricity_service | 0 | 0 | 0 | 0 | 0 | 12 |
| Census2018Municipal | share_sewer | 0 | 0 | 0 | 0 | 0 | 44 |
| Census2018Municipal | share_stratum | 0 | 138 | 0 | 0 | 0 | 0 |
| Census2018Municipal | share_stratum_1 | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | share_stratum_1_2 | 0 | 0 | 0 | 0 | 0 | 6 |
| Census2018Municipal | share_stratum_2 | 0 | 0 | 0 | 0 | 0 | 17 |
| Census2018Municipal | share_stratum_3 | 0 | 0 | 0 | 0 | 0 | 156 |
| Census2018Municipal | share_stratum_4 | 0 | 0 | 0 | 0 | 0 | 54 |
| Census2018Municipal | share_water | 0 | 0 | 0 | 0 | 0 | 12 |
| MunicipalLineage | mother_id | 0 | 36 | 0 | 0 | 0 | 0 |
| Population | population | 0 | 241 | 0 | 44 | 0 | 0 |

**Census2018Municipal.dep_child_labour**

- extreme (1 municipalities): Pacoa (ANM) (Vaupés) [1].

**Census2018Municipal.dep_critical_overcrowding**

- extreme (3 municipalities): La Pedrera (ANM) (Amazonas) [1], La Victoria (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1].

**Census2018Municipal.dep_dependency_rate**

- extreme (6 municipalities): Sucre (Cauca) [1], Alto Baudó (Chocó) [1], Providencia (Nariño) [1], Pacoa (ANM) (Vaupés) [1], Taraira (Vaupés) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.dep_early_childhood_care_barriers**

- extreme (8 municipalities): Guapi (Cauca) [1], López de Micay (Cauca) [1], Alto Baudó (Chocó) [1], Bagadó (Chocó) [1], El Litoral del San Juan (Chocó) [1], Manaure (La Guajira) [1], Taraira (Vaupés) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.dep_health_access_barriers**

- extreme (2 municipalities): Usiacurí (Atlántico) [1], Papunahua (ANM) (Vaupés) [1].

**Census2018Municipal.dep_illiteracy**

- extreme (2 municipalities): San Juanito (Meta) [1], California (Santander) [1].

**Census2018Municipal.dep_inadequate_excreta_disposal**

- extreme (8 municipalities): San Jacinto (Bolívar) [1], Santa Rosa (Bolívar) [1], Soplaviento (Bolívar) [1], Zambrano (Bolívar) [1], Uribia (La Guajira) [1], Mosquera (Nariño) [1], Olaya Herrera (Nariño) [1], Santa Bárbara (Nariño) [1].

**Census2018Municipal.dep_informal_work**

- extreme (5 municipalities): Magüí (Nariño) [1], La Victoria (ANM) (Amazonas) [1], Puerto Alegría (ANM) (Amazonas) [1], Barrancominas (Guainía) [1], La Guadalupe (ANM) (Guainía) [1].

**Census2018Municipal.dep_low_educational_attainment**

- extreme (5 municipalities): Chíquiza (Boyacá) [1], El Paso (Cesar) [1], Restrepo (Meta) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1], Puerto Carreño (Vichada) [1].

**Census2018Municipal.dep_no_health_insurance**

- extreme (13 municipalities): Alto Baudó (Chocó) [1], Manaure (La Guajira) [1], Guaitarilla (Nariño) [1], Gualmatán (Nariño) [1], Iles (Nariño) [1], La Cruz (Nariño) [1], Mosquera (Nariño) [1], Ospina (Nariño) [1], Providencia (Nariño) [1], Samaniego (Nariño) [1], San Pedro de Cartago (Nariño) [1], Pacoa (ANM) (Vaupés) [1] and 1 more.

**Census2018Municipal.dep_no_improved_water**

- extreme (9 municipalities): Clemencia (Bolívar) [1], San Jacinto (Bolívar) [1], Santa Catalina (Bolívar) [1], Istmina (Chocó) [1], La Tola (Nariño) [1], Mosquera (Nariño) [1], Olaya Herrera (Nariño) [1], Potosí (Nariño) [1], Puerto Asís (Putumayo) [1].

**Census2018Municipal.dep_school_non_attendance**

- extreme (1 municipalities): María La Baja (Bolívar) [1].

**Census2018Municipal.dwellings_occupied**

- inconsistent (25 municipalities): Tuchín (Córdoba) [1], Puerto Nariño (Amazonas) [1], Yavaraté (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Morichal (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Barrancominas (Guainía) [1] and 13 more.
- extreme (2 municipalities): Bogotá, D.C. (Bogotá, D.C.) [1], Pacoa (ANM) (Vaupés) [1].

**Census2018Municipal.ipm**

- extreme (4 municipalities): Alto Baudó (Chocó) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.ipm_vs_nbi**

- extreme (3 municipalities): San Jacinto (Bolívar), 2018: IPM 60.3 against NBI 93.4; NBI's largest component: services; Quibdó (Chocó), 2018: IPM 44.4 against NBI 72.8; NBI's largest component: services; Istmina (Chocó), 2018: IPM 55.1 against NBI 84.0; NBI's largest component: services.

**Census2018Municipal.nbi**

- extreme (18 municipalities): Arboletes (Antioquia) [1], San Pedro de Urabá (Antioquia) [1], Olaya Herrera (Nariño) [1], Mosquera (Nariño) [1], La Tola (Nariño) [1], Uribia (La Guajira) [1], Manaure (La Guajira) [1], Lloró (Chocó) [1], Istmina (Chocó) [1], Quibdó (Chocó) [1], Tuchín (Córdoba) [1], San Andrés Sotavento (Córdoba) [1] and 6 more.

**Census2018Municipal.nbi_economic_dependency**

- extreme (2 municipalities): San Juanito (Meta) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1].

**Census2018Municipal.nbi_misery**

- extreme (14 municipalities): Turbo (Antioquia) [1], Arjona (Bolívar) [1], Clemencia (Bolívar) [1], Santa Rosa (Bolívar) [1], Turbaná (Bolívar) [1], Villanueva (Bolívar) [1], Quibdó (Chocó) [1], Riohacha (La Guajira) [1], Maicao (La Guajira) [1], Ciénaga (Magdalena) [1], La Pedrera (ANM) (Amazonas) [1], La Victoria (ANM) (Amazonas) [1] and 2 more.

**Census2018Municipal.nbi_overcrowding**

- extreme (3 municipalities): Maicao (La Guajira) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1].

**Census2018Municipal.nbi_school_non_attendance**

- extreme (2 municipalities): María La Baja (Bolívar) [1], La Victoria (ANM) (Amazonas) [1].

**Census2018Municipal.nbi_services**

- extreme (18 municipalities): San Juan de Urabá (Antioquia) [1], San Pedro de Urabá (Antioquia) [1], Unión Panamericana (Chocó) [1], Quibdó (Chocó) [1], Tierralta (Córdoba) [1], Moñitos (Córdoba) [1], Villanueva (Bolívar) [1], Turbaná (Bolívar) [1], Soplaviento (Bolívar) [1], Santa Rosa (Bolívar) [1], Santa Catalina (Bolívar) [1], San Juan Nepomuceno (Bolívar) [1] and 6 more.

**Census2018Municipal.share_electricity**

- inconsistent (14 municipalities): Frontino (Antioquia) [1], Milán (Caquetá) [1], Solano (Caquetá) [1], Pueblo Bello (Cesar) [1], Alto Baudó (Chocó) [1], Bagadó (Chocó) [1], Juradó (Chocó) [1], Lloró (Chocó) [1], Puerto Gaitán (Meta) [1], Puerto Santander (ANM) (Amazonas) [1], La Guadalupe (ANM) (Guainía) [1], Mitú (Vaupés) [1] and 2 more.
- extreme (10 municipalities): Medio Atrato (Chocó) [1], Sipí (Chocó) [1], Riohacha (La Guajira) [1], Maicao (La Guajira) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], Mosquera (Nariño) [1], San Andrés de Tumaco (Nariño) [1], Puerto Asís (Putumayo) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.share_garbage**

- extreme (13 municipalities): Altos del Rosario (Bolívar) [1], Barranco de Loba (Bolívar) [1], Cicuco (Bolívar) [1], Clemencia (Bolívar) [1], Margarita (Bolívar) [1], Pinillos (Bolívar) [1], San Fernando (Bolívar) [1], San Martín de Loba (Bolívar) [1], Chíquiza (Boyacá) [1], Uribia (La Guajira) [1], Pedraza (Magdalena) [1], Zapayán (Magdalena) [1] and 1 more.

**Census2018Municipal.share_gas**

- extreme (30 municipalities): Monguí (Boyacá) [1], Muzo (Boyacá) [1], Valle del Guamuez (Putumayo) [1], Saravena (Arauca) [1], Argelia (Valle Del Cauca) [1], Ragonvalia (Norte De Santander) [1], San Andrés de Tumaco (Nariño) [1], San Pedro de Cartago (Nariño) [1], San Pablo (Nariño) [1], San Bernardo (Nariño) [1], Sandoná (Nariño) [1], Samaniego (Nariño) [1] and 18 more.

**Census2018Municipal.share_internet**

- extreme (2 municipalities): Usiacurí (Atlántico) [1], Pacoa (ANM) (Vaupés) [1].

**Census2018Municipal.share_no_electricity_service**

- extreme (12 municipalities): Medio Atrato (Chocó) [1], Sipí (Chocó) [1], Riohacha (La Guajira) [1], Maicao (La Guajira) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], San Andrés de Tumaco (Nariño) [1], Buenaventura (Valle Del Cauca) [1], Puerto Asís (Putumayo) [1], Barrancominas (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.share_sewer**

- extreme (44 municipalities): Vigía del Fuerte (Antioquia) [1], Juan de Acosta (Atlántico) [1], Puerto Escondido (Córdoba) [1], San Carlos (Córdoba) [1], Medio Atrato (Chocó) [1], Medio Baudó (Chocó) [1], Algarrobo (Magdalena) [1], Cerro de San Antonio (Magdalena) [1], Puebloviejo (Magdalena) [1], Remolino (Magdalena) [1], Sitionuevo (Magdalena) [1], Zapayán (Magdalena) [1] and 32 more.

**Census2018Municipal.share_stratum**

- missing (138 municipalities): Murindó (Antioquia) [1], Nunchía (Casanare) [1], El Carmen (Norte De Santander) [1], Sardinata (Norte De Santander) [1], Tibú (Norte De Santander) [1], Cravo Norte (Arauca) [1], Chámeza (Casanare) [1], Hato Corozal (Casanare) [1], Orocué (Casanare) [1], Puerto Leguízamo (Putumayo) [1], Recetor (Casanare) [1], Sácama (Casanare) [1] and 126 more.

**Census2018Municipal.share_stratum_1**

- extreme (2 municipalities): Sipí (Chocó) [1], Herrán (Norte De Santander) [1].

**Census2018Municipal.share_stratum_1_2**

- extreme (6 municipalities): Murindó (Antioquia) [1], Medio Atrato (Chocó) [1], Sipí (Chocó) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.share_stratum_2**

- extreme (17 municipalities): Clemencia (Bolívar) [1], Concordia (Magdalena) [1], La Pedrera (ANM) (Amazonas) [1], Palmito (Sucre) [1], El Roble (Sucre) [1], San Andrés de Tumaco (Nariño) [1], Zona Bananera (Magdalena) [1], El Retén (Magdalena) [1], Tuchín (Córdoba) [1], Regidor (Bolívar) [1], Moñitos (Córdoba) [1], Villa Rica (Cauca) [1] and 5 more.

**Census2018Municipal.share_stratum_3**

- extreme (156 municipalities): Abejorral (Antioquia) [1], San Martín (Meta) [1], Barrancas (La Guajira) [1], San Juan del Cesar (La Guajira) [1], Castilla la Nueva (Meta) [1], Cumaral (Meta) [1], Fuente de Oro (Meta) [1], Guamal (Meta) [1], Restrepo (Meta) [1], Bochalema (Norte De Santander) [1], Yaguará (Huila) [1], Convención (Norte De Santander) [1] and 144 more.

**Census2018Municipal.share_stratum_4**

- extreme (54 municipalities): Santafé de Antioquia (Antioquia) [1], Belén de Umbría (Risaralda) [1], Ricaurte (Cundinamarca) [1], Tenjo (Cundinamarca) [1], Palermo (Huila) [1], Rivera (Huila) [1], Albania (La Guajira) [1], Acacías (Meta) [1], Puerto López (Meta) [1], Restrepo (Meta) [1], San Martín (Meta) [1], Chinácota (Norte De Santander) [1] and 42 more.

**Census2018Municipal.share_water**

- extreme (12 municipalities): Clemencia (Bolívar) [1], Norosí (Bolívar) [1], San Jacinto (Bolívar) [1], Santa Catalina (Bolívar) [1], Istmina (Chocó) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], La Tola (Nariño) [1], Magüí (Nariño) [1], Mosquera (Nariño) [1], Potosí (Nariño) [1], San Miguel (Putumayo) [1].

**MunicipalLineage.mother_id**

- missing (36 municipalities): Arenal (Bolívar) [1], Clemencia (Bolívar) [1], Unión Panamericana (Chocó) [1], Dibulla (La Guajira) [1], Distracción (La Guajira) [1], La Jagua del Pilar (La Guajira) [1], Algarrobo (Magdalena) [1], Concordia (Magdalena) [1], El Retén (Magdalena) [1], Nueva Granada (Magdalena) [1], Pijiño del Carmen (Magdalena) [1], Sabanas de San Ángel (Magdalena) [1] and 24 more.

**Population.population**

- missing (56 municipalities): Mapiripana (ANM) (Guainía) [23], Norosí (Bolívar) [13], Tuchín (Córdoba) [13], San José de Uré (Córdoba) [13], Guachené (Cauca) [12], Coveñas (Sucre) [7], Medio San Juan (Chocó) [6], Nuevo Belén de Bajirá (Chocó) [6], Río Iró (Chocó) [6], Carmen del Darién (Chocó) [6], Nueva Granada (Magdalena) [5], Cértegui (Chocó) [5] and 44 more.
- break (37 municipalities): Río Quito (Chocó) [3], Istmina (Chocó) [2], Carmen del Darién (Chocó) [2], Río Viejo (Bolívar) [2], Santa Ana (Magdalena) [2], Medio Atrato (Chocó) [2], Ciénaga (Magdalena) [1], Riosucio (Chocó) [1], Tadó (Chocó) [1], Aracataca (Magdalena) [1], Cerro de San Antonio (Magdalena) [1], Santa Bárbara (Antioquia) [1] and 25 more.

## DNP

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| MunicipalIndicators | 010010011 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalIndicators | 020050024 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 020100038 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 020100039 | 0 | 0 | 102 | 0 | 0 | 0 |
| MunicipalIndicators | 030010045 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalIndicators | 040040003 | 0 | 0 | 0 | 122 | 0 | 0 |
| MunicipalIndicators | 050010005 | 0 | 0 | 0 | 15 | 0 | 0 |
| MunicipalIndicators | 050020001 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 050020003 | 0 | 0 | 0 | 10 | 0 | 0 |
| MunicipalIndicators | 050020012 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 050020013 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 050020014 | 0 | 0 | 0 | 18 | 0 | 0 |
| MunicipalIndicators | 050020015 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 050020016 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 050020017 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 050020022 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 050020023 | 0 | 0 | 0 | 21 | 0 | 0 |
| MunicipalIndicators | 050020027 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 050020028 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 050020029 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 050020033 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 050020034 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 050020035 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 050020041 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 050020043 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 050020063 | 0 | 0 | 0 | 443 | 0 | 0 |
| MunicipalIndicators | 050020075 | 0 | 0 | 0 | 38 | 0 | 0 |
| MunicipalIndicators | 060010001 | 0 | 0 | 0 | 185 | 0 | 0 |
| MunicipalIndicators | 060010002 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 060010003 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 060010006 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 060010007 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 060010008 | 0 | 0 | 0 | 159 | 0 | 0 |
| MunicipalIndicators | 060010009 | 0 | 0 | 0 | 14 | 0 | 0 |
| MunicipalIndicators | 060010010 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 060010011 | 0 | 0 | 0 | 243 | 0 | 0 |
| MunicipalIndicators | 060010012 | 0 | 0 | 0 | 32 | 0 | 0 |
| MunicipalIndicators | 060010013 | 0 | 0 | 0 | 44 | 0 | 0 |
| MunicipalIndicators | 060010014 | 0 | 0 | 0 | 49 | 0 | 0 |
| MunicipalIndicators | 060010015 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 060010016 | 0 | 0 | 0 | 31 | 0 | 0 |
| MunicipalIndicators | 060010017 | 0 | 0 | 0 | 63 | 0 | 0 |
| MunicipalIndicators | 060010018 | 0 | 0 | 0 | 7 | 0 | 0 |
| MunicipalIndicators | 060010026 | 0 | 0 | 1,643 | 0 | 0 | 0 |
| MunicipalIndicators | 060020001 | 0 | 0 | 0 | 190 | 0 | 0 |
| MunicipalIndicators | 060020012 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 060020013 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 060020014 | 0 | 0 | 0 | 9 | 0 | 0 |
| MunicipalIndicators | 060020015 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 060020016 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 060020017 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 060020020 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 060020021 | 0 | 0 | 0 | 48 | 0 | 0 |
| MunicipalIndicators | 060020022 | 0 | 0 | 0 | 32 | 0 | 0 |
| MunicipalIndicators | 060020026 | 0 | 0 | 0 | 79 | 0 | 0 |
| MunicipalIndicators | 070040001 | 0 | 0 | 0 | 18 | 0 | 0 |
| MunicipalIndicators | 070040004 | 0 | 0 | 0 | 11 | 0 | 0 |
| MunicipalIndicators | 070050002 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 070050003 | 0 | 0 | 0 | 24 | 0 | 0 |
| MunicipalIndicators | 070050004 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 070050005 | 0 | 0 | 0 | 12 | 0 | 0 |
| MunicipalIndicators | 070100001 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 070100002 | 0 | 0 | 0 | 118 | 0 | 0 |
| MunicipalIndicators | 070100004 | 0 | 0 | 0 | 26 | 0 | 0 |
| MunicipalIndicators | 070100006 | 0 | 0 | 0 | 52 | 0 | 0 |
| MunicipalIndicators | 070120020 | 1 | 0 | 0 | 0 | 0 | 0 |
| MunicipalIndicators | 070130003 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalIndicators | 070130004 | 26 | 0 | 0 | 0 | 0 | 0 |
| MunicipalIndicators | 070130005 | 756 | 0 | 13 | 0 | 0 | 0 |
| MunicipalIndicators | 070130007 | 0 | 0 | 4,584 | 0 | 0 | 0 |
| MunicipalIndicators | 070130008 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalIndicators | 070130010 | 0 | 0 | 0 | 22 | 0 | 0 |
| MunicipalIndicators | 070130011 | 0 | 0 | 72 | 0 | 0 | 0 |
| MunicipalIndicators | 070150002 | 0 | 0 | 0 | 19 | 0 | 0 |
| MunicipalIndicators | 070150003 | 0 | 0 | 0 | 18 | 0 | 0 |
| MunicipalIndicators | 080010003 | 0 | 0 | 0 | 41 | 0 | 0 |
| MunicipalIndicators | 080010006 | 0 | 0 | 0 | 13 | 0 | 0 |
| MunicipalIndicators | 080010009 | 0 | 0 | 0 | 52 | 0 | 0 |
| MunicipalIndicators | 080010011 | 0 | 0 | 0 | 11 | 0 | 0 |
| MunicipalIndicators | 080010012 | 0 | 0 | 0 | 82 | 0 | 0 |
| MunicipalIndicators | 080010013 | 0 | 0 | 0 | 14 | 0 | 0 |
| MunicipalIndicators | 080020001 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 080020002 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 080020004 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 080030003 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 110010005 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 110030003 | 0 | 0 | 0 | 252 | 0 | 0 |
| MunicipalIndicators | 110070003 | 0 | 0 | 0 | 17 | 0 | 0 |
| MunicipalIndicators | 110070005 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 110070008 | 0 | 0 | 0 | 19 | 0 | 0 |
| MunicipalIndicators | 110070010 | 0 | 0 | 0 | 593 | 0 | 0 |
| MunicipalIndicators | 120210003 | 0 | 0 | 3,240 | 0 | 0 | 0 |
| MunicipalIndicators | 120220001 | 0 | 0 | 0 | 30 | 0 | 0 |
| MunicipalIndicators | 120220002 | 0 | 0 | 0 | 31 | 0 | 0 |
| MunicipalIndicators | 120220003 | 0 | 0 | 0 | 27 | 0 | 0 |
| MunicipalIndicators | 120220004 | 0 | 0 | 0 | 30 | 0 | 0 |
| MunicipalIndicators | 120240001 | 0 | 0 | 0 | 22 | 0 | 0 |
| MunicipalIndicators | 120240002 | 0 | 0 | 0 | 36 | 0 | 0 |
| MunicipalIndicators | 120240003 | 0 | 0 | 0 | 21 | 0 | 0 |
| MunicipalIndicators | 120240004 | 0 | 0 | 0 | 19 | 0 | 0 |
| MunicipalIndicators | 120260003 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260005 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260006 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260014 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260022 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 120260028 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260034 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260035 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 120260036 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 120260040 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260043 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260044 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260046 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260060 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260062 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 120260066 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260068 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260070 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 120260073 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260081 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 120260083 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 120260085 | 0 | 0 | 0 | 7 | 0 | 0 |
| MunicipalIndicators | 120260086 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260089 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 120260090 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260093 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260094 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260095 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260097 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 120260100 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260107 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 120260109 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260114 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260115 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260117 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260118 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260119 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260122 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260131 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260132 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260140 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 120260141 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 120260144 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 120260148 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 120290002 | 0 | 0 | 0 | 69 | 0 | 0 |
| MunicipalIndicators | 120290003 | 0 | 0 | 0 | 254 | 0 | 0 |
| MunicipalIndicators | 120290005 | 0 | 0 | 0 | 134 | 0 | 0 |
| MunicipalIndicators | 120290006 | 0 | 0 | 0 | 720 | 0 | 0 |
| MunicipalIndicators | 120290008 | 0 | 0 | 0 | 164 | 0 | 0 |
| MunicipalIndicators | 120290009 | 0 | 0 | 0 | 967 | 0 | 0 |
| MunicipalIndicators | 120290011 | 0 | 0 | 0 | 182 | 0 | 0 |
| MunicipalIndicators | 120290012 | 0 | 0 | 0 | 1,004 | 0 | 0 |
| MunicipalIndicators | 120290014 | 0 | 0 | 0 | 234 | 0 | 0 |
| MunicipalIndicators | 120290015 | 0 | 0 | 0 | 888 | 0 | 0 |
| MunicipalIndicators | 120300001 | 0 | 0 | 0 | 7 | 0 | 0 |
| MunicipalIndicators | 120300002 | 0 | 0 | 0 | 167 | 0 | 0 |
| MunicipalIndicators | 120300007 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 150030004 | 13 | 0 | 0 | 0 | 0 | 0 |
| MunicipalIndicators | 150040004 | 13 | 0 | 0 | 0 | 0 | 0 |
| MunicipalIndicators | 150070003 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 160040001 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 160040006 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 160040007 | 0 | 0 | 0 | 29 | 0 | 0 |
| MunicipalIndicators | 160060002 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010001 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 190010008 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010011 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 190010012 | 0 | 0 | 0 | 7 | 0 | 0 |
| MunicipalIndicators | 190010013 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010014 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010015 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 190010016 | 0 | 0 | 0 | 10 | 0 | 0 |
| MunicipalIndicators | 190010018 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010022 | 0 | 0 | 0 | 15 | 0 | 0 |
| MunicipalIndicators | 190010023 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 190010026 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 190010027 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010029 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 190010032 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010033 | 0 | 0 | 0 | 4 | 0 | 0 |
| MunicipalIndicators | 190010034 | 0 | 0 | 0 | 8 | 0 | 0 |
| MunicipalIndicators | 190010037 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010038 | 0 | 0 | 0 | 9 | 0 | 0 |
| MunicipalIndicators | 190010041 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 190010044 | 0 | 0 | 0 | 18 | 0 | 0 |
| MunicipalIndicators | 190020001 | 0 | 0 | 0 | 47 | 0 | 0 |
| MunicipalIndicators | 190020002 | 0 | 0 | 0 | 91 | 0 | 0 |
| MunicipalIndicators | 190020003 | 0 | 0 | 0 | 113 | 0 | 0 |
| MunicipalIndicators | 190020004 | 0 | 0 | 0 | 162 | 0 | 0 |
| MunicipalIndicators | 190020005 | 0 | 0 | 0 | 132 | 0 | 0 |
| MunicipalIndicators | 190030002 | 0 | 0 | 0 | 10 | 0 | 0 |
| MunicipalIndicators | 190030003 | 0 | 0 | 0 | 8 | 0 | 0 |
| MunicipalIndicators | 190030004 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 190030005 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 200010002 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200020007 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200020008 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200020009 | 0 | 0 | 0 | 14 | 0 | 0 |
| MunicipalIndicators | 200020011 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200020013 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200020015 | 0 | 0 | 0 | 5 | 0 | 0 |
| MunicipalIndicators | 200020016 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 200020023 | 0 | 0 | 0 | 7 | 0 | 0 |
| MunicipalIndicators | 200020024 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 200030002 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 200030009 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 260020001 | 0 | 0 | 0 | 16 | 0 | 0 |
| MunicipalIndicators | 260020002 | 0 | 0 | 0 | 61 | 0 | 0 |
| MunicipalIndicators | 260020003 | 0 | 0 | 0 | 102 | 0 | 0 |
| MunicipalIndicators | 260020004 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 260020007 | 0 | 0 | 0 | 9 | 0 | 0 |
| MunicipalIndicators | 260020014 | 0 | 0 | 0 | 3 | 0 | 0 |
| MunicipalIndicators | 260030001 | 0 | 0 | 0 | 121 | 0 | 0 |
| MunicipalIndicators | 260030002 | 0 | 0 | 0 | 139 | 0 | 0 |
| MunicipalIndicators | 260030003 | 0 | 0 | 0 | 69 | 0 | 0 |
| MunicipalIndicators | 310010005 | 0 | 0 | 0 | 6 | 0 | 0 |
| MunicipalIndicators | 310010009 | 0 | 0 | 0 | 1 | 0 | 0 |
| MunicipalIndicators | 310010012 | 0 | 0 | 0 | 20 | 0 | 0 |
| MunicipalIndicators | 310010015 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 310010017 | 0 | 0 | 0 | 2 | 0 | 0 |
| MunicipalIndicators | 310010018 | 0 | 0 | 0 | 42 | 0 | 0 |
| MunicipalIndicators | 310010021 | 0 | 0 | 0 | 2 | 0 | 0 |

**MunicipalIndicators.010010011**

- inconsistent (9 municipalities): La Jagua de Ibirico (Cesar) [1], Mosquera (Cundinamarca) [1], Carmen del Darién (Chocó) [1], Nuquí (Chocó) [1], Barranca de Upía (Meta) [1], Castilla la Nueva (Meta) [1], Puerto Gaitán (Meta) [1], Taraira (Vaupés) [1], Cumaribo (Vichada) [1].

**MunicipalIndicators.020050024**

- break (2 municipalities): San José de Uré (Córdoba), 2023: 11.0 times the year before (323); Santiago (Putumayo), 2020: 0.1 times the year before (4074).

**MunicipalIndicators.020100038**

- break (5 municipalities): San Francisco (Antioquia), 2021: 11.0 times the year before (8); San Juan Nepomuceno (Bolívar), 2021: 0.0 times the year before (136); Tiquisio (Bolívar), 2021: 41.0 times the year before (2); Santander de Quilichao (Cauca), 2021: 0.0 times the year before (456); Santa Rosa (Cauca), 2021: 261.5 times the year before (2).

**MunicipalIndicators.020100039**

- inconsistent (62 municipalities): Abejorral (Antioquia) [2], Atrato (Chocó) [2], López de Micay (Cauca) [2], Beltrán (Cundinamarca) [2], Bojacá (Cundinamarca) [2], Cabrera (Cundinamarca) [2], Jerusalén (Cundinamarca) [2], Venecia (Cundinamarca) [2], Quetame (Cundinamarca) [2], Apulo (Cundinamarca) [2], San Bernardo (Cundinamarca) [2], Ubaque (Cundinamarca) [2] and 50 more.

**MunicipalIndicators.030010045**

- inconsistent (1 municipalities): Abejorral (Antioquia), 2020: percentage above 100.

**MunicipalIndicators.040040003**

- break (88 municipalities): Ipiales (Nariño) [3], Pueblo Nuevo (Córdoba) [3], Tadó (Chocó) [3], Tuluá (Valle Del Cauca) [3], Urrao (Antioquia) [3], Calamar (Bolívar) [2], Planeta Rica (Córdoba) [2], San Pelayo (Córdoba) [2], Bucaramanga (Santander) [2], Floridablanca (Santander) [2], Zona Bananera (Magdalena) [2], Quibdó (Chocó) [2] and 76 more.

**MunicipalIndicators.050010005**

- break (15 municipalities): Barranco de Loba (Bolívar) [1], San Martín de Loba (Bolívar) [1], Villanueva (Bolívar) [1], Miranda (Cauca) [1], El Paso (Cesar) [1], Puerto Escondido (Córdoba) [1], Maicao (La Guajira) [1], El Banco (Magdalena) [1], Guamal (Magdalena) [1], San Sebastián de Buenavista (Magdalena) [1], Puerto Gaitán (Meta) [1], Olaya Herrera (Nariño) [1] and 3 more.

**MunicipalIndicators.050020001**

- break (2 municipalities): Nariño (Cundinamarca), 2008: 18.1 times the year before (0.47); Palmas del Socorro (Santander), 2009: 0.1 times the year before (7.14).

**MunicipalIndicators.050020003**

- break (8 municipalities): El Litoral del San Juan (Chocó) [3], Pueblo Nuevo (Córdoba) [1], Bituima (Cundinamarca) [1], San Agustín (Huila) [1], Ricaurte (Nariño) [1], Barbosa (Santander) [1], Majagual (Sucre) [1], Rioblanco (Tolima) [1].

**MunicipalIndicators.050020012**

- break (6 municipalities): El Tambo (Cauca), 2024: 0.1 times the year before (5.24); Becerril (Cesar), 2021: 10.8 times the year before (0.81); Bajo Baudó (Chocó), 2019: 0.1 times the year before (8.76); Hatonuevo (La Guajira), 2018: 0.1 times the year before (8.41); Sabanas de San Ángel (Magdalena), 2011: 0.1 times the year before (11.07); Tauramena (Casanare), 2014: 0.1 times the year before (10.24).

**MunicipalIndicators.050020013**

- break (3 municipalities): Iza (Boyacá), 2013: 0.1 times the year before (65.09); Pachavita (Boyacá), 2011: 0.1 times the year before (54.46); Pachavita (Boyacá), 2012: 12.3 times the year before (5.1); Pachavita (Boyacá), 2013: 0.1 times the year before (62.5); San Juanito (Meta), 2006: 0.1 times the year before (63.83).

**MunicipalIndicators.050020014**

- break (18 municipalities): Puerto Triunfo (Antioquia) [1], Villanueva (Bolívar) [1], Tauramena (Casanare) [1], Bolívar (Valle Del Cauca) [1], Rioblanco (Tolima) [1], Santiago de Tolú (Sucre) [1], Socorro (Santander) [1], Simacota (Santander) [1], Barbosa (Santander) [1], Santa Bárbara (Nariño) [1], Uribe (Meta) [1], Villanueva (La Guajira) [1] and 6 more.

**MunicipalIndicators.050020015**

- break (1 municipalities): Páez (Cauca), 2009: 10.1 times the year before (23.01).

**MunicipalIndicators.050020016**

- break (1 municipalities): Leticia (Amazonas), 2013: 10.0 times the year before (20.4).

**MunicipalIndicators.050020017**

- break (1 municipalities): Pueblo Rico (Risaralda), 2013: 0.1 times the year before (682.59).

**MunicipalIndicators.050020022**

- break (17 municipalities): Chigorodó (Antioquia) [1], Tibú (Norte De Santander) [1], Villanueva (Casanare) [1], Saravena (Arauca) [1], Fortul (Arauca) [1], Pradera (Valle Del Cauca) [1], Candelaria (Valle Del Cauca) [1], Sabana de Torres (Santander) [1], Guachucal (Nariño) [1], Marinilla (Antioquia) [1], Mosquera (Cundinamarca) [1], Chía (Cundinamarca) [1] and 5 more.

**MunicipalIndicators.050020023**

- break (21 municipalities): Puerto Triunfo (Antioquia) [1], Puerto Gaitán (Meta) [1], Tame (Arauca) [1], Pradera (Valle Del Cauca) [1], Candelaria (Valle Del Cauca) [1], Sabana de Torres (Santander) [1], Tibú (Norte De Santander) [1], Túquerres (Nariño) [1], San Andrés de Tumaco (Nariño) [1], Guachucal (Nariño) [1], El Banco (Magdalena) [1], Santana (Boyacá) [1] and 9 more.

**MunicipalIndicators.050020027**

- break (3 municipalities): San Juan del Cesar (La Guajira), 2020: 0.1 times the year before (30.47); Ancuya (Nariño), 2023: 0.1 times the year before (59.13); San Gil (Santander), 2024: 0.1 times the year before (21.97).

**MunicipalIndicators.050020028**

- break (1 municipalities): Villa del Rosario (Norte De Santander), 2021: 10.3 times the year before (1.59).

**MunicipalIndicators.050020029**

- break (3 municipalities): San Pelayo (Córdoba), 2021: 11.0 times the year before (1.81); Silvania (Cundinamarca), 2019: 0.1 times the year before (56.67); Los Patios (Norte De Santander), 2023: 12.3 times the year before (2.09).

**MunicipalIndicators.050020033**

- break (17 municipalities): Concordia (Antioquia) [1], Madrid (Cundinamarca) [1], Saravena (Arauca) [1], San Luis (Tolima) [1], Marsella (Risaralda) [1], Herrán (Norte De Santander) [1], Acevedo (Huila) [1], Tocancipá (Cundinamarca) [1], Los Córdobas (Córdoba) [1], Remedios (Antioquia) [1], Cotorra (Córdoba) [1], Morales (Cauca) [1] and 5 more.

**MunicipalIndicators.050020034**

- break (16 municipalities): Ponedera (Atlántico) [2], Concordia (Antioquia) [1], Altos del Rosario (Bolívar) [1], Magangué (Bolívar) [1], Arcabuco (Boyacá) [1], Santana (Boyacá) [1], Siachoque (Boyacá) [1], Caldono (Cauca) [1], Morales (Cauca) [1], Madrid (Cundinamarca) [1], Acevedo (Huila) [1], Yaguará (Huila) [1] and 4 more.

**MunicipalIndicators.050020035**

- break (3 municipalities): Carepa (Antioquia), 2020: 12.7 times the year before (3.33); Puerto Berrío (Antioquia), 2020: 11.9 times the year before (3.98); Magangué (Bolívar), 2020: 0.1 times the year before (179.67).

**MunicipalIndicators.050020041**

- break (2 municipalities): Puerto Salgar (Cundinamarca), 2020: 0.1 times the year before (74.73); Líbano (Tolima), 2020: 11.1 times the year before (2.74).

**MunicipalIndicators.050020043**

- break (2 municipalities): Maripí (Boyacá), 2024: 0.1 times the year before (48.31); Cértegui (Chocó), 2024: 10.1 times the year before (3.76).

**MunicipalIndicators.050020063**

- break (346 municipalities): Oporapa (Huila) [4], Nimaima (Cundinamarca) [4], Vergara (Cundinamarca) [3], Toro (Valle Del Cauca) [3], San Jacinto (Bolívar) [3], Coloso (Sucre) [3], San Antonio (Tolima) [3], El Cerrito (Valle Del Cauca) [3], Ginebra (Valle Del Cauca) [3], La Celia (Risaralda) [3], Santa Rosalía (Vichada) [3], El Colegio (Cundinamarca) [2] and 334 more.

**MunicipalIndicators.050020075**

- break (35 municipalities): San Pablo (Bolívar) [2], Trinidad (Casanare) [2], Matanza (Santander) [2], Fresno (Tolima) [1], Cerrito (Santander) [1], Charta (Santander) [1], El Peñón (Santander) [1], El Playón (Santander) [1], Zapatoca (Santander) [1], Concordia (Antioquia) [1], Cepitá (Santander) [1], Aguazul (Casanare) [1] and 23 more.

**MunicipalIndicators.060010001**

- break (167 municipalities): Los Santos (Santander) [2], Fusagasugá (Cundinamarca) [2], La Dorada (Caldas) [2], Manzanares (Caldas) [2], Puerto Boyacá (Boyacá) [2], Riosucio (Caldas) [2], Magangué (Bolívar) [2], Flandes (Tolima) [2], Cali (Valle Del Cauca) [2], Soacha (Cundinamarca) [2], Dolores (Tolima) [2], Cumaral (Meta) [2] and 155 more.

**MunicipalIndicators.060010002**

- break (4 municipalities): Abriaquí (Antioquia), 2021: 0.1 times the year before (402.19); El Dorado (Meta), 2021: 11.9 times the year before (25.18); La Belleza (Santander), 2020: 0.1 times the year before (161.97); Vetas (Santander), 2020: 0.1 times the year before (513.54).

**MunicipalIndicators.060010003**

- break (3 municipalities): Piamonte (Cauca), 2022: 11.9 times the year before (10.71); Viotá (Cundinamarca), 2020: 0.1 times the year before (81.43); El Cairo (Valle Del Cauca), 2019: 10.3 times the year before (14.61).

**MunicipalIndicators.060010006**

- break (2 municipalities): Guapi (Cauca), 2019: 13.0 times the year before (7.18); El Tarra (Norte De Santander), 2019: 0.1 times the year before (131.41).

**MunicipalIndicators.060010007**

- break (2 municipalities): San Pedro de Urabá (Antioquia), 2019: 0.1 times the year before (65.08); Mapiripán (Meta), 2019: 0.1 times the year before (220.46).

**MunicipalIndicators.060010008**

- break (131 municipalities): La Palma (Cundinamarca) [3], Gámeza (Boyacá) [2], Anzá (Antioquia) [2], Puracé (Cauca) [2], Anapoima (Cundinamarca) [2], Cáqueza (Cundinamarca) [2], Une (Cundinamarca) [2], Soracá (Boyacá) [2], El Colegio (Cundinamarca) [2], San Luis de Gaceno (Boyacá) [2], Saboyá (Boyacá) [2], Quípama (Boyacá) [2] and 119 more.

**MunicipalIndicators.060010009**

- break (13 municipalities): Algeciras (Huila) [2], Yolombó (Antioquia) [1], Argelia (Cauca) [1], Curumaní (Cesar) [1], San Diego (Cesar) [1], Villeta (Cundinamarca) [1], Riohacha (La Guajira) [1], Acacías (Meta) [1], Dagua (Valle Del Cauca) [1], Arauquita (Arauca) [1], Saravena (Arauca) [1], Tame (Arauca) [1] and 1 more.

**MunicipalIndicators.060010010**

- break (16 municipalities): Concordia (Antioquia) [2], Sogamoso (Boyacá) [1], Buenos Aires (Cauca) [1], Guaduas (Cundinamarca) [1], Riohacha (La Guajira) [1], Aracataca (Magdalena) [1], Villavicencio (Meta) [1], Fuente de Oro (Meta) [1], Granada (Meta) [1], Santa Rosa de Cabal (Risaralda) [1], Chaparral (Tolima) [1], Guamo (Tolima) [1] and 4 more.

**MunicipalIndicators.060010011**

- break (190 municipalities): Beltrán (Cundinamarca) [2], Fusagasugá (Cundinamarca) [2], La Vega (Cundinamarca) [2], Lebrija (Santander) [2], Piedecuesta (Santander) [2], Guaduas (Cundinamarca) [2], Granada (Cundinamarca) [2], Girardot (Cundinamarca) [2], Fúquene (Cundinamarca) [2], Natagaima (Tolima) [2], Cota (Cundinamarca) [2], Cogua (Cundinamarca) [2] and 178 more.

**MunicipalIndicators.060010012**

- break (29 municipalities): Chipaque (Cundinamarca) [2], Santa Catalina (Bolívar) [2], Urumita (La Guajira) [2], Carepa (Antioquia) [1], Guacarí (Valle Del Cauca) [1], Fresno (Tolima) [1], Barbosa (Santander) [1], La Esperanza (Norte De Santander) [1], Yacuanquer (Nariño) [1], Cumaral (Meta) [1], Fonseca (La Guajira) [1], Albania (La Guajira) [1] and 17 more.

**MunicipalIndicators.060010013**

- break (42 municipalities): Hatonuevo (La Guajira) [2], Maceo (Antioquia) [2], Betania (Antioquia) [1], Magüí (Nariño) [1], Algeciras (Huila) [1], San Agustín (Huila) [1], Tarqui (Huila) [1], Barrancas (La Guajira) [1], Mesetas (Meta) [1], La Macarena (Meta) [1], Linares (Nariño) [1], Francisco Pizarro (Nariño) [1] and 30 more.

**MunicipalIndicators.060010014**

- break (46 municipalities): Peñol (Antioquia) [3], El Dovio (Valle Del Cauca) [2], Betania (Antioquia) [1], Santa Bárbara (Nariño) [1], Algeciras (Huila) [1], Isnos (Huila) [1], Tarqui (Huila) [1], Barrancas (La Guajira) [1], Hatonuevo (La Guajira) [1], Cubarral (Meta) [1], La Macarena (Meta) [1], Magüí (Nariño) [1] and 34 more.

**MunicipalIndicators.060010015**

- break (5 municipalities): Caucasia (Antioquia), 2021: 0.1 times the year before (25.2); Copacabana (Antioquia), 2004: 0.1 times the year before (31.3); Santander de Quilichao (Cauca), 2024: 0.1 times the year before (31.6); Jamundí (Valle Del Cauca), 2013: 0.1 times the year before (13.6); Saravena (Arauca), 2022: 11.9 times the year before (3.4); Saravena (Arauca), 2023: 0.1 times the year before (40.4).

**MunicipalIndicators.060010016**

- break (26 municipalities): Amalfi (Antioquia) [2], Guapi (Cauca) [2], Vistahermosa (Meta) [2], Puerto López (Meta) [2], Valle del Guamuez (Putumayo) [2], Segovia (Antioquia) [1], El Tarra (Norte De Santander) [1], Saravena (Arauca) [1], Fortul (Arauca) [1], Arauquita (Arauca) [1], Toro (Valle Del Cauca) [1], La Victoria (Valle Del Cauca) [1] and 14 more.

**MunicipalIndicators.060010017**

- break (57 municipalities): Cubarral (Meta) [2], San Antero (Córdoba) [2], Santa Bárbara (Antioquia) [2], El Dovio (Valle Del Cauca) [2], Chaparral (Tolima) [2], Ciénaga (Magdalena) [2], Teorama (Norte De Santander) [1], Mesetas (Meta) [1], El Rosario (Nariño) [1], Linares (Nariño) [1], Pupiales (Nariño) [1], Santa Bárbara (Nariño) [1] and 45 more.

**MunicipalIndicators.060010018**

- break (6 municipalities): La Unión (Antioquia) [2], Pensilvania (Caldas) [1], La Esperanza (Norte De Santander) [1], San Gil (Santander) [1], Coyaima (Tolima) [1], Lérida (Tolima) [1].

**MunicipalIndicators.060010026**

- inconsistent (598 municipalities): Leticia (Amazonas) [14], Gachantivá (Boyacá) [12], San José del Guaviare (Guaviare) [11], Chaparral (Tolima) [10], Cimitarra (Santander) [9], Acevedo (Huila) [9], Cuítiva (Boyacá) [9], Iza (Boyacá) [9], Landázuri (Santander) [8], Chitaraque (Boyacá) [8], Barranca de Upía (Meta) [8], Cabuyaro (Meta) [8] and 586 more.

**MunicipalIndicators.060020001**

- break (164 municipalities): San José de La Montaña (Antioquia) [3], Potosí (Nariño) [2], Icononzo (Tolima) [2], Boavita (Boyacá) [2], Susacón (Boyacá) [2], El Playón (Santander) [2], Timbío (Cauca) [2], Salento (Quindío) [2], Chimá (Córdoba) [2], Caloto (Cauca) [2], Natagaima (Tolima) [2], Anolaima (Cundinamarca) [2] and 152 more.

**MunicipalIndicators.060020012**

- break (2 municipalities): San Pedro de Los Milagros (Antioquia), 2019: 10.8 times the year before (38.01); Paz de Ariporo (Casanare), 2021: 10.0 times the year before (25.33).

**MunicipalIndicators.060020013**

- break (3 municipalities): Remedios (Antioquia), 2020: 0.1 times the year before (368.06); La Argentina (Huila), 2020: 0.1 times the year before (744.88); Orocué (Casanare), 2019: 0.0 times the year before (1269.04).

**MunicipalIndicators.060020014**

- break (9 municipalities): Girardota (Antioquia) [1], Salgar (Antioquia) [1], Ráquira (Boyacá) [1], Puerto Salgar (Cundinamarca) [1], Mogotes (Santander) [1], Suaita (Santander) [1], Ovejas (Sucre) [1], Carmen de Apicalá (Tolima) [1], Hato Corozal (Casanare) [1].

**MunicipalIndicators.060020015**

- break (1 municipalities): Pradera (Valle Del Cauca), 2019: 14.8 times the year before (18.44).

**MunicipalIndicators.060020016**

- break (6 municipalities): Sahagún (Córdoba), 2020: 0.1 times the year before (102.74); Zipaquirá (Cundinamarca), 2020: 0.1 times the year before (97.18); La Virginia (Risaralda), 2020: 0.1 times the year before (783.29); Honda (Tolima), 2019: 11.9 times the year before (44.07); Melgar (Tolima), 2020: 0.1 times the year before (327.28); Fortul (Arauca), 2021: 0.1 times the year before (394.01).

**MunicipalIndicators.060020017**

- break (1 municipalities): Tello (Huila), 2019: 10.6 times the year before (56.24).

**MunicipalIndicators.060020020**

- break (4 municipalities): Anapoima (Cundinamarca), 2020: 12.4 times the year before (75.93); Piedecuesta (Santander), 2020: 0.1 times the year before (138.2); San Gil (Santander), 2020: 0.1 times the year before (300.12); Corozal (Sucre), 2020: 0.1 times the year before (154.2).

**MunicipalIndicators.060020021**

- break (44 municipalities): Guadalajara de Buga (Valle Del Cauca) [2], Ortega (Tolima) [2], Villamaría (Caldas) [2], Dosquebradas (Risaralda) [2], Andes (Antioquia) [1], Barbosa (Santander) [1], El Banco (Magdalena) [1], Fuente de Oro (Meta) [1], Puerto Gaitán (Meta) [1], La Tebaida (Quindío) [1], Montenegro (Quindío) [1], La Virginia (Risaralda) [1] and 32 more.

**MunicipalIndicators.060020022**

- break (29 municipalities): San Luis (Tolima) [2], Purificación (Tolima) [2], Fonseca (La Guajira) [2], Apartadó (Antioquia) [1], Tello (Huila) [1], Zarzal (Valle Del Cauca) [1], Pradera (Valle Del Cauca) [1], Dagua (Valle Del Cauca) [1], Ambalema (Tolima) [1], Puerto Parra (Santander) [1], Santa Rosa de Cabal (Risaralda) [1], Vistahermosa (Meta) [1] and 17 more.

**MunicipalIndicators.060020026**

- break (73 municipalities): Jerusalén (Cundinamarca) [2], Rionegro (Santander) [2], Tello (Huila) [2], La Unión (Antioquia) [2], Silvia (Cauca) [2], Sandoná (Nariño) [2], Santafé de Antioquia (Antioquia) [1], El Carmen de Chucurí (Santander) [1], Aratoca (Santander) [1], Salento (Quindío) [1], Quimbaya (Quindío) [1], Circasia (Quindío) [1] and 61 more.

**MunicipalIndicators.070040001**

- break (16 municipalities): La Jagua de Ibirico (Cesar) [2], Orito (Putumayo) [2], Yondó (Antioquia) [1], El Tambo (Cauca) [1], Agustín Codazzi (Cesar) [1], Becerril (Cesar) [1], Los Córdobas (Córdoba) [1], San Antero (Córdoba) [1], San José de Uré (Córdoba) [1], Villavicencio (Meta) [1], Buesaco (Nariño) [1], Leiva (Nariño) [1] and 4 more.

**MunicipalIndicators.070040004**

- break (11 municipalities): Yondó (Antioquia) [1], Becerril (Cesar) [1], La Jagua de Ibirico (Cesar) [1], Los Córdobas (Córdoba) [1], Suaza (Huila) [1], Villavicencio (Meta) [1], Leiva (Nariño) [1], Rionegro (Santander) [1], Sabana de Torres (Santander) [1], Mocoa (Putumayo) [1], Orito (Putumayo) [1].

**MunicipalIndicators.070050002**

- break (3 municipalities): Betulia (Antioquia), 2018: 0.1 times the year before (65.42); Tutazá (Boyacá), 2018: 0.1 times the year before (97.92); Yacopí (Cundinamarca), 2018: 0.1 times the year before (86.33).

**MunicipalIndicators.070050003**

- break (24 municipalities): Puerto Triunfo (Antioquia) [1], Candelaria (Atlántico) [1], San José del Guaviare (Guaviare) [1], Puerto Caicedo (Putumayo) [1], Puerto Asís (Putumayo) [1], Ataco (Tolima) [1], Sucre (Sucre) [1], Balboa (Risaralda) [1], San José de Cúcuta (Norte De Santander) [1], El Banco (Magdalena) [1], Albania (La Guajira) [1], Villavieja (Huila) [1] and 12 more.

**MunicipalIndicators.070050004**

- break (1 municipalities): Cabrera (Cundinamarca), 2018: 0.1 times the year before (31.3).

**MunicipalIndicators.070050005**

- break (12 municipalities): Segovia (Antioquia) [1], Cabrera (Cundinamarca) [1], Nóvita (Chocó) [1], San José del Palmar (Chocó) [1], Cumbitara (Nariño) [1], Funes (Nariño) [1], Santacruz (Nariño) [1], La Belleza (Santander) [1], Palocabildo (Tolima) [1], El Dovio (Valle Del Cauca) [1], Cravo Norte (Arauca) [1], San Luis de Palenque (Casanare) [1].

**MunicipalIndicators.070100001**

- break (4 municipalities): Ebéjico (Antioquia), 2002: 10.4 times the year before (13.81); Montecristo (Bolívar), 2015: 742.6 times the year before (78.51); Montecristo (Bolívar), 2016: 0.0 times the year before (58300.34); Tiquisio (Bolívar), 2015: 17.9 times the year before (78.92); Tiquisio (Bolívar), 2016: 0.1 times the year before (1413.46); El Rosario (Nariño), 2004: 11.9 times the year before (23.85).

**MunicipalIndicators.070100002**

- break (103 municipalities): Unguía (Chocó) [3], Morroa (Sucre) [2], Cajicá (Cundinamarca) [2], Girardot (Cundinamarca) [2], La Palma (Cundinamarca) [2], San Vicente de Chucurí (Santander) [2], Puerto Boyacá (Boyacá) [2], Otanche (Boyacá) [2], Nuquí (Chocó) [2], Chimá (Córdoba) [2], Pedraza (Magdalena) [2], Puerto Gaitán (Meta) [2] and 91 more.

**MunicipalIndicators.070100004**

- break (25 municipalities): Bajo Baudó (Chocó) [2], Nariño (Antioquia) [1], Barrancas (La Guajira) [1], Trinidad (Casanare) [1], Saravena (Arauca) [1], San Luis de Sincé (Sucre) [1], San Onofre (Sucre) [1], San Marcos (Sucre) [1], San Andrés (Santander) [1], Quinchía (Risaralda) [1], Bochalema (Norte De Santander) [1], Samaniego (Nariño) [1] and 13 more.

**MunicipalIndicators.070100006**

- break (46 municipalities): El Cantón del San Pablo (Chocó) [2], Santo Domingo (Antioquia) [2], Vegachí (Antioquia) [2], Dagua (Valle Del Cauca) [2], Páez (Boyacá) [2], Montelíbano (Córdoba) [2], Leiva (Nariño) [1], Urumita (La Guajira) [1], El Retén (Magdalena) [1], Puebloviejo (Magdalena) [1], Villavicencio (Meta) [1], Cubarral (Meta) [1] and 34 more.

**MunicipalIndicators.070120020**

- error (1 municipalities): Providencia (Nariño), 2020: negative percentage; not loaded.

**MunicipalIndicators.070130003**

- inconsistent (7 municipalities): Ocaña (Norte De Santander) [4], Malambo (Atlántico) [2], Balboa (Risaralda) [2], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [2], Calamar (Bolívar) [1], Salamina (Caldas) [1], Plato (Magdalena) [1].

**MunicipalIndicators.070130004**

- error (25 municipalities): Turbo (Antioquia) [2], Caramanta (Antioquia) [1], Socotá (Boyacá) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1], San Francisco (Putumayo) [1], San Joaquín (Santander) [1], Buenavista (Quindío) [1], Zapayán (Magdalena) [1], Pedraza (Magdalena) [1], Santa Marta (Magdalena) [1], Maicao (La Guajira) [1], Alto Baudó (Chocó) [1] and 13 more.

**MunicipalIndicators.070130005**

- error (499 municipalities): San Antero (Córdoba) [5], Baranoa (Atlántico) [4], Aracataca (Magdalena) [4], Bogotá, D.C. (Bogotá, D.C.) [4], Manatí (Atlántico) [4], Turbo (Antioquia) [4], Ambalema (Tolima) [3], Alcalá (Valle Del Cauca) [3], Valparaíso (Antioquia) [3], Uramita (Antioquia) [3], Cajamarca (Tolima) [3], Tarso (Antioquia) [3] and 487 more.
- inconsistent (10 municipalities): Miraflores (Guaviare) [3], Barrancominas (Guainía) [2], Caracolí (Antioquia) [1], Cucaita (Boyacá) [1], Muzo (Boyacá) [1], Nobsa (Boyacá) [1], Tununguá (Boyacá) [1], San Pelayo (Córdoba) [1], Charta (Santander) [1], Jordán (Santander) [1].

**MunicipalIndicators.070130007**

- inconsistent (1089 municipalities): Tausa (Cundinamarca) [5], Barichara (Santander) [5], Albania (Santander) [5], Tamalameque (Cesar) [5], Buenavista (Córdoba) [5], Quinchía (Risaralda) [5], Pueblo Rico (Risaralda) [5], Mistrató (Risaralda) [5], La Celia (Risaralda) [5], La Apartada (Córdoba) [5], Los Córdobas (Córdoba) [5], Dosquebradas (Risaralda) [5] and 1077 more.

**MunicipalIndicators.070130008**

- inconsistent (4 municipalities): Cáceres (Antioquia), 2020: percentage above 100; Nimaima (Cundinamarca), 2022: percentage above 100; Buenavista (Sucre), 2021: percentage above 100; Natagaima (Tolima), 2021: percentage above 100.

**MunicipalIndicators.070130010**

- break (19 municipalities): Providencia (Nariño) [2], Pauna (Boyacá) [2], Zapayán (Magdalena) [2], Belmira (Antioquia) [1], Nariño (Cundinamarca) [1], Cucutilla (Norte De Santander) [1], Samaniego (Nariño) [1], La Tola (Nariño) [1], La Llanada (Nariño) [1], Cerro de San Antonio (Magdalena) [1], Milán (Caquetá) [1], Norosí (Bolívar) [1] and 7 more.

**MunicipalIndicators.070130011**

- inconsistent (66 municipalities): Granada (Meta) [3], Medellín (Antioquia) [2], Dagua (Valle Del Cauca) [2], La Plata (Huila) [2], Cogua (Cundinamarca) [2], El Charco (Nariño) [1], Cumbal (Nariño) [1], Pasto (Nariño) [1], San Carlos de Guaroa (Meta) [1], Santa Marta (Magdalena) [1], El Calvario (Meta) [1], Tibú (Norte De Santander) [1] and 54 more.

**MunicipalIndicators.070150002**

- break (19 municipalities): Andes (Antioquia) [1], Medina (Cundinamarca) [1], Valle de San Juan (Tolima) [1], Guavatá (Santander) [1], Calarcá (Quindío) [1], Nariño (Nariño) [1], Restrepo (Meta) [1], Elías (Huila) [1], Acandí (Chocó) [1], Jambaló (Cauca) [1], Anorí (Antioquia) [1], Labranzagrande (Boyacá) [1] and 7 more.

**MunicipalIndicators.070150003**

- break (18 municipalities): Andes (Antioquia) [1], Anorí (Antioquia) [1], Valle de San Juan (Tolima) [1], Guavatá (Santander) [1], Calarcá (Quindío) [1], Nariño (Nariño) [1], Pasto (Nariño) [1], Elías (Huila) [1], Acandí (Chocó) [1], Medina (Cundinamarca) [1], Jambaló (Cauca) [1], Villamaría (Caldas) [1] and 6 more.

**MunicipalIndicators.080010003**

- break (40 municipalities): Beltrán (Cundinamarca) [2], Andes (Antioquia) [1], Zipacón (Cundinamarca) [1], El Litoral del San Juan (Chocó) [1], Consacá (Nariño) [1], Cumbitara (Nariño) [1], Pupiales (Nariño) [1], Salazar (Norte De Santander) [1], Villa Caro (Norte De Santander) [1], Cabrera (Santander) [1], Curití (Santander) [1], Guaca (Santander) [1] and 28 more.

**MunicipalIndicators.080010006**

- break (13 municipalities): Abejorral (Antioquia) [1], Arenal (Bolívar) [1], Tasco (Boyacá) [1], Becerril (Cesar) [1], San Diego (Cesar) [1], Guayabetal (Cundinamarca) [1], Acandí (Chocó) [1], La Plata (Huila) [1], Montenegro (Quindío) [1], Palmar (Santander) [1], San José de Miranda (Santander) [1], Chalán (Sucre) [1] and 1 more.

**MunicipalIndicators.080010009**

- break (48 municipalities): Beltrán (Cundinamarca) [3], La Apartada (Córdoba) [2], Sipí (Chocó) [2], Betania (Antioquia) [1], Cabrera (Santander) [1], Suaza (Huila) [1], Teruel (Huila) [1], Urumita (La Guajira) [1], Granada (Meta) [1], Consacá (Nariño) [1], La Unión (Nariño) [1], Pupiales (Nariño) [1] and 36 more.

**MunicipalIndicators.080010011**

- break (9 municipalities): Cabuyaro (Meta) [2], Piedecuesta (Santander) [2], Cisneros (Antioquia) [1], Galapa (Atlántico) [1], Guachené (Cauca) [1], Sipí (Chocó) [1], Albania (Santander) [1], Zapatoca (Santander) [1], Bugalagrande (Valle Del Cauca) [1].

**MunicipalIndicators.080010012**

- break (72 municipalities): Cuítiva (Boyacá) [2], Manta (Cundinamarca) [2], Labranzagrande (Boyacá) [2], González (Cesar) [2], Pisba (Boyacá) [2], San Jacinto del Cauca (Bolívar) [2], El Calvario (Meta) [2], Nilo (Cundinamarca) [2], Valdivia (Antioquia) [2], Cácota (Norte De Santander) [2], Une (Cundinamarca) [1], Amagá (Antioquia) [1] and 60 more.

**MunicipalIndicators.080010013**

- break (12 municipalities): Galapa (Atlántico) [2], Cabuyaro (Meta) [2], Cisneros (Antioquia) [1], Tubará (Atlántico) [1], Guachené (Cauca) [1], Unión Panamericana (Chocó) [1], Albania (Santander) [1], Barrancabermeja (Santander) [1], Cabrera (Santander) [1], Piedecuesta (Santander) [1], Puerto Wilches (Santander) [1], Zapatoca (Santander) [1].

**MunicipalIndicators.080020001**

- break (3 municipalities): Soplaviento (Bolívar), 2024: 0.1 times the year before (23.57); Medio Atrato (Chocó), 2019: 12.1 times the year before (3.52); Medio San Juan (Chocó), 2019: 12.0 times the year before (3.14).

**MunicipalIndicators.080020002**

- break (4 municipalities): Agrado (Huila), 2022: 10.2 times the year before (9.2); Guamal (Magdalena), 2022: 10.8 times the year before (8.33); Pedraza (Magdalena), 2021: 0.1 times the year before (96.38); Puerto Nariño (Amazonas), 2022: 10.2 times the year before (8.33).

**MunicipalIndicators.080020004**

- break (17 municipalities): San Juan Nepomuceno (Bolívar) [1], Santa Bárbara (Nariño) [1], Valle del Guamuez (Putumayo) [1], Puerto Leguízamo (Putumayo) [1], Puerto Guzmán (Putumayo) [1], Támara (Casanare) [1], Rionegro (Santander) [1], Sapuyes (Nariño) [1], Buesaco (Nariño) [1], Villamaría (Caldas) [1], Salamina (Magdalena) [1], Pedraza (Magdalena) [1] and 5 more.

**MunicipalIndicators.080030003**

- break (1 municipalities): Mitú (Vaupés), 2024: 10.7 times the year before (6.22).

**MunicipalIndicators.110010005**

- break (1 municipalities): Ciénaga (Magdalena), 2017: 0.0 times the year before (55961.63); Ciénaga (Magdalena), 2018: 106.1 times the year before (505.5).

**MunicipalIndicators.110030003**

- break (195 municipalities): La Gloria (Cesar) [3], Santiago (Putumayo) [3], Balboa (Cauca) [3], La Vega (Cauca) [3], Simití (Bolívar) [3], Algeciras (Huila) [3], Unguía (Chocó) [3], Bahía Solano (Chocó) [2], Baraya (Huila) [2], Neiva (Huila) [2], El Litoral del San Juan (Chocó) [2], El Carmen de Atrato (Chocó) [2] and 183 more.

**MunicipalIndicators.110070003**

- break (15 municipalities): Ortega (Tolima) [2], Dagua (Valle Del Cauca) [2], Páez (Cauca) [1], Fómeque (Cundinamarca) [1], Junín (Cundinamarca) [1], Ricaurte (Cundinamarca) [1], Útica (Cundinamarca) [1], Viotá (Cundinamarca) [1], Aracataca (Magdalena) [1], Acacías (Meta) [1], Puerto López (Meta) [1], Puerto Rico (Meta) [1] and 3 more.

**MunicipalIndicators.110070005**

- break (2 municipalities): Mistrató (Risaralda), 2021: 12.0 times the year before (1); Mocoa (Putumayo), 2020: 0.1 times the year before (11).

**MunicipalIndicators.110070008**

- break (17 municipalities): La Primavera (Vichada) [2], Aracataca (Magdalena) [2], Puerto López (Meta) [1], Arauca (Arauca) [1], Purificación (Tolima) [1], Ortega (Tolima) [1], Chinácota (Norte De Santander) [1], San Martín (Meta) [1], Puerto Lleras (Meta) [1], Manizales (Caldas) [1], Popayán (Cauca) [1], Útica (Cundinamarca) [1] and 5 more.

**MunicipalIndicators.110070010**

- break (385 municipalities): Dibulla (La Guajira) [7], Piamonte (Cauca) [7], Nóvita (Chocó) [5], Quetame (Cundinamarca) [5], El Castillo (Meta) [5], Tamalameque (Cesar) [4], Paz de Ariporo (Casanare) [4], Condoto (Chocó) [4], La Virginia (Risaralda) [4], Fundación (Magdalena) [4], Puerto Caicedo (Putumayo) [4], Leticia (Amazonas) [4] and 373 more.

**MunicipalIndicators.120210003**

- inconsistent (476 municipalities): Medellín (Antioquia) [11], Samacá (Boyacá) [11], La Mesa (Cundinamarca) [11], Lenguazaque (Cundinamarca) [11], Mosquera (Cundinamarca) [11], Paratebueno (Cundinamarca) [11], Quipile (Cundinamarca) [11], San Cayetano (Cundinamarca) [11], Sasaima (Cundinamarca) [11], Sesquilé (Cundinamarca) [11], Sibaté (Cundinamarca) [11], Sopó (Cundinamarca) [11] and 464 more.

**MunicipalIndicators.120220001**

- break (24 municipalities): San Luis de Palenque (Casanare) [2], Paz de Ariporo (Casanare) [2], Maní (Casanare) [2], Corozal (Sucre) [2], San Antero (Córdoba) [2], San Juan de Arama (Meta) [2], Acacías (Meta) [1], Saravena (Arauca) [1], Arauca (Arauca) [1], Caicedonia (Valle Del Cauca) [1], Chimá (Santander) [1], San Pablo (Nariño) [1] and 12 more.

**MunicipalIndicators.120220002**

- break (24 municipalities): Caucasia (Antioquia) [2], Arroyohondo (Bolívar) [2], Pinchote (Santander) [2], Puerto Rico (Meta) [2], Puerto Gaitán (Meta) [2], Granada (Meta) [2], El Molino (La Guajira) [2], Rivera (Huila) [1], Lérida (Tolima) [1], Sucre (Sucre) [1], Galeras (Sucre) [1], Puerto Lleras (Meta) [1] and 12 more.

**MunicipalIndicators.120220003**

- break (22 municipalities): Coello (Tolima) [2], Granada (Meta) [2], Momil (Córdoba) [2], Sahagún (Córdoba) [2], San Antero (Córdoba) [2], Córdoba (Bolívar) [1], El Banco (Magdalena) [1], Puerto Rondón (Arauca) [1], Armero (Tolima) [1], Tolú Viejo (Sucre) [1], El Castillo (Meta) [1], Puebloviejo (Magdalena) [1] and 10 more.

**MunicipalIndicators.120220004**

- break (28 municipalities): Chocontá (Cundinamarca) [2], Tamalameque (Cesar) [2], Gutiérrez (Cundinamarca) [1], Planadas (Tolima) [1], Fresno (Tolima) [1], San José de Miranda (Santander) [1], Ospina (Nariño) [1], Lejanías (Meta) [1], El Castillo (Meta) [1], Sitionuevo (Magdalena) [1], Algarrobo (Magdalena) [1], Algeciras (Huila) [1] and 16 more.

**MunicipalIndicators.120240001**

- break (20 municipalities): Vianí (Cundinamarca) [2], San Cayetano (Cundinamarca) [2], Alejandría (Antioquia) [1], Cisneros (Antioquia) [1], Villarrica (Tolima) [1], Santa Isabel (Tolima) [1], Santa Ana (Magdalena) [1], Fundación (Magdalena) [1], Ariguaní (Magdalena) [1], Tena (Cundinamarca) [1], Pacho (Cundinamarca) [1], La Palma (Cundinamarca) [1] and 8 more.

**MunicipalIndicators.120240002**

- break (30 municipalities): Samaniego (Nariño) [2], Valparaíso (Antioquia) [2], Tununguá (Boyacá) [2], El Retén (Magdalena) [2], Vianí (Cundinamarca) [2], El Peñón (Santander) [2], Güepsa (Santander) [1], Montenegro (Quindío) [1], Pijao (Quindío) [1], Cañasgordas (Antioquia) [1], Génova (Quindío) [1], Venadillo (Tolima) [1] and 18 more.

**MunicipalIndicators.120240003**

- break (20 municipalities): Santander de Quilichao (Cauca) [2], Salgar (Antioquia) [1], Barranca de Upía (Meta) [1], Caicedonia (Valle Del Cauca) [1], Bugalagrande (Valle Del Cauca) [1], Rovira (Tolima) [1], San Benito (Santander) [1], Armenia (Quindío) [1], Gramalote (Norte De Santander) [1], Buesaco (Nariño) [1], Villavicencio (Meta) [1], Santa Bárbara (Antioquia) [1] and 8 more.

**MunicipalIndicators.120240004**

- break (18 municipalities): Neira (Caldas) [2], Concordia (Antioquia) [1], Córdoba (Quindío) [1], Arauquita (Arauca) [1], Arauca (Arauca) [1], Bugalagrande (Valle Del Cauca) [1], Alcalá (Valle Del Cauca) [1], San Benito (Santander) [1], Montenegro (Quindío) [1], Sardinata (Norte De Santander) [1], Anserma (Caldas) [1], Santa Bárbara (Nariño) [1] and 6 more.

**MunicipalIndicators.120260003**

- break (1 municipalities): San Pedro de Cartago (Nariño), 2021: 0.1 times the year before (22.08).

**MunicipalIndicators.120260005**

- break (1 municipalities): Arboledas (Norte De Santander), 2021: 0.0 times the year before (654).

**MunicipalIndicators.120260006**

- break (1 municipalities): Pajarito (Boyacá), 2020: 0.1 times the year before (15).

**MunicipalIndicators.120260014**

- break (1 municipalities): Cajicá (Cundinamarca), 2023: 0.1 times the year before (10.8).

**MunicipalIndicators.120260022**

- break (3 municipalities): Tarqui (Huila), 2021: 0.0 times the year before (295.44); Chipatá (Santander), 2021: 11.0 times the year before (1); Guacarí (Valle Del Cauca), 2021: 0.1 times the year before (18).

**MunicipalIndicators.120260028**

- break (1 municipalities): Riofrío (Valle Del Cauca), 2021: 0.1 times the year before (2.44).

**MunicipalIndicators.120260034**

- break (1 municipalities): Guacamayas (Boyacá), 2022: 0.1 times the year before (6).

**MunicipalIndicators.120260035**

- break (5 municipalities): Caramanta (Antioquia), 2020: 0.1 times the year before (6.7); Murindó (Antioquia), 2020: 0.1 times the year before (5); Guacamayas (Boyacá), 2022: 0.1 times the year before (6); San Eduardo (Boyacá), 2021: 11.6 times the year before (0.5); Tenza (Boyacá), 2020: 0.1 times the year before (4.64).

**MunicipalIndicators.120260036**

- break (5 municipalities): Frontino (Antioquia), 2020: 10.5 times the year before (0.84); Cubará (Boyacá), 2021: 0.1 times the year before (11); Guacamayas (Boyacá), 2022: 0.1 times the year before (6); Paratebueno (Cundinamarca), 2020: 0.1 times the year before (14); Obando (Valle Del Cauca), 2020: 0.0 times the year before (12.94); Obando (Valle Del Cauca), 2021: 22.7 times the year before (0.57).

**MunicipalIndicators.120260040**

- break (1 municipalities): Palmira (Valle Del Cauca), 2021: 0.1 times the year before (20).

**MunicipalIndicators.120260043**

- break (1 municipalities): Rosas (Cauca), 2021: 26.0 times the year before (0.5).

**MunicipalIndicators.120260044**

- break (1 municipalities): La Uvita (Boyacá), 2021: 11.3 times the year before (0.71).

**MunicipalIndicators.120260046**

- break (1 municipalities): Tasco (Boyacá), 2021: 27.0 times the year before (1).

**MunicipalIndicators.120260060**

- break (2 municipalities): Distracción (La Guajira), 2021: 13.1 times the year before (0.13); Túquerres (Nariño), 2021: 16.7 times the year before (0.12).

**MunicipalIndicators.120260062**

- break (3 municipalities): Aguadas (Caldas), 2021: 0.1 times the year before (53.33); Soacha (Cundinamarca), 2023: 0.1 times the year before (51); Roldanillo (Valle Del Cauca), 2022: 0.0 times the year before (43).

**MunicipalIndicators.120260066**

- break (1 municipalities): Dosquebradas (Risaralda), 2021: 0.1 times the year before (90).

**MunicipalIndicators.120260068**

- break (1 municipalities): Cunday (Tolima), 2020: 0.1 times the year before (20).

**MunicipalIndicators.120260070**

- break (3 municipalities): Soplaviento (Bolívar), 2021: 10.3 times the year before (3.5); Soplaviento (Bolívar), 2022: 0.1 times the year before (36); Villanueva (Bolívar), 2021: 0.1 times the year before (47.5); Ricaurte (Nariño), 2022: 10.7 times the year before (2.8).

**MunicipalIndicators.120260073**

- break (1 municipalities): Ulloa (Valle Del Cauca), 2021: 0.1 times the year before (9.15).

**MunicipalIndicators.120260081**

- break (5 municipalities): Albán (Nariño), 2022: 10.0 times the year before (1.51); El Rosario (Nariño), 2020: 14.0 times the year before (1.72); Puerto Parra (Santander), 2021: 10.5 times the year before (2.25); Piedras (Tolima), 2022: 12.3 times the year before (1.87); El Águila (Valle Del Cauca), 2022: 11.0 times the year before (1).

**MunicipalIndicators.120260083**

- break (3 municipalities): Rosas (Cauca), 2021: 10.5 times the year before (2); Guacarí (Valle Del Cauca), 2021: 0.0 times the year before (27); Santiago (Putumayo), 2024: 0.1 times the year before (35).

**MunicipalIndicators.120260085**

- break (7 municipalities): Galapa (Atlántico) [1], Ponedera (Atlántico) [1], Nuevo Colón (Boyacá) [1], Marulanda (Caldas) [1], Villapinzón (Cundinamarca) [1], Barichara (Santander) [1], Santiago (Putumayo) [1].

**MunicipalIndicators.120260086**

- break (1 municipalities): La Jagua del Pilar (La Guajira), 2022: 0.1 times the year before (11.57).

**MunicipalIndicators.120260089**

- break (3 municipalities): Santa María (Huila), 2022: 0.1 times the year before (13); Leiva (Nariño), 2022: 11.1 times the year before (0.9); Palmito (Sucre), 2021: 11.2 times the year before (2.5).

**MunicipalIndicators.120260090**

- break (1 municipalities): Cumaral (Meta), 2021: 0.1 times the year before (10.2).

**MunicipalIndicators.120260093**

- break (2 municipalities): Rosas (Cauca), 2021: 14.7 times the year before (1.5); Sabanalarga (Casanare), 2022: 0.1 times the year before (30).

**MunicipalIndicators.120260094**

- break (2 municipalities): Santo Tomás (Atlántico), 2020: 0.1 times the year before (17.12); Chinú (Córdoba), 2020: 0.0 times the year before (12.35).

**MunicipalIndicators.120260095**

- break (1 municipalities): Candelaria (Atlántico), 2020: 12.6 times the year before (2).

**MunicipalIndicators.120260097**

- break (4 municipalities): Sogamoso (Boyacá), 2022: 12.0 times the year before (1); Facatativá (Cundinamarca), 2021: 0.1 times the year before (15.42); Gachetá (Cundinamarca), 2022: 13.0 times the year before (2); Contadero (Nariño), 2020: 0.1 times the year before (14).

**MunicipalIndicators.120260100**

- break (1 municipalities): Talaigua Nuevo (Bolívar), 2022: 0.1 times the year before (30.24).

**MunicipalIndicators.120260107**

- break (4 municipalities): Vistahermosa (Meta), 2021: 0.1 times the year before (42); Sabana de Torres (Santander), 2020: 16.0 times the year before (5); Sabana de Torres (Santander), 2021: 0.1 times the year before (80); Sucre (Santander), 2021: 0.0 times the year before (43.15); Rovira (Tolima), 2021: 0.1 times the year before (230).

**MunicipalIndicators.120260109**

- break (2 municipalities): Montecristo (Bolívar), 2022: 0.0 times the year before (60); Pore (Casanare), 2022: 12.9 times the year before (1.24).

**MunicipalIndicators.120260114**

- break (2 municipalities): Capitanejo (Santander), 2021: 18.0 times the year before (1); Palmira (Valle Del Cauca), 2022: 0.1 times the year before (25).

**MunicipalIndicators.120260115**

- break (1 municipalities): Curití (Santander), 2021: 11.9 times the year before (1.68).

**MunicipalIndicators.120260117**

- break (2 municipalities): Mercaderes (Cauca), 2021: 17.8 times the year before (2); Mocoa (Putumayo), 2025: 0.1 times the year before (35).

**MunicipalIndicators.120260118**

- break (1 municipalities): Rosas (Cauca), 2021: 15.0 times the year before (1).

**MunicipalIndicators.120260119**

- break (1 municipalities): Facatativá (Cundinamarca), 2021: 0.1 times the year before (53.02).

**MunicipalIndicators.120260122**

- break (2 municipalities): Villanueva (Bolívar), 2021: 0.1 times the year before (19.68); San Juan de Rioseco (Cundinamarca), 2021: 0.1 times the year before (24.73).

**MunicipalIndicators.120260131**

- break (1 municipalities): Enciso (Santander), 2020: 0.0 times the year before (57.5); Enciso (Santander), 2021: 33.6 times the year before (1.5).

**MunicipalIndicators.120260132**

- break (1 municipalities): Chitaraque (Boyacá), 2022: 14.0 times the year before (0.5).

**MunicipalIndicators.120260140**

- break (1 municipalities): Guadalajara de Buga (Valle Del Cauca), 2023: 10.0 times the year before (4.58).

**MunicipalIndicators.120260141**

- break (5 municipalities): Firavitoba (Boyacá), 2021: 0.0 times the year before (20); Paipa (Boyacá), 2021: 0.0 times the year before (53); Chía (Cundinamarca), 2023: 0.1 times the year before (15.3); Chipaque (Cundinamarca), 2022: 0.1 times the year before (25); Facatativá (Cundinamarca), 2025: 10.7 times the year before (3).

**MunicipalIndicators.120260144**

- break (2 municipalities): Cajicá (Cundinamarca), 2022: 0.1 times the year before (24); Pupiales (Nariño), 2022: 10.8 times the year before (1.67).

**MunicipalIndicators.120260148**

- break (5 municipalities): Solita (Caquetá), 2020: 11.4 times the year before (1.14); El Paso (Cesar), 2021: 0.1 times the year before (21.7); Unguía (Chocó), 2021: 12.0 times the year before (2.5); Galán (Santander), 2021: 12.7 times the year before (1); Valle de San José (Santander), 2020: 12.0 times the year before (1).

**MunicipalIndicators.120290002**

- break (63 municipalities): Arboletes (Antioquia) [2], San Luis de Palenque (Casanare) [2], Paz de Ariporo (Casanare) [2], Pandi (Cundinamarca) [2], Gutiérrez (Cundinamarca) [2], Corozal (Sucre) [2], Armenia (Quindío) [1], Belén de Umbría (Risaralda) [1], Pijao (Quindío) [1], Calarcá (Quindío) [1], Uribe (Meta) [1], Santa Bárbara (Nariño) [1] and 51 more.

**MunicipalIndicators.120290003**

- break (150 municipalities): Samaniego (Nariño) [7], San Martín (Meta) [5], Chachagüí (Nariño) [5], San Pablo (Nariño) [4], San Miguel de Sema (Boyacá) [4], Alpujarra (Tolima) [4], Galán (Santander) [4], Chiriguaná (Cesar) [4], Toledo (Antioquia) [4], Suaza (Huila) [4], Gachalá (Cundinamarca) [3], La Llanada (Nariño) [3] and 138 more.

**MunicipalIndicators.120290005**

- break (123 municipalities): Villapinzón (Cundinamarca) [2], Vianí (Cundinamarca) [2], Florencia (Caquetá) [2], Sutamarchán (Boyacá) [2], Chipatá (Santander) [2], Córdoba (Bolívar) [2], Pijao (Quindío) [2], Arroyohondo (Bolívar) [2], San José (Caldas) [2], Maní (Casanare) [2], Caucasia (Antioquia) [2], Ricaurte (Nariño) [1] and 111 more.

**MunicipalIndicators.120290006**

- break (376 municipalities): Gama (Cundinamarca) [8], Tibirita (Cundinamarca) [7], Somondoco (Boyacá) [6], Colón (Nariño) [6], Dabeiba (Antioquia) [6], Angostura (Antioquia) [5], Usiacurí (Atlántico) [5], Circasia (Quindío) [5], Ospina (Nariño) [5], Sutatenza (Boyacá) [5], Barrancas (La Guajira) [5], Samaniego (Nariño) [5] and 364 more.

**MunicipalIndicators.120290008**

- break (149 municipalities): Margarita (Bolívar) [2], Puerto Gaitán (Meta) [2], Sincelejo (Sucre) [2], Medina (Cundinamarca) [2], Francisco Pizarro (Nariño) [2], El Peñón (Cundinamarca) [2], Colón (Nariño) [2], Supía (Caldas) [2], Tona (Santander) [2], Jamundí (Valle Del Cauca) [2], Cabuyaro (Meta) [2], Socorro (Santander) [2] and 137 more.

**MunicipalIndicators.120290009**

- break (461 municipalities): Consacá (Nariño) [7], Sandoná (Nariño) [7], Guadalupe (Antioquia) [7], Tipacoque (Boyacá) [7], Villamaría (Caldas) [7], Suesca (Cundinamarca) [7], Tota (Boyacá) [6], Cali (Valle Del Cauca) [6], Salamina (Magdalena) [6], Macanal (Boyacá) [6], Circasia (Quindío) [6], Fortul (Arauca) [6] and 449 more.

**MunicipalIndicators.120290011**

- break (175 municipalities): Sahagún (Córdoba) [2], Chigorodó (Antioquia) [2], Colón (Nariño) [2], Montecristo (Bolívar) [2], Puerto Rico (Meta) [2], Manzanares (Caldas) [2], El Castillo (Meta) [2], Arboledas (Norte De Santander) [1], Francisco Pizarro (Nariño) [1], Samaniego (Nariño) [1], San Lorenzo (Nariño) [1], Taminango (Nariño) [1] and 163 more.

**MunicipalIndicators.120290012**

- break (506 municipalities): Puerto Boyacá (Boyacá) [8], Consacá (Nariño) [7], Sandoná (Nariño) [7], Guaitarilla (Nariño) [6], Aguadas (Caldas) [6], Cachipay (Cundinamarca) [6], Imués (Nariño) [6], Valle de San José (Santander) [6], Santa Rosa de Osos (Antioquia) [5], Hato (Santander) [5], Salento (Quindío) [5], Luruaco (Atlántico) [5] and 494 more.

**MunicipalIndicators.120290014**

- break (216 municipalities): Remolino (Magdalena) [3], Regidor (Bolívar) [2], Topaipí (Cundinamarca) [2], Santander de Quilichao (Cauca) [2], Neira (Caldas) [2], San Benito (Santander) [2], Nuevo Colón (Boyacá) [2], Tunja (Boyacá) [2], Linares (Nariño) [2], Andalucía (Valle Del Cauca) [2], Paime (Cundinamarca) [2], San Carlos de Guaroa (Meta) [2] and 204 more.

**MunicipalIndicators.120290015**

- break (477 municipalities): Gachantivá (Boyacá) [8], Tierralta (Córdoba) [7], Imués (Nariño) [6], Jordán (Santander) [5], Caldono (Cauca) [5], Donmatías (Antioquia) [5], Páez (Boyacá) [5], La Uvita (Boyacá) [5], Santa Marta (Magdalena) [5], Pacho (Cundinamarca) [5], La Paz (Cesar) [5], Guapotá (Santander) [5] and 465 more.

**MunicipalIndicators.120300001**

- break (6 municipalities): Ocaña (Norte De Santander) [2], Timbío (Cauca) [1], La Plata (Huila) [1], Nueva Granada (Magdalena) [1], Santuario (Risaralda) [1], Armero (Tolima) [1].

**MunicipalIndicators.120300002**

- break (126 municipalities): Valledupar (Cesar) [3], Fonseca (La Guajira) [3], Villagarzón (Putumayo) [3], Taminango (Nariño) [3], Barrancas (La Guajira) [2], Hato Corozal (Casanare) [2], Yopal (Casanare) [2], Solano (Caquetá) [2], Rioblanco (Tolima) [2], Planadas (Tolima) [2], Puerto Gaitán (Meta) [2], San Onofre (Sucre) [2] and 114 more.

**MunicipalIndicators.120300007**

- break (1 municipalities): Puerto Carreño (Vichada), 2022: 10.0 times the year before (31).

**MunicipalIndicators.150030004**

- error (13 municipalities): Quibdó (Chocó) [1], Alto Baudó (Chocó) [1], Atrato (Chocó) [1], Bagadó (Chocó) [1], Cértegui (Chocó) [1], El Litoral del San Juan (Chocó) [1], Medio San Juan (Chocó) [1], Sipí (Chocó) [1], Tadó (Chocó) [1], Unión Panamericana (Chocó) [1], Barbacoas (Nariño) [1], Roberto Payán (Nariño) [1] and 1 more.

**MunicipalIndicators.150040004**

- error (13 municipalities): Quibdó (Chocó) [1], Alto Baudó (Chocó) [1], Atrato (Chocó) [1], Bagadó (Chocó) [1], Cértegui (Chocó) [1], El Litoral del San Juan (Chocó) [1], Medio San Juan (Chocó) [1], Sipí (Chocó) [1], Tadó (Chocó) [1], Unión Panamericana (Chocó) [1], Barbacoas (Nariño) [1], Roberto Payán (Nariño) [1] and 1 more.

**MunicipalIndicators.150070003**

- break (1 municipalities): Bello (Antioquia), 2024: 12.2 times the year before (1246).

**MunicipalIndicators.160040001**

- break (1 municipalities): Fómeque (Cundinamarca), 2014: 13.7 times the year before (1).

**MunicipalIndicators.160040006**

- break (1 municipalities): Cumaribo (Vichada), 2014: 11.8 times the year before (13.58).

**MunicipalIndicators.160040007**

- break (29 municipalities): Medellín (Antioquia) [1], Neiva (Huila) [1], Cali (Valle Del Cauca) [1], Espinal (Tolima) [1], Chaparral (Tolima) [1], Ibagué (Tolima) [1], Girón (Santander) [1], Barrancabermeja (Santander) [1], Bucaramanga (Santander) [1], Pereira (Risaralda) [1], Armenia (Quindío) [1], San José de Cúcuta (Norte De Santander) [1] and 17 more.

**MunicipalIndicators.160060002**

- break (1 municipalities): Bochalema (Norte De Santander), 2016: 0.1 times the year before (706.92).

**MunicipalIndicators.190010001**

- break (2 municipalities): Socorro (Santander), 2010: 13.5 times the year before (4); Villanueva (Casanare), 2012: 0.1 times the year before (67).

**MunicipalIndicators.190010008**

- break (1 municipalities): Montería (Córdoba), 2021: 12.5 times the year before (8).

**MunicipalIndicators.190010011**

- break (2 municipalities): Girardota (Antioquia), 2022: 11.2 times the year before (14); Pacho (Cundinamarca), 2019: 0.1 times the year before (96.3).

**MunicipalIndicators.190010012**

- break (6 municipalities): Socorro (Santander) [2], Amalfi (Antioquia) [1], Chitaraque (Boyacá) [1], Soacha (Cundinamarca) [1], Puerto Parra (Santander) [1], Yopal (Casanare) [1].

**MunicipalIndicators.190010013**

- break (1 municipalities): Cali (Valle Del Cauca), 2019: 15.3 times the year before (3).

**MunicipalIndicators.190010014**

- break (1 municipalities): Ibagué (Tolima), 2018: 20.0 times the year before (5).

**MunicipalIndicators.190010015**

- break (2 municipalities): San Andrés de Tumaco (Nariño), 2010: 14.3 times the year before (7); San Andrés de Tumaco (Nariño), 2011: 0.1 times the year before (100); Pereira (Risaralda), 2016: 0.1 times the year before (100).

**MunicipalIndicators.190010016**

- break (10 municipalities): Amalfi (Antioquia) [1], Angelópolis (Antioquia) [1], Apartadó (Antioquia) [1], El Carmen de Viboral (Antioquia) [1], Retiro (Antioquia) [1], Cucunubá (Cundinamarca) [1], Facatativá (Cundinamarca) [1], Uribe (Meta) [1], Ipiales (Nariño) [1], Cartago (Valle Del Cauca) [1].

**MunicipalIndicators.190010018**

- break (1 municipalities): Facatativá (Cundinamarca), 2025: 0.1 times the year before (66).

**MunicipalIndicators.190010022**

- break (14 municipalities): Ocamonte (Santander) [2], Amagá (Antioquia) [1], Caldas (Antioquia) [1], San Rafael (Antioquia) [1], Chitaraque (Boyacá) [1], Zetaquira (Boyacá) [1], Caparrapí (Cundinamarca) [1], Une (Cundinamarca) [1], Túquerres (Nariño) [1], Calarcá (Quindío) [1], Confines (Santander) [1], Cajamarca (Tolima) [1] and 2 more.

**MunicipalIndicators.190010023**

- break (2 municipalities): Facatativá (Cundinamarca), 2010: 0.0 times the year before (88); Girardot (Cundinamarca), 2011: 0.1 times the year before (29); Girardot (Cundinamarca), 2012: 22.5 times the year before (2).

**MunicipalIndicators.190010026**

- break (2 municipalities): Facatativá (Cundinamarca), 2009: 16.7 times the year before (6); Puerto Salgar (Cundinamarca), 2019: 10.5 times the year before (2).

**MunicipalIndicators.190010027**

- break (1 municipalities): Facatativá (Cundinamarca), 2010: 0.0 times the year before (100).

**MunicipalIndicators.190010029**

- break (3 municipalities): Medellín (Antioquia), 2020: 0.1 times the year before (13); Popayán (Cauca), 2023: 14.0 times the year before (1); Popayán (Cauca), 2025: 0.0 times the year before (20); Chía (Cundinamarca), 2025: 0.1 times the year before (100).

**MunicipalIndicators.190010032**

- break (1 municipalities): San José de Cúcuta (Norte De Santander), 2015: 19.0 times the year before (1).

**MunicipalIndicators.190010033**

- break (4 municipalities): Mosquera (Cundinamarca), 2018: 0.1 times the year before (18.18); La Plata (Huila), 2022: 17.2 times the year before (0.98); La Tebaida (Quindío), 2025: 0.1 times the year before (12.6); Cartago (Valle Del Cauca), 2024: 0.1 times the year before (2.61).

**MunicipalIndicators.190010034**

- break (8 municipalities): Sogamoso (Boyacá) [1], Sotará Paispamba (Cauca) [1], Riohacha (La Guajira) [1], Villavicencio (Meta) [1], Ocaña (Norte De Santander) [1], Piedecuesta (Santander) [1], Buenaventura (Valle Del Cauca) [1], Yopal (Casanare) [1].

**MunicipalIndicators.190010037**

- break (1 municipalities): Chía (Cundinamarca), 2020: 11.1 times the year before (9).

**MunicipalIndicators.190010038**

- break (9 municipalities): Amalfi (Antioquia) [1], Bello (Antioquia) [1], Remedios (Antioquia) [1], Momil (Córdoba) [1], Madrid (Cundinamarca) [1], Soacha (Cundinamarca) [1], Armenia (Quindío) [1], Jamundí (Valle Del Cauca) [1], Mocoa (Putumayo) [1].

**MunicipalIndicators.190010041**

- break (1 municipalities): Quibdó (Chocó), 2011: 20.0 times the year before (5).

**MunicipalIndicators.190010044**

- break (16 municipalities): Caldas (Antioquia) [2], Sotará Paispamba (Cauca) [2], Remedios (Antioquia) [1], Buenavista (Boyacá) [1], Paipa (Boyacá) [1], Aguachica (Cesar) [1], Momil (Córdoba) [1], Facatativá (Cundinamarca) [1], Puerto Salgar (Cundinamarca) [1], Villavicencio (Meta) [1], La Tebaida (Quindío) [1], Belén de Umbría (Risaralda) [1] and 4 more.

**MunicipalIndicators.190020001**

- break (38 municipalities): Ábrego (Norte De Santander) [3], Piendamó - Tunía (Cauca) [2], El Carmen de Viboral (Antioquia) [2], San Vicente de Chucurí (Santander) [2], Girardot (Cundinamarca) [2], Barrancabermeja (Santander) [2], Sibaté (Cundinamarca) [2], La Dorada (Caldas) [2], Caicedo (Antioquia) [1], La Argentina (Huila) [1], Saladoblanco (Huila) [1], Teruel (Huila) [1] and 26 more.

**MunicipalIndicators.190020002**

- break (77 municipalities): Machetá (Cundinamarca) [2], Puerto Colombia (Atlántico) [2], Girardot (Cundinamarca) [2], Momil (Córdoba) [2], La Plata (Huila) [2], Fonseca (La Guajira) [2], El Doncello (Caquetá) [2], San Sebastián de Buenavista (Magdalena) [2], Togüí (Boyacá) [2], Soacha (Cundinamarca) [2], Chiquinquirá (Boyacá) [2], Quebradanegra (Cundinamarca) [2] and 65 more.

**MunicipalIndicators.190020003**

- break (85 municipalities): Mosquera (Cundinamarca) [4], Saravena (Arauca) [3], Sibundoy (Putumayo) [2], San Gil (Santander) [2], Piendamó - Tunía (Cauca) [2], Pital (Huila) [2], La Plata (Huila) [2], Sardinata (Norte De Santander) [2], Isnos (Huila) [2], Circasia (Quindío) [2], Gigante (Huila) [2], Floridablanca (Santander) [2] and 73 more.

**MunicipalIndicators.190020004**

- break (124 municipalities): El Bagre (Antioquia) [4], Tuta (Boyacá) [4], Floridablanca (Santander) [4], Acacías (Meta) [3], Tuluá (Valle Del Cauca) [3], La Calera (Cundinamarca) [3], Caparrapí (Cundinamarca) [3], Momil (Córdoba) [3], Nobsa (Boyacá) [2], Aratoca (Santander) [2], Guática (Risaralda) [2], Tierralta (Córdoba) [2] and 112 more.

**MunicipalIndicators.190020005**

- break (89 municipalities): Ocaña (Norte De Santander) [5], La Dorada (Caldas) [4], Chinchiná (Caldas) [4], Tibaná (Boyacá) [4], Buenavista (Boyacá) [3], Oporapa (Huila) [3], Girón (Santander) [3], Cajicá (Cundinamarca) [3], Manzanares (Caldas) [2], Chía (Cundinamarca) [2], Ospina (Nariño) [2], Villamaría (Caldas) [2] and 77 more.

**MunicipalIndicators.190030002**

- break (10 municipalities): Nariño (Antioquia) [1], Nechí (Antioquia) [1], San Carlos (Antioquia) [1], San Luis (Antioquia) [1], La Montañita (Caquetá) [1], Guapi (Cauca) [1], López de Micay (Cauca) [1], Barbacoas (Nariño) [1], Roberto Payán (Nariño) [1], Puerto Asís (Putumayo) [1].

**MunicipalIndicators.190030003**

- break (7 municipalities): Caldono (Cauca) [2], Santa Rosa del Sur (Bolívar) [1], La Montañita (Caquetá) [1], López de Micay (Cauca) [1], Barbacoas (Nariño) [1], Tibú (Norte De Santander) [1], Puerto Asís (Putumayo) [1].

**MunicipalIndicators.190030004**

- break (2 municipalities): Guapi (Cauca), 2018: 0.0 times the year before (767); Roberto Payán (Nariño), 2020: 0.1 times the year before (269).

**MunicipalIndicators.190030005**

- break (2 municipalities): La Montañita (Caquetá), 2018: 0.1 times the year before (339); Caldono (Cauca), 2018: 0.0 times the year before (875).

**MunicipalIndicators.200010002**

- break (1 municipalities): Acandí (Chocó), 2022: 13.0 times the year before (2).

**MunicipalIndicators.200020007**

- break (1 municipalities): Santa Bárbara (Nariño), 2022: 11.0 times the year before (3).

**MunicipalIndicators.200020008**

- break (1 municipalities): Bahía Solano (Chocó), 2022: 11.7 times the year before (3).

**MunicipalIndicators.200020009**

- break (14 municipalities): Tarazá (Antioquia) [1], Achí (Bolívar) [1], El Carmen de Bolívar (Bolívar) [1], San Vicente del Caguán (Caquetá) [1], Guapi (Cauca) [1], Bahía Solano (Chocó) [1], Bojayá (Chocó) [1], Nuquí (Chocó) [1], Riosucio (Chocó) [1], La Macarena (Meta) [1], Mosquera (Nariño) [1], Santa Bárbara (Nariño) [1] and 2 more.

**MunicipalIndicators.200020011**

- break (1 municipalities): Puerto Leguízamo (Putumayo), 2022: 0.1 times the year before (264.51).

**MunicipalIndicators.200020013**

- break (1 municipalities): Nuquí (Chocó), 2022: 0.0 times the year before (1941).

**MunicipalIndicators.200020015**

- break (5 municipalities): Cartagena del Chairá (Caquetá), 2022: 1878.1 times the year before (1.23); Bahía Solano (Chocó), 2022: 23.2 times the year before (28.64); Juradó (Chocó), 2022: 0.0 times the year before (1313.72); Arauquita (Arauca), 2022: 32.7 times the year before (0.52); Puerto Leguízamo (Putumayo), 2022: 0.0 times the year before (29.4).

**MunicipalIndicators.200020016**

- break (3 municipalities): La Montañita (Caquetá), 2022: 19.3 times the year before (12); Solano (Caquetá), 2022: 0.1 times the year before (177.4); Riosucio (Chocó), 2022: 811.0 times the year before (3.84).

**MunicipalIndicators.200020023**

- break (7 municipalities): Turbo (Antioquia) [1], El Charco (Nariño) [1], La Tola (Nariño) [1], San Andrés de Tumaco (Nariño) [1], Buenaventura (Valle Del Cauca) [1], Puerto Leguízamo (Putumayo) [1], Cumaribo (Vichada) [1].

**MunicipalIndicators.200020024**

- break (1 municipalities): Miraflores (Guaviare), 2021: 0.1 times the year before (19).

**MunicipalIndicators.200030002**

- break (2 municipalities): Achí (Bolívar), 2022: 22.0 times the year before (1); Cartagena del Chairá (Caquetá), 2022: 25.0 times the year before (1).

**MunicipalIndicators.200030009**

- break (1 municipalities): Achí (Bolívar), 2022: 11.0 times the year before (7).

**MunicipalIndicators.260020001**

- break (16 municipalities): Briceño (Antioquia) [1], Ituango (Antioquia) [1], Zaragoza (Antioquia) [1], Samaná (Caldas) [1], Florencia (Caquetá) [1], El Doncello (Caquetá) [1], Argelia (Cauca) [1], Balboa (Cauca) [1], Mercaderes (Cauca) [1], Yacopí (Cundinamarca) [1], Puerto Gaitán (Meta) [1], Santacruz (Nariño) [1] and 4 more.

**MunicipalIndicators.260020002**

- break (54 municipalities): Puerto Leguízamo (Putumayo) [2], Patía (Cauca) [2], Remedios (Antioquia) [2], Argelia (Cauca) [2], Teorama (Norte De Santander) [2], Hacarí (Norte De Santander) [2], Puerto Rico (Meta) [2], Magüí (Nariño) [1], Colombia (Huila) [1], El Castillo (Meta) [1], Mesetas (Meta) [1], Uribe (Meta) [1] and 42 more.

**MunicipalIndicators.260020003**

- break (83 municipalities): Chitagá (Norte De Santander) [3], Santa Rosalía (Vichada) [2], Sipí (Chocó) [2], Sutatausa (Cundinamarca) [2], Santacruz (Nariño) [2], Argelia (Valle Del Cauca) [2], El Cocuy (Boyacá) [2], Cértegui (Chocó) [2], Bolívar (Santander) [2], Guayabetal (Cundinamarca) [2], Hato Corozal (Casanare) [2], Baraya (Huila) [2] and 71 more.

**MunicipalIndicators.260020004**

- break (2 municipalities): Medellín (Antioquia), 2023: 0.1 times the year before (12); Bogotá, D.C. (Bogotá, D.C.), 2023: 0.1 times the year before (13).

**MunicipalIndicators.260020007**

- break (8 municipalities): Lérida (Tolima) [2], Yalí (Antioquia) [1], Manaure Balcón del Cesar (Cesar) [1], La Paz (Cesar) [1], San Juan de Arama (Meta) [1], Quimbaya (Quindío) [1], Honda (Tolima) [1], La Unión (Valle Del Cauca) [1].

**MunicipalIndicators.260020014**

- break (3 municipalities): Medio San Juan (Chocó), 2025: 12.0 times the year before (1); Olaya Herrera (Nariño), 2024: 17.0 times the year before (1); San Andrés de Tumaco (Nariño), 2025: 0.0 times the year before (179).

**MunicipalIndicators.260030001**

- break (87 municipalities): Nuquí (Chocó) [4], Norosí (Bolívar) [3], San Marcos (Sucre) [3], Juradó (Chocó) [3], Medio San Juan (Chocó) [3], Almaguer (Cauca) [3], Samaniego (Nariño) [2], Acandí (Chocó) [2], Bagadó (Chocó) [2], El Tarra (Norte De Santander) [2], Santacruz (Nariño) [2], Pueblo Rico (Risaralda) [2] and 75 more.

**MunicipalIndicators.260030002**

- break (103 municipalities): San Marcos (Sucre) [3], Tierralta (Córdoba) [3], Norosí (Bolívar) [3], Juradó (Chocó) [3], Almaguer (Cauca) [3], Briceño (Antioquia) [2], Carmen del Darién (Chocó) [2], Suárez (Cauca) [2], Pueblo Rico (Risaralda) [2], Acandí (Chocó) [2], Alto Baudó (Chocó) [2], El Tarra (Norte De Santander) [2] and 91 more.

**MunicipalIndicators.260030003**

- break (58 municipalities): Juradó (Chocó) [3], Medio San Juan (Chocó) [3], Río Quito (Chocó) [2], Nuquí (Chocó) [2], Pueblo Rico (Risaralda) [2], Almaguer (Cauca) [2], Cértegui (Chocó) [2], Santacruz (Nariño) [2], Cravo Norte (Arauca) [2], Ábrego (Norte De Santander) [1], El Tarra (Norte De Santander) [1], Cáchira (Norte De Santander) [1] and 46 more.

**MunicipalIndicators.310010005**

- break (6 municipalities): Güicán de La Sierra (Boyacá), 2013: 11.5 times the year before (1.96); Valparaíso (Caquetá), 2011: 12.2 times the year before (1.15); Aguachica (Cesar), 2015: 10.6 times the year before (2.61); Arboledas (Norte De Santander), 2011: 11.7 times the year before (1.03); Palmas del Socorro (Santander), 2011: 0.1 times the year before (18.37); Tauramena (Casanare), 2014: 11.7 times the year before (2.3).

**MunicipalIndicators.310010009**

- break (1 municipalities): Pinchote (Santander), 2019: 11.0 times the year before (3.35).

**MunicipalIndicators.310010012**

- break (19 municipalities): Carurú (Vaupés) [2], Istmina (Chocó) [1], Mitú (Vaupés) [1], Corozal (Sucre) [1], Oiba (Santander) [1], Málaga (Santander) [1], Cabrera (Santander) [1], Chachagüí (Nariño) [1], Aipe (Huila) [1], Giraldo (Antioquia) [1], San Andrés de Cuerquía (Antioquia) [1], Tausa (Cundinamarca) [1] and 7 more.

**MunicipalIndicators.310010015**

- break (2 municipalities): Silvia (Cauca), 2012: 10.1 times the year before (3.3); Albania (Santander), 2019: 11.3 times the year before (5.73).

**MunicipalIndicators.310010017**

- break (2 municipalities): Boavita (Boyacá), 2021: 11.3 times the year before (3.14); Oiba (Santander), 2019: 0.1 times the year before (30.19).

**MunicipalIndicators.310010018**

- break (40 municipalities): Yaguará (Huila) [2], Palmas del Socorro (Santander) [2], Recetor (Casanare) [1], Aguazul (Casanare) [1], Arboledas (Norte De Santander) [1], Durania (Norte De Santander) [1], El Carmen (Norte De Santander) [1], Labateca (Norte De Santander) [1], Teorama (Norte De Santander) [1], Filandia (Quindío) [1], Pueblo Rico (Risaralda) [1], Aguada (Santander) [1] and 28 more.

**MunicipalIndicators.310010021**

- break (2 municipalities): Carmen del Darién (Chocó), 2015: 11.5 times the year before (7.48); El Castillo (Meta), 2014: 0.1 times the year before (56.54).

## CUIPO

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| MunicipalIncome | 1.1.01.02.300 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0401020 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0401094 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0401101 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 0401102 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 0401104 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0401105 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 0402013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0406001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 0406003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 0406004 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 0406016 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1102001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1202001 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1202002 | 0 | 0 | 72 | 0 | 0 | 0 |
| MunicipalSpending | 1202003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1202004 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 1202005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1202006 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1202007 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 1202008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1202012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1202013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1202014 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 1202018 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1202019 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 1202020 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 1202023 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 1202024 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1202026 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1202031 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 1203001 | 0 | 0 | 19 | 0 | 0 | 0 |
| MunicipalSpending | 1203002 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 1203003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1203004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1203005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1203009 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 1203010 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 1203011 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 1203014 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1204018 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1205001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1205005 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1205006 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1205008 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1206002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1206003 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1206004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1206005 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1206006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1206007 | 0 | 0 | 31 | 0 | 0 | 0 |
| MunicipalSpending | 1206008 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 1206010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1206012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1206018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1207002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1207011 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 1207012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1207014 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1207015 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1207017 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1207018 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1299001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1299065 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1399064 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1501005 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1702007 | 0 | 0 | 39 | 0 | 0 | 0 |
| MunicipalSpending | 1702009 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 1702010 | 0 | 0 | 144 | 0 | 0 | 0 |
| MunicipalSpending | 1702011 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 1702014 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1702016 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 1702017 | 0 | 0 | 27 | 0 | 0 | 0 |
| MunicipalSpending | 1702021 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 1702023 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 1702024 | 0 | 0 | 25 | 0 | 0 | 0 |
| MunicipalSpending | 1702025 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1702032 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1702035 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1702037 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1702038 | 0 | 0 | 27 | 0 | 0 | 0 |
| MunicipalSpending | 1702040 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1702042 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1702044 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1702045 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 1703008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1703009 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1704002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1704006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1704010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1704046 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1706004 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1706008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1707030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1707042 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1707043 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1707069 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1708018 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1708032 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1708040 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1708041 | 0 | 0 | 21 | 0 | 0 | 0 |
| MunicipalSpending | 1708055 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1708056 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709040 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709043 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1709052 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709059 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709062 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709065 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 1709078 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1709081 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 1709084 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709092 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1709099 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1709105 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1709106 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1709112 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1709114 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 1710001 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1901008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901011 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901084 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901095 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901100 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901119 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901127 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1901129 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901159 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1901163 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1902010 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1902016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903001 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1903002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903003 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1903004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1903011 | 0 | 0 | 74 | 0 | 0 | 0 |
| MunicipalSpending | 1903015 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 1903016 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 1903019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903020 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1903022 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903023 | 0 | 0 | 22 | 0 | 0 | 0 |
| MunicipalSpending | 1903025 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 1903026 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903027 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1903030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903031 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 1903032 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903034 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 1903035 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1903038 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 1903041 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 1903042 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1903045 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1903046 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903047 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903050 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1903051 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1903057 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1904017 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905001 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1905003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1905004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1905005 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905014 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 1905015 | 0 | 0 | 29 | 0 | 0 | 0 |
| MunicipalSpending | 1905016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905017 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905019 | 0 | 0 | 35 | 0 | 0 | 0 |
| MunicipalSpending | 1905020 | 0 | 0 | 23 | 0 | 0 | 0 |
| MunicipalSpending | 1905021 | 0 | 0 | 41 | 0 | 0 | 0 |
| MunicipalSpending | 1905022 | 0 | 0 | 42 | 0 | 0 | 0 |
| MunicipalSpending | 1905023 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 1905024 | 0 | 0 | 43 | 0 | 0 | 0 |
| MunicipalSpending | 1905025 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 1905026 | 0 | 0 | 30 | 0 | 0 | 0 |
| MunicipalSpending | 1905027 | 0 | 0 | 40 | 0 | 0 | 0 |
| MunicipalSpending | 1905028 | 0 | 0 | 37 | 0 | 0 | 0 |
| MunicipalSpending | 1905029 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 1905030 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 1905031 | 0 | 0 | 46 | 0 | 0 | 0 |
| MunicipalSpending | 1905035 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 1905036 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 1905037 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1905040 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1905041 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1905042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905043 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 1905049 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 1905050 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 1905051 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905052 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1905053 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1905054 | 0 | 0 | 40 | 0 | 0 | 0 |
| MunicipalSpending | 1906001 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1906004 | 0 | 0 | 54 | 0 | 0 | 0 |
| MunicipalSpending | 1906005 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1906006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906007 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906022 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1906023 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1906024 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906025 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906026 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 1906028 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1906029 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 1906030 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 1906031 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 1906032 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906035 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1906037 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906041 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 1906043 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1906044 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 1999050 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1999055 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 1999056 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2101002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2101003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2101009 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2101011 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2101015 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2101016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102001 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2102007 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102008 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2102009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102010 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 2102011 | 0 | 0 | 42 | 0 | 0 | 0 |
| MunicipalSpending | 2102012 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2102013 | 0 | 0 | 23 | 0 | 0 | 0 |
| MunicipalSpending | 2102014 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2102015 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2102021 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2102024 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2102025 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2102030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102045 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2102058 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2102059 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2102060 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2102061 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2102069 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 2102071 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2104012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2105019 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 2106002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2106010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201006 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 2201012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201014 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 2201015 | 0 | 0 | 20 | 0 | 0 | 0 |
| MunicipalSpending | 2201017 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 2201019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201020 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201021 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 2201022 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201023 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201026 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 2201028 | 0 | 0 | 99 | 0 | 0 | 0 |
| MunicipalSpending | 2201029 | 0 | 0 | 95 | 0 | 0 | 0 |
| MunicipalSpending | 2201030 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2201033 | 0 | 0 | 26 | 0 | 0 | 0 |
| MunicipalSpending | 2201034 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201035 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201036 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2201037 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201039 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201043 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201044 | 0 | 0 | 21 | 0 | 0 | 0 |
| MunicipalSpending | 2201047 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2201049 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2201050 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 2201051 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 2201052 | 0 | 0 | 82 | 0 | 0 | 0 |
| MunicipalSpending | 2201054 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201056 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201058 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201060 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201062 | 0 | 0 | 52 | 0 | 0 | 0 |
| MunicipalSpending | 2201063 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2201067 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2201068 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201069 | 0 | 0 | 28 | 0 | 0 | 0 |
| MunicipalSpending | 2201070 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2201071 | 0 | 0 | 104 | 0 | 0 | 0 |
| MunicipalSpending | 2201072 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2201073 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2201074 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 2201075 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2201078 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2201079 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2201080 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2201081 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2201083 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 2201084 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2201087 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2202005 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2202007 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 2202008 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2202009 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 2202011 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2202023 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2202030 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2202045 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2202051 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2202061 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2202062 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2202065 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2202070 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2202079 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2203022 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2299016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2301005 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 2301008 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2301013 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2301014 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2301024 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 2301027 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2301075 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2301076 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2301077 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2301079 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2302002 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2302003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302021 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302041 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302066 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302073 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302076 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302082 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302086 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2302101 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401004 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401017 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2401036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401041 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401051 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2401075 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402006 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 2402009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402011 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402012 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2402021 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 2402028 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2402039 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 2402041 | 0 | 0 | 163 | 0 | 0 | 0 |
| MunicipalSpending | 2402042 | 0 | 0 | 59 | 0 | 0 | 0 |
| MunicipalSpending | 2402044 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 2402045 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 2402046 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2402048 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2402055 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2402056 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2402063 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2402092 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402093 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402095 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402096 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2402098 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2402105 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2402111 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402112 | 0 | 0 | 204 | 0 | 0 | 0 |
| MunicipalSpending | 2402113 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 2402114 | 0 | 0 | 71 | 0 | 0 | 0 |
| MunicipalSpending | 2402115 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 2402116 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 2402118 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 2402120 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2402121 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2402125 | 0 | 0 | 28 | 0 | 0 | 0 |
| MunicipalSpending | 2402128 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 2402141 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2406001 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2406008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2406055 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2406057 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2407007 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2408001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2408004 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2408008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2408010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2408038 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2408039 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2408052 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2409002 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 2409003 | 0 | 0 | 25 | 0 | 0 | 0 |
| MunicipalSpending | 2409004 | 0 | 0 | 15 | 0 | 0 | 0 |
| MunicipalSpending | 2409007 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2409009 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 2409010 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2409011 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 2409012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2409013 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 2409014 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2409016 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 2409020 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2409022 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 2409023 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 2409025 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2409029 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2409038 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2409039 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 2409043 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2409059 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 2409063 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2499060 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2499066 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 2501001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3201002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3201007 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3201010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3201021 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3201023 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3201036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202001 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 3202002 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3202003 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3202005 | 0 | 0 | 17 | 0 | 0 | 0 |
| MunicipalSpending | 3202006 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 3202012 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 3202014 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202015 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3202018 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202029 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202038 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3202039 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202040 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202043 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 3202044 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202045 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202047 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3202048 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202052 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3202068 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203002 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3203005 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3203008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203023 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203033 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 3203034 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3203035 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3203036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203047 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3203050 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 3204001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3204004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3204011 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3204019 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3204046 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3204049 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3205001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3205002 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 3205006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3205007 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3205018 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 3205019 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3205021 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3205022 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3206001 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3206002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3206003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3206004 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3206005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3206014 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3206016 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3207013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3208005 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3208006 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 3208007 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3208008 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3208009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3208010 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3301001 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 3301003 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 3301005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301011 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301018 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 3301022 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301027 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301033 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3301035 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301051 | 0 | 0 | 30 | 0 | 0 | 0 |
| MunicipalSpending | 3301052 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301053 | 0 | 0 | 259 | 0 | 0 | 0 |
| MunicipalSpending | 3301054 | 0 | 0 | 32 | 0 | 0 | 0 |
| MunicipalSpending | 3301055 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 3301058 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301060 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301061 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301064 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3301065 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 3301068 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 3301070 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 3301071 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301073 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 3301074 | 0 | 0 | 40 | 0 | 0 | 0 |
| MunicipalSpending | 3301075 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301078 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301085 | 0 | 0 | 28 | 0 | 0 | 0 |
| MunicipalSpending | 3301086 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301087 | 0 | 0 | 38 | 0 | 0 | 0 |
| MunicipalSpending | 3301088 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 3301090 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301094 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301095 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 3301096 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 3301098 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301099 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3301120 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3301122 | 0 | 0 | 20 | 0 | 0 | 0 |
| MunicipalSpending | 3301124 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3301126 | 0 | 0 | 54 | 0 | 0 | 0 |
| MunicipalSpending | 3301127 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 3301128 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3302011 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3302018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3302041 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3302042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3302043 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3302044 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 3302049 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3302051 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3302070 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3302073 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3302075 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3399016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3399061 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502004 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3502008 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3502009 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502010 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 3502012 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 3502015 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3502017 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502019 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3502020 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502022 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502024 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502025 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502027 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502036 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3502037 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 3502039 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502044 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502045 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 3502046 | 0 | 0 | 52 | 0 | 0 | 0 |
| MunicipalSpending | 3502047 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 3502049 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502055 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502056 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502059 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 3502081 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502083 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502093 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502094 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502095 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3502113 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 3502116 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3601010 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3601012 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3601015 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3602001 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602002 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3602003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3602004 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3602005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3602011 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602013 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3602017 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602032 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 3602033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3602034 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3602035 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3602040 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3603010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3603019 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3604004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3701024 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 3704001 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3707021 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3708013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3903002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3903012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 3904020 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 3906011 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4001001 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4001002 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4001004 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4001007 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4001008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001018 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4001019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001021 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001022 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4001030 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4001031 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4001032 | 0 | 0 | 27 | 0 | 0 | 0 |
| MunicipalSpending | 4001033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001034 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4001035 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001039 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4001041 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4001042 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4001044 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4001046 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4001047 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4001049 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002001 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4002003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4002007 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002013 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4002016 | 0 | 0 | 31 | 0 | 0 | 0 |
| MunicipalSpending | 4002017 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002018 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4002019 | 0 | 0 | 17 | 0 | 0 | 0 |
| MunicipalSpending | 4002020 | 0 | 0 | 53 | 0 | 0 | 0 |
| MunicipalSpending | 4002021 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4002022 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4002023 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 4002025 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002026 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4002030 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4002032 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002034 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4002036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4002038 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4003001 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003002 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003006 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 4003007 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003008 | 0 | 0 | 26 | 0 | 0 | 0 |
| MunicipalSpending | 4003009 | 0 | 0 | 46 | 0 | 0 | 0 |
| MunicipalSpending | 4003010 | 0 | 0 | 71 | 0 | 0 | 0 |
| MunicipalSpending | 4003012 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 4003014 | 0 | 0 | 33 | 0 | 0 | 0 |
| MunicipalSpending | 4003015 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4003016 | 0 | 0 | 17 | 0 | 0 | 0 |
| MunicipalSpending | 4003017 | 0 | 0 | 84 | 0 | 0 | 0 |
| MunicipalSpending | 4003018 | 0 | 0 | 28 | 0 | 0 | 0 |
| MunicipalSpending | 4003019 | 0 | 0 | 23 | 0 | 0 | 0 |
| MunicipalSpending | 4003020 | 0 | 0 | 77 | 0 | 0 | 0 |
| MunicipalSpending | 4003021 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4003022 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 4003023 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4003024 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003025 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4003026 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4003028 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4003031 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4003032 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003040 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4003042 | 0 | 0 | 23 | 0 | 0 | 0 |
| MunicipalSpending | 4003043 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003044 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4003046 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4003047 | 0 | 0 | 178 | 0 | 0 | 0 |
| MunicipalSpending | 4003048 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4003049 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003052 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4003053 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4003055 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4099016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4099057 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101007 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101011 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4101014 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4101018 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101020 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4101023 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 4101024 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101025 | 0 | 0 | 42 | 0 | 0 | 0 |
| MunicipalSpending | 4101026 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4101027 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4101030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101031 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4101035 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101038 | 0 | 0 | 59 | 0 | 0 | 0 |
| MunicipalSpending | 4101042 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4101044 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4101046 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4101047 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4101063 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4101068 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4101073 | 0 | 0 | 17 | 0 | 0 | 0 |
| MunicipalSpending | 4101074 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101076 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101079 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4101092 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4101099 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4101100 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4101103 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102001 | 0 | 0 | 67 | 0 | 0 | 0 |
| MunicipalSpending | 4102002 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4102003 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4102005 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4102006 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102010 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102013 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102017 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102022 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4102023 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102024 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102026 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102028 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102035 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4102036 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4102037 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102038 | 0 | 0 | 57 | 0 | 0 | 0 |
| MunicipalSpending | 4102040 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102041 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4102042 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4102043 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4102045 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4102046 | 0 | 0 | 27 | 0 | 0 | 0 |
| MunicipalSpending | 4102047 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 4102051 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4102052 | 0 | 0 | 37 | 0 | 0 | 0 |
| MunicipalSpending | 4103004 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4103005 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4103006 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4103009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4103011 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4103015 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4103017 | 0 | 0 | 17 | 0 | 0 | 0 |
| MunicipalSpending | 4103025 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4103027 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4103047 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4103050 | 0 | 0 | 38 | 0 | 0 | 0 |
| MunicipalSpending | 4103052 | 0 | 0 | 58 | 0 | 0 | 0 |
| MunicipalSpending | 4103053 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4103054 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4103055 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4103057 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4103058 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4103060 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4103061 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4103064 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4103065 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4103067 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4103068 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4104001 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4104002 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4104004 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104005 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4104007 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4104008 | 0 | 0 | 248 | 0 | 0 | 0 |
| MunicipalSpending | 4104009 | 0 | 0 | 15 | 0 | 0 | 0 |
| MunicipalSpending | 4104010 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104012 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4104013 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104014 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4104015 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4104017 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104020 | 0 | 0 | 59 | 0 | 0 | 0 |
| MunicipalSpending | 4104022 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104023 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4104026 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4104027 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4104036 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4104042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4199019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301001 | 0 | 0 | 141 | 0 | 0 | 0 |
| MunicipalSpending | 4301003 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4301004 | 0 | 0 | 85 | 0 | 0 | 0 |
| MunicipalSpending | 4301005 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4301007 | 0 | 0 | 44 | 0 | 0 | 0 |
| MunicipalSpending | 4301009 | 0 | 0 | 7 | 0 | 0 | 0 |
| MunicipalSpending | 4301010 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4301011 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4301012 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4301013 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4301014 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4301015 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4301016 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301017 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4301018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4301019 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4301020 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301022 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4301023 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4301025 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4301026 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301027 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4301028 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4301029 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4301030 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4301031 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4301032 | 0 | 0 | 51 | 0 | 0 | 0 |
| MunicipalSpending | 4301033 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301034 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4301035 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4301037 | 0 | 0 | 112 | 0 | 0 | 0 |
| MunicipalSpending | 4301038 | 0 | 0 | 31 | 0 | 0 | 0 |
| MunicipalSpending | 4302001 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4302002 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4302012 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4302014 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4302025 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4302029 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4302042 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4302043 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4302059 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4302062 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4302063 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4302064 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4302069 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4302070 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4302073 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4302075 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4302089 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4399009 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501001 | 0 | 0 | 71 | 0 | 0 | 0 |
| MunicipalSpending | 4501003 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4501004 | 0 | 0 | 74 | 0 | 0 | 0 |
| MunicipalSpending | 4501006 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4501007 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4501008 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501010 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501013 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501018 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501026 | 0 | 0 | 39 | 0 | 0 | 0 |
| MunicipalSpending | 4501028 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 4501029 | 0 | 0 | 134 | 0 | 0 | 0 |
| MunicipalSpending | 4501031 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4501040 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4501042 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501043 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501046 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4501047 | 0 | 0 | 18 | 0 | 0 | 0 |
| MunicipalSpending | 4501048 | 0 | 0 | 34 | 0 | 0 | 0 |
| MunicipalSpending | 4501049 | 0 | 0 | 22 | 0 | 0 | 0 |
| MunicipalSpending | 4501050 | 0 | 0 | 22 | 0 | 0 | 0 |
| MunicipalSpending | 4501051 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501052 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4501054 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4501056 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4501057 | 0 | 0 | 34 | 0 | 0 | 0 |
| MunicipalSpending | 4501058 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501061 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4501063 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4501064 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4501066 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501068 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4501077 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4501079 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4501081 | 0 | 0 | 25 | 0 | 0 | 0 |
| MunicipalSpending | 4501082 | 0 | 0 | 64 | 0 | 0 | 0 |
| MunicipalSpending | 4501083 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4502001 | 0 | 0 | 72 | 0 | 0 | 0 |
| MunicipalSpending | 4502003 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4502008 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4502009 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4502010 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4502015 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4502016 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4502017 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4502020 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4502021 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4502022 | 0 | 0 | 24 | 0 | 0 | 0 |
| MunicipalSpending | 4502024 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4502025 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4502026 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4502027 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4502029 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4502032 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4502033 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4502034 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4502035 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4502037 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4502038 | 0 | 0 | 30 | 0 | 0 | 0 |
| MunicipalSpending | 4502039 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4503002 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4503003 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 4503004 | 0 | 0 | 107 | 0 | 0 | 0 |
| MunicipalSpending | 4503011 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4503012 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4503013 | 0 | 0 | 20 | 0 | 0 | 0 |
| MunicipalSpending | 4503014 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4503015 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4503016 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 4503017 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | 4503018 | 0 | 0 | 8 | 0 | 0 | 0 |
| MunicipalSpending | 4503019 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4503021 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4503022 | 0 | 0 | 28 | 0 | 0 | 0 |
| MunicipalSpending | 4503023 | 0 | 0 | 14 | 0 | 0 | 0 |
| MunicipalSpending | 4503024 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4503028 | 0 | 0 | 39 | 0 | 0 | 0 |
| MunicipalSpending | 4503030 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4503031 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4503032 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4503035 | 0 | 0 | 20 | 0 | 0 | 0 |
| MunicipalSpending | 4503036 | 0 | 0 | 9 | 0 | 0 | 0 |
| MunicipalSpending | 4599001 | 0 | 0 | 22 | 0 | 0 | 0 |
| MunicipalSpending | 4599002 | 0 | 0 | 44 | 0 | 0 | 0 |
| MunicipalSpending | 4599003 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4599004 | 0 | 0 | 5 | 0 | 0 | 0 |
| MunicipalSpending | 4599005 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4599006 | 0 | 0 | 15 | 0 | 0 | 0 |
| MunicipalSpending | 4599007 | 0 | 0 | 16 | 0 | 0 | 0 |
| MunicipalSpending | 4599008 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4599009 | 0 | 0 | 12 | 0 | 0 | 0 |
| MunicipalSpending | 4599010 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4599011 | 0 | 0 | 32 | 0 | 0 | 0 |
| MunicipalSpending | 4599013 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4599014 | 0 | 0 | 2 | 0 | 0 | 0 |
| MunicipalSpending | 4599015 | 0 | 0 | 1 | 0 | 0 | 0 |
| MunicipalSpending | 4599016 | 0 | 0 | 65 | 0 | 0 | 0 |
| MunicipalSpending | 4599017 | 0 | 0 | 34 | 0 | 0 | 0 |
| MunicipalSpending | 4599018 | 0 | 0 | 27 | 0 | 0 | 0 |
| MunicipalSpending | 4599019 | 0 | 0 | 29 | 0 | 0 | 0 |
| MunicipalSpending | 4599020 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4599021 | 0 | 0 | 6 | 0 | 0 | 0 |
| MunicipalSpending | 4599023 | 0 | 0 | 89 | 0 | 0 | 0 |
| MunicipalSpending | 4599025 | 0 | 0 | 26 | 0 | 0 | 0 |
| MunicipalSpending | 4599026 | 0 | 0 | 3 | 0 | 0 | 0 |
| MunicipalSpending | 4599028 | 0 | 0 | 25 | 0 | 0 | 0 |
| MunicipalSpending | 4599029 | 0 | 0 | 13 | 0 | 0 | 0 |
| MunicipalSpending | 4599030 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4599031 | 0 | 0 | 260 | 0 | 0 | 0 |
| MunicipalSpending | 4599032 | 0 | 0 | 10 | 0 | 0 | 0 |
| MunicipalSpending | 4599033 | 0 | 0 | 26 | 0 | 0 | 0 |
| MunicipalSpending | 4599034 | 0 | 0 | 15 | 0 | 0 | 0 |
| MunicipalSpending | 4599036 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4599037 | 0 | 0 | 4 | 0 | 0 | 0 |
| MunicipalSpending | 4599038 | 0 | 0 | 11 | 0 | 0 | 0 |
| MunicipalSpending | NO APLICA | 0 | 0 | 9,252 | 0 | 0 | 0 |

**MunicipalIncome.1.1.01.02.300**

- inconsistent (1 municipalities): Tinjacá (Boyacá), 20241201: children add up to 63147310.

**MunicipalSpending.0401020**

- inconsistent (1 municipalities): Gutiérrez (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.0401094**

- inconsistent (1 municipalities): Santiago (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.0401101**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.0401102**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villa de San Diego de Ubaté (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.0401104**

- inconsistent (1 municipalities): Gutiérrez (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.0401105**

- inconsistent (6 municipalities): Villavicencio (Meta) [3], Riohacha (La Guajira) [2], Palmira (Valle Del Cauca) [2], Galapa (Atlántico) [1], Vetas (Santander) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.0402013**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.0406001**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.0406003**

- inconsistent (2 municipalities): San Bernardo (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.0406004**

- inconsistent (2 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.0406016**

- inconsistent (5 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1102001**

- inconsistent (1 municipalities): Murindó (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202001**

- inconsistent (3 municipalities): Barrancas (La Guajira), 20251201: payments above obligations or obligations above commitments; Barrancas (La Guajira), 20260601: payments above obligations or obligations above commitments; Guaca (Santander), 20241201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202002**

- inconsistent (23 municipalities): Sabanalarga (Atlántico) [16], Los Palmitos (Sucre) [9], Usiacurí (Atlántico) [8], Chámeza (Casanare) [7], Santa Lucía (Atlántico) [4], Villanueva (Bolívar) [3], Medellín (Antioquia) [2], San Bernardo (Cundinamarca) [2], Guaca (Santander) [2], Sabanas de San Ángel (Magdalena) [2], Siachoque (Boyacá) [2], Quípama (Boyacá) [2] and 11 more.

**MunicipalSpending.1202003**

- inconsistent (2 municipalities): Regidor (Bolívar), 20260601: payments above obligations or obligations above commitments; Tame (Arauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202004**

- inconsistent (4 municipalities): Altos del Rosario (Bolívar) [10], Guataquí (Cundinamarca) [2], Los Santos (Santander) [1], Puerto Guzmán (Putumayo) [1].

**MunicipalSpending.1202005**

- inconsistent (2 municipalities): Santa Bárbara (Santander), 20231201: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1202006**

- inconsistent (1 municipalities): Matanza (Santander), 20231201: payments above obligations or obligations above commitments; Matanza (Santander), 20231201: payments above obligations or obligations above commitments; Matanza (Santander), 20241201: payments above obligations or obligations above commitments; Matanza (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202007**

- inconsistent (3 municipalities): San Antero (Córdoba) [9], Pivijay (Magdalena) [3], Villanueva (Bolívar) [1].

**MunicipalSpending.1202008**

- inconsistent (1 municipalities): Arroyohondo (Bolívar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1202012**

- inconsistent (1 municipalities): Yacuanquer (Nariño), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202013**

- inconsistent (1 municipalities): Natagaima (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202014**

- inconsistent (6 municipalities): Iles (Nariño) [10], Ovejas (Sucre) [7], Los Santos (Santander) [3], San Francisco (Putumayo) [2], Tunja (Boyacá) [1], Los Andes (Nariño) [1].

**MunicipalSpending.1202018**

- inconsistent (4 municipalities): Iles (Nariño), 20251201: payments above obligations or obligations above commitments; Imués (Nariño), 20260601: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20241201: payments above obligations or obligations above commitments; Coyaima (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202019**

- inconsistent (6 municipalities): Contratación (Santander) [3], Yacuanquer (Nariño) [2], Venadillo (Tolima) [2], Tunja (Boyacá) [1], Iles (Nariño) [1], Puerto Parra (Santander) [1].

**MunicipalSpending.1202020**

- inconsistent (4 municipalities): Usiacurí (Atlántico) [10], Tunja (Boyacá) [2], Iles (Nariño) [1], Santa Bárbara (Santander) [1].

**MunicipalSpending.1202023**

- inconsistent (4 municipalities): Iles (Nariño) [9], Pajarito (Boyacá) [2], Gómez Plata (Antioquia) [1], Inzá (Cauca) [1].

**MunicipalSpending.1202024**

- inconsistent (1 municipalities): Iles (Nariño), 20260601: payments above obligations or obligations above commitments; Iles (Nariño), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1202026**

- inconsistent (1 municipalities): San Jerónimo (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1202031**

- inconsistent (2 municipalities): Galapa (Atlántico) [12], Anolaima (Cundinamarca) [1].

**MunicipalSpending.1203001**

- inconsistent (5 municipalities): La Salina (Casanare) [8], Santiago (Putumayo) [5], Contratación (Santander) [4], Maripí (Boyacá) [1], Ráquira (Boyacá) [1].

**MunicipalSpending.1203002**

- inconsistent (7 municipalities): Ariguaní (Magdalena) [6], Santacruz (Nariño) [6], San Bernardo (Cundinamarca) [2], Aratoca (Santander) [1], Coromoro (Santander) [1], Tame (Arauca) [1], Santiago (Putumayo) [1].

**MunicipalSpending.1203003**

- inconsistent (1 municipalities): Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments; Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1203004**

- inconsistent (2 municipalities): Tibacuy (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Matanza (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1203005**

- inconsistent (1 municipalities): Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1203009**

- inconsistent (4 municipalities): Tibacuy (Cundinamarca) [4], Cachipay (Cundinamarca) [3], Viotá (Cundinamarca) [3], Anolaima (Cundinamarca) [1].

**MunicipalSpending.1203010**

- inconsistent (2 municipalities): Sampués (Sucre) [8], Guaranda (Sucre) [1].

**MunicipalSpending.1203011**

- inconsistent (7 municipalities): Tierralta (Córdoba) [14], Chinú (Córdoba) [3], Barichara (Santander) [2], Sampués (Sucre) [2], Cachipay (Cundinamarca) [1], Gutiérrez (Cundinamarca) [1], Potosí (Nariño) [1].

**MunicipalSpending.1203014**

- inconsistent (1 municipalities): Tibacuy (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1204018**

- inconsistent (2 municipalities): Cucunubá (Cundinamarca), 20241201: payments above obligations or obligations above commitments; San Joaquín (Santander), 20251201: payments above obligations or obligations above commitments; San Joaquín (Santander), 20251201: payments above obligations or obligations above commitments; San Joaquín (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1205001**

- inconsistent (1 municipalities): San Miguel de Sema (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1205005**

- inconsistent (2 municipalities): Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1205006**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1205008**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206002**

- inconsistent (1 municipalities): Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206003**

- inconsistent (2 municipalities): Valdivia (Antioquia), 20231201: payments above obligations or obligations above commitments; Valle de San José (Santander), 20251201: payments above obligations or obligations above commitments; Valle de San José (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1206004**

- inconsistent (2 municipalities): Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206005**

- inconsistent (2 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206006**

- inconsistent (1 municipalities): Muzo (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206007**

- inconsistent (23 municipalities): Pailitas (Cesar) [3], Tame (Arauca) [2], Toribío (Cauca) [2], Chaparral (Tolima) [2], San Antero (Córdoba) [2], Sabana de Torres (Santander) [2], Villavicencio (Meta) [2], Altos del Rosario (Bolívar) [1], Matanza (Santander) [1], Puerto Caicedo (Putumayo) [1], Puerto Rondón (Arauca) [1], Sampués (Sucre) [1] and 11 more.

**MunicipalSpending.1206008**

- inconsistent (6 municipalities): San Vicente de Chucurí (Santander) [2], Iles (Nariño) [1], Albania (Santander) [1], San Luis (Tolima) [1], Puerto Rondón (Arauca) [1], Tame (Arauca) [1].

**MunicipalSpending.1206010**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206012**

- inconsistent (1 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1206018**

- inconsistent (2 municipalities): Marquetalia (Caldas), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207002**

- inconsistent (1 municipalities): Marquetalia (Caldas), 20231201: payments above obligations or obligations above commitments; Marquetalia (Caldas), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207011**

- inconsistent (2 municipalities): Marquetalia (Caldas), 20231201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207012**

- inconsistent (1 municipalities): Tuluá (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207014**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207015**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207017**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1207018**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1299001**

- inconsistent (1 municipalities): Sasaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1299065**

- inconsistent (1 municipalities): Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1399064**

- inconsistent (1 municipalities): Villanueva (Bolívar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1501005**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702007**

- inconsistent (22 municipalities): Chaparral (Tolima) [6], Oiba (Santander) [4], Villavicencio (Meta) [3], Puerto Guzmán (Putumayo) [3], Cucunubá (Cundinamarca) [3], Iles (Nariño) [2], Lebrija (Santander) [2], Nueva Granada (Magdalena) [2], Nocaima (Cundinamarca) [1], Valle de San José (Santander) [1], Puerto Caicedo (Putumayo) [1], Orito (Putumayo) [1] and 10 more.

**MunicipalSpending.1702009**

- inconsistent (10 municipalities): Riohacha (La Guajira) [2], Medellín (Antioquia) [1], San Jerónimo (Antioquia) [1], San Estanislao (Bolívar) [1], Anolaima (Cundinamarca) [1], Sasaima (Cundinamarca) [1], Susa (Cundinamarca) [1], San Luis (Tolima) [1], Puerto Caicedo (Putumayo) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.1702010**

- inconsistent (54 municipalities): Tierralta (Córdoba) [14], Nocaima (Cundinamarca) [12], Toledo (Norte De Santander) [11], Fúquene (Cundinamarca) [9], Luruaco (Atlántico) [8], Gutiérrez (Cundinamarca) [8], Riohacha (La Guajira) [4], Cucunubá (Cundinamarca) [4], Contratación (Santander) [4], Quebradanegra (Cundinamarca) [4], Tibacuy (Cundinamarca) [4], Cachipay (Cundinamarca) [3] and 42 more.

**MunicipalSpending.1702011**

- inconsistent (5 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Sitionuevo (Magdalena), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments; Matanza (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702014**

- inconsistent (1 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1702016**

- inconsistent (5 municipalities): Toribío (Cauca) [5], San Joaquín (Santander) [2], Bolívar (Santander) [1], Venadillo (Tolima) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.1702017**

- inconsistent (11 municipalities): Altos del Rosario (Bolívar) [10], Zipacón (Cundinamarca) [4], Cucunubá (Cundinamarca) [2], Aratoca (Santander) [2], Guavatá (Santander) [2], Sabana de Torres (Santander) [2], San Bernardo (Cundinamarca) [1], Ariguaní (Magdalena) [1], Yacuanquer (Nariño) [1], Venadillo (Tolima) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.1702021**

- inconsistent (9 municipalities): Los Palmitos (Sucre) [9], Jamundí (Valle Del Cauca) [2], Juan de Acosta (Atlántico) [1], San Bernardo (Cundinamarca) [1], Viotá (Cundinamarca) [1], Barrancas (La Guajira) [1], Sitionuevo (Magdalena) [1], Villavicencio (Meta) [1], Caicedonia (Valle Del Cauca) [1].

**MunicipalSpending.1702023**

- inconsistent (3 municipalities): Sitionuevo (Magdalena) [9], San Joaquín (Santander) [2], Coromoro (Santander) [1].

**MunicipalSpending.1702024**

- inconsistent (6 municipalities): Iles (Nariño) [15], Mocoa (Putumayo) [6], Gómez Plata (Antioquia) [1], Pailitas (Cesar) [1], Dosquebradas (Risaralda) [1], Oiba (Santander) [1].

**MunicipalSpending.1702025**

- inconsistent (1 municipalities): Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702032**

- inconsistent (2 municipalities): San Bernardo del Viento (Córdoba), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702035**

- inconsistent (3 municipalities): Guapotá (Santander), 20251201: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments; San Joaquín (Santander), 20251201: payments above obligations or obligations above commitments; San Joaquín (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1702037**

- inconsistent (6 municipalities): Acacías (Meta), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Guapotá (Santander), 20251201: payments above obligations or obligations above commitments; Guavatá (Santander), 20260601: payments above obligations or obligations above commitments; Coloso (Sucre), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702038**

- inconsistent (13 municipalities): Toribío (Cauca) [13], Guadalupe (Santander) [2], Landázuri (Santander) [2], El Colegio (Cundinamarca) [1], Barrancas (La Guajira) [1], Dosquebradas (Risaralda) [1], Galán (Santander) [1], Guavatá (Santander) [1], Lebrija (Santander) [1], Chaparral (Tolima) [1], Venadillo (Tolima) [1], Caicedonia (Valle Del Cauca) [1] and 1 more.

**MunicipalSpending.1702040**

- inconsistent (1 municipalities): Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1702042**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1702044**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1702045**

- inconsistent (2 municipalities): Gutiérrez (Cundinamarca) [4], Nocaima (Cundinamarca) [4].

**MunicipalSpending.1703008**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1703009**

- inconsistent (2 municipalities): Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1704002**

- inconsistent (1 municipalities): Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments; Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1704006**

- inconsistent (1 municipalities): San Bernardo del Viento (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1704010**

- inconsistent (1 municipalities): Guaca (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1704046**

- inconsistent (1 municipalities): San Bernardo del Viento (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1706004**

- inconsistent (1 municipalities): Coromoro (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1706008**

- inconsistent (1 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1707030**

- inconsistent (1 municipalities): Arenal (Bolívar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1707042**

- inconsistent (2 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Jordán (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1707043**

- inconsistent (2 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1707069**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1708018**

- inconsistent (3 municipalities): San Pablo de Borbur (Boyacá), 20260601: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1708032**

- inconsistent (2 municipalities): Matanza (Santander), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1708040**

- inconsistent (2 municipalities): San Joaquín (Santander), 20251201: payments above obligations or obligations above commitments; San Joaquín (Santander), 20260601: payments above obligations or obligations above commitments; Sabanalarga (Casanare), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1708041**

- inconsistent (13 municipalities): San Luis de Palenque (Casanare) [3], La Jagua de Ibirico (Cesar) [2], Susa (Cundinamarca) [2], Villavicencio (Meta) [2], San Joaquín (Santander) [2], Santa Bárbara (Santander) [2], Valle de San José (Santander) [2], Nemocón (Cundinamarca) [1], Nimaima (Cundinamarca) [1], Coromoro (Santander) [1], Jordán (Santander) [1], Tame (Arauca) [1] and 1 more.

**MunicipalSpending.1708055**

- inconsistent (1 municipalities): Toribío (Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1708056**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709013**

- inconsistent (1 municipalities): Toribío (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709016**

- inconsistent (1 municipalities): Gutiérrez (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709040**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709043**

- inconsistent (1 municipalities): Prado (Tolima), 20260601: payments above obligations or obligations above commitments; Prado (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1709052**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709059**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709062**

- inconsistent (1 municipalities): San Luis de Palenque (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1709065**

- inconsistent (2 municipalities): Anolaima (Cundinamarca) [6], Chaparral (Tolima) [3].

**MunicipalSpending.1709078**

- inconsistent (2 municipalities): Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; El Colegio (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709081**

- inconsistent (4 municipalities): Bolívar (Cauca) [2], Nemocón (Cundinamarca) [2], La Virginia (Risaralda) [2], Gutiérrez (Cundinamarca) [1].

**MunicipalSpending.1709084**

- inconsistent (1 municipalities): Oiba (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709092**

- inconsistent (2 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709099**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709105**

- inconsistent (4 municipalities): Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments; Charta (Santander), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20241201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20241201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1709106**

- inconsistent (3 municipalities): Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; San Joaquín (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1709112**

- inconsistent (3 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villanueva (Santander), 20231201: payments above obligations or obligations above commitments; Villanueva (Santander), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1709114**

- inconsistent (5 municipalities): Nocaima (Cundinamarca) [3], Nemocón (Cundinamarca) [2], Albania (Santander) [2], Piamonte (Cauca) [1], Chinú (Córdoba) [1].

**MunicipalSpending.1710001**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments; Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1901008**

- inconsistent (1 municipalities): Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1901011**

- inconsistent (1 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901084**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901095**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1901100**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1901119**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901127**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901129**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901159**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1901163**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1902010**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1902016**

- inconsistent (1 municipalities): Manaure Balcón del Cesar (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903001**

- inconsistent (3 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments; Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903002**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903003**

- inconsistent (4 municipalities): Malambo (Atlántico), 20251201: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments; Los Santos (Santander), 20251201: payments above obligations or obligations above commitments; Santiago (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903004**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903011**

- inconsistent (24 municipalities): Iles (Nariño) [14], Usiacurí (Atlántico) [9], Galapa (Atlántico) [8], Santacruz (Nariño) [6], Barrancas (La Guajira) [5], Tame (Arauca) [5], Tunja (Boyacá) [5], Aratoca (Santander) [2], Toribío (Cauca) [2], San Bernardo del Viento (Córdoba) [2], Tierralta (Córdoba) [2], Oiba (Santander) [2] and 12 more.

**MunicipalSpending.1903015**

- inconsistent (5 municipalities): Dosquebradas (Risaralda) [3], Villavicencio (Meta) [2], Palmira (Valle Del Cauca) [1], La Salina (Casanare) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1].

**MunicipalSpending.1903016**

- inconsistent (11 municipalities): Tunja (Boyacá) [1], Bolívar (Cauca) [1], Montería (Córdoba) [1], Tierralta (Córdoba) [1], Yacuanquer (Nariño) [1], Confines (Santander) [1], Los Santos (Santander) [1], San Joaquín (Santander) [1], Coyaima (Tolima) [1], Icononzo (Tolima) [1], Venadillo (Tolima) [1].

**MunicipalSpending.1903019**

- inconsistent (1 municipalities): Villanueva (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903020**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903022**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903023**

- inconsistent (11 municipalities): Iles (Nariño) [5], Tunja (Boyacá) [3], Pailitas (Cesar) [2], Belén (Nariño) [2], Dosquebradas (Risaralda) [2], La Salina (Casanare) [2], Mocoa (Putumayo) [2], Puerto Boyacá (Boyacá) [1], Bosconia (Cesar) [1], Pelaya (Cesar) [1], Cereté (Córdoba) [1].

**MunicipalSpending.1903025**

- inconsistent (5 municipalities): Tunja (Boyacá) [5], Dosquebradas (Risaralda) [4], Tierralta (Córdoba) [2], Palmira (Valle Del Cauca) [2], Villavicencio (Meta) [1].

**MunicipalSpending.1903026**

- inconsistent (1 municipalities): Venadillo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903027**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Carmen de Apicalá (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903030**

- inconsistent (1 municipalities): Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1903031**

- inconsistent (8 municipalities): Villa de San Diego de Ubaté (Cundinamarca) [2], Villavicencio (Meta) [2], Tunja (Boyacá) [1], Toledo (Norte De Santander) [1], Dosquebradas (Risaralda) [1], Coyaima (Tolima) [1], Palmira (Valle Del Cauca) [1], Puerto Guzmán (Putumayo) [1].

**MunicipalSpending.1903032**

- inconsistent (1 municipalities): Iles (Nariño), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1903034**

- inconsistent (6 municipalities): Tunja (Boyacá) [2], Montería (Córdoba) [2], Iles (Nariño) [2], Palmira (Valle Del Cauca) [2], Villagarzón (Putumayo) [2], Mosquera (Nariño) [1].

**MunicipalSpending.1903035**

- inconsistent (3 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Venadillo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903038**

- inconsistent (4 municipalities): Dosquebradas (Risaralda) [5], Tunja (Boyacá) [1], San Pablo de Borbur (Boyacá) [1], Barrancas (La Guajira) [1].

**MunicipalSpending.1903041**

- inconsistent (3 municipalities): Viotá (Cundinamarca) [3], Dosquebradas (Risaralda) [2], San Francisco (Putumayo) [2].

**MunicipalSpending.1903042**

- inconsistent (4 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Viotá (Cundinamarca), 20231201: payments above obligations or obligations above commitments; San Francisco (Putumayo), 20241201: payments above obligations or obligations above commitments; San Francisco (Putumayo), 20241201: payments above obligations or obligations above commitments; San Francisco (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903045**

- inconsistent (2 municipalities): La Llanada (Nariño), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903046**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903047**

- inconsistent (1 municipalities): Sasaima (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903050**

- inconsistent (1 municipalities): Chimichagua (Cesar), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1903051**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1903057**

- inconsistent (2 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1904017**

- inconsistent (1 municipalities): San Luis de Palenque (Casanare), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905001**

- inconsistent (2 municipalities): Juan de Acosta (Atlántico), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905003**

- inconsistent (2 municipalities): Oiba (Santander), 20260601: payments above obligations or obligations above commitments; Tame (Arauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905004**

- inconsistent (1 municipalities): Sabana de Torres (Santander), 20231201: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905005**

- inconsistent (1 municipalities): Puerto Rondón (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905013**

- inconsistent (1 municipalities): Iles (Nariño), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905014**

- inconsistent (5 municipalities): Jamundí (Valle Del Cauca) [6], Dosquebradas (Risaralda) [3], Montería (Córdoba) [2], Nueva Granada (Magdalena) [1], Recetor (Casanare) [1].

**MunicipalSpending.1905015**

- inconsistent (15 municipalities): Riohacha (La Guajira) [5], Montería (Córdoba) [4], Villa de San Diego de Ubaté (Cundinamarca) [4], Toribío (Cauca) [3], Yacuanquer (Nariño) [2], Puerto Guzmán (Putumayo) [2], San Estanislao (Bolívar) [1], La Jagua de Ibirico (Cesar) [1], Anolaima (Cundinamarca) [1], Chachagüí (Nariño) [1], Guadalupe (Santander) [1], Carmen de Apicalá (Tolima) [1] and 3 more.

**MunicipalSpending.1905016**

- inconsistent (1 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905017**

- inconsistent (1 municipalities): Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905019**

- inconsistent (24 municipalities): Riohacha (La Guajira) [5], Montería (Córdoba) [3], Villavicencio (Meta) [3], Chaparral (Tolima) [2], Cereté (Córdoba) [2], Gutiérrez (Cundinamarca) [2], Villanueva (Bolívar) [1], Sibundoy (Putumayo) [1], Puerto Guzmán (Putumayo) [1], Puerto Caicedo (Putumayo) [1], Sácama (Casanare) [1], La Salina (Casanare) [1] and 12 more.

**MunicipalSpending.1905020**

- inconsistent (17 municipalities): Piamonte (Cauca) [3], Riohacha (La Guajira) [3], Toribío (Cauca) [2], Venadillo (Tolima) [2], Juan de Acosta (Atlántico) [1], Los Santos (Santander) [1], Santiago (Putumayo) [1], Jamundí (Valle Del Cauca) [1], Suaita (Santander) [1], Palmar (Santander) [1], Magüí (Nariño) [1], Barichara (Santander) [1] and 5 more.

**MunicipalSpending.1905021**

- inconsistent (31 municipalities): Riohacha (La Guajira) [4], Villavicencio (Meta) [3], Venadillo (Tolima) [2], Toribío (Cauca) [2], Pailitas (Cesar) [2], Los Santos (Santander) [2], Malambo (Atlántico) [2], Mocoa (Putumayo) [1], San Luis de Palenque (Casanare) [1], Jamundí (Valle Del Cauca) [1], Guadalupe (Santander) [1], Sibundoy (Putumayo) [1] and 19 more.

**MunicipalSpending.1905022**

- inconsistent (30 municipalities): Tunja (Boyacá) [4], Riohacha (La Guajira) [3], Malambo (Atlántico) [2], Villavicencio (Meta) [2], Puerto Guzmán (Putumayo) [2], Pailitas (Cesar) [2], Cereté (Córdoba) [2], Venadillo (Tolima) [2], Tierralta (Córdoba) [2], Juan de Acosta (Atlántico) [1], Sampués (Sucre) [1], Suaita (Santander) [1] and 18 more.

**MunicipalSpending.1905023**

- inconsistent (10 municipalities): Piamonte (Cauca) [2], Riohacha (La Guajira) [2], Los Santos (Santander) [2], Venadillo (Tolima) [2], Medellín (Antioquia) [1], Malambo (Atlántico) [1], Magüí (Nariño) [1], Barichara (Santander) [1], Suaita (Santander) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.1905024**

- inconsistent (27 municipalities): Villavicencio (Meta) [7], Dosquebradas (Risaralda) [4], Riohacha (La Guajira) [3], Jamundí (Valle Del Cauca) [2], Venadillo (Tolima) [2], Toribío (Cauca) [2], Palmar (Santander) [2], Los Santos (Santander) [2], Gómez Plata (Antioquia) [1], Palmira (Valle Del Cauca) [1], Carmen de Apicalá (Tolima) [1], Sampués (Sucre) [1] and 15 more.

**MunicipalSpending.1905025**

- inconsistent (19 municipalities): Riohacha (La Guajira) [4], Los Santos (Santander) [2], Malambo (Atlántico) [2], Juan de Acosta (Atlántico) [1], Puerto Guzmán (Putumayo) [1], Puerto Caicedo (Putumayo) [1], Mocoa (Putumayo) [1], Jamundí (Valle Del Cauca) [1], Palmar (Santander) [1], Oiba (Santander) [1], Barichara (Santander) [1], Jordán (Santander) [1] and 7 more.

**MunicipalSpending.1905026**

- inconsistent (17 municipalities): Riohacha (La Guajira) [7], Puerto Guzmán (Putumayo) [3], Jamundí (Valle Del Cauca) [2], Santa Lucía (Atlántico) [2], Malambo (Atlántico) [2], Tunja (Boyacá) [2], Villavicencio (Meta) [2], Tierralta (Córdoba) [1], San Bernardo del Viento (Córdoba) [1], Cerro de San Antonio (Magdalena) [1], Toribío (Cauca) [1], Barichara (Santander) [1] and 5 more.

**MunicipalSpending.1905027**

- inconsistent (30 municipalities): Toribío (Cauca) [4], Malambo (Atlántico) [2], Mocoa (Putumayo) [2], Villavicencio (Meta) [2], Riohacha (La Guajira) [2], Los Santos (Santander) [2], Piamonte (Cauca) [2], Inzá (Cauca) [2], Puerto Guzmán (Putumayo) [1], Santiago (Putumayo) [1], Oiba (Santander) [1], Sácama (Casanare) [1] and 18 more.

**MunicipalSpending.1905028**

- inconsistent (27 municipalities): Riohacha (La Guajira) [6], Venadillo (Tolima) [3], Malambo (Atlántico) [2], Los Santos (Santander) [2], Dosquebradas (Risaralda) [2], San Jerónimo (Antioquia) [1], Guadalupe (Santander) [1], Puerto Guzmán (Putumayo) [1], Puerto Caicedo (Putumayo) [1], Mocoa (Putumayo) [1], Jamundí (Valle Del Cauca) [1], Coloso (Sucre) [1] and 15 more.

**MunicipalSpending.1905029**

- inconsistent (5 municipalities): Fúquene (Cundinamarca) [3], Barrancas (La Guajira) [2], Circasia (Quindío) [1], Los Santos (Santander) [1], Natagaima (Tolima) [1].

**MunicipalSpending.1905030**

- inconsistent (6 municipalities): Toribío (Cauca) [2], Tierralta (Córdoba) [1], Los Santos (Santander) [1], Palmar (Santander) [1], Natagaima (Tolima) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.1905031**

- inconsistent (28 municipalities): Villavicencio (Meta) [6], Riohacha (La Guajira) [4], Tunja (Boyacá) [4], Toribío (Cauca) [3], Montería (Córdoba) [3], Anolaima (Cundinamarca) [3], Pailitas (Cesar) [2], Malambo (Atlántico) [1], Sampués (Sucre) [1], Carmen de Apicalá (Tolima) [1], Coyaima (Tolima) [1], Puerto Caicedo (Putumayo) [1] and 16 more.

**MunicipalSpending.1905035**

- inconsistent (9 municipalities): Tunja (Boyacá) [2], Chinú (Córdoba) [2], Sampués (Sucre) [2], San Francisco (Putumayo) [2], Malambo (Atlántico) [1], Bolívar (Cauca) [1], San Bernardo (Cundinamarca) [1], Pivijay (Magdalena) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.1905036**

- inconsistent (7 municipalities): Palmira (Valle Del Cauca) [4], Santacruz (Nariño) [2], Sibundoy (Putumayo) [2], Tierralta (Córdoba) [1], Jamundí (Valle Del Cauca) [1], Tame (Arauca) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.1905037**

- inconsistent (3 municipalities): Ariguaní (Magdalena), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Los Santos (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905040**

- inconsistent (3 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; San Bernardo del Viento (Córdoba), 20260601: payments above obligations or obligations above commitments; Guadalupe (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905041**

- inconsistent (2 municipalities): Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905042**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905043**

- inconsistent (6 municipalities): Dosquebradas (Risaralda) [2], Tierralta (Córdoba) [1], Riohacha (La Guajira) [1], Magüí (Nariño) [1], Mocoa (Putumayo) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.1905049**

- inconsistent (17 municipalities): Guapotá (Santander) [2], Ciudad Bolívar (Antioquia) [1], Villavicencio (Meta) [1], Mocoa (Putumayo) [1], La Salina (Casanare) [1], Tame (Arauca) [1], Chaparral (Tolima) [1], Suaita (Santander) [1], Ariguaní (Magdalena) [1], Sabanalarga (Atlántico) [1], El Colegio (Cundinamarca) [1], Anolaima (Cundinamarca) [1] and 5 more.

**MunicipalSpending.1905050**

- inconsistent (9 municipalities): Piamonte (Cauca) [2], Oiba (Santander) [2], Pajarito (Boyacá) [1], San Bernardo del Viento (Córdoba) [1], Villavicencio (Meta) [1], Iles (Nariño) [1], La Salina (Casanare) [1], Recetor (Casanare) [1], San Luis de Palenque (Casanare) [1].

**MunicipalSpending.1905051**

- inconsistent (1 municipalities): Los Santos (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905052**

- inconsistent (1 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1905053**

- inconsistent (2 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1905054**

- inconsistent (27 municipalities): Pailitas (Cesar) [3], Villavicencio (Meta) [3], Tame (Arauca) [3], Inzá (Cauca) [2], Gómez Plata (Antioquia) [2], Cereté (Córdoba) [2], Dosquebradas (Risaralda) [2], Tunja (Boyacá) [2], Puerto Guzmán (Putumayo) [2], Oiba (Santander) [2], Mocoa (Putumayo) [1], Los Palmitos (Sucre) [1] and 15 more.

**MunicipalSpending.1906001**

- inconsistent (3 municipalities): Imués (Nariño), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1906004**

- inconsistent (38 municipalities): Villavicencio (Meta) [6], La Jagua de Ibirico (Cesar) [4], Confines (Santander) [3], Dosquebradas (Risaralda) [3], Sampués (Sucre) [2], San Pablo (Bolívar) [2], Albania (Santander) [2], Cereté (Córdoba) [2], Villanueva (Santander) [1], Palmar (Santander) [1], Valle de San José (Santander) [1], Vetas (Santander) [1] and 26 more.

**MunicipalSpending.1906005**

- inconsistent (3 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Los Santos (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906006**

- inconsistent (1 municipalities): Venadillo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906007**

- inconsistent (1 municipalities): El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906022**

- inconsistent (2 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Guadalupe (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906023**

- inconsistent (2 municipalities): Galapa (Atlántico), 20251201: payments above obligations or obligations above commitments; Galapa (Atlántico), 20251201: payments above obligations or obligations above commitments; Pailitas (Cesar), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906024**

- inconsistent (1 municipalities): Venadillo (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906025**

- inconsistent (1 municipalities): San Joaquín (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906026**

- inconsistent (2 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906028**

- inconsistent (3 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1906029**

- inconsistent (5 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Bolívar (Cauca), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Oiba (Santander), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906030**

- inconsistent (3 municipalities): Contratación (Santander), 20241201: payments above obligations or obligations above commitments; Los Santos (Santander), 20251201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906031**

- inconsistent (2 municipalities): Barrancas (La Guajira), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906032**

- inconsistent (1 municipalities): Venadillo (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906033**

- inconsistent (1 municipalities): Venadillo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906035**

- inconsistent (2 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1906037**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906041**

- inconsistent (2 municipalities): Barichara (Santander), 20260601: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1906043**

- inconsistent (1 municipalities): Charta (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.1906044**

- inconsistent (12 municipalities): Pelaya (Cesar) [4], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [3], San Estanislao (Bolívar) [2], Usiacurí (Atlántico) [1], Villa de San Diego de Ubaté (Cundinamarca) [1], Zipacón (Cundinamarca) [1], Los Santos (Santander) [1], Guamo (Tolima) [1], Prado (Tolima) [1], La Salina (Casanare) [1], Sácama (Casanare) [1], Orito (Putumayo) [1].

**MunicipalSpending.1999050**

- inconsistent (1 municipalities): Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1999055**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.1999056**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2101002**

- inconsistent (2 municipalities): Sitionuevo (Magdalena), 20241201: payments above obligations or obligations above commitments; Albania (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2101003**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2101009**

- inconsistent (2 municipalities): Albania (Santander), 20241201: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2101011**

- inconsistent (3 municipalities): El Cocuy (Boyacá), 20241201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20231201: payments above obligations or obligations above commitments; Barrancas (La Guajira), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2101015**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2101016**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102001**

- inconsistent (1 municipalities): Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments; Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102007**

- inconsistent (1 municipalities): Guaranda (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2102008**

- inconsistent (2 municipalities): Pueblo Nuevo (Córdoba), 20231201: payments above obligations or obligations above commitments; Guaranda (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2102009**

- inconsistent (1 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102010**

- inconsistent (6 municipalities): Susa (Cundinamarca) [5], Landázuri (Santander) [3], San Pelayo (Córdoba) [2], Palmar (Santander) [1], San Luis (Tolima) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.2102011**

- inconsistent (27 municipalities): Guavatá (Santander) [6], Palmar (Santander) [3], Chaparral (Tolima) [3], Confines (Santander) [2], Puerto Rondón (Arauca) [2], Guamo (Tolima) [2], Iles (Nariño) [2], Suaita (Santander) [2], Toribío (Cauca) [2], San Pedro (Valle Del Cauca) [1], Jamundí (Valle Del Cauca) [1], Venadillo (Tolima) [1] and 15 more.

**MunicipalSpending.2102012**

- inconsistent (2 municipalities): El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments; Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102013**

- inconsistent (14 municipalities): Guataquí (Cundinamarca) [4], San Pablo de Borbur (Boyacá) [3], Quebradanegra (Cundinamarca) [3], Pelaya (Cesar) [2], Puerto Rondón (Arauca) [2], Gómez Plata (Antioquia) [1], Galapa (Atlántico) [1], Nemocón (Cundinamarca) [1], Susa (Cundinamarca) [1], Confines (Santander) [1], Guadalupe (Santander) [1], Vetas (Santander) [1] and 2 more.

**MunicipalSpending.2102014**

- inconsistent (3 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments; Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Toribío (Cauca), 20241201: payments above obligations or obligations above commitments; Suaita (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102015**

- inconsistent (2 municipalities): Murindó (Antioquia), 20231201: payments above obligations or obligations above commitments; Murindó (Antioquia), 20231201: payments above obligations or obligations above commitments; Bolívar (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102021**

- inconsistent (1 municipalities): Bolívar (Santander), 20231201: payments above obligations or obligations above commitments; Bolívar (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102024**

- inconsistent (3 municipalities): Muzo (Boyacá), 20231201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; Sibundoy (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102025**

- inconsistent (2 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20251201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2102030**

- inconsistent (1 municipalities): San Bernardo del Viento (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102033**

- inconsistent (1 municipalities): Iles (Nariño), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2102045**

- inconsistent (2 municipalities): Toribío (Cauca), 20241201: payments above obligations or obligations above commitments; San Antero (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102058**

- inconsistent (3 municipalities): Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102059**

- inconsistent (2 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Corozal (Sucre), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102060**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2102061**

- inconsistent (1 municipalities): Nueva Granada (Magdalena), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2102069**

- inconsistent (9 municipalities): Piamonte (Cauca) [2], Iles (Nariño) [2], Gómez Plata (Antioquia) [1], Cachipay (Cundinamarca) [1], El Colegio (Cundinamarca) [1], Nocaima (Cundinamarca) [1], Coyaima (Tolima) [1], San Luis de Palenque (Casanare) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.2102071**

- inconsistent (1 municipalities): Pailitas (Cesar), 20251201: payments above obligations or obligations above commitments; Pailitas (Cesar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2104012**

- inconsistent (1 municipalities): Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2105019**

- inconsistent (1 municipalities): Altos del Rosario (Bolívar) [8].

**MunicipalSpending.2106002**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2106010**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201001**

- inconsistent (1 municipalities): Onzaga (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201002**

- inconsistent (1 municipalities): San Carlos (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201003**

- inconsistent (2 municipalities): Galapa (Atlántico), 20260601: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201006**

- inconsistent (8 municipalities): Dosquebradas (Risaralda) [9], Villanueva (Bolívar) [1], Montería (Córdoba) [1], San Bernardo del Viento (Córdoba) [1], Imués (Nariño) [1], Venadillo (Tolima) [1], Jamundí (Valle Del Cauca) [1], Tuluá (Valle Del Cauca) [1].

**MunicipalSpending.2201012**

- inconsistent (1 municipalities): Zipacón (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201014**

- inconsistent (2 municipalities): Tunja (Boyacá) [13], Siachoque (Boyacá) [1].

**MunicipalSpending.2201015**

- inconsistent (2 municipalities): Dosquebradas (Risaralda) [19], Malambo (Atlántico) [1].

**MunicipalSpending.2201017**

- inconsistent (9 municipalities): Malambo (Atlántico) [7], San Luis (Tolima) [2], Medellín (Antioquia) [1], Ráquira (Boyacá) [1], Agustín Codazzi (Cesar) [1], Toledo (Norte De Santander) [1], Palmira (Valle Del Cauca) [1], Tuluá (Valle Del Cauca) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.2201019**

- inconsistent (1 municipalities): Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201020**

- inconsistent (2 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201021**

- inconsistent (7 municipalities): Tunja (Boyacá) [3], Guadalupe (Santander) [2], Sabanalarga (Atlántico) [1], Usiacurí (Atlántico) [1], Maripí (Boyacá) [1], Zipacón (Cundinamarca) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.2201022**

- inconsistent (1 municipalities): Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201023**

- inconsistent (1 municipalities): Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201026**

- inconsistent (6 municipalities): Sampués (Sucre) [2], Sabanalarga (Atlántico) [1], Usiacurí (Atlántico) [1], Tunja (Boyacá) [1], Chinú (Córdoba) [1], Puerto Guzmán (Putumayo) [1].

**MunicipalSpending.2201028**

- inconsistent (53 municipalities): Jamundí (Valle Del Cauca) [6], Pailitas (Cesar) [6], Villavicencio (Meta) [6], Pelaya (Cesar) [5], Tinjacá (Boyacá) [3], El Colegio (Cundinamarca) [3], Palmira (Valle Del Cauca) [3], Riohacha (La Guajira) [3], Toledo (Norte De Santander) [3], Coloso (Sucre) [2], El Cerrito (Valle Del Cauca) [2], Guamo (Tolima) [2] and 41 more.

**MunicipalSpending.2201029**

- inconsistent (47 municipalities): Fúquene (Cundinamarca) [8], Susa (Cundinamarca) [8], Oiba (Santander) [6], Riohacha (La Guajira) [5], Zipacón (Cundinamarca) [5], Matanza (Santander) [3], Guadalupe (Santander) [3], Pailitas (Cesar) [3], Valle de San José (Santander) [3], Villavicencio (Meta) [3], Viotá (Cundinamarca) [3], Vetas (Santander) [2] and 35 more.

**MunicipalSpending.2201030**

- inconsistent (4 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201033**

- inconsistent (7 municipalities): Riohacha (La Guajira) [17], Sabanalarga (Atlántico) [2], Villavicencio (Meta) [2], Puerto Guzmán (Putumayo) [2], Tunja (Boyacá) [1], Otanche (Boyacá) [1], Sitionuevo (Magdalena) [1].

**MunicipalSpending.2201034**

- inconsistent (1 municipalities): La Salina (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201035**

- inconsistent (1 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201036**

- inconsistent (2 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Corozal (Sucre), 20231201: payments above obligations or obligations above commitments; Corozal (Sucre), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201037**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201039**

- inconsistent (2 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201043**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201044**

- inconsistent (10 municipalities): Tunja (Boyacá) [5], Arenal (Bolívar) [4], Villavicencio (Meta) [3], Riohacha (La Guajira) [2], Jamundí (Valle Del Cauca) [2], Malambo (Atlántico) [1], Sabanalarga (Atlántico) [1], Pelaya (Cesar) [1], San Carlos (Córdoba) [1], Valle de San José (Santander) [1].

**MunicipalSpending.2201047**

- inconsistent (2 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Iles (Nariño), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201049**

- inconsistent (3 municipalities): Caicedo (Antioquia), 20260601: payments above obligations or obligations above commitments; Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Los Santos (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201050**

- inconsistent (5 municipalities): Riohacha (La Guajira) [3], Tunja (Boyacá) [2], Palmira (Valle Del Cauca) [2], Villavicencio (Meta) [1], Roncesvalles (Tolima) [1].

**MunicipalSpending.2201051**

- inconsistent (13 municipalities): San Carlos (Córdoba) [5], San Antonio del Tequendama (Cundinamarca) [4], Malambo (Atlántico) [2], Toribío (Cauca) [2], Jordán (Santander) [2], Icononzo (Tolima) [2], Bolívar (Cauca) [1], San Pelayo (Córdoba) [1], Riohacha (La Guajira) [1], Villavicencio (Meta) [1], Toledo (Norte De Santander) [1], Dosquebradas (Risaralda) [1] and 1 more.

**MunicipalSpending.2201052**

- inconsistent (35 municipalities): Gutiérrez (Cundinamarca) [7], Chaparral (Tolima) [6], Palmira (Valle Del Cauca) [5], Viotá (Cundinamarca) [5], Villavicencio (Meta) [4], Puerto Parra (Santander) [4], El Colegio (Cundinamarca) [4], Anolaima (Cundinamarca) [3], Puerto Caicedo (Putumayo) [3], Orito (Putumayo) [3], Sácama (Casanare) [3], Tame (Arauca) [3] and 23 more.

**MunicipalSpending.2201054**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201056**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201058**

- inconsistent (1 municipalities): Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201060**

- inconsistent (1 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201062**

- inconsistent (23 municipalities): Nimaima (Cundinamarca) [7], Nocaima (Cundinamarca) [5], Guavatá (Santander) [5], Cereté (Córdoba) [4], Sabana de Torres (Santander) [4], Siachoque (Boyacá) [3], Sasaima (Cundinamarca) [3], Sácama (Casanare) [2], Anolaima (Cundinamarca) [2], Fúquene (Cundinamarca) [2], Malambo (Atlántico) [2], Oiba (Santander) [2] and 11 more.

**MunicipalSpending.2201063**

- inconsistent (4 municipalities): San Miguel de Sema (Boyacá), 20251201: payments above obligations or obligations above commitments; La Vega (Cauca), 20251201: payments above obligations or obligations above commitments; Tibacuy (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20231201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201067**

- inconsistent (1 municipalities): Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Inzá (Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201068**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201069**

- inconsistent (15 municipalities): Montería (Córdoba) [3], Dosquebradas (Risaralda) [3], Chámeza (Casanare) [3], San Antero (Córdoba) [2], Anolaima (Cundinamarca) [2], Quebradanegra (Cundinamarca) [2], Iles (Nariño) [2], Guadalupe (Santander) [2], Valle de San José (Santander) [2], Mocoa (Putumayo) [2], Medellín (Antioquia) [1], Santa Lucía (Atlántico) [1] and 3 more.

**MunicipalSpending.2201070**

- inconsistent (4 municipalities): Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20241201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20251201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201071**

- inconsistent (26 municipalities): Palmira (Valle Del Cauca) [34], Jamundí (Valle Del Cauca) [17], Villavicencio (Meta) [15], Dosquebradas (Risaralda) [7], Medellín (Antioquia) [4], San Francisco (Putumayo) [3], Riohacha (La Guajira) [3], San Pelayo (Córdoba) [2], Cartago (Valle Del Cauca) [2], Sabana de Torres (Santander) [1], Orito (Putumayo) [1], Recetor (Casanare) [1] and 14 more.

**MunicipalSpending.2201072**

- inconsistent (1 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201073**

- inconsistent (4 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; La Salina (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201074**

- inconsistent (5 municipalities): Medellín (Antioquia) [4], Tunja (Boyacá) [3], Pueblo Nuevo (Córdoba) [2], Bolívar (Cauca) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.2201075**

- inconsistent (2 municipalities): Aratoca (Santander), 20231201: payments above obligations or obligations above commitments; Aratoca (Santander), 20231201: payments above obligations or obligations above commitments; Valle del Guamuez (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201078**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201079**

- inconsistent (4 municipalities): Pajarito (Boyacá), 20260601: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; Venadillo (Tolima), 20251201: payments above obligations or obligations above commitments; Venadillo (Tolima), 20251201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201080**

- inconsistent (3 municipalities): Cereté (Córdoba), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201081**

- inconsistent (3 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2201083**

- inconsistent (3 municipalities): Tunja (Boyacá) [12], San Carlos (Córdoba) [1], Sabanalarga (Casanare) [1].

**MunicipalSpending.2201084**

- inconsistent (3 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Corozal (Sucre), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2201087**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202005**

- inconsistent (5 municipalities): Galapa (Atlántico), 20260601: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Tierralta (Córdoba), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Orito (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202007**

- inconsistent (7 municipalities): Malambo (Atlántico) [2], Nueva Granada (Magdalena) [2], Venadillo (Tolima) [2], Cerro de San Antonio (Magdalena) [1], Albania (Santander) [1], Charalá (Santander) [1], Guamo (Tolima) [1].

**MunicipalSpending.2202008**

- inconsistent (2 municipalities): Ariguaní (Magdalena), 20251201: payments above obligations or obligations above commitments; Valle de San José (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202009**

- inconsistent (7 municipalities): Galapa (Atlántico) [3], San Antero (Córdoba) [2], Arenal (Bolívar) [1], Siachoque (Boyacá) [1], Bolívar (Cauca) [1], Chaparral (Tolima) [1], Palmira (Valle Del Cauca) [1].

**MunicipalSpending.2202011**

- inconsistent (2 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Mosquera (Nariño), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202023**

- inconsistent (1 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2202030**

- inconsistent (2 municipalities): Los Santos (Santander), 20241201: payments above obligations or obligations above commitments; Tuluá (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202045**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202051**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202061**

- inconsistent (5 municipalities): Malambo (Atlántico), 20251201: payments above obligations or obligations above commitments; Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20251201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202062**

- inconsistent (2 municipalities): Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Guamo (Tolima), 20260601: payments above obligations or obligations above commitments; Guamo (Tolima), 20260601: payments above obligations or obligations above commitments; Guamo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2202065**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202070**

- inconsistent (1 municipalities): Gutiérrez (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2202079**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2203022**

- inconsistent (1 municipalities): Aguachica (Cesar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2299016**

- inconsistent (1 municipalities): Santiago (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301005**

- inconsistent (2 municipalities): Villavicencio (Meta) [5], Dosquebradas (Risaralda) [2].

**MunicipalSpending.2301008**

- inconsistent (1 municipalities): Tame (Arauca), 20251201: payments above obligations or obligations above commitments; Tame (Arauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301013**

- inconsistent (2 municipalities): Nocaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301014**

- inconsistent (1 municipalities): Venadillo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301024**

- inconsistent (6 municipalities): Villavicencio (Meta) [4], Tunja (Boyacá) [3], Cucunubá (Cundinamarca) [3], Fúquene (Cundinamarca) [1], Riohacha (La Guajira) [1], Santiago (Putumayo) [1].

**MunicipalSpending.2301027**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2301075**

- inconsistent (4 municipalities): Caicedo (Antioquia), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301076**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2301077**

- inconsistent (2 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2301079**

- inconsistent (2 municipalities): Guamo (Tolima), 20231201: payments above obligations or obligations above commitments; Santiago (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302002**

- inconsistent (4 municipalities): Pajarito (Boyacá), 20251201: payments above obligations or obligations above commitments; San Bernardo del Viento (Córdoba), 20260601: payments above obligations or obligations above commitments; Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302003**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302021**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302033**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302036**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302041**

- inconsistent (1 municipalities): Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302042**

- inconsistent (1 municipalities): Pelaya (Cesar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302066**

- inconsistent (1 municipalities): San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302073**

- inconsistent (1 municipalities): Susa (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2302076**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302082**

- inconsistent (1 municipalities): Pueblorrico (Antioquia), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302086**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2302101**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401001**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401004**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401008**

- inconsistent (1 municipalities): Ariguaní (Magdalena), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401012**

- inconsistent (1 municipalities): Malambo (Atlántico), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401017**

- inconsistent (1 municipalities): San Carlos (Córdoba), 20231201: payments above obligations or obligations above commitments; San Carlos (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401036**

- inconsistent (1 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2401041**

- inconsistent (1 municipalities): Villanueva (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401051**

- inconsistent (1 municipalities): Marquetalia (Caldas), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2401075**

- inconsistent (1 municipalities): Caramanta (Antioquia), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2402001**

- inconsistent (1 municipalities): San Estanislao (Bolívar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402006**

- inconsistent (5 municipalities): Villavicencio (Meta) [2], Aratoca (Santander) [2], Jamundí (Valle Del Cauca) [2], Chámeza (Casanare) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.2402009**

- inconsistent (1 municipalities): Muzo (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402011**

- inconsistent (1 municipalities): Toribío (Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402012**

- inconsistent (4 municipalities): Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Sasaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Charta (Santander), 20231201: payments above obligations or obligations above commitments; Charta (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402021**

- inconsistent (7 municipalities): Zipacón (Cundinamarca) [6], Anolaima (Cundinamarca) [5], Villavicencio (Meta) [5], Cabrera (Cundinamarca) [3], El Colegio (Cundinamarca) [3], Chimá (Santander) [1], Tame (Arauca) [1].

**MunicipalSpending.2402028**

- inconsistent (1 municipalities): San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402039**

- inconsistent (5 municipalities): Chaparral (Tolima) [4], Chinú (Córdoba) [2], San Bernardo del Viento (Córdoba) [1], Tame (Arauca) [1], San Luis de Palenque (Casanare) [1].

**MunicipalSpending.2402041**

- inconsistent (63 municipalities): Chaparral (Tolima) [12], Ráquira (Boyacá) [11], Nocaima (Cundinamarca) [9], San Bernardo (Cundinamarca) [7], Tame (Arauca) [7], Toribío (Cauca) [6], Jamundí (Valle Del Cauca) [5], Venadillo (Tolima) [4], Riohacha (La Guajira) [4], San Jerónimo (Antioquia) [4], Nimaima (Cundinamarca) [4], Iles (Nariño) [4] and 51 more.

**MunicipalSpending.2402042**

- inconsistent (20 municipalities): Dosquebradas (Risaralda) [7], Gutiérrez (Cundinamarca) [6], Marquetalia (Caldas) [6], Oiba (Santander) [6], Otanche (Boyacá) [4], Venadillo (Tolima) [4], Bolívar (Santander) [4], Villa de San Diego de Ubaté (Cundinamarca) [3], Nocaima (Cundinamarca) [3], Nemocón (Cundinamarca) [2], Tinjacá (Boyacá) [2], Susa (Cundinamarca) [2] and 8 more.

**MunicipalSpending.2402044**

- inconsistent (5 municipalities): Chaparral (Tolima) [6], Santacruz (Nariño) [1], Coyaima (Tolima) [1], San Luis de Palenque (Casanare) [1], Orito (Putumayo) [1].

**MunicipalSpending.2402045**

- inconsistent (7 municipalities): Nemocón (Cundinamarca) [3], San Pablo de Borbur (Boyacá) [2], Chinú (Córdoba) [2], Viotá (Cundinamarca) [2], Venadillo (Tolima) [2], San Antonio del Tequendama (Cundinamarca) [1], Sampués (Sucre) [1].

**MunicipalSpending.2402046**

- inconsistent (2 municipalities): Gutiérrez (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402048**

- inconsistent (3 municipalities): Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2402055**

- inconsistent (2 municipalities): Chimá (Santander), 20241201: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2402056**

- inconsistent (4 municipalities): Pajarito (Boyacá), 20251201: payments above obligations or obligations above commitments; Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20241201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402063**

- inconsistent (2 municipalities): Nemocón (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Orito (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402092**

- inconsistent (1 municipalities): Nocaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2402093**

- inconsistent (1 municipalities): Sitionuevo (Magdalena), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402095**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402096**

- inconsistent (1 municipalities): Venadillo (Tolima), 20251201: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2402098**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402105**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402111**

- inconsistent (1 municipalities): San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402112**

- inconsistent (64 municipalities): Oiba (Santander) [12], Quebradanegra (Cundinamarca) [11], Guavatá (Santander) [11], San Luis de Palenque (Casanare) [11], Gutiérrez (Cundinamarca) [10], Anolaima (Cundinamarca) [9], Susa (Cundinamarca) [8], Tibacuy (Cundinamarca) [7], Fúquene (Cundinamarca) [7], Viotá (Cundinamarca) [7], Villa de San Diego de Ubaté (Cundinamarca) [6], Cucunubá (Cundinamarca) [5] and 52 more.

**MunicipalSpending.2402113**

- inconsistent (14 municipalities): Malambo (Atlántico) [4], Medellín (Antioquia) [3], Luruaco (Atlántico) [3], Cereté (Córdoba) [3], Santa Lucía (Atlántico) [2], Arenal (Bolívar) [1], San Pablo (Bolívar) [1], Turbaná (Bolívar) [1], Toribío (Cauca) [1], Anolaima (Cundinamarca) [1], Nocaima (Cundinamarca) [1], Taminango (Nariño) [1] and 2 more.

**MunicipalSpending.2402114**

- inconsistent (33 municipalities): Pailitas (Cesar) [7], Chaparral (Tolima) [5], Medellín (Antioquia) [4], Orito (Putumayo) [4], Tunja (Boyacá) [4], El Cerrito (Valle Del Cauca) [4], San Jerónimo (Antioquia) [4], Cachipay (Cundinamarca) [3], Puerto Caicedo (Putumayo) [3], Riohacha (La Guajira) [3], Montería (Córdoba) [3], San Pelayo (Córdoba) [2] and 21 more.

**MunicipalSpending.2402115**

- inconsistent (9 municipalities): Villavicencio (Meta) [6], Tame (Arauca) [3], Tunja (Boyacá) [2], Puerto Nariño (Amazonas) [2], San Estanislao (Bolívar) [1], Toribío (Cauca) [1], Villa de San Diego de Ubaté (Cundinamarca) [1], Barichara (Santander) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.2402116**

- inconsistent (4 municipalities): Chalán (Sucre) [4], Villavicencio (Meta) [3], Nocaima (Cundinamarca) [2], Dosquebradas (Risaralda) [2].

**MunicipalSpending.2402118**

- inconsistent (8 municipalities): Chaparral (Tolima) [5], Bolívar (Santander) [3], Iles (Nariño) [2], Los Santos (Santander) [2], San Bernardo del Viento (Córdoba) [1], Anolaima (Cundinamarca) [1], Albania (Santander) [1], Guavatá (Santander) [1].

**MunicipalSpending.2402120**

- inconsistent (2 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402121**

- inconsistent (1 municipalities): Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402125**

- inconsistent (15 municipalities): Dosquebradas (Risaralda) [4], Cucunubá (Cundinamarca) [3], Nimaima (Cundinamarca) [3], Tinjacá (Boyacá) [2], Gutiérrez (Cundinamarca) [2], Nemocón (Cundinamarca) [2], Venecia (Cundinamarca) [2], Viotá (Cundinamarca) [2], Albania (Santander) [2], Cereté (Córdoba) [1], Anolaima (Cundinamarca) [1], Fúquene (Cundinamarca) [1] and 3 more.

**MunicipalSpending.2402128**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2402141**

- inconsistent (1 municipalities): Cachipay (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Cachipay (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Cachipay (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2406001**

- inconsistent (1 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2406008**

- inconsistent (1 municipalities): Puerto Guzmán (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2406055**

- inconsistent (1 municipalities): Orito (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2406057**

- inconsistent (1 municipalities): Sitionuevo (Magdalena), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2407007**

- inconsistent (2 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408001**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408004**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408008**

- inconsistent (1 municipalities): Medellín (Antioquia), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408010**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408038**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Charalá (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408039**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2408052**

- inconsistent (1 municipalities): Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409002**

- inconsistent (3 municipalities): Tunja (Boyacá) [7], Villavicencio (Meta) [5], Jamundí (Valle Del Cauca) [4].

**MunicipalSpending.2409003**

- inconsistent (6 municipalities): Dosquebradas (Risaralda) [18], Palmira (Valle Del Cauca) [3], San Miguel de Sema (Boyacá) [1], Sitionuevo (Magdalena) [1], Villavicencio (Meta) [1], Tame (Arauca) [1].

**MunicipalSpending.2409004**

- inconsistent (3 municipalities): Oiba (Santander) [11], Bolívar (Cauca) [2], Villavicencio (Meta) [2].

**MunicipalSpending.2409007**

- inconsistent (3 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409009**

- inconsistent (4 municipalities): Villavicencio (Meta) [7], Malambo (Atlántico) [1], Charalá (Santander) [1], Guamo (Tolima) [1].

**MunicipalSpending.2409010**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409011**

- inconsistent (6 municipalities): Villavicencio (Meta) [5], Malambo (Atlántico) [3], Palmira (Valle Del Cauca) [2], Montería (Córdoba) [1], La Virginia (Risaralda) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.2409012**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409013**

- inconsistent (5 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409014**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409016**

- inconsistent (3 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Prado (Tolima), 20260601: payments above obligations or obligations above commitments; Prado (Tolima), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409020**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409022**

- inconsistent (6 municipalities): Dosquebradas (Risaralda) [6], Malambo (Atlántico) [2], Cerro de San Antonio (Magdalena) [1], Villavicencio (Meta) [1], Jamundí (Valle Del Cauca) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.2409023**

- inconsistent (2 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Charalá (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409025**

- inconsistent (1 municipalities): Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409029**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409038**

- inconsistent (1 municipalities): Guamo (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409039**

- inconsistent (4 municipalities): Dosquebradas (Risaralda) [8], Palmira (Valle Del Cauca) [3], Villavicencio (Meta) [1], Sabana de Torres (Santander) [1].

**MunicipalSpending.2409043**

- inconsistent (1 municipalities): Fortul (Arauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.2409059**

- inconsistent (2 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2409063**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.2499060**

- inconsistent (1 municipalities): Sibundoy (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.2499066**

- inconsistent (1 municipalities): Guaranda (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.2501001**

- inconsistent (1 municipalities): Ráquira (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3201002**

- inconsistent (2 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments; Los Santos (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3201007**

- inconsistent (2 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3201010**

- inconsistent (1 municipalities): Toribío (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3201021**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3201023**

- inconsistent (2 municipalities): San Carlos (Córdoba), 20260601: payments above obligations or obligations above commitments; Sitionuevo (Magdalena), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3201036**

- inconsistent (1 municipalities): San Francisco (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202001**

- inconsistent (5 municipalities): Dosquebradas (Risaralda) [4], Jamundí (Valle Del Cauca) [2], Piamonte (Cauca) [1], Coloso (Sucre) [1], San Francisco (Putumayo) [1].

**MunicipalSpending.3202002**

- inconsistent (2 municipalities): Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202003**

- inconsistent (2 municipalities): Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202005**

- inconsistent (14 municipalities): Toribío (Cauca) [3], Villavicencio (Meta) [2], Juan de Acosta (Atlántico) [1], Siachoque (Boyacá) [1], Riohacha (La Guajira) [1], Yacuanquer (Nariño) [1], Charalá (Santander) [1], Palmira (Valle Del Cauca) [1], Puerto Rondón (Arauca) [1], Tame (Arauca) [1], Monterrey (Casanare) [1], Recetor (Casanare) [1] and 2 more.

**MunicipalSpending.3202006**

- inconsistent (9 municipalities): Toribío (Cauca) [2], Icononzo (Tolima) [2], Tunja (Boyacá) [1], El Cocuy (Boyacá) [1], Ráquira (Boyacá) [1], San Bernardo del Viento (Córdoba) [1], Barrancas (La Guajira) [1], Chachagüí (Nariño) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.3202012**

- inconsistent (6 municipalities): El Cocuy (Boyacá) [2], Fúquene (Cundinamarca) [2], Dosquebradas (Risaralda) [2], Caramanta (Antioquia) [1], Tierralta (Córdoba) [1], El Cerrito (Valle Del Cauca) [1].

**MunicipalSpending.3202014**

- inconsistent (1 municipalities): El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202015**

- inconsistent (1 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202018**

- inconsistent (1 municipalities): Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202029**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202038**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3202039**

- inconsistent (1 municipalities): Jordán (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202040**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202042**

- inconsistent (1 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202043**

- inconsistent (6 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; San Vicente de Chucurí (Santander), 20260601: payments above obligations or obligations above commitments; Venadillo (Tolima), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202044**

- inconsistent (1 municipalities): Guaca (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202045**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202047**

- inconsistent (4 municipalities): Caracolí (Antioquia), 20241201: payments above obligations or obligations above commitments; San Antero (Córdoba), 20251201: payments above obligations or obligations above commitments; Susa (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20260601: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3202048**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202052**

- inconsistent (1 municipalities): Yacuanquer (Nariño), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3202068**

- inconsistent (1 municipalities): Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3203002**

- inconsistent (3 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Viotá (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203005**

- inconsistent (1 municipalities): Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203008**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203009**

- inconsistent (1 municipalities): Matanza (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3203023**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203033**

- inconsistent (4 municipalities): San Jerónimo (Antioquia), 20251201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203034**

- inconsistent (1 municipalities): Tinjacá (Boyacá), 20241201: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203035**

- inconsistent (2 municipalities): Becerril (Cesar), 20231201: payments above obligations or obligations above commitments; Sampués (Sucre), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203036**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3203047**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3203050**

- inconsistent (6 municipalities): Prado (Tolima) [4], Cereté (Córdoba) [1], San Antero (Córdoba) [1], Susa (Cundinamarca) [1], Villavicencio (Meta) [1], Icononzo (Tolima) [1].

**MunicipalSpending.3204001**

- inconsistent (1 municipalities): Piamonte (Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3204004**

- inconsistent (2 municipalities): San Pablo (Bolívar), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3204011**

- inconsistent (1 municipalities): Iza (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3204019**

- inconsistent (1 municipalities): Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3204046**

- inconsistent (2 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3204049**

- inconsistent (1 municipalities): San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3205001**

- inconsistent (1 municipalities): Guamo (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3205002**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3205006**

- inconsistent (1 municipalities): Puerto Nariño (Amazonas), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3205007**

- inconsistent (4 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Bolívar (Cauca), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3205018**

- inconsistent (1 municipalities): Dosquebradas (Risaralda) [9].

**MunicipalSpending.3205019**

- inconsistent (2 municipalities): Santa Lucía (Atlántico), 20251201: payments above obligations or obligations above commitments; Santa Lucía (Atlántico), 20251201: payments above obligations or obligations above commitments; Santa Lucía (Atlántico), 20251201: payments above obligations or obligations above commitments; Tame (Arauca), 20231201: payments above obligations or obligations above commitments; Tame (Arauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3205021**

- inconsistent (1 municipalities): Luruaco (Atlántico), 20241201: payments above obligations or obligations above commitments; Luruaco (Atlántico), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3205022**

- inconsistent (2 municipalities): El Colegio (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206001**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206002**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3206003**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206004**

- inconsistent (1 municipalities): Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206005**

- inconsistent (2 municipalities): Puerto Rondón (Arauca), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206014**

- inconsistent (1 municipalities): Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments; Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3206016**

- inconsistent (2 municipalities): Gutiérrez (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3207013**

- inconsistent (1 municipalities): Altos del Rosario (Bolívar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3208005**

- inconsistent (1 municipalities): Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3208006**

- inconsistent (6 municipalities): Gutiérrez (Cundinamarca) [4], Nemocón (Cundinamarca) [2], Villavicencio (Meta) [1], Chachagüí (Nariño) [1], Tame (Arauca) [1], La Salina (Casanare) [1].

**MunicipalSpending.3208007**

- inconsistent (1 municipalities): Cereté (Córdoba), 20241201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3208008**

- inconsistent (3 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; San Luis (Tolima), 20260601: payments above obligations or obligations above commitments; Orito (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3208009**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3208010**

- inconsistent (3 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3301001**

- inconsistent (5 municipalities): El Cocuy (Boyacá) [2], Villavicencio (Meta) [2], Medellín (Antioquia) [1], San Zenón (Magdalena) [1], Santacruz (Nariño) [1].

**MunicipalSpending.3301003**

- inconsistent (6 municipalities): Gutiérrez (Cundinamarca) [4], Pailitas (Cesar) [2], Iles (Nariño) [1], La Virginia (Risaralda) [1], Espinal (Tolima) [1], Tame (Arauca) [1].

**MunicipalSpending.3301005**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301011**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301016**

- inconsistent (1 municipalities): Coyaima (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301018**

- inconsistent (4 municipalities): Susa (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Guavatá (Santander), 20251201: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301022**

- inconsistent (1 municipalities): Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301027**

- inconsistent (1 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301033**

- inconsistent (1 municipalities): Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301035**

- inconsistent (1 municipalities): Tame (Arauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301051**

- inconsistent (15 municipalities): Dosquebradas (Risaralda) [10], Tunja (Boyacá) [3], Riohacha (La Guajira) [2], Villavicencio (Meta) [2], Icononzo (Tolima) [2], Tame (Arauca) [2], Medellín (Antioquia) [1], Piamonte (Cauca) [1], Toribío (Cauca) [1], Manaure Balcón del Cesar (Cesar) [1], Montería (Córdoba) [1], Cachipay (Cundinamarca) [1] and 3 more.

**MunicipalSpending.3301052**

- inconsistent (1 municipalities): San Francisco (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301053**

- inconsistent (88 municipalities): San Joaquín (Santander) [12], Guadalupe (Santander) [9], El Colegio (Cundinamarca) [8], Zipacón (Cundinamarca) [8], Santiago (Putumayo) [8], Coromoro (Santander) [7], San Bernardo del Viento (Córdoba) [7], Pailitas (Cesar) [6], Nemocón (Cundinamarca) [6], Chaparral (Tolima) [6], Lourdes (Norte De Santander) [6], Anolaima (Cundinamarca) [6] and 76 more.

**MunicipalSpending.3301054**

- inconsistent (16 municipalities): Pueblo Nuevo (Córdoba) [5], Riohacha (La Guajira) [5], Pajarito (Boyacá) [4], Villavicencio (Meta) [3], Dosquebradas (Risaralda) [3], Coromoro (Santander) [2], Tunja (Boyacá) [1], Cereté (Córdoba) [1], Nimaima (Cundinamarca) [1], Sitionuevo (Magdalena) [1], Santacruz (Nariño) [1], Guavatá (Santander) [1] and 4 more.

**MunicipalSpending.3301055**

- inconsistent (6 municipalities): Tunja (Boyacá) [4], Pelaya (Cesar) [2], Mocoa (Putumayo) [2], Arenal (Bolívar) [1], Riohacha (La Guajira) [1], Dosquebradas (Risaralda) [1].

**MunicipalSpending.3301058**

- inconsistent (1 municipalities): Coromoro (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301060**

- inconsistent (1 municipalities): Sampués (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3301061**

- inconsistent (1 municipalities): Santa Lucía (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3301064**

- inconsistent (3 municipalities): Cota (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Iles (Nariño), 20231201: payments above obligations or obligations above commitments; Coromoro (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301065**

- inconsistent (6 municipalities): Corozal (Sucre) [4], Chaparral (Tolima) [4], San Estanislao (Bolívar) [1], Fúquene (Cundinamarca) [1], Riohacha (La Guajira) [1], Villavicencio (Meta) [1].

**MunicipalSpending.3301068**

- inconsistent (7 municipalities): Palmira (Valle Del Cauca) [5], La Virginia (Risaralda) [2], Tame (Arauca) [2], Galapa (Atlántico) [1], Malambo (Atlántico) [1], Cerro de San Antonio (Magdalena) [1], Palmar (Santander) [1].

**MunicipalSpending.3301070**

- inconsistent (4 municipalities): Dosquebradas (Risaralda) [8], Jamundí (Valle Del Cauca) [4], Zaragoza (Antioquia) [1], Puerto Nariño (Amazonas) [1].

**MunicipalSpending.3301071**

- inconsistent (2 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301073**

- inconsistent (7 municipalities): Riohacha (La Guajira) [5], Tunja (Boyacá) [3], Medellín (Antioquia) [1], Malambo (Atlántico) [1], Cerro de San Antonio (Magdalena) [1], Santacruz (Nariño) [1], Tame (Arauca) [1].

**MunicipalSpending.3301074**

- inconsistent (26 municipalities): Macaravita (Santander) [4], Tunja (Boyacá) [3], Gutiérrez (Cundinamarca) [3], Gómez Plata (Antioquia) [2], La Salina (Casanare) [2], Coromoro (Santander) [2], La Jagua de Ibirico (Cesar) [2], Fúquene (Cundinamarca) [2], Riohacha (La Guajira) [2], Nueva Granada (Magdalena) [2], Villavicencio (Meta) [1], Mocoa (Putumayo) [1] and 14 more.

**MunicipalSpending.3301075**

- inconsistent (2 municipalities): Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments; Los Santos (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301078**

- inconsistent (1 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301085**

- inconsistent (14 municipalities): Riohacha (La Guajira) [4], Tame (Arauca) [4], Toribío (Cauca) [3], Jamundí (Valle Del Cauca) [3], Anolaima (Cundinamarca) [2], Cachipay (Cundinamarca) [2], Bolívar (Santander) [2], Guavatá (Santander) [2], Muzo (Boyacá) [1], Siachoque (Boyacá) [1], Cereté (Córdoba) [1], Villavicencio (Meta) [1] and 2 more.

**MunicipalSpending.3301086**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301087**

- inconsistent (19 municipalities): Tunja (Boyacá) [5], Jamundí (Valle Del Cauca) [4], Oiba (Santander) [4], Riohacha (La Guajira) [4], Gutiérrez (Cundinamarca) [3], San Joaquín (Santander) [3], Piamonte (Cauca) [2], Pailitas (Cesar) [2], Medellín (Antioquia) [1], Bolívar (Santander) [1], Guamo (Tolima) [1], Chaparral (Tolima) [1] and 7 more.

**MunicipalSpending.3301088**

- inconsistent (2 municipalities): Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20241201: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20241201: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301090**

- inconsistent (2 municipalities): Nemocón (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301094**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301095**

- inconsistent (6 municipalities): Dosquebradas (Risaralda) [3], Puerto Nariño (Amazonas) [3], Riohacha (La Guajira) [1], Villavicencio (Meta) [1], Mocoa (Putumayo) [1], Santiago (Putumayo) [1].

**MunicipalSpending.3301096**

- inconsistent (4 municipalities): La Salina (Casanare) [4], El Cocuy (Boyacá) [1], Nocaima (Cundinamarca) [1], La Virginia (Risaralda) [1].

**MunicipalSpending.3301098**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301099**

- inconsistent (2 municipalities): Coyaima (Tolima), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301120**

- inconsistent (1 municipalities): Altos del Rosario (Bolívar), 20260601: payments above obligations or obligations above commitments; Altos del Rosario (Bolívar), 20260601: payments above obligations or obligations above commitments; Altos del Rosario (Bolívar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3301122**

- inconsistent (8 municipalities): Altos del Rosario (Bolívar) [10], Riohacha (La Guajira) [3], Santiago (Putumayo) [2], Piamonte (Cauca) [1], Guataquí (Cundinamarca) [1], Gramalote (Norte De Santander) [1], Dosquebradas (Risaralda) [1], Natagaima (Tolima) [1].

**MunicipalSpending.3301124**

- inconsistent (1 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3301126**

- inconsistent (29 municipalities): Villa de San Diego de Ubaté (Cundinamarca) [6], Villanueva (Bolívar) [4], Tame (Arauca) [4], Piamonte (Cauca) [3], Toribío (Cauca) [3], Dosquebradas (Risaralda) [3], Susa (Cundinamarca) [3], Nemocón (Cundinamarca) [2], San Pablo de Borbur (Boyacá) [2], Sibundoy (Putumayo) [2], La Virginia (Risaralda) [2], Jamundí (Valle Del Cauca) [2] and 17 more.

**MunicipalSpending.3301127**

- inconsistent (3 municipalities): Toribío (Cauca) [8], Cereté (Córdoba) [2], Cucunubá (Cundinamarca) [2].

**MunicipalSpending.3301128**

- inconsistent (5 municipalities): San Pablo de Borbur (Boyacá), 20251201: payments above obligations or obligations above commitments; La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302011**

- inconsistent (1 municipalities): Río Iró (Chocó), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302018**

- inconsistent (2 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3302041**

- inconsistent (2 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; San Francisco (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302042**

- inconsistent (1 municipalities): Zipacón (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3302043**

- inconsistent (1 municipalities): Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302044**

- inconsistent (5 municipalities): Maripí (Boyacá) [4], Jamundí (Valle Del Cauca) [3], Sabanalarga (Atlántico) [1], Ariguaní (Magdalena) [1], Santacruz (Nariño) [1].

**MunicipalSpending.3302049**

- inconsistent (2 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302051**

- inconsistent (1 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302070**

- inconsistent (2 municipalities): Jamundí (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302073**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3302075**

- inconsistent (1 municipalities): Ancuya (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3399016**

- inconsistent (1 municipalities): Tame (Arauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3399061**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502002**

- inconsistent (2 municipalities): Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502003**

- inconsistent (1 municipalities): Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502004**

- inconsistent (3 municipalities): Iles (Nariño), 20231201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502008**

- inconsistent (3 municipalities): Toledo (Norte De Santander), 20251201: payments above obligations or obligations above commitments; Sampués (Sucre), 20231201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502009**

- inconsistent (1 municipalities): Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502010**

- inconsistent (2 municipalities): Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments; Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments; Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502012**

- inconsistent (7 municipalities): Dosquebradas (Risaralda) [5], Palmira (Valle Del Cauca) [3], Juan de Acosta (Atlántico) [1], Pasto (Nariño) [1], La Virginia (Risaralda) [1], Santa Bárbara (Santander) [1], Puerto Rondón (Arauca) [1].

**MunicipalSpending.3502015**

- inconsistent (2 municipalities): Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502017**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502019**

- inconsistent (3 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502020**

- inconsistent (1 municipalities): Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502022**

- inconsistent (2 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502024**

- inconsistent (1 municipalities): Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502025**

- inconsistent (1 municipalities): Santiago (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502027**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502036**

- inconsistent (2 municipalities): Toledo (Norte De Santander), 20260601: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502037**

- inconsistent (4 municipalities): El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; El Colegio (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Villa de San Diego de Ubaté (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502039**

- inconsistent (1 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502044**

- inconsistent (1 municipalities): Sibundoy (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502045**

- inconsistent (8 municipalities): Medellín (Antioquia) [1], Juan de Acosta (Atlántico) [1], Toribío (Cauca) [1], San Antero (Córdoba) [1], Zipacón (Cundinamarca) [1], Coromoro (Santander) [1], El Cerrito (Valle Del Cauca) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.3502046**

- inconsistent (28 municipalities): Nemocón (Cundinamarca) [5], Dosquebradas (Risaralda) [4], Pelaya (Cesar) [4], Riohacha (La Guajira) [4], San Luis de Palenque (Casanare) [3], Quebradanegra (Cundinamarca) [3], Puerto Nariño (Amazonas) [3], Guadalupe (Santander) [2], Palmar (Santander) [2], Pajarito (Boyacá) [2], Barichara (Santander) [2], Coyaima (Tolima) [2] and 16 more.

**MunicipalSpending.3502047**

- inconsistent (5 municipalities): San Bernardo del Viento (Córdoba), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Palmar (Santander), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Puerto Rondón (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502049**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502055**

- inconsistent (1 municipalities): Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502056**

- inconsistent (1 municipalities): Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502059**

- inconsistent (4 municipalities): Guadalupe (Santander) [4], Tunja (Boyacá) [1], Lebrija (Santander) [1], Suaita (Santander) [1].

**MunicipalSpending.3502081**

- inconsistent (1 municipalities): La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502083**

- inconsistent (1 municipalities): Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502093**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502094**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502095**

- inconsistent (1 municipalities): San Antero (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3502113**

- inconsistent (2 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Iles (Nariño), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3502116**

- inconsistent (2 municipalities): Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3601010**

- inconsistent (2 municipalities): Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Piamonte (Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3601012**

- inconsistent (1 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments; Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3601015**

- inconsistent (1 municipalities): Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602001**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments; La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602002**

- inconsistent (3 municipalities): Gómez Plata (Antioquia), 20251201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3602003**

- inconsistent (1 municipalities): Toledo (Norte De Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602004**

- inconsistent (1 municipalities): Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602005**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602006**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3602011**

- inconsistent (2 municipalities): Riohacha (La Guajira), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3602013**

- inconsistent (3 municipalities): Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Coromoro (Santander), 20231201: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602017**

- inconsistent (2 municipalities): Guataquí (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602018**

- inconsistent (1 municipalities): Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3602032**

- inconsistent (2 municipalities): Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Medellín (Antioquia), 20260601: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20260601: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20260601: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3602033**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602034**

- inconsistent (2 municipalities): Pueblo Nuevo (Córdoba), 20231201: payments above obligations or obligations above commitments; Pueblo Nuevo (Córdoba), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602035**

- inconsistent (2 municipalities): Juan de Acosta (Atlántico), 20251201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.3602040**

- inconsistent (1 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3603010**

- inconsistent (1 municipalities): Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.3603019**

- inconsistent (2 municipalities): Arenal (Bolívar), 20260601: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3604004**

- inconsistent (1 municipalities): Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3701024**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3704001**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3707021**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3708013**

- inconsistent (1 municipalities): Villanueva (Bolívar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.3903002**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3903012**

- inconsistent (1 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3904020**

- inconsistent (2 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.3906011**

- inconsistent (2 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001001**

- inconsistent (9 municipalities): San Luis (Tolima) [3], Juan de Acosta (Atlántico) [1], San Pablo (Bolívar) [1], Pailitas (Cesar) [1], Gutiérrez (Cundinamarca) [1], Riohacha (La Guajira) [1], Sabana de Torres (Santander) [1], Guamo (Tolima) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.4001002**

- inconsistent (4 municipalities): San Francisco (Antioquia) [5], Villavicencio (Meta) [2], Villanueva (Bolívar) [1], Pivijay (Magdalena) [1].

**MunicipalSpending.4001004**

- inconsistent (2 municipalities): Pailitas (Cesar), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001007**

- inconsistent (5 municipalities): Riohacha (La Guajira) [3], Pelaya (Cesar) [1], Villavicencio (Meta) [1], Jamundí (Valle Del Cauca) [1], Chámeza (Casanare) [1].

**MunicipalSpending.4001008**

- inconsistent (1 municipalities): Pelaya (Cesar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4001018**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001019**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001021**

- inconsistent (1 municipalities): Luruaco (Atlántico), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001022**

- inconsistent (1 municipalities): Villanueva (Bolívar) [7].

**MunicipalSpending.4001030**

- inconsistent (5 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20231201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001031**

- inconsistent (3 municipalities): San Francisco (Antioquia), 20231201: payments above obligations or obligations above commitments; Charalá (Santander), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4001032**

- inconsistent (16 municipalities): Tame (Arauca) [5], Florián (Santander) [3], Chaparral (Tolima) [3], Gutiérrez (Cundinamarca) [2], Venadillo (Tolima) [2], Palmira (Valle Del Cauca) [2], Tunja (Boyacá) [1], Valparaíso (Caquetá) [1], Cachipay (Cundinamarca) [1], Fúquene (Cundinamarca) [1], Guataquí (Cundinamarca) [1], Quebradanegra (Cundinamarca) [1] and 4 more.

**MunicipalSpending.4001033**

- inconsistent (1 municipalities): Cereté (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001034**

- inconsistent (3 municipalities): Guataquí (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Guataquí (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20241201: payments above obligations or obligations above commitments; Sácama (Casanare), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001035**

- inconsistent (1 municipalities): Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001039**

- inconsistent (4 municipalities): San Jerónimo (Antioquia), 20251201: payments above obligations or obligations above commitments; Marquetalia (Caldas), 20231201: payments above obligations or obligations above commitments; Marquetalia (Caldas), 20241201: payments above obligations or obligations above commitments; Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001041**

- inconsistent (7 municipalities): Guavatá (Santander) [3], San Jerónimo (Antioquia) [2], Coromoro (Santander) [2], Puerto Caicedo (Putumayo) [2], Gómez Plata (Antioquia) [1], Marquetalia (Caldas) [1], Pailitas (Cesar) [1].

**MunicipalSpending.4001042**

- inconsistent (4 municipalities): Gutiérrez (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Iles (Nariño), 20231201: payments above obligations or obligations above commitments; Recetor (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4001044**

- inconsistent (3 municipalities): Chaparral (Tolima) [5], Chámeza (Casanare) [5], Mocoa (Putumayo) [1].

**MunicipalSpending.4001046**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001047**

- inconsistent (1 municipalities): Ariguaní (Magdalena), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4001049**

- inconsistent (1 municipalities): Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002001**

- inconsistent (2 municipalities): Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002003**

- inconsistent (1 municipalities): Guavatá (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002004**

- inconsistent (2 municipalities): La Virginia (Risaralda), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002007**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002013**

- inconsistent (1 municipalities): Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4002016**

- inconsistent (15 municipalities): Tunja (Boyacá) [5], Villavicencio (Meta) [5], Dosquebradas (Risaralda) [3], Palmira (Valle Del Cauca) [3], San Luis de Palenque (Casanare) [3], La Virginia (Risaralda) [2], Mocoa (Putumayo) [2], Toribío (Cauca) [1], Quebradanegra (Cundinamarca) [1], Riohacha (La Guajira) [1], Charalá (Santander) [1], Coromoro (Santander) [1] and 3 more.

**MunicipalSpending.4002017**

- inconsistent (1 municipalities): Anolaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002018**

- inconsistent (4 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; La Jagua de Ibirico (Cesar), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002019**

- inconsistent (10 municipalities): Medellín (Antioquia) [5], Toribío (Cauca) [2], Villavicencio (Meta) [2], Chámeza (Casanare) [2], San Jerónimo (Antioquia) [1], Malambo (Atlántico) [1], Cerro de San Antonio (Magdalena) [1], Guaitarilla (Nariño) [1], Guaranda (Sucre) [1], Palmira (Valle Del Cauca) [1].

**MunicipalSpending.4002020**

- inconsistent (19 municipalities): Palmira (Valle Del Cauca) [9], Villavicencio (Meta) [8], El Cocuy (Boyacá) [6], Toribío (Cauca) [5], Jamundí (Valle Del Cauca) [4], San Jerónimo (Antioquia) [3], Gómez Plata (Antioquia) [2], Puerto Rondón (Arauca) [2], Tunja (Boyacá) [2], Anolaima (Cundinamarca) [2], Iles (Nariño) [2], Icononzo (Tolima) [1] and 7 more.

**MunicipalSpending.4002021**

- inconsistent (3 municipalities): Gutiérrez (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002022**

- inconsistent (5 municipalities): Guadalupe (Santander) [4], Cucunubá (Cundinamarca) [2], Chaparral (Tolima) [2], Medellín (Antioquia) [1], Coromoro (Santander) [1].

**MunicipalSpending.4002023**

- inconsistent (6 municipalities): Nocaima (Cundinamarca) [3], Icononzo (Tolima) [3], Gutiérrez (Cundinamarca) [2], Riohacha (La Guajira) [2], Puerto Rondón (Arauca) [2], Venadillo (Tolima) [1].

**MunicipalSpending.4002025**

- inconsistent (1 municipalities): El Colegio (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4002026**

- inconsistent (3 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; San Pablo de Borbur (Boyacá), 20260601: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002030**

- inconsistent (2 municipalities): La Virginia (Risaralda), 20241201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002032**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002034**

- inconsistent (3 municipalities): El Cocuy (Boyacá), 20231201: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4002036**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4002038**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003001**

- inconsistent (2 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; San Miguel de Sema (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003002**

- inconsistent (2 municipalities): Piamonte (Cauca), 20241201: payments above obligations or obligations above commitments; Tibacuy (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003005**

- inconsistent (1 municipalities): Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments; Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003006**

- inconsistent (10 municipalities): Villavicencio (Meta) [4], Coromoro (Santander) [2], Valle de San José (Santander) [2], Jamundí (Valle Del Cauca) [2], Malambo (Atlántico) [1], Sabanalarga (Atlántico) [1], Riohacha (La Guajira) [1], Aratoca (Santander) [1], Charalá (Santander) [1], San Luis (Tolima) [1].

**MunicipalSpending.4003007**

- inconsistent (2 municipalities): Iles (Nariño), 20260601: payments above obligations or obligations above commitments; Guaranda (Sucre), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4003008**

- inconsistent (14 municipalities): Susa (Cundinamarca) [6], Guadalupe (Santander) [3], Tunja (Boyacá) [2], Pajarito (Boyacá) [2], Tinjacá (Boyacá) [2], San Pelayo (Córdoba) [2], Iles (Nariño) [2], San Estanislao (Bolívar) [1], Cabrera (Cundinamarca) [1], Toledo (Norte De Santander) [1], Guavatá (Santander) [1], Vetas (Santander) [1] and 2 more.

**MunicipalSpending.4003009**

- inconsistent (24 municipalities): Charalá (Santander) [10], Susa (Cundinamarca) [4], Villavicencio (Meta) [4], Tunja (Boyacá) [3], Tibacuy (Cundinamarca) [3], Iles (Nariño) [2], Charta (Santander) [2], Gutiérrez (Cundinamarca) [2], Orito (Putumayo) [1], Mocoa (Putumayo) [1], Villanueva (Casanare) [1], San Luis de Palenque (Casanare) [1] and 12 more.

**MunicipalSpending.4003010**

- inconsistent (34 municipalities): Charalá (Santander) [11], Gutiérrez (Cundinamarca) [9], Cachipay (Cundinamarca) [5], Tibacuy (Cundinamarca) [4], Anolaima (Cundinamarca) [3], San Bernardo (Cundinamarca) [3], Usiacurí (Atlántico) [3], Susa (Cundinamarca) [2], Guavatá (Santander) [2], Tame (Arauca) [2], Vetas (Santander) [2], Villanueva (Santander) [2] and 22 more.

**MunicipalSpending.4003012**

- inconsistent (6 municipalities): Cabrera (Cundinamarca) [4], Aratoca (Santander) [3], Puerto Guzmán (Putumayo) [3], Valparaíso (Antioquia) [1], Tunja (Boyacá) [1], El Cerrito (Valle Del Cauca) [1].

**MunicipalSpending.4003014**

- inconsistent (13 municipalities): Charalá (Santander) [9], Tunja (Boyacá) [5], Medellín (Antioquia) [3], Susa (Cundinamarca) [3], Alejandría (Antioquia) [2], Venecia (Cundinamarca) [2], Tibacuy (Cundinamarca) [2], Orito (Putumayo) [2], San Jerónimo (Antioquia) [1], Muzo (Boyacá) [1], Gutiérrez (Cundinamarca) [1], San Antonio del Tequendama (Cundinamarca) [1] and 1 more.

**MunicipalSpending.4003015**

- inconsistent (8 municipalities): Puerto Parra (Santander) [3], Toribío (Cauca) [2], Piamonte (Cauca) [1], San Carlos (Córdoba) [1], Arboleda (Nariño) [1], Yacuanquer (Nariño) [1], Mistrató (Risaralda) [1], Venadillo (Tolima) [1].

**MunicipalSpending.4003016**

- inconsistent (15 municipalities): Nemocón (Cundinamarca) [2], Nocaima (Cundinamarca) [2], Malambo (Atlántico) [1], Ráquira (Boyacá) [1], Tinjacá (Boyacá) [1], Toribío (Cauca) [1], La Jagua de Ibirico (Cesar) [1], Sasaima (Cundinamarca) [1], Iles (Nariño) [1], Los Santos (Santander) [1], Palmar (Santander) [1], Puerto Rondón (Arauca) [1] and 3 more.

**MunicipalSpending.4003017**

- inconsistent (45 municipalities): Toribío (Cauca) [7], Susa (Cundinamarca) [6], Guapotá (Santander) [6], Galán (Santander) [5], Anolaima (Cundinamarca) [4], Guavatá (Santander) [3], Dosquebradas (Risaralda) [3], Bolívar (Cauca) [3], Tame (Arauca) [3], Cabrera (Cundinamarca) [3], Sabana de Torres (Santander) [2], Yacuanquer (Nariño) [2] and 33 more.

**MunicipalSpending.4003018**

- inconsistent (17 municipalities): Palmira (Valle Del Cauca) [4], Recetor (Casanare) [3], Chaparral (Tolima) [3], Prado (Tolima) [2], Guamo (Tolima) [2], Oiba (Santander) [2], Tunja (Boyacá) [2], Guavatá (Santander) [1], Jamundí (Valle Del Cauca) [1], Malambo (Atlántico) [1], Iles (Nariño) [1], Riohacha (La Guajira) [1] and 5 more.

**MunicipalSpending.4003019**

- inconsistent (11 municipalities): Nocaima (Cundinamarca) [7], Toribío (Cauca) [6], La Jagua de Ibirico (Cesar) [2], Siachoque (Boyacá) [1], San Pelayo (Córdoba) [1], Iles (Nariño) [1], Suaita (Santander) [1], Valle de San José (Santander) [1], Coyaima (Tolima) [1], La Salina (Casanare) [1], San Luis de Palenque (Casanare) [1].

**MunicipalSpending.4003020**

- inconsistent (43 municipalities): Toribío (Cauca) [9], Valle de San José (Santander) [7], Susa (Cundinamarca) [4], Gómez Plata (Antioquia) [3], Puerto Rondón (Arauca) [3], Palmar (Santander) [3], Chaparral (Tolima) [3], Viotá (Cundinamarca) [3], Santa Lucía (Atlántico) [2], Cachipay (Cundinamarca) [2], Juan de Acosta (Atlántico) [2], Guavatá (Santander) [2] and 31 more.

**MunicipalSpending.4003021**

- inconsistent (3 municipalities): Tunja (Boyacá), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Suaita (Santander), 20231201: payments above obligations or obligations above commitments; Suaita (Santander), 20241201: payments above obligations or obligations above commitments; Suaita (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003022**

- inconsistent (18 municipalities): Tunja (Boyacá) [3], Anolaima (Cundinamarca) [2], Cachipay (Cundinamarca) [2], Inzá (Cauca) [2], Toledo (Norte De Santander) [2], Puerto Rondón (Arauca) [1], Chalán (Sucre) [1], Valle de San José (Santander) [1], Charalá (Santander) [1], Gutiérrez (Cundinamarca) [1], Carolina (Antioquia) [1], Gómez Plata (Antioquia) [1] and 6 more.

**MunicipalSpending.4003023**

- inconsistent (5 municipalities): San Bernardo (Cundinamarca) [2], Tibacuy (Cundinamarca) [2], Cucunubá (Cundinamarca) [1], Villavicencio (Meta) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.4003024**

- inconsistent (2 municipalities): Valle de San José (Santander), 20231201: payments above obligations or obligations above commitments; Coyaima (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003025**

- inconsistent (7 municipalities): Sabanalarga (Atlántico) [2], Anolaima (Cundinamarca) [1], San Bernardo (Cundinamarca) [1], Susa (Cundinamarca) [1], Guaca (Santander) [1], Landázuri (Santander) [1], Chaparral (Tolima) [1].

**MunicipalSpending.4003026**

- inconsistent (5 municipalities): Vetas (Santander) [3], San Estanislao (Bolívar) [1], Turbaná (Bolívar) [1], Charta (Santander) [1], Los Santos (Santander) [1].

**MunicipalSpending.4003028**

- inconsistent (1 municipalities): Santiago (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003031**

- inconsistent (1 municipalities): Chachagüí (Nariño), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003032**

- inconsistent (2 municipalities): Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003040**

- inconsistent (4 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Barichara (Santander), 20231201: payments above obligations or obligations above commitments; Guapotá (Santander), 20260601: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003042**

- inconsistent (10 municipalities): Toribío (Cauca) [6], Chaparral (Tolima) [4], Nemocón (Cundinamarca) [2], Quebradanegra (Cundinamarca) [2], Galán (Santander) [2], Guaranda (Sucre) [2], San Luis de Palenque (Casanare) [2], Inzá (Cauca) [1], Los Santos (Santander) [1], Vetas (Santander) [1].

**MunicipalSpending.4003043**

- inconsistent (2 municipalities): Guapotá (Santander), 20251201: payments above obligations or obligations above commitments; Puerto Nariño (Amazonas), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003044**

- inconsistent (5 municipalities): Marquetalia (Caldas), 20241201: payments above obligations or obligations above commitments; Toribío (Cauca), 20241201: payments above obligations or obligations above commitments; Coromoro (Santander), 20231201: payments above obligations or obligations above commitments; Guavatá (Santander), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003046**

- inconsistent (1 municipalities): Bolívar (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003047**

- inconsistent (67 municipalities): Sácama (Casanare) [9], La Virginia (Risaralda) [8], Riohacha (La Guajira) [7], Bolívar (Cauca) [6], Dosquebradas (Risaralda) [6], San Bernardo del Viento (Córdoba) [5], Sabana de Torres (Santander) [5], Sasaima (Cundinamarca) [5], Santa Lucía (Atlántico) [5], Malambo (Atlántico) [5], Palmira (Valle Del Cauca) [5], Tunja (Boyacá) [4] and 55 more.

**MunicipalSpending.4003048**

- inconsistent (7 municipalities): Los Santos (Santander) [2], Gómez Plata (Antioquia) [1], Pelaya (Cesar) [1], San Pelayo (Córdoba) [1], La Virginia (Risaralda) [1], Aratoca (Santander) [1], San Luis (Tolima) [1].

**MunicipalSpending.4003049**

- inconsistent (2 municipalities): Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4003052**

- inconsistent (5 municipalities): Gómez Plata (Antioquia) [4], Tibacuy (Cundinamarca) [2], Villavicencio (Meta) [2], Piamonte (Cauca) [1], Yopal (Casanare) [1].

**MunicipalSpending.4003053**

- inconsistent (1 municipalities): Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4003055**

- inconsistent (2 municipalities): Charalá (Santander), 20260601: payments above obligations or obligations above commitments; Coromoro (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4099016**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4099057**

- inconsistent (1 municipalities): Sasaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101007**

- inconsistent (1 municipalities): El Colegio (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101011**

- inconsistent (6 municipalities): Villavicencio (Meta) [2], Guamo (Tolima) [2], Piamonte (Cauca) [1], San Bernardo del Viento (Córdoba) [1], Riohacha (La Guajira) [1], Sabana de Torres (Santander) [1].

**MunicipalSpending.4101014**

- inconsistent (5 municipalities): Arenal (Bolívar), 20251201: payments above obligations or obligations above commitments; Sampués (Sucre), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments; San Luis (Tolima), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101018**

- inconsistent (1 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101020**

- inconsistent (2 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Tame (Arauca), 20251201: payments above obligations or obligations above commitments; Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101023**

- inconsistent (11 municipalities): San Bernardo del Viento (Córdoba) [3], Quebradanegra (Cundinamarca) [3], Toledo (Norte De Santander) [2], Luruaco (Atlántico) [1], Malambo (Atlántico) [1], Bolívar (Cauca) [1], Cereté (Córdoba) [1], Cachipay (Cundinamarca) [1], Villavicencio (Meta) [1], Mocoa (Putumayo) [1], Orito (Putumayo) [1].

**MunicipalSpending.4101024**

- inconsistent (1 municipalities): El Colegio (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101025**

- inconsistent (24 municipalities): Toribío (Cauca) [7], Mocoa (Putumayo) [6], Tunja (Boyacá) [2], Chaparral (Tolima) [2], Gutiérrez (Cundinamarca) [2], Sampués (Sucre) [2], Juan de Acosta (Atlántico) [2], Villavicencio (Meta) [2], Los Santos (Santander) [2], Medellín (Antioquia) [1], Sabana de Torres (Santander) [1], Puerto Rondón (Arauca) [1] and 12 more.

**MunicipalSpending.4101026**

- inconsistent (1 municipalities): Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101027**

- inconsistent (8 municipalities): Arenal (Bolívar) [2], Toribío (Cauca) [2], Guaranda (Sucre) [2], Pailitas (Cesar) [1], Cereté (Córdoba) [1], San Bernardo del Viento (Córdoba) [1], Valle de San José (Santander) [1], La Unión (Sucre) [1].

**MunicipalSpending.4101030**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101031**

- inconsistent (7 municipalities): Luruaco (Atlántico) [1], Tunja (Boyacá) [1], Pajarito (Boyacá) [1], Cucunubá (Cundinamarca) [1], Quebradanegra (Cundinamarca) [1], Aratoca (Santander) [1], Guamo (Tolima) [1].

**MunicipalSpending.4101035**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101038**

- inconsistent (37 municipalities): Altos del Rosario (Bolívar) [8], Pelaya (Cesar) [4], Iles (Nariño) [4], La Salina (Casanare) [3], Guapotá (Santander) [2], Zipacón (Cundinamarca) [2], Vetas (Santander) [2], Oiba (Santander) [2], Matanza (Santander) [2], Villagarzón (Putumayo) [2], Toribío (Cauca) [2], Gutiérrez (Cundinamarca) [1] and 25 more.

**MunicipalSpending.4101042**

- inconsistent (3 municipalities): Sasaima (Cundinamarca) [3], Cereté (Córdoba) [2], Nocaima (Cundinamarca) [2].

**MunicipalSpending.4101044**

- inconsistent (1 municipalities): San Pablo (Bolívar), 20231201: payments above obligations or obligations above commitments; San Pablo (Bolívar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101046**

- inconsistent (2 municipalities): San Luis (Tolima), 20241201: payments above obligations or obligations above commitments; Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101047**

- inconsistent (2 municipalities): Zipacón (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20251201: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101063**

- inconsistent (2 municipalities): Piamonte (Cauca), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101068**

- inconsistent (3 municipalities): Coromoro (Santander), 20260601: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments; San Luis (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101073**

- inconsistent (13 municipalities): Ráquira (Boyacá) [3], Siachoque (Boyacá) [2], Iles (Nariño) [2], Luruaco (Atlántico) [1], Malambo (Atlántico) [1], Cucunubá (Cundinamarca) [1], Guadalupe (Santander) [1], San Joaquín (Santander) [1], Guamo (Tolima) [1], San Luis (Tolima) [1], El Cerrito (Valle Del Cauca) [1], Puerto Rondón (Arauca) [1] and 1 more.

**MunicipalSpending.4101074**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101076**

- inconsistent (1 municipalities): Nueva Granada (Magdalena), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101079**

- inconsistent (4 municipalities): Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Pasto (Nariño), 20241201: payments above obligations or obligations above commitments; La Salina (Casanare), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4101092**

- inconsistent (2 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Puerto Rondón (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101099**

- inconsistent (1 municipalities): Orito (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101100**

- inconsistent (4 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4101103**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102001**

- inconsistent (31 municipalities): Medellín (Antioquia) [11], Palmira (Valle Del Cauca) [6], Nocaima (Cundinamarca) [5], Viotá (Cundinamarca) [4], Toribío (Cauca) [4], Chaparral (Tolima) [4], Tunja (Boyacá) [2], San Luis de Palenque (Casanare) [2], La Salina (Casanare) [2], Juan de Acosta (Atlántico) [2], Guamo (Tolima) [2], Riohacha (La Guajira) [2] and 19 more.

**MunicipalSpending.4102002**

- inconsistent (2 municipalities): Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20231201: payments above obligations or obligations above commitments; Confines (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102003**

- inconsistent (2 municipalities): Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Oiba (Santander), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102004**

- inconsistent (2 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102005**

- inconsistent (4 municipalities): Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Chaparral (Tolima), 20231201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20241201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20241201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102006**

- inconsistent (2 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Aratoca (Santander), 20231201: payments above obligations or obligations above commitments; Aratoca (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102010**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102013**

- inconsistent (1 municipalities): Sibundoy (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102016**

- inconsistent (1 municipalities): Sibundoy (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102017**

- inconsistent (2 municipalities): Pajarito (Boyacá), 20260601: payments above obligations or obligations above commitments; Pajarito (Boyacá), 20260601: payments above obligations or obligations above commitments; Iles (Nariño), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102022**

- inconsistent (2 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; El Piñón (Magdalena), 20241201: payments above obligations or obligations above commitments; El Piñón (Magdalena), 20241201: payments above obligations or obligations above commitments; El Piñón (Magdalena), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102023**

- inconsistent (1 municipalities): Arenal (Bolívar), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102024**

- inconsistent (1 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102026**

- inconsistent (1 municipalities): Pajarito (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102028**

- inconsistent (1 municipalities): Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102030**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102033**

- inconsistent (1 municipalities): Villa de San Diego de Ubaté (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102035**

- inconsistent (8 municipalities): Dosquebradas (Risaralda) [3], Siachoque (Boyacá) [1], Inzá (Cauca) [1], Zipacón (Cundinamarca) [1], Riohacha (La Guajira) [1], Lebrija (Santander) [1], Jamundí (Valle Del Cauca) [1], Chámeza (Casanare) [1].

**MunicipalSpending.4102036**

- inconsistent (1 municipalities): Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102037**

- inconsistent (3 municipalities): Iles (Nariño), 20231201: payments above obligations or obligations above commitments; Sabana de Torres (Santander), 20241201: payments above obligations or obligations above commitments; San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102038**

- inconsistent (22 municipalities): Tierralta (Córdoba) [15], Tinjacá (Boyacá) [7], Gutiérrez (Cundinamarca) [5], Ráquira (Boyacá) [3], La Salina (Casanare) [3], Tunja (Boyacá) [3], San Bernardo del Viento (Córdoba) [2], San Luis (Tolima) [2], Villa de San Diego de Ubaté (Cundinamarca) [2], Iles (Nariño) [2], Guadalupe (Santander) [2], Galapa (Atlántico) [1] and 10 more.

**MunicipalSpending.4102040**

- inconsistent (2 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102041**

- inconsistent (4 municipalities): Contratación (Santander) [5], Guadalupe (Santander) [2], Tunja (Boyacá) [1], Sabana de Torres (Santander) [1].

**MunicipalSpending.4102042**

- inconsistent (3 municipalities): Villa de San Diego de Ubaté (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Guadalupe (Santander), 20251201: payments above obligations or obligations above commitments; Guadalupe (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102043**

- inconsistent (3 municipalities): Mosquera (Nariño), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Puerto Guzmán (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4102045**

- inconsistent (4 municipalities): Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102046**

- inconsistent (17 municipalities): Mocoa (Putumayo) [5], San Luis de Palenque (Casanare) [4], Confines (Santander) [2], La Salina (Casanare) [2], Toledo (Norte De Santander) [2], Jamundí (Valle Del Cauca) [1], Venadillo (Tolima) [1], Sabana de Torres (Santander) [1], Guadalupe (Santander) [1], Inzá (Cauca) [1], Montería (Córdoba) [1], Dosquebradas (Risaralda) [1] and 5 more.

**MunicipalSpending.4102047**

- inconsistent (10 municipalities): Sampués (Sucre) [3], Malambo (Atlántico) [2], Cereté (Córdoba) [2], San Bernardo del Viento (Córdoba) [2], Villa de San Diego de Ubaté (Cundinamarca) [2], Riohacha (La Guajira) [2], Corozal (Sucre) [2], San Pablo (Bolívar) [1], Bolívar (Cauca) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.4102051**

- inconsistent (3 municipalities): Gramalote (Norte De Santander), 20231201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4102052**

- inconsistent (17 municipalities): Guamo (Tolima) [17], Pajarito (Boyacá) [3], Dosquebradas (Risaralda) [2], San Joaquín (Santander) [2], Malambo (Atlántico) [1], Tame (Arauca) [1], Palmira (Valle Del Cauca) [1], Chaparral (Tolima) [1], Guapotá (Santander) [1], Iles (Nariño) [1], Nemocón (Cundinamarca) [1], Pueblo Nuevo (Córdoba) [1] and 5 more.

**MunicipalSpending.4103004**

- inconsistent (3 municipalities): Villanueva (Bolívar) [10], Villavicencio (Meta) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.4103005**

- inconsistent (3 municipalities): Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20260601: payments above obligations or obligations above commitments; Icononzo (Tolima), 20260601: payments above obligations or obligations above commitments; La Salina (Casanare), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4103006**

- inconsistent (1 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103009**

- inconsistent (1 municipalities): Ricaurte (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103011**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103015**

- inconsistent (6 municipalities): Venecia (Cundinamarca) [2], San Antero (Córdoba) [1], Anolaima (Cundinamarca) [1], La Virginia (Risaralda) [1], Puerto Caicedo (Putumayo) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.4103017**

- inconsistent (7 municipalities): Medellín (Antioquia) [5], La Virginia (Risaralda) [3], Sabanalarga (Atlántico) [2], Lebrija (Santander) [2], Palmira (Valle Del Cauca) [2], San Miguel (Putumayo) [2], San Francisco (Putumayo) [1].

**MunicipalSpending.4103025**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4103027**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4103047**

- inconsistent (2 municipalities): Venecia (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Sampués (Sucre), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103050**

- inconsistent (26 municipalities): Medellín (Antioquia) [3], San Luis de Palenque (Casanare) [3], Chinú (Córdoba) [3], Sampués (Sucre) [2], Bolívar (Cauca) [2], Pelaya (Cesar) [2], La Salina (Casanare) [2], Riohacha (La Guajira) [2], Villavicencio (Meta) [2], Tame (Arauca) [1], Puerto Rondón (Arauca) [1], San Luis (Tolima) [1] and 14 more.

**MunicipalSpending.4103052**

- inconsistent (27 municipalities): Palmira (Valle Del Cauca) [12], Medellín (Antioquia) [5], Tame (Arauca) [5], Chinú (Córdoba) [4], Jamundí (Valle Del Cauca) [3], Sampués (Sucre) [3], Zipacón (Cundinamarca) [2], Villavicencio (Meta) [2], Toribío (Cauca) [2], Tunja (Boyacá) [2], Bolívar (Cauca) [2], Chaparral (Tolima) [1] and 15 more.

**MunicipalSpending.4103053**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103054**

- inconsistent (1 municipalities): Sabana de Torres (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103055**

- inconsistent (1 municipalities): Puerto Rondón (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4103057**

- inconsistent (2 municipalities): Riohacha (La Guajira), 20241201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103058**

- inconsistent (4 municipalities): Altos del Rosario (Bolívar) [8], Pailitas (Cesar) [1], Fúquene (Cundinamarca) [1], El Cerrito (Valle Del Cauca) [1].

**MunicipalSpending.4103060**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103061**

- inconsistent (3 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Pasca (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Vetas (Santander), 20231201: payments above obligations or obligations above commitments; Vetas (Santander), 20231201: payments above obligations or obligations above commitments; Vetas (Santander), 20231201: payments above obligations or obligations above commitments; Vetas (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103064**

- inconsistent (2 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Pasca (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103065**

- inconsistent (2 municipalities): Malambo (Atlántico), 20251201: payments above obligations or obligations above commitments; Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments; Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments; Pajarito (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4103067**

- inconsistent (4 municipalities): Zipacón (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4103068**

- inconsistent (1 municipalities): Zipacón (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4104001**

- inconsistent (5 municipalities): Dosquebradas (Risaralda) [3], Tunja (Boyacá) [1], Nocaima (Cundinamarca) [1], Villavicencio (Meta) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.4104002**

- inconsistent (6 municipalities): Villavicencio (Meta) [3], Yacuanquer (Nariño) [2], Usiacurí (Atlántico) [1], San Pablo de Borbur (Boyacá) [1], Jamundí (Valle Del Cauca) [1], Chámeza (Casanare) [1].

**MunicipalSpending.4104004**

- inconsistent (1 municipalities): Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments; Santacruz (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104005**

- inconsistent (1 municipalities): Contratación (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104007**

- inconsistent (8 municipalities): Mocoa (Putumayo) [4], Matanza (Santander) [2], Malambo (Atlántico) [1], Pajarito (Boyacá) [1], Cereté (Córdoba) [1], Barichara (Santander) [1], Charalá (Santander) [1], Los Santos (Santander) [1].

**MunicipalSpending.4104008**

- inconsistent (85 municipalities): Susa (Cundinamarca) [14], Toribío (Cauca) [11], Tame (Arauca) [8], Zipacón (Cundinamarca) [8], Mocoa (Putumayo) [8], Pajarito (Boyacá) [7], San Bernardo del Viento (Córdoba) [7], Iles (Nariño) [7], San Joaquín (Santander) [7], Pelaya (Cesar) [7], Vetas (Santander) [6], Palmira (Valle Del Cauca) [6] and 73 more.

**MunicipalSpending.4104009**

- inconsistent (12 municipalities): Nemocón (Cundinamarca) [3], Nocaima (Cundinamarca) [2], Malambo (Atlántico) [1], Toribío (Cauca) [1], Anolaima (Cundinamarca) [1], Riohacha (La Guajira) [1], Iles (Nariño) [1], San Joaquín (Santander) [1], Jamundí (Valle Del Cauca) [1], Recetor (Casanare) [1], San Luis de Palenque (Casanare) [1], Puerto Guzmán (Putumayo) [1].

**MunicipalSpending.4104010**

- inconsistent (2 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104012**

- inconsistent (1 municipalities): Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104013**

- inconsistent (1 municipalities): Orito (Putumayo), 20260601: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4104014**

- inconsistent (7 municipalities): Guadalupe (Santander) [3], Marquetalia (Caldas) [2], Nimaima (Cundinamarca) [2], Matanza (Santander) [2], Pajarito (Boyacá) [1], Quebradanegra (Cundinamarca) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.4104015**

- inconsistent (8 municipalities): Pajarito (Boyacá) [2], Sasaima (Cundinamarca) [2], Oiba (Santander) [2], Juan de Acosta (Atlántico) [1], Manaure Balcón del Cesar (Cesar) [1], San Bernardo (Cundinamarca) [1], Chimá (Santander) [1], Recetor (Casanare) [1].

**MunicipalSpending.4104017**

- inconsistent (1 municipalities): Tame (Arauca), 20231201: payments above obligations or obligations above commitments; Tame (Arauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104018**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104020**

- inconsistent (40 municipalities): Zipacón (Cundinamarca) [7], Chaparral (Tolima) [4], Toribío (Cauca) [3], Gutiérrez (Cundinamarca) [3], Villavicencio (Meta) [2], Tunja (Boyacá) [2], Guamo (Tolima) [2], Fúquene (Cundinamarca) [2], Tibacuy (Cundinamarca) [2], Nimaima (Cundinamarca) [2], Oiba (Santander) [1], Guaca (Santander) [1] and 28 more.

**MunicipalSpending.4104022**

- inconsistent (1 municipalities): Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Nimaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104023**

- inconsistent (1 municipalities): San Bernardo (Cundinamarca), 20251201: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20251201: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4104026**

- inconsistent (2 municipalities): Medellín (Antioquia), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4104027**

- inconsistent (4 municipalities): Dosquebradas (Risaralda) [4], La Virginia (Risaralda) [2], Medellín (Antioquia) [1], Guamo (Tolima) [1].

**MunicipalSpending.4104036**

- inconsistent (2 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4104042**

- inconsistent (1 municipalities): Aratoca (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4199019**

- inconsistent (1 municipalities): Bello (Antioquia), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301001**

- inconsistent (61 municipalities): Gutiérrez (Cundinamarca) [10], Dosquebradas (Risaralda) [6], Charalá (Santander) [6], Chaparral (Tolima) [6], Tame (Arauca) [5], Prado (Tolima) [5], Montería (Córdoba) [5], Icononzo (Tolima) [4], Iles (Nariño) [4], Susa (Cundinamarca) [4], Quebradanegra (Cundinamarca) [4], Ariguaní (Magdalena) [3] and 49 more.

**MunicipalSpending.4301003**

- inconsistent (2 municipalities): La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; Valle del Guamuez (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301004**

- inconsistent (40 municipalities): Chaparral (Tolima) [5], Iles (Nariño) [5], Dosquebradas (Risaralda) [5], Usiacurí (Atlántico) [4], Albania (Santander) [4], Tame (Arauca) [4], Santa Bárbara (Santander) [3], Cucunubá (Cundinamarca) [3], Yacuanquer (Nariño) [3], Puerto Rondón (Arauca) [3], Toribío (Cauca) [3], Tunja (Boyacá) [3] and 28 more.

**MunicipalSpending.4301005**

- inconsistent (3 municipalities): Dosquebradas (Risaralda) [7], El Piñón (Magdalena) [2], Cereté (Córdoba) [1].

**MunicipalSpending.4301007**

- inconsistent (24 municipalities): Gutiérrez (Cundinamarca) [6], Susa (Cundinamarca) [3], Inzá (Cauca) [3], Nocaima (Cundinamarca) [3], Fúquene (Cundinamarca) [3], Guamo (Tolima) [2], Chaparral (Tolima) [2], San Joaquín (Santander) [2], Oiba (Santander) [2], Zipacón (Cundinamarca) [2], Tame (Arauca) [2], Anolaima (Cundinamarca) [2] and 12 more.

**MunicipalSpending.4301009**

- inconsistent (4 municipalities): Venecia (Cundinamarca) [2], Nueva Granada (Magdalena) [2], Guadalupe (Santander) [2], Sabanalarga (Atlántico) [1].

**MunicipalSpending.4301010**

- inconsistent (3 municipalities): Marquetalia (Caldas), 20231201: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Villagarzón (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301011**

- inconsistent (2 municipalities): Ariguaní (Magdalena) [7], Riohacha (La Guajira) [1].

**MunicipalSpending.4301012**

- inconsistent (3 municipalities): Tinjacá (Boyacá) [5], Cereté (Córdoba) [3], Nocaima (Cundinamarca) [2].

**MunicipalSpending.4301013**

- inconsistent (3 municipalities): Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; Riohacha (La Guajira), 20260601: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20241201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; Orito (Putumayo), 20251201: payments above obligations or obligations above commitments; Orito (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301014**

- inconsistent (5 municipalities): Gutiérrez (Cundinamarca) [3], Oiba (Santander) [3], Marquetalia (Caldas) [1], Cachipay (Cundinamarca) [1], Cucunubá (Cundinamarca) [1].

**MunicipalSpending.4301015**

- inconsistent (3 municipalities): Malambo (Atlántico), 20241201: payments above obligations or obligations above commitments; Malambo (Atlántico), 20241201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301016**

- inconsistent (1 municipalities): Sasaima (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301017**

- inconsistent (2 municipalities): Nocaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nocaima (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Santiago (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301018**

- inconsistent (2 municipalities): Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301019**

- inconsistent (3 municipalities): Almaguer (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301020**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301022**

- inconsistent (1 municipalities): Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments; Quípama (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301023**

- inconsistent (2 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Curillo (Caquetá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301025**

- inconsistent (4 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Gutiérrez (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Viotá (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4301026**

- inconsistent (1 municipalities): La Jagua de Ibirico (Cesar), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301027**

- inconsistent (1 municipalities): Chinú (Córdoba), 20231201: payments above obligations or obligations above commitments; Chinú (Córdoba), 20231201: payments above obligations or obligations above commitments; Chinú (Córdoba), 20231201: payments above obligations or obligations above commitments; Chinú (Córdoba), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301028**

- inconsistent (2 municipalities): Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301029**

- inconsistent (2 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4301030**

- inconsistent (4 municipalities): Gómez Plata (Antioquia), 20260601: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20241201: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20241201: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20241201: payments above obligations or obligations above commitments; Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Viotá (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301031**

- inconsistent (8 municipalities): Yacuanquer (Nariño) [3], La Vega (Cauca) [2], Orito (Putumayo) [2], Ráquira (Boyacá) [1], Toribío (Cauca) [1], Anolaima (Cundinamarca) [1], Iles (Nariño) [1], Guaranda (Sucre) [1].

**MunicipalSpending.4301032**

- inconsistent (29 municipalities): San Joaquín (Santander) [5], Villa de San Diego de Ubaté (Cundinamarca) [4], Lebrija (Santander) [3], Piamonte (Cauca) [3], Barichara (Santander) [3], Riohacha (La Guajira) [3], Palmar (Santander) [2], San Miguel de Sema (Boyacá) [2], Inzá (Cauca) [2], Pelaya (Cesar) [2], Guadalupe (Santander) [2], Quebradanegra (Cundinamarca) [2] and 17 more.

**MunicipalSpending.4301033**

- inconsistent (1 municipalities): Pajarito (Boyacá), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301034**

- inconsistent (1 municipalities): Iles (Nariño), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301035**

- inconsistent (4 municipalities): San Antero (Córdoba), 20251201: payments above obligations or obligations above commitments; San Pelayo (Córdoba), 20241201: payments above obligations or obligations above commitments; Ovejas (Sucre), 20260601: payments above obligations or obligations above commitments; Tame (Arauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4301037**

- inconsistent (47 municipalities): Altos del Rosario (Bolívar) [12], Pailitas (Cesar) [7], Chaparral (Tolima) [7], Riohacha (La Guajira) [6], Dosquebradas (Risaralda) [6], Palmar (Santander) [5], La Salina (Casanare) [4], Mocoa (Putumayo) [4], Barichara (Santander) [4], San Bernardo del Viento (Córdoba) [4], Santa Lucía (Atlántico) [3], Puerto Guzmán (Putumayo) [3] and 35 more.

**MunicipalSpending.4301038**

- inconsistent (20 municipalities): La Paz (Santander) [3], Bolívar (Santander) [3], San Joaquín (Santander) [3], Galán (Santander) [2], Palmira (Valle Del Cauca) [2], Prado (Tolima) [2], Cucunubá (Cundinamarca) [2], Sabanalarga (Atlántico) [2], Guapotá (Santander) [1], Guavatá (Santander) [1], Coromoro (Santander) [1], Matanza (Santander) [1] and 8 more.

**MunicipalSpending.4302001**

- inconsistent (2 municipalities): Toribío (Cauca), 20231201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments; Montería (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302002**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302012**

- inconsistent (1 municipalities): Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Oiba (Santander), 20251201: payments above obligations or obligations above commitments; Oiba (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302014**

- inconsistent (1 municipalities): Prado (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302025**

- inconsistent (1 municipalities): La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302029**

- inconsistent (2 municipalities): El Colegio (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Ariguaní (Magdalena), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302042**

- inconsistent (1 municipalities): San Jerónimo (Antioquia), 20251201: payments above obligations or obligations above commitments; San Jerónimo (Antioquia), 20260601: payments above obligations or obligations above commitments; San Jerónimo (Antioquia), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302043**

- inconsistent (2 municipalities): San Carlos (Córdoba), 20241201: payments above obligations or obligations above commitments; Barichara (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302059**

- inconsistent (1 municipalities): Susa (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Susa (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302062**

- inconsistent (2 municipalities): Inzá (Cauca), 20260601: payments above obligations or obligations above commitments; San Antero (Córdoba), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302063**

- inconsistent (1 municipalities): Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302064**

- inconsistent (2 municipalities): Cachipay (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Cachipay (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302069**

- inconsistent (2 municipalities): Suaita (Santander), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302070**

- inconsistent (2 municipalities): Zipacón (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Zipacón (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments; Guapotá (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302073**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4302075**

- inconsistent (1 municipalities): Mocoa (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4302089**

- inconsistent (1 municipalities): Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4399009**

- inconsistent (1 municipalities): La Paz (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501001**

- inconsistent (24 municipalities): Oiba (Santander) [10], Toledo (Norte De Santander) [9], Fúquene (Cundinamarca) [9], San Bernardo del Viento (Córdoba) [7], San Antero (Córdoba) [4], Sitionuevo (Magdalena) [4], San Francisco (Putumayo) [3], Nimaima (Cundinamarca) [3], Nocaima (Cundinamarca) [3], Villa de San Diego de Ubaté (Cundinamarca) [2], Villavicencio (Meta) [2], Juan de Acosta (Atlántico) [2] and 12 more.

**MunicipalSpending.4501003**

- inconsistent (3 municipalities): Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments; Tinjacá (Boyacá), 20260601: payments above obligations or obligations above commitments; Piamonte (Cauca), 20241201: payments above obligations or obligations above commitments; San Luis de Palenque (Casanare), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501004**

- inconsistent (29 municipalities): Oiba (Santander) [12], Toribío (Cauca) [11], Jamundí (Valle Del Cauca) [6], Gutiérrez (Cundinamarca) [4], Orito (Putumayo) [4], Cabrera (Cundinamarca) [3], Venadillo (Tolima) [3], Dosquebradas (Risaralda) [3], Chámeza (Casanare) [3], Ráquira (Boyacá) [3], Tame (Arauca) [2], Puerto Rondón (Arauca) [2] and 17 more.

**MunicipalSpending.4501006**

- inconsistent (1 municipalities): Cereté (Córdoba), 20231201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20231201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501007**

- inconsistent (2 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501008**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501010**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501013**

- inconsistent (2 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Jordán (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501018**

- inconsistent (2 municipalities): Piamonte (Cauca), 20241201: payments above obligations or obligations above commitments; Chimá (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501019**

- inconsistent (1 municipalities): Guadalupe (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501026**

- inconsistent (9 municipalities): Dosquebradas (Risaralda) [25], Tunja (Boyacá) [3], Yacuanquer (Nariño) [3], Sabana de Torres (Santander) [2], Palmira (Valle Del Cauca) [2], Nocaima (Cundinamarca) [1], San Luis (Tolima) [1], Jamundí (Valle Del Cauca) [1], Puerto Nariño (Amazonas) [1].

**MunicipalSpending.4501028**

- inconsistent (10 municipalities): Palmira (Valle Del Cauca) [3], Recetor (Casanare) [3], Malambo (Atlántico) [2], Susa (Cundinamarca) [2], Caucasia (Antioquia) [1], Guataquí (Cundinamarca) [1], San Bernardo (Cundinamarca) [1], Cerro de San Antonio (Magdalena) [1], San Luis (Tolima) [1], Orito (Putumayo) [1].

**MunicipalSpending.4501029**

- inconsistent (59 municipalities): Chaparral (Tolima) [13], Guapotá (Santander) [10], Riohacha (La Guajira) [6], Guavatá (Santander) [6], Charalá (Santander) [5], Villavicencio (Meta) [5], Valle de San José (Santander) [4], Toledo (Norte De Santander) [4], Quípama (Boyacá) [4], Sácama (Casanare) [4], Viotá (Cundinamarca) [3], El Cocuy (Boyacá) [3] and 47 more.

**MunicipalSpending.4501031**

- inconsistent (2 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501040**

- inconsistent (1 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501042**

- inconsistent (1 municipalities): Barrancas (La Guajira), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501043**

- inconsistent (1 municipalities): Guapotá (Santander), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501046**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501047**

- inconsistent (9 municipalities): Luruaco (Atlántico) [7], Sampués (Sucre) [3], Cabrera (Cundinamarca) [2], Tunja (Boyacá) [1], Chinú (Córdoba) [1], Nueva Granada (Magdalena) [1], Capitanejo (Santander) [1], Prado (Tolima) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.4501048**

- inconsistent (13 municipalities): Palmira (Valle Del Cauca) [7], Vetas (Santander) [5], Galapa (Atlántico) [3], Villavicencio (Meta) [3], Bolívar (Santander) [3], California (Santander) [3], Fúquene (Cundinamarca) [2], Susa (Cundinamarca) [2], San Luis (Tolima) [2], Luruaco (Atlántico) [1], Charta (Santander) [1], Chaparral (Tolima) [1] and 1 more.

**MunicipalSpending.4501049**

- inconsistent (3 municipalities): Cubarral (Meta) [12], San Joaquín (Santander) [9], Tinjacá (Boyacá) [1].

**MunicipalSpending.4501050**

- inconsistent (8 municipalities): Vetas (Santander) [6], Sitionuevo (Magdalena) [4], La Jagua de Ibirico (Cesar) [3], Toledo (Norte De Santander) [3], Toribío (Cauca) [2], Nocaima (Cundinamarca) [2], Sabanagrande (Atlántico) [1], Sampués (Sucre) [1].

**MunicipalSpending.4501051**

- inconsistent (1 municipalities): San Bernardo del Viento (Córdoba), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501052**

- inconsistent (2 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501054**

- inconsistent (2 municipalities): Tunja (Boyacá), 20241201: payments above obligations or obligations above commitments; Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20251201: payments above obligations or obligations above commitments; Toledo (Norte De Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501056**

- inconsistent (5 municipalities): Pelaya (Cesar) [5], Caicedo (Antioquia) [2], Tibacuy (Cundinamarca) [1], Palmira (Valle Del Cauca) [1], Mocoa (Putumayo) [1].

**MunicipalSpending.4501057**

- inconsistent (16 municipalities): Palmira (Valle Del Cauca) [7], Susa (Cundinamarca) [6], Nocaima (Cundinamarca) [3], Riohacha (La Guajira) [3], Nemocón (Cundinamarca) [2], Barichara (Santander) [2], Bolívar (Santander) [2], Pailitas (Cesar) [1], Cabrera (Cundinamarca) [1], Ricaurte (Cundinamarca) [1], San Bernardo (Cundinamarca) [1], Tibacuy (Cundinamarca) [1] and 4 more.

**MunicipalSpending.4501058**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501061**

- inconsistent (3 municipalities): Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Anolaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villa de San Diego de Ubaté (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villa de San Diego de Ubaté (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501063**

- inconsistent (4 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20260601: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; Guadalupe (Santander), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4501064**

- inconsistent (1 municipalities): San Vicente de Chucurí (Santander), 20260601: payments above obligations or obligations above commitments; San Vicente de Chucurí (Santander), 20260601: payments above obligations or obligations above commitments; San Vicente de Chucurí (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501066**

- inconsistent (1 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501068**

- inconsistent (1 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501077**

- inconsistent (2 municipalities): San Luis (Tolima), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501079**

- inconsistent (6 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Cucunubá (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Nocaima (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Quebradanegra (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Albania (Santander), 20260601: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4501081**

- inconsistent (10 municipalities): San Luis de Palenque (Casanare) [7], Gutiérrez (Cundinamarca) [6], Valle de San José (Santander) [4], Quebradanegra (Cundinamarca) [2], Tinjacá (Boyacá) [1], Pailitas (Cesar) [1], Nocaima (Cundinamarca) [1], Toledo (Norte De Santander) [1], Charalá (Santander) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.4501082**

- inconsistent (23 municipalities): La Salina (Casanare) [11], Prado (Tolima) [10], Matanza (Santander) [8], Tinjacá (Boyacá) [6], Chinú (Córdoba) [4], San Luis de Palenque (Casanare) [4], Puerto Nare (Antioquia) [2], Cucunubá (Cundinamarca) [2], Tame (Arauca) [2], Quebradanegra (Cundinamarca) [2], Sabana de Torres (Santander) [1], Puerto Caicedo (Putumayo) [1] and 11 more.

**MunicipalSpending.4501083**

- inconsistent (1 municipalities): Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502001**

- inconsistent (45 municipalities): Toribío (Cauca) [5], Chaparral (Tolima) [5], Tame (Arauca) [5], San Luis de Palenque (Casanare) [5], Guamo (Tolima) [3], Villavicencio (Meta) [3], Jamundí (Valle Del Cauca) [3], La Virginia (Risaralda) [2], Tunja (Boyacá) [2], Guapotá (Santander) [2], Malambo (Atlántico) [2], Iles (Nariño) [2] and 33 more.

**MunicipalSpending.4502003**

- inconsistent (2 municipalities): Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Nemocón (Cundinamarca), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502008**

- inconsistent (1 municipalities): Cabrera (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502009**

- inconsistent (3 municipalities): Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments; Icononzo (Tolima), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502010**

- inconsistent (2 municipalities): Cabrera (Cundinamarca), 20241201: payments above obligations or obligations above commitments; San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502015**

- inconsistent (1 municipalities): Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments; Medellín (Antioquia), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502016**

- inconsistent (2 municipalities): Riohacha (La Guajira) [5], Dosquebradas (Risaralda) [4].

**MunicipalSpending.4502017**

- inconsistent (1 municipalities): Palmira (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502020**

- inconsistent (1 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502021**

- inconsistent (2 municipalities): Curillo (Caquetá), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502022**

- inconsistent (10 municipalities): Dosquebradas (Risaralda) [11], Villagarzón (Putumayo) [3], Gutiérrez (Cundinamarca) [2], Riohacha (La Guajira) [2], Sabanalarga (Atlántico) [1], Quebradanegra (Cundinamarca) [1], El Piñón (Magdalena) [1], Iles (Nariño) [1], San Joaquín (Santander) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.4502024**

- inconsistent (3 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Puerto Rondón (Arauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502025**

- inconsistent (3 municipalities): Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments; Cereté (Córdoba), 20260601: payments above obligations or obligations above commitments; Vetas (Santander), 20231201: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502026**

- inconsistent (3 municipalities): Galapa (Atlántico), 20241201: payments above obligations or obligations above commitments; Susacón (Boyacá), 20231201: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502027**

- inconsistent (1 municipalities): Sitionuevo (Magdalena), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502029**

- inconsistent (1 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502032**

- inconsistent (1 municipalities): Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502033**

- inconsistent (3 municipalities): Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20241201: payments above obligations or obligations above commitments; Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4502034**

- inconsistent (8 municipalities): Dosquebradas (Risaralda) [3], Lebrija (Santander) [2], Medellín (Antioquia) [1], Toribío (Cauca) [1], Zipacón (Cundinamarca) [1], Villavicencio (Meta) [1], Santacruz (Nariño) [1], Jamundí (Valle Del Cauca) [1].

**MunicipalSpending.4502035**

- inconsistent (4 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20260601: payments above obligations or obligations above commitments; San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502037**

- inconsistent (2 municipalities): Juan de Acosta (Atlántico), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4502038**

- inconsistent (20 municipalities): Villavicencio (Meta) [4], Jamundí (Valle Del Cauca) [3], Inzá (Cauca) [2], Tame (Arauca) [2], Riohacha (La Guajira) [2], Gómez Plata (Antioquia) [2], San Luis (Tolima) [2], Medellín (Antioquia) [1], Coyaima (Tolima) [1], Santiago (Putumayo) [1], Puerto Caicedo (Putumayo) [1], Monterrey (Casanare) [1] and 8 more.

**MunicipalSpending.4502039**

- inconsistent (3 municipalities): Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Lebrija (Santander), 20260601: payments above obligations or obligations above commitments; Tame (Arauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4503002**

- inconsistent (7 municipalities): Palmira (Valle Del Cauca) [5], Toribío (Cauca) [2], Medellín (Antioquia) [1], Villavicencio (Meta) [1], Confines (Santander) [1], Jamundí (Valle Del Cauca) [1], Puerto Caicedo (Putumayo) [1].

**MunicipalSpending.4503003**

- inconsistent (8 municipalities): Chaparral (Tolima) [4], San Bernardo del Viento (Córdoba) [2], Fúquene (Cundinamarca) [2], Villavicencio (Meta) [2], Confines (Santander) [2], Valle de San José (Santander) [2], Medellín (Antioquia) [1], Tame (Arauca) [1].

**MunicipalSpending.4503004**

- inconsistent (47 municipalities): Mocoa (Putumayo) [9], Villanueva (Bolívar) [8], Chaparral (Tolima) [6], Tame (Arauca) [5], Tunja (Boyacá) [4], Juan de Acosta (Atlántico) [3], Guadalupe (Santander) [3], Guavatá (Santander) [3], Fúquene (Cundinamarca) [3], Cucunubá (Cundinamarca) [3], Venadillo (Tolima) [3], Cereté (Córdoba) [3] and 35 more.

**MunicipalSpending.4503011**

- inconsistent (3 municipalities): Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20251201: payments above obligations or obligations above commitments; Toribío (Cauca), 20260601: payments above obligations or obligations above commitments; San Antero (Córdoba), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503012**

- inconsistent (2 municipalities): Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments; Orito (Putumayo), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4503013**

- inconsistent (11 municipalities): Vetas (Santander) [4], Matanza (Santander) [3], Medellín (Antioquia) [2], Galapa (Atlántico) [2], Pelaya (Cesar) [2], Suaita (Santander) [2], Barrancas (La Guajira) [1], Nueva Granada (Magdalena) [1], Iles (Nariño) [1], Oiba (Santander) [1], San Luis (Tolima) [1].

**MunicipalSpending.4503014**

- inconsistent (2 municipalities): Medellín (Antioquia), 20241201: payments above obligations or obligations above commitments; Villanueva (Santander), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503015**

- inconsistent (2 municipalities): Malambo (Atlántico), 20241201: payments above obligations or obligations above commitments; Malambo (Atlántico), 20251201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503016**

- inconsistent (7 municipalities): Pailitas (Cesar) [6], Piamonte (Cauca) [2], Yacuanquer (Nariño) [2], Villavicencio (Meta) [1], La Virginia (Risaralda) [1], Sabana de Torres (Santander) [1], Orito (Putumayo) [1].

**MunicipalSpending.4503017**

- inconsistent (5 municipalities): Medellín (Antioquia) [7], Nocaima (Cundinamarca) [1], Pivijay (Magdalena) [1], Jamundí (Valle Del Cauca) [1], Palmira (Valle Del Cauca) [1].

**MunicipalSpending.4503018**

- inconsistent (5 municipalities): Villavicencio (Meta) [4], Palmar de Varela (Atlántico) [1], Fúquene (Cundinamarca) [1], Dosquebradas (Risaralda) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.4503019**

- inconsistent (1 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503021**

- inconsistent (2 municipalities): Cereté (Córdoba), 20251201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20241201: payments above obligations or obligations above commitments; Chaparral (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503022**

- inconsistent (19 municipalities): Villavicencio (Meta) [3], Cachipay (Cundinamarca) [3], Villagarzón (Putumayo) [3], Marquetalia (Caldas) [2], Nocaima (Cundinamarca) [2], Viotá (Cundinamarca) [2], Pueblo Nuevo (Córdoba) [1], Manizales (Caldas) [1], Nemocón (Cundinamarca) [1], Arenal (Bolívar) [1], Santacruz (Nariño) [1], Toledo (Norte De Santander) [1] and 7 more.

**MunicipalSpending.4503023**

- inconsistent (10 municipalities): Dosquebradas (Risaralda) [3], Medellín (Antioquia) [2], Anolaima (Cundinamarca) [2], Gutiérrez (Cundinamarca) [1], Coromoro (Santander) [1], Macaravita (Santander) [1], San Vicente de Chucurí (Santander) [1], Natagaima (Tolima) [1], Palmira (Valle Del Cauca) [1], Chámeza (Casanare) [1].

**MunicipalSpending.4503024**

- inconsistent (1 municipalities): San Bernardo (Cundinamarca), 20260601: payments above obligations or obligations above commitments; San Bernardo (Cundinamarca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4503028**

- inconsistent (23 municipalities): San Bernardo del Viento (Córdoba) [4], Tunja (Boyacá) [3], Jamundí (Valle Del Cauca) [3], Luruaco (Atlántico) [3], Quebradanegra (Cundinamarca) [2], Yacuanquer (Nariño) [2], Pajarito (Boyacá) [2], Icononzo (Tolima) [2], Albania (Santander) [2], San Francisco (Putumayo) [2], Toribío (Cauca) [2], Pelaya (Cesar) [1] and 11 more.

**MunicipalSpending.4503030**

- inconsistent (1 municipalities): Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503031**

- inconsistent (1 municipalities): Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503032**

- inconsistent (1 municipalities): Maripí (Boyacá), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4503035**

- inconsistent (14 municipalities): Tinjacá (Boyacá) [2], Nocaima (Cundinamarca) [2], Guapotá (Santander) [2], Vetas (Santander) [2], Venadillo (Tolima) [2], Puerto Caicedo (Putumayo) [2], Galapa (Atlántico) [1], San Antero (Córdoba) [1], San Carlos (Córdoba) [1], Viotá (Cundinamarca) [1], Riohacha (La Guajira) [1], Guavatá (Santander) [1] and 2 more.

**MunicipalSpending.4503036**

- inconsistent (6 municipalities): Valle de San José (Santander) [3], Guataquí (Cundinamarca) [2], Nemocón (Cundinamarca) [1], Iles (Nariño) [1], Puerto Caicedo (Putumayo) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.4599001**

- inconsistent (8 municipalities): Villavicencio (Meta) [8], Riohacha (La Guajira) [5], Medellín (Antioquia) [2], Dosquebradas (Risaralda) [2], Los Santos (Santander) [2], Nueva Granada (Magdalena) [1], El Cerrito (Valle Del Cauca) [1], San Francisco (Putumayo) [1].

**MunicipalSpending.4599002**

- inconsistent (26 municipalities): Villavicencio (Meta) [6], Puerto Rondón (Arauca) [4], Jamundí (Valle Del Cauca) [3], Dosquebradas (Risaralda) [3], La Virginia (Risaralda) [2], Riohacha (La Guajira) [2], El Cerrito (Valle Del Cauca) [2], San Luis (Tolima) [2], San Joaquín (Santander) [2], Mocoa (Putumayo) [2], Susa (Cundinamarca) [1], Sasaima (Cundinamarca) [1] and 14 more.

**MunicipalSpending.4599003**

- inconsistent (1 municipalities): Riohacha (La Guajira), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599004**

- inconsistent (5 municipalities): Malambo (Atlántico), 20260601: payments above obligations or obligations above commitments; Sabanalarga (Atlántico), 20260601: payments above obligations or obligations above commitments; Villanueva (Bolívar), 20231201: payments above obligations or obligations above commitments; Belén de Los Andaquíes (Caquetá), 20251201: payments above obligations or obligations above commitments; Pelaya (Cesar), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599005**

- inconsistent (1 municipalities): San Luis (Tolima), 20241201: payments above obligations or obligations above commitments; San Luis (Tolima), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4599006**

- inconsistent (8 municipalities): Villavicencio (Meta) [6], Tunja (Boyacá) [2], Icononzo (Tolima) [2], La Virginia (Risaralda) [1], Guapotá (Santander) [1], Sabana de Torres (Santander) [1], San Luis de Palenque (Casanare) [1], Sibundoy (Putumayo) [1].

**MunicipalSpending.4599007**

- inconsistent (11 municipalities): Medellín (Antioquia) [3], Palmira (Valle Del Cauca) [3], San Luis de Palenque (Casanare) [2], Tunja (Boyacá) [1], Pelaya (Cesar) [1], Anolaima (Cundinamarca) [1], Sasaima (Cundinamarca) [1], Susa (Cundinamarca) [1], Santacruz (Nariño) [1], Villanueva (Santander) [1], Chaparral (Tolima) [1].

**MunicipalSpending.4599008**

- inconsistent (3 municipalities): Malambo (Atlántico), 20231201: payments above obligations or obligations above commitments; Cerro de San Antonio (Magdalena), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599009**

- inconsistent (5 municipalities): Fúquene (Cundinamarca) [5], Guapotá (Santander) [3], La Salina (Casanare) [2], Maripí (Boyacá) [1], Villavicencio (Meta) [1].

**MunicipalSpending.4599010**

- inconsistent (2 municipalities): Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Fúquene (Cundinamarca), 20231201: payments above obligations or obligations above commitments; La Salina (Casanare), 20231201: payments above obligations or obligations above commitments; La Salina (Casanare), 20231201: payments above obligations or obligations above commitments; La Salina (Casanare), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599011**

- inconsistent (15 municipalities): Tunja (Boyacá) [6], Orito (Putumayo) [6], Pelaya (Cesar) [4], Gutiérrez (Cundinamarca) [3], Usiacurí (Atlántico) [2], Sasaima (Cundinamarca) [2], Medellín (Antioquia) [1], Tinjacá (Boyacá) [1], Cereté (Córdoba) [1], Cabrera (Cundinamarca) [1], El Colegio (Cundinamarca) [1], Macaravita (Santander) [1] and 3 more.

**MunicipalSpending.4599013**

- inconsistent (4 municipalities): Mutatá (Antioquia), 20241201: payments above obligations or obligations above commitments; Piamonte (Cauca), 20251201: payments above obligations or obligations above commitments; Venecia (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Venecia (Cundinamarca), 20241201: payments above obligations or obligations above commitments; Venecia (Cundinamarca), 20251201: payments above obligations or obligations above commitments; San Luis (Tolima), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599014**

- inconsistent (2 municipalities): Galapa (Atlántico), 20251201: payments above obligations or obligations above commitments; Sibundoy (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599015**

- inconsistent (1 municipalities): Coyaima (Tolima), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599016**

- inconsistent (26 municipalities): Usiacurí (Atlántico) [15], Palmira (Valle Del Cauca) [9], Marquetalia (Caldas) [4], Villavicencio (Meta) [4], Nimaima (Cundinamarca) [3], Susa (Cundinamarca) [3], Toribío (Cauca) [3], Cereté (Córdoba) [2], San Carlos (Córdoba) [2], Fúquene (Cundinamarca) [2], Toledo (Norte De Santander) [2], Zipacón (Cundinamarca) [2] and 14 more.

**MunicipalSpending.4599017**

- inconsistent (23 municipalities): Medellín (Antioquia) [4], Chaparral (Tolima) [3], San Francisco (Putumayo) [3], Tame (Arauca) [2], Villavicencio (Meta) [2], Natagaima (Tolima) [2], Guamo (Tolima) [2], Villanueva (Bolívar) [1], San Pablo (Bolívar) [1], Sibundoy (Putumayo) [1], Mocoa (Putumayo) [1], Jamundí (Valle Del Cauca) [1] and 11 more.

**MunicipalSpending.4599018**

- inconsistent (9 municipalities): Dosquebradas (Risaralda) [6], Ariguaní (Magdalena) [5], Villavicencio (Meta) [5], Gómez Plata (Antioquia) [3], Jamundí (Valle Del Cauca) [3], Palmira (Valle Del Cauca) [2], Medellín (Antioquia) [1], Pailitas (Cesar) [1], Riohacha (La Guajira) [1].

**MunicipalSpending.4599019**

- inconsistent (18 municipalities): Palmira (Valle Del Cauca) [5], Tunja (Boyacá) [3], Dosquebradas (Risaralda) [3], Medellín (Antioquia) [2], Villavicencio (Meta) [2], Yacuanquer (Nariño) [2], Cereté (Córdoba) [1], Nueva Granada (Magdalena) [1], Toribío (Cauca) [1], Luruaco (Atlántico) [1], Piamonte (Cauca) [1], Guavatá (Santander) [1] and 6 more.

**MunicipalSpending.4599020**

- inconsistent (5 municipalities): Montebello (Antioquia), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Dosquebradas (Risaralda), 20251201: payments above obligations or obligations above commitments; Guamo (Tolima), 20231201: payments above obligations or obligations above commitments; Mocoa (Putumayo), 20241201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599021**

- inconsistent (5 municipalities): Ráquira (Boyacá), 20231201: payments above obligations or obligations above commitments; Nocaima (Cundinamarca), 20251201: payments above obligations or obligations above commitments; Tibacuy (Cundinamarca), 20231201: payments above obligations or obligations above commitments; Tibacuy (Cundinamarca), 20260601: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Jamundí (Valle Del Cauca), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599023**

- inconsistent (37 municipalities): Juan de Acosta (Atlántico) [10], Villavicencio (Meta) [8], Neiva (Huila) [7], Dosquebradas (Risaralda) [6], Palmira (Valle Del Cauca) [5], Oiba (Santander) [5], Guavatá (Santander) [4], Riohacha (La Guajira) [3], Puerto Nariño (Amazonas) [3], Cabrera (Cundinamarca) [3], Chaparral (Tolima) [2], Palmar (Santander) [2] and 25 more.

**MunicipalSpending.4599025**

- inconsistent (14 municipalities): Dosquebradas (Risaralda) [6], San Jerónimo (Antioquia) [5], Palmira (Valle Del Cauca) [4], Medellín (Antioquia) [1], San Pablo (Bolívar) [1], Inzá (Cauca) [1], Cabrera (Cundinamarca) [1], Fúquene (Cundinamarca) [1], Nemocón (Cundinamarca) [1], Guadalupe (Santander) [1], Guapotá (Santander) [1], Rionegro (Santander) [1] and 2 more.

**MunicipalSpending.4599026**

- inconsistent (2 municipalities): Galapa (Atlántico), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4599028**

- inconsistent (16 municipalities): Palmira (Valle Del Cauca) [5], Malambo (Atlántico) [2], Villavicencio (Meta) [2], Dosquebradas (Risaralda) [2], Venadillo (Tolima) [2], Puerto Rondón (Arauca) [2], Medellín (Antioquia) [1], Villanueva (Bolívar) [1], Coper (Boyacá) [1], Ráquira (Boyacá) [1], Piamonte (Cauca) [1], Imués (Nariño) [1] and 4 more.

**MunicipalSpending.4599029**

- inconsistent (6 municipalities): Nocaima (Cundinamarca) [4], Dosquebradas (Risaralda) [3], Natagaima (Tolima) [2], Jamundí (Valle Del Cauca) [2], Cucunubá (Cundinamarca) [1], Villavicencio (Meta) [1].

**MunicipalSpending.4599030**

- inconsistent (4 municipalities): Pelaya (Cesar), 20231201: payments above obligations or obligations above commitments; La Virginia (Risaralda), 20260601: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20231201: payments above obligations or obligations above commitments; San Francisco (Putumayo), 20231201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599031**

- inconsistent (98 municipalities): Pelaya (Cesar) [10], Tierralta (Córdoba) [10], Palmira (Valle Del Cauca) [10], Villavicencio (Meta) [10], Oiba (Santander) [9], Contratación (Santander) [8], Cereté (Córdoba) [7], San Bernardo del Viento (Córdoba) [7], San Francisco (Putumayo) [6], Sampués (Sucre) [5], Rionegro (Santander) [5], Fúquene (Cundinamarca) [5] and 86 more.

**MunicipalSpending.4599032**

- inconsistent (7 municipalities): Dosquebradas (Risaralda) [2], Natagaima (Tolima) [2], La Salina (Casanare) [2], Luruaco (Atlántico) [1], Santa Lucía (Atlántico) [1], Villanueva (Bolívar) [1], Villavicencio (Meta) [1].

**MunicipalSpending.4599033**

- inconsistent (14 municipalities): Villavicencio (Meta) [4], San Bernardo del Viento (Córdoba) [3], Riohacha (La Guajira) [3], Jamundí (Valle Del Cauca) [3], Chachagüí (Nariño) [2], Chaparral (Tolima) [2], Prado (Tolima) [2], San Pablo (Bolívar) [1], Bolívar (Cauca) [1], San Carlos (Córdoba) [1], La Virginia (Risaralda) [1], Charalá (Santander) [1] and 2 more.

**MunicipalSpending.4599034**

- inconsistent (7 municipalities): Villavicencio (Meta) [4], Guapotá (Santander) [3], Cereté (Córdoba) [2], Cucunubá (Cundinamarca) [2], Tuluá (Valle Del Cauca) [2], San Jerónimo (Antioquia) [1], Montería (Córdoba) [1].

**MunicipalSpending.4599036**

- inconsistent (3 municipalities): Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; El Cerrito (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments; Palmira (Valle Del Cauca), 20260601: payments above obligations or obligations above commitments.

**MunicipalSpending.4599037**

- inconsistent (3 municipalities): Tunja (Boyacá), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20251201: payments above obligations or obligations above commitments; Villavicencio (Meta), 20260601: payments above obligations or obligations above commitments; Puerto Caicedo (Putumayo), 20251201: payments above obligations or obligations above commitments.

**MunicipalSpending.4599038**

- inconsistent (8 municipalities): Sabanalarga (Atlántico) [2], Villanueva (Bolívar) [2], La Jagua de Ibirico (Cesar) [2], Belén de Los Andaquíes (Caquetá) [1], Fúquene (Cundinamarca) [1], Villavicencio (Meta) [1], Tame (Arauca) [1], Villagarzón (Putumayo) [1].

**MunicipalSpending.NO APLICA**

- inconsistent (266 municipalities): Juan de Acosta (Atlántico) [200], Sampués (Sucre) [152], Palmira (Valle Del Cauca) [150], Charta (Santander) [145], Chibolo (Magdalena) [144], Tierralta (Córdoba) [126], Usiacurí (Atlántico) [125], Riohacha (La Guajira) [119], Chaparral (Tolima) [115], La Salina (Casanare) [115], San Bernardo del Viento (Córdoba) [115], Malambo (Atlántico) [112] and 254 more.

## ICFES

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| MunicipalScoresMicro | global_z | 0 | 0 | 0 | 0 | 66 | 265 |
| MunicipalScoresMicro | math_z | 0 | 0 | 0 | 0 | 148 | 258 |
| MunicipalScoresMicro | students | 0 | 0 | 0 | 826 | 0 | 0 |
| MunicipalStudentContext | share_car | 0 | 0 | 0 | 0 | 109 | 46 |
| MunicipalStudentContext | share_computer | 0 | 0 | 0 | 0 | 186 | 68 |
| MunicipalStudentContext | share_internet | 0 | 0 | 0 | 0 | 124 | 41 |
| MunicipalStudentContext | share_mother_higher_ed | 0 | 0 | 0 | 0 | 302 | 86 |
| MunicipalStudentContext | share_mother_primary_or_less | 0 | 0 | 0 | 0 | 126 | 42 |
| MunicipalStudentContext | share_stratum_1_2 | 0 | 0 | 0 | 0 | 549 | 200 |
| MunicipalStudentContext | share_washing_machine | 0 | 0 | 0 | 0 | 226 | 140 |
| SaberProByMunicipality | citizenship | 0 | 0 | 0 | 0 | 179 | 84 |
| SaberProByMunicipality | critical_reading | 0 | 0 | 0 | 0 | 182 | 149 |
| SaberProByMunicipality | english | 0 | 0 | 0 | 0 | 163 | 207 |
| SaberProByMunicipality | quantitative_reasoning | 0 | 0 | 0 | 0 | 153 | 119 |
| SaberProByMunicipality | written_communication | 0 | 0 | 0 | 0 | 261 | 175 |

**MunicipalScoresMicro.global_z**

- small_base (54 municipalities): San José de Miranda (Santander) [4], Sipí (Chocó) [4], Tenjo (Cundinamarca) [3], Barrancominas (Guainía) [2], Puerto Santander (ANM) (Amazonas) [2], Cabrera (Santander) [2], Páramo (Santander) [2], Gámbita (Santander) [1], Pamplonita (Norte De Santander) [1], Pijao (Quindío) [1], Salento (Quindío) [1], Marsella (Risaralda) [1] and 42 more.
- extreme (67 municipalities): Cota (Cundinamarca) [20], Albania (La Guajira) [17], La Calera (Cundinamarca) [14], Salento (Quindío) [14], Retiro (Antioquia) [13], Sopó (Cundinamarca) [13], Cajicá (Cundinamarca) [11], Tenjo (Cundinamarca) [11], Puerto Colombia (Atlántico) [11], Villamaría (Caldas) [10], Chía (Cundinamarca) [9], Roldanillo (Valle Del Cauca) [8] and 55 more.

**MunicipalScoresMicro.math_z**

- small_base (119 municipalities): San José de Miranda (Santander) [4], Puerto Santander (ANM) (Amazonas) [4], Suratá (Santander) [4], Tenjo (Cundinamarca) [3], La Calera (Cundinamarca) [3], Roldanillo (Valle Del Cauca) [3], El Litoral del San Juan (Chocó) [2], Cabrera (Santander) [2], Gámbita (Santander) [2], Páramo (Santander) [2], San Bernardo (Cundinamarca) [2], Santa Rosa de Viterbo (Boyacá) [2] and 107 more.
- extreme (97 municipalities): Albania (La Guajira) [17], Salento (Quindío) [15], Cota (Cundinamarca) [14], Retiro (Antioquia) [11], Sopó (Cundinamarca) [10], La Calera (Cundinamarca) [10], Villamaría (Caldas) [10], Puerto Colombia (Atlántico) [9], Floridablanca (Santander) [8], Tenjo (Cundinamarca) [8], Roldanillo (Valle Del Cauca) [7], Charalá (Santander) [7] and 85 more.

**MunicipalScoresMicro.students**

- break (404 municipalities): Ipiales (Nariño) [10], Florida (Valle Del Cauca) [9], Apartadó (Antioquia) [8], Espinal (Tolima) [8], El Cerrito (Valle Del Cauca) [7], Tuluá (Valle Del Cauca) [7], Itagüí (Antioquia) [7], Garzón (Huila) [7], Arauca (Arauca) [6], Hispania (Antioquia) [6], Funza (Cundinamarca) [6], Toledo (Antioquia) [6] and 392 more.

**MunicipalStudentContext.share_car**

- small_base (79 municipalities): Clemencia (Bolívar) [6], Villanueva (Bolívar) [4], San Cristóbal (Bolívar) [3], Regidor (Bolívar) [3], Ponedera (Atlántico) [3], Florencia (Cauca) [3], Padilla (Cauca) [3], La Victoria (Boyacá) [2], Albán (Nariño) [2], Circasia (Quindío) [2], Palmar (Santander) [2], Sativasur (Boyacá) [2] and 67 more.
- extreme (24 municipalities): Tenjo (Cundinamarca) [8], Retiro (Antioquia) [6], Salento (Quindío) [5], Albania (La Guajira) [4], El Cerrito (Valle Del Cauca) [2], Tuchín (Córdoba) [2], La Calera (Cundinamarca) [2], Maicao (La Guajira) [1], Valle del Guamuez (Putumayo) [1], Roldanillo (Valle Del Cauca) [1], Dagua (Valle Del Cauca) [1], Ortega (Tolima) [1] and 12 more.

**MunicipalStudentContext.share_computer**

- small_base (123 municipalities): Medio Atrato (Chocó) [8], Sipí (Chocó) [5], Ocaña (Norte De Santander) [5], El Litoral del San Juan (Chocó) [4], Alto Baudó (Chocó) [4], San Calixto (Norte De Santander) [4], Regidor (Bolívar) [3], Gama (Cundinamarca) [3], Quibdó (Chocó) [3], Río Iró (Chocó) [3], Mosquera (Nariño) [3], Francisco Pizarro (Nariño) [3] and 111 more.
- extreme (38 municipalities): Tuchín (Córdoba) [6], Timbiquí (Cauca) [5], Tenjo (Cundinamarca) [5], Retiro (Antioquia) [4], Villanueva (Bolívar) [4], Salento (Quindío) [4], Albania (La Guajira) [3], Alto Baudó (Chocó) [2], Palmar de Varela (Atlántico) [2], Puerto Colombia (Atlántico) [2], La Calera (Cundinamarca) [2], Puebloviejo (Magdalena) [2] and 26 more.

**MunicipalStudentContext.share_internet**

- small_base (90 municipalities): Regidor (Bolívar) [4], San Cristóbal (Bolívar) [4], Albán (Nariño) [3], Florencia (Cauca) [3], Ocaña (Norte De Santander) [3], Ospina (Nariño) [3], Sutatenza (Boyacá) [3], Tuchín (Córdoba) [3], Unión Panamericana (Chocó) [2], Sucre (Cauca) [2], Padilla (Cauca) [2], Puerres (Nariño) [2] and 78 more.
- extreme (26 municipalities): Retiro (Antioquia) [4], Salento (Quindío) [4], Tenjo (Cundinamarca) [4], Albania (La Guajira) [4], Usiacurí (Atlántico) [2], La Calera (Cundinamarca) [2], Puerto Colombia (Atlántico) [2], Yumbo (Valle Del Cauca) [1], Pradera (Valle Del Cauca) [1], Palmira (Valle Del Cauca) [1], Jamundí (Valle Del Cauca) [1], El Cerrito (Valle Del Cauca) [1] and 14 more.

**MunicipalStudentContext.share_mother_higher_ed**

- small_base (182 municipalities): Chivatá (Boyacá) [9], Guataquí (Cundinamarca) [5], Boyacá (Boyacá) [5], Palmar (Santander) [5], Viracachá (Boyacá) [5], Clemencia (Bolívar) [4], Ocamonte (Santander) [4], Ponedera (Atlántico) [4], Guavatá (Santander) [4], La Victoria (Boyacá) [4], Nariño (Nariño) [4], Tutazá (Boyacá) [3] and 170 more.
- extreme (33 municipalities): Tenjo (Cundinamarca) [18], Retiro (Antioquia) [12], Salento (Quindío) [6], Albania (La Guajira) [6], Roldanillo (Valle Del Cauca) [3], El Cerrito (Valle Del Cauca) [3], San Juan del Cesar (La Guajira) [3], Timbiquí (Cauca) [2], Dibulla (La Guajira) [2], Mitú (Vaupés) [2], Aguachica (Cesar) [2], Restrepo (Meta) [2] and 21 more.

**MunicipalStudentContext.share_mother_primary_or_less**

- small_base (89 municipalities): Nariño (Nariño) [7], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [5], Medio Atrato (Chocó) [5], Sipí (Chocó) [4], Málaga (Santander) [3], Cali (Valle Del Cauca) [2], San Andrés de Tumaco (Nariño) [2], Sibaté (Cundinamarca) [2], Cartago (Valle Del Cauca) [2], Jordán (Santander) [2], Belén de Umbría (Risaralda) [2], Palmira (Valle Del Cauca) [2] and 77 more.
- extreme (30 municipalities): Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [5], Albania (La Guajira) [4], Salento (Quindío) [3], Soplaviento (Bolívar) [2], Tuchín (Córdoba) [2], Sutatausa (Cundinamarca) [2], Villanueva (La Guajira) [1], La Pedrera (ANM) (Amazonas) [1], El Encanto (ANM) (Amazonas) [1], Puerto Asís (Putumayo) [1], Pradera (Valle Del Cauca) [1], Enciso (Santander) [1] and 18 more.

**MunicipalStudentContext.share_stratum_1_2**

- small_base (272 municipalities): Castilla la Nueva (Meta) [5], Santa Rosa de Osos (Antioquia) [5], Nilo (Cundinamarca) [5], Balboa (Risaralda) [5], Oiba (Santander) [4], San Carlos (Antioquia) [4], Barrancas (La Guajira) [4], Remedios (Antioquia) [4], Puerto Salgar (Cundinamarca) [4], Amalfi (Antioquia) [4], Tenza (Boyacá) [4], Santafé de Antioquia (Antioquia) [4] and 260 more.
- extreme (100 municipalities): Tenjo (Cundinamarca) [11], Salento (Quindío) [11], Retiro (Antioquia) [10], Albania (La Guajira) [9], San Martín (Meta) [8], Entrerríos (Antioquia) [5], Guatavita (Cundinamarca) [5], La Ceja (Antioquia) [4], Guasca (Cundinamarca) [3], Santa Rosa de Osos (Antioquia) [3], Sonsón (Antioquia) [3], Urrao (Antioquia) [3] and 88 more.

**MunicipalStudentContext.share_washing_machine**

- small_base (137 municipalities): Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [7], Providencia (Nariño) [7], Gama (Cundinamarca) [6], Chivatá (Boyacá) [5], Contadero (Nariño) [5], Arboleda (Nariño) [4], El Litoral del San Juan (Chocó) [4], Nariño (Nariño) [4], Ocaña (Norte De Santander) [4], Medio Atrato (Chocó) [4], Santa Bárbara (Nariño) [4], Málaga (Santander) [3] and 125 more.
- extreme (60 municipalities): Guaitarilla (Nariño) [9], Ospina (Nariño) [6], Colón (Nariño) [6], Cuaspud Carlosama (Nariño) [6], San Pedro de Cartago (Nariño) [6], San Bernardo (Nariño) [6], Iles (Nariño) [5], Jambaló (Cauca) [5], Padilla (Cauca) [4], Florencia (Cauca) [4], Albán (Nariño) [4], Palmar de Varela (Atlántico) [4] and 48 more.

**SaberProByMunicipality.citizenship**

- small_base (130 municipalities): San Cristóbal (Bolívar) [5], Ponedera (Atlántico) [4], Chalán (Sucre) [3], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [3], La Tola (Nariño) [3], Caicedo (Antioquia) [3], Nariño (Nariño) [3], Unión Panamericana (Chocó) [3], Villa Rica (Cauca) [3], Clemencia (Bolívar) [3], Jerusalén (Cundinamarca) [2], Hatillo de Loba (Bolívar) [2] and 118 more.
- extreme (52 municipalities): Quibdó (Chocó) [8], Retiro (Antioquia) [5], Cota (Cundinamarca) [3], Tadó (Chocó) [3], Manaure (La Guajira) [3], Barbacoas (Nariño) [3], Timbiquí (Cauca) [2], Río Quito (Chocó) [2], Uribia (La Guajira) [2], Istmina (Chocó) [2], Tenjo (Cundinamarca) [2], Subachoque (Cundinamarca) [2] and 40 more.

**SaberProByMunicipality.critical_reading**

- small_base (141 municipalities): Padilla (Cauca) [5], San Cristóbal (Bolívar) [3], Jordán (Santander) [3], Ponedera (Atlántico) [3], Campamento (Antioquia) [3], Tubará (Atlántico) [3], Santa Rosa (Bolívar) [3], Pajarito (Boyacá) [2], Yalí (Antioquia) [2], Aguada (Santander) [2], Barranco de Loba (Bolívar) [2], Clemencia (Bolívar) [2] and 129 more.
- extreme (83 municipalities): Quibdó (Chocó) [10], Marinilla (Antioquia) [7], Cota (Cundinamarca) [6], Istmina (Chocó) [5], Tenjo (Cundinamarca) [5], Retiro (Antioquia) [5], Santa Rosa de Osos (Antioquia) [5], Subachoque (Cundinamarca) [4], Guapi (Cauca) [4], Manaure (La Guajira) [4], El Santuario (Antioquia) [4], Paipa (Boyacá) [3] and 71 more.

**SaberProByMunicipality.english**

- small_base (131 municipalities): Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [7], Concordia (Antioquia) [4], Salento (Quindío) [3], Padilla (Cauca) [2], Solita (Caquetá) [2], Cómbita (Boyacá) [2], La Capilla (Boyacá) [2], Campohermoso (Boyacá) [2], Lejanías (Meta) [2], San Eduardo (Boyacá) [2], San Cristóbal (Bolívar) [2], Río Viejo (Bolívar) [2] and 119 more.
- extreme (91 municipalities): Cota (Cundinamarca) [12], Tenjo (Cundinamarca) [11], Retiro (Antioquia) [10], Salento (Quindío) [8], Marinilla (Antioquia) [7], Subachoque (Cundinamarca) [7], Puerto Colombia (Atlántico) [6], Albania (La Guajira) [6], Guapi (Cauca) [5], Nobsa (Boyacá) [4], La Ceja (Antioquia) [4], Barbacoas (Nariño) [4] and 79 more.

**SaberProByMunicipality.quantitative_reasoning**

- small_base (106 municipalities): Padilla (Cauca) [6], Clemencia (Bolívar) [5], Unión Panamericana (Chocó) [4], Tubará (Atlántico) [3], Palmito (Sucre) [3], San Eduardo (Boyacá) [3], Distracción (La Guajira) [3], San Cristóbal (Bolívar) [3], Regidor (Bolívar) [3], Ponedera (Atlántico) [3], Panqueba (Boyacá) [3], Zipacón (Cundinamarca) [3] and 94 more.
- extreme (65 municipalities): Quibdó (Chocó) [12], Tadó (Chocó) [6], Istmina (Chocó) [6], Guapi (Cauca) [5], Manaure (La Guajira) [4], Paipa (Boyacá) [4], Condoto (Chocó) [3], Uribia (La Guajira) [3], Barbacoas (Nariño) [3], La Mesa (Cundinamarca) [2], Olaya Herrera (Nariño) [2], Cota (Cundinamarca) [2] and 53 more.

**SaberProByMunicipality.written_communication**

- small_base (191 municipalities): Clemencia (Bolívar) [7], Unión Panamericana (Chocó) [5], Cerinza (Boyacá) [4], Tópaga (Boyacá) [4], Vijes (Valle Del Cauca) [4], Turbaná (Bolívar) [4], Polonuevo (Atlántico) [3], Córdoba (Quindío) [3], Ponedera (Atlántico) [3], Santa Lucía (Atlántico) [3], Argelia (Cauca) [3], Santo Tomás (Atlántico) [3] and 179 more.
- extreme (147 municipalities): Quibdó (Chocó) [7], Juradó (Chocó) [4], Cota (Cundinamarca) [3], Barbacoas (Nariño) [3], Marulanda (Caldas) [3], Alto Baudó (Chocó) [2], Paipa (Boyacá) [2], Lloró (Chocó) [2], Nóvita (Chocó) [2], Nuquí (Chocó) [2], Río Quito (Chocó) [2], San José del Palmar (Chocó) [2] and 135 more.

## MEN

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| EducationAuthority | entity_id | 0 | 0 | 0 | 2 | 0 | 0 |
| EnrolmentAndDropout | approval | 0 | 0 | 0 | 4 | 0 | 300 |
| EnrolmentAndDropout | dropout | 0 | 0 | 0 | 0 | 0 | 35 |
| EnrolmentAndDropout | dropout_upper_secondary | 0 | 0 | 0 | 59 | 0 | 40 |
| EnrolmentAndDropout | net_enrolment | 0 | 0 | 2,190 | 453 | 0 | 226 |
| EnrolmentAndDropout | net_enrolment_upper_secondary | 0 | 0 | 31 | 191 | 0 | 252 |
| EnrolmentAndDropout | repetition | 0 | 0 | 0 | 1 | 0 | 191 |
| SchoolYears | character_code | 0 | 21,248 | 0 | 0 | 0 | 0 |
| SchoolYears | codigo_dane | 300 | 0 | 16,157 | 0 | 0 | 0 |
| SchoolYears | enrolment | 0 | 0 | 0 | 626 | 0 | 0 |
| SchoolYears | municipality_id | 0 | 0 | 9,753 | 0 | 0 | 0 |

**EducationAuthority.entity_id**

- break (2 municipalities): La Estrella (Antioquia), 2023: the certified entity changes: 3758 to 7738; Funza (Cundinamarca), 2019: the certified entity changes: 3785 to 10851.

**EnrolmentAndDropout.approval**

- break (3 municipalities): Norosí (Bolívar), 2020: 83.7 the year before; Unión Panamericana (Chocó), 2020: 91.5 the year before; Unión Panamericana (Chocó), 2021: 53.0 the year before; Pana Pana (ANM) (Guainía), 2023: 58.2 the year before.
- extreme (153 municipalities): La Tola (Nariño) [7], Ipiales (Nariño) [7], Sutatausa (Cundinamarca) [6], Mosquera (Nariño) [6], Ancuya (Nariño) [5], Tabio (Cundinamarca) [5], Cumbal (Nariño) [5], Pupiales (Nariño) [4], Tibirita (Cundinamarca) [4], La Unión (Nariño) [4], La Florida (Nariño) [4], Imués (Nariño) [4] and 141 more.

**EnrolmentAndDropout.dropout**

- extreme (25 municipalities): Clemencia (Bolívar) [3], Cerinza (Boyacá) [3], Nariño (Nariño) [3], Papunahua (ANM) (Vaupés) [2], Providencia (Nariño) [2], El Encanto (ANM) (Amazonas) [2], Suan (Atlántico) [2], Morichal (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Tarapacá (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1], Puerto Alegría (ANM) (Amazonas) [1] and 13 more.

**EnrolmentAndDropout.dropout_upper_secondary**

- break (29 municipalities): Magüí (Nariño) [3], Aguachica (Cesar) [2], Pailitas (Cesar) [2], Morichal (ANM) (Guainía) [2], Útica (Cundinamarca) [2], Funza (Cundinamarca) [2], Tamalameque (Cesar) [2], San Martín (Cesar) [2], San Diego (Cesar) [2], San Alberto (Cesar) [2], La Paz (Cesar) [2], Río de Oro (Cesar) [2] and 17 more.
- extreme (36 municipalities): Santa Rosa (Bolívar) [3], El Encanto (ANM) (Amazonas) [2], Magüí (Nariño) [2], San Martín (Cesar) [1], Pailitas (Cesar) [1], Pelaya (Cesar) [1], Río de Oro (Cesar) [1], La Paz (Cesar) [1], San Alberto (Cesar) [1], San Diego (Cesar) [1], Tamalameque (Cesar) [1], La Jagua de Ibirico (Cesar) [1] and 24 more.

**EnrolmentAndDropout.net_enrolment**

- inconsistent (433 municipalities): La Calera (Cundinamarca) [13], Bahía Solano (Chocó) [13], Fúquene (Cundinamarca) [13], Corozal (Sucre) [13], San Gil (Santander) [13], Istmina (Chocó) [13], Puente Nacional (Santander) [13], Retiro (Antioquia) [13], Soracá (Boyacá) [13], Sogamoso (Boyacá) [13], Barrancabermeja (Santander) [13], Turmequé (Boyacá) [13] and 421 more.
- break (265 municipalities): Concepción (Antioquia) [4], Cértegui (Chocó) [3], Santa Rosa (Cauca) [3], Palmar (Santander) [3], San Benito (Santander) [3], San Gil (Santander) [3], El Paso (Cesar) [3], Curumaní (Cesar) [3], Chiriguaná (Cesar) [3], Becerril (Cesar) [3], Guamal (Meta) [3], Coloso (Sucre) [3] and 253 more.
- extreme (172 municipalities): Papunahua (ANM) (Vaupés) [6], Taraira (Vaupés) [4], Villa de San Diego de Ubaté (Cundinamarca) [3], Mutatá (Antioquia) [3], Sativasur (Boyacá) [3], El Paso (Cesar) [3], Talaigua Nuevo (Bolívar) [3], Rionegro (Santander) [3], Suaita (Santander) [3], Paipa (Boyacá) [3], La Victoria (ANM) (Amazonas) [3], Cunday (Tolima) [2] and 160 more.

**EnrolmentAndDropout.net_enrolment_upper_secondary**

- inconsistent (10 municipalities): Cota (Cundinamarca) [9], Turmequé (Boyacá) [6], Quetame (Cundinamarca) [4], Fúquene (Cundinamarca) [3], Puerto Colombia (Atlántico) [2], Soracá (Boyacá) [2], Puente Nacional (Santander) [2], Panqueba (Boyacá) [1], Soatá (Boyacá) [1], Restrepo (Meta) [1].
- break (133 municipalities): Berbeo (Boyacá) [3], Albán (Nariño) [3], Nilo (Cundinamarca) [3], Caloto (Cauca) [3], La Macarena (Meta) [2], San Juanito (Meta) [2], Restrepo (Meta) [2], González (Cesar) [2], Gámbita (Santander) [2], Bituima (Cundinamarca) [2], El Guacamayo (Santander) [2], Cabrera (Santander) [2] and 121 more.
- extreme (74 municipalities): Manaure (La Guajira) [13], Medio Atrato (Chocó) [13], Tenjo (Cundinamarca) [11], Santa Bárbara (Nariño) [10], Puente Nacional (Santander) [8], Mosquera (Nariño) [8], Magüí (Nariño) [7], Alto Baudó (Chocó) [7], Turmequé (Boyacá) [7], Cumaribo (Vichada) [7], Francisco Pizarro (Nariño) [7], Pijao (Quindío) [6] and 62 more.

**EnrolmentAndDropout.repetition**

- break (1 municipalities): Norosí (Bolívar), 2021: 5.9 the year before.
- extreme (159 municipalities): San Cristóbal (Bolívar) [3], Sutatausa (Cundinamarca) [3], San Luis de Palenque (Casanare) [2], Junín (Cundinamarca) [2], Manta (Cundinamarca) [2], Coper (Boyacá) [2], Cubará (Boyacá) [2], Nariño (Nariño) [2], Chámeza (Casanare) [2], Gachantivá (Boyacá) [2], Macanal (Boyacá) [2], Nocaima (Cundinamarca) [2] and 147 more.

**SchoolYears.character_code**

- missing (470 municipalities): Bogotá, D.C. (Bogotá, D.C.) [1292], Cartagena de Indias (Bolívar) [855], Santa Marta (Magdalena) [661], Barranquilla (Atlántico) [657], Medellín (Antioquia) [652], Pereira (Risaralda) [545], Buenaventura (Valle Del Cauca) [539], Valledupar (Cesar) [513], Villavicencio (Meta) [484], Tunja (Boyacá) [434], Riohacha (La Guajira) [388], Popayán (Cauca) [372] and 458 more.

**SchoolYears.codigo_dane**

- error (142 municipalities): Bogotá, D.C. (Bogotá, D.C.) [56], Abejorral (Antioquia) [28], Cali (Valle Del Cauca) [12], Ituango (Antioquia) [8], Morales (Cauca) [7], Ansermanuevo (Valle Del Cauca) [6], Jamundí (Valle Del Cauca) [6], Florida (Valle Del Cauca) [5], Inírida (Guainía) [4], Medellín (Antioquia) [3], El Carmen de Viboral (Antioquia) [3], Dagua (Valle Del Cauca) [3] and 130 more.
- inconsistent (1116 municipalities): Bogotá, D.C. (Bogotá, D.C.) [1779], Cali (Valle Del Cauca) [652], Medellín (Antioquia) [518], Barranquilla (Atlántico) [452], Cartagena de Indias (Bolívar) [283], Santa Marta (Magdalena) [250], Soledad (Atlántico) [239], San José de Cúcuta (Norte De Santander) [234], Villavicencio (Meta) [210], Ibagué (Tolima) [197], Soacha (Cundinamarca) [181], Pereira (Risaralda) [179] and 1104 more.

**SchoolYears.enrolment**

- break (128 municipalities): Bogotá, D.C. (Bogotá, D.C.) [95], Soledad (Atlántico) [64], Cali (Valle Del Cauca) [56], Cartagena de Indias (Bolívar) [35], Medellín (Antioquia) [35], Villavicencio (Meta) [19], Soacha (Cundinamarca) [17], Buenaventura (Valle Del Cauca) [16], Barranquilla (Atlántico) [15], Bucaramanga (Santander) [15], Bello (Antioquia) [12], Florencia (Caquetá) [11] and 116 more.

**SchoolYears.municipality_id**

- inconsistent (214 municipalities): Bogotá, D.C. (Bogotá, D.C.) [2804], Cumaribo (Vichada) [271], Florencia (Caquetá) [240], Zona Bananera (Magdalena) [146], Puerto Guzmán (Putumayo) [143], Puerto Rico (Caquetá) [132], Tuchín (Córdoba) [132], San Vicente del Caguán (Caquetá) [114], Solano (Caquetá) [110], San Bernardo (Nariño) [102], Pueblo Bello (Cesar) [99], Chachagüí (Nariño) [97] and 202 more.

## Police

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | police_domestic_violence | 0 | 14 | 0 | 0 | 94 | 46 |
| PeriodRates | police_homicide | 0 | 14 | 0 | 0 | 102 | 2 |
| PeriodRates | police_massacre_events | 0 | 6 | 0 | 0 | 92 | 18 |
| PeriodRates | police_massacre_victims | 0 | 6 | 0 | 0 | 18 | 148 |
| PeriodRates | police_sexual_violence | 0 | 14 | 0 | 0 | 109 | 72 |
| PoliceDailyCases | police_domestic_violence | 0 | 0 | 0 | 273 | 0 | 0 |
| PoliceDailyCases | police_homicide | 0 | 0 | 0 | 16 | 0 | 0 |
| PoliceDailyCases | police_sexual_violence | 0 | 0 | 0 | 82 | 0 | 0 |

**PeriodRates.police_domestic_violence**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (57 municipalities): Cepitá (Santander) [5], San Jacinto del Cauca (Bolívar) [5], Bojayá (Chocó) [4], Río Quito (Chocó) [3], La Pedrera (ANM) (Amazonas) [3], Sácama (Casanare) [3], Jordán (Santander) [3], San Calixto (Norte De Santander) [3], Norosí (Bolívar) [3], Concordia (Magdalena) [3], Padilla (Cauca) [2], La Victoria (ANM) (Amazonas) [2] and 45 more.
- extreme (17 municipalities): Carmen del Darién (Chocó) [5], Olaya Herrera (Nariño) [4], San Felipe (ANM) (Guainía) [4], Barrancominas (Guainía) [4], Manaure (La Guajira) [4], Uribia (La Guajira) [4], Zapayán (Magdalena) [4], San Jacinto del Cauca (Bolívar) [2], La Chorrera (ANM) (Amazonas) [2], Roberto Payán (Nariño) [2], Remolino (Magdalena) [2], Mosquera (Nariño) [2] and 5 more.

**PeriodRates.police_homicide**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (48 municipalities): San Cristóbal (Bolívar) [8], Polonuevo (Atlántico) [2], California (Santander) [2], Nemocón (Cundinamarca) [2], Susa (Cundinamarca) [2], Tibirita (Cundinamarca) [2], Cértegui (Chocó) [2], Cerro de San Antonio (Magdalena) [2], Remolino (Magdalena) [2], Salamina (Magdalena) [2], Zapayán (Magdalena) [2], Nariño (Nariño) [2] and 36 more.
- extreme (1 municipalities): Puerto Alegría (ANM) (Amazonas) [2].

**PeriodRates.police_massacre_events**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (46 municipalities): Abejorral (Antioquia) [2], Landázuri (Santander) [2], Nátaga (Huila) [2], Zona Bananera (Magdalena) [2], Uribe (Meta) [2], Puerto Lleras (Meta) [2], Colón (Nariño) [2], Policarpa (Nariño) [2], San Andrés de Tumaco (Nariño) [2], El Carmen (Norte De Santander) [2], La Celia (Risaralda) [2], Chaparral (Tolima) [2] and 34 more.
- extreme (9 municipalities): Soledad (Atlántico) [2], Corinto (Cauca) [2], Miranda (Cauca) [2], Quibdó (Chocó) [2], Ipiales (Nariño) [2], San José de Cúcuta (Norte De Santander) [2], Ansermanuevo (Valle Del Cauca) [2], Cartago (Valle Del Cauca) [2], Toro (Valle Del Cauca) [2].

**PeriodRates.police_massacre_victims**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (9 municipalities): Remedios (Antioquia) [2], Tarso (Antioquia) [2], Puerto Rico (Caquetá) [2], Buenos Aires (Cauca) [2], Mercaderes (Cauca) [2], El Copey (Cesar) [2], La Celia (Risaralda) [2], Saravena (Arauca) [2], Maní (Casanare) [2].
- extreme (70 municipalities): Balboa (Cauca) [4], Guadalajara de Buga (Valle Del Cauca) [4], Puerto Guzmán (Putumayo) [4], Cartago (Valle Del Cauca) [4], Abejorral (Antioquia) [2], San Andrés de Tumaco (Nariño) [2], Santuario (Risaralda) [2], El Carmen (Norte De Santander) [2], Ábrego (Norte De Santander) [2], San José de Cúcuta (Norte De Santander) [2], Policarpa (Nariño) [2], Landázuri (Santander) [2] and 58 more.

**PeriodRates.police_sexual_violence**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (68 municipalities): La Victoria (ANM) (Amazonas) [4], Bituima (Cundinamarca) [3], Sutatausa (Cundinamarca) [3], Arroyohondo (Bolívar) [3], Jordán (Santander) [3], Cabrera (Santander) [3], Remolino (Magdalena) [3], Mosquera (Nariño) [2], Nemocón (Cundinamarca) [2], Medio Atrato (Chocó) [2], Sabanalarga (Antioquia) [2], Belén (Nariño) [2] and 56 more.
- extreme (25 municipalities): Tarapacá (ANM) (Amazonas) [6], Manaure (La Guajira) [6], Tuchín (Córdoba) [5], Marinilla (Antioquia) [4], Olaya Herrera (Nariño) [4], Zapayán (Magdalena) [4], Uribia (La Guajira) [4], Carmen del Darién (Chocó) [4], Cacahual (ANM) (Guainía) [4], El Litoral del San Juan (Chocó) [3], Alto Baudó (Chocó) [2], San Pelayo (Córdoba) [2] and 13 more.

**PoliceDailyCases.police_domestic_violence**

- break (241 municipalities): San Bernardo del Viento (Córdoba) [3], Zipaquirá (Cundinamarca) [3], Soacha (Cundinamarca) [2], Maicao (La Guajira) [2], San Antero (Córdoba) [2], San Andrés Sotavento (Córdoba) [2], Melgar (Tolima) [2], Planeta Rica (Córdoba) [2], San Juan Nepomuceno (Bolívar) [2], Icononzo (Tolima) [2], Montelíbano (Córdoba) [2], Aquitania (Boyacá) [2] and 229 more.

**PoliceDailyCases.police_homicide**

- break (16 municipalities): Briceño (Antioquia) [1], Girardota (Antioquia) [1], Remedios (Antioquia) [1], Santa Rosa de Osos (Antioquia) [1], Segovia (Antioquia) [1], Vegachí (Antioquia) [1], Baranoa (Atlántico) [1], Toribío (Cauca) [1], Ayapel (Córdoba) [1], La Apartada (Córdoba) [1], Planeta Rica (Córdoba) [1], Valencia (Córdoba) [1] and 4 more.

**PoliceDailyCases.police_sexual_violence**

- break (81 municipalities): Zipaquirá (Cundinamarca) [2], Medellín (Antioquia) [1], Riohacha (La Guajira) [1], San José de Cúcuta (Norte De Santander) [1], La Unión (Nariño) [1], Acacías (Meta) [1], Villavicencio (Meta) [1], Guamal (Magdalena) [1], Fundación (Magdalena) [1], Ciénaga (Magdalena) [1], Quibdó (Chocó) [1], Funza (Cundinamarca) [1] and 69 more.

## CNMH

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | cnmh_act_of_war_events | 0 | 14 | 0 | 0 | 30 | 815 |
| PeriodRates | cnmh_act_of_war_victims | 0 | 14 | 0 | 0 | 30 | 802 |
| PeriodRates | cnmh_attack_on_a_town_events | 0 | 14 | 0 | 0 | 56 | 8 |
| PeriodRates | cnmh_attack_on_a_town_victims | 0 | 14 | 0 | 0 | 8 | 18 |
| PeriodRates | cnmh_damage_to_civilian_property_events | 0 | 14 | 0 | 0 | 79 | 495 |
| PeriodRates | cnmh_damage_to_civilian_property_victims | 0 | 14 | 0 | 0 | 92 | 32 |
| PeriodRates | cnmh_forced_disappearance_events | 0 | 14 | 0 | 0 | 169 | 528 |
| PeriodRates | cnmh_forced_disappearance_victims | 0 | 14 | 0 | 0 | 114 | 588 |
| PeriodRates | cnmh_kidnapping_events | 0 | 14 | 0 | 0 | 127 | 415 |
| PeriodRates | cnmh_kidnapping_victims | 0 | 14 | 0 | 0 | 43 | 579 |
| PeriodRates | cnmh_landmines_and_explosive_remnants_events | 0 | 14 | 0 | 0 | 66 | 624 |
| PeriodRates | cnmh_landmines_and_explosive_remnants_victims | 0 | 14 | 0 | 0 | 52 | 587 |
| PeriodRates | cnmh_massacre_events | 0 | 14 | 0 | 0 | 306 | 67 |
| PeriodRates | cnmh_massacre_victims | 0 | 14 | 0 | 0 | 0 | 561 |
| PeriodRates | cnmh_recruitment_of_children_and_adolescents_events | 0 | 14 | 0 | 0 | 149 | 297 |
| PeriodRates | cnmh_recruitment_of_children_and_adolescents_victims | 0 | 14 | 0 | 0 | 113 | 344 |
| PeriodRates | cnmh_selective_killing_events | 0 | 14 | 0 | 0 | 5 | 864 |
| PeriodRates | cnmh_selective_killing_victims | 0 | 14 | 0 | 0 | 5 | 994 |
| PeriodRates | cnmh_sexual_violence_events | 0 | 14 | 0 | 0 | 62 | 358 |
| PeriodRates | cnmh_sexual_violence_victims | 0 | 14 | 0 | 0 | 51 | 407 |
| PeriodRates | cnmh_terrorist_attack_events | 0 | 14 | 0 | 0 | 180 | 40 |
| PeriodRates | cnmh_terrorist_attack_victims | 0 | 14 | 0 | 0 | 42 | 78 |

**PeriodRates.cnmh_act_of_war_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (15 municipalities): Florencia (Cauca) [3], Betulia (Antioquia) [2], Guadalupe (Antioquia) [2], Jericó (Antioquia) [2], Venecia (Antioquia) [2], Usiacurí (Atlántico) [2], Santa Rosa (Bolívar) [2], El Espino (Boyacá) [2], Padilla (Cauca) [2], Nariño (Nariño) [2], Chalán (Sucre) [2], Pradera (Valle Del Cauca) [2] and 3 more.
- extreme (181 municipalities): Corinto (Cauca) [13], Tame (Arauca) [13], Tibú (Norte De Santander) [13], El Tarra (Norte De Santander) [13], San Andrés de Tumaco (Nariño) [13], Toribío (Cauca) [12], Buenaventura (Valle Del Cauca) [12], Caloto (Cauca) [11], Teorama (Norte De Santander) [11], Saravena (Arauca) [11], Arauquita (Arauca) [11], Apartadó (Antioquia) [11] and 169 more.

**PeriodRates.cnmh_act_of_war_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (21 municipalities): Santa Rosa (Bolívar) [3], Guadalupe (Antioquia) [2], Rosas (Cauca) [2], Venecia (Antioquia) [2], Usiacurí (Atlántico) [2], Providencia (Nariño) [2], Florencia (Cauca) [2], Miranda (Cauca) [2], Recetor (Casanare) [1], Florida (Valle Del Cauca) [1], Chinácota (Norte De Santander) [1], Uribe (Meta) [1] and 9 more.
- extreme (223 municipalities): Teorama (Norte De Santander) [11], San Andrés de Tumaco (Nariño) [11], Arauquita (Arauca) [10], Tibú (Norte De Santander) [10], Tame (Arauca) [10], Tarazá (Antioquia) [10], Ocaña (Norte De Santander) [10], San Vicente del Caguán (Caquetá) [10], Corinto (Cauca) [10], Buenaventura (Valle Del Cauca) [10], Calamar (Guaviare) [9], San Pablo (Bolívar) [9] and 211 more.

**PeriodRates.cnmh_attack_on_a_town_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (23 municipalities): Caldono (Cauca) [6], San Calixto (Norte De Santander) [4], Caloto (Cauca) [4], Toribío (Cauca) [4], Córdoba (Bolívar) [2], Quibdó (Chocó) [2], Santacruz (Nariño) [2], Francisco Pizarro (Nariño) [2], Los Andes (Nariño) [2], La Llanada (Nariño) [2], Cumbal (Nariño) [2], Vistahermosa (Meta) [2] and 11 more.
- extreme (4 municipalities): Argelia (Cauca) [2], Sipí (Chocó) [2], Samaniego (Nariño) [2], Casabianca (Tolima) [2].

**PeriodRates.cnmh_attack_on_a_town_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (4 municipalities): Caloto (Cauca) [2], Vistahermosa (Meta) [2], Los Andes (Nariño) [2], Santacruz (Nariño) [2].
- extreme (9 municipalities): Marulanda (Caldas) [2], Corinto (Cauca) [2], Toribío (Cauca) [2], Sipí (Chocó) [2], Cumbal (Nariño) [2], La Llanada (Nariño) [2], Francisco Pizarro (Nariño) [2], Samaniego (Nariño) [2], Ibagué (Tolima) [2].

**PeriodRates.cnmh_damage_to_civilian_property_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (49 municipalities): San Pablo (Bolívar) [4], Puerto Asís (Putumayo) [3], Tarazá (Antioquia) [3], San Calixto (Norte De Santander) [3], La Llanada (Nariño) [2], Venecia (Cundinamarca) [2], Sipí (Chocó) [2], Briceño (Antioquia) [2], Contadero (Nariño) [2], Nariño (Nariño) [2], Los Andes (Nariño) [2], Padilla (Cauca) [2] and 37 more.
- extreme (133 municipalities): Buenaventura (Valle Del Cauca) [13], San Andrés de Tumaco (Nariño) [11], Corinto (Cauca) [10], Valdivia (Antioquia) [10], Saravena (Arauca) [9], Tibú (Norte De Santander) [9], Arauquita (Arauca) [9], Neiva (Huila) [8], Tame (Arauca) [8], El Tarra (Norte De Santander) [8], Convención (Norte De Santander) [8], Teorama (Norte De Santander) [8] and 121 more.

**PeriodRates.cnmh_damage_to_civilian_property_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (41 municipalities): San José de Cúcuta (Norte De Santander) [6], Valdivia (Antioquia) [4], Condoto (Chocó) [4], Argelia (Cauca) [4], Apartadó (Antioquia) [2], Hatonuevo (La Guajira) [2], Fundación (Magdalena) [2], Tenerife (Magdalena) [2], Acacías (Meta) [2], El Castillo (Meta) [2], Pasto (Nariño) [2], Túquerres (Nariño) [2] and 29 more.
- extreme (15 municipalities): Barbacoas (Nariño) [4], Granada (Antioquia) [2], San Carlos (Antioquia) [2], San Francisco (Antioquia) [2], San Jacinto del Cauca (Bolívar) [2], Puerto Rico (Caquetá) [2], Planeta Rica (Córdoba) [2], Quibdó (Chocó) [2], Neiva (Huila) [2], Villavicencio (Meta) [2], Puerres (Nariño) [2], Santa Bárbara (Nariño) [2] and 3 more.

**PeriodRates.cnmh_forced_disappearance_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (91 municipalities): Caloto (Cauca) [6], Puerto Tejada (Cauca) [4], Curillo (Caquetá) [4], Segovia (Antioquia) [4], Cáceres (Antioquia) [3], Ipiales (Nariño) [3], Tarazá (Antioquia) [3], Apartadó (Antioquia) [2], Fundación (Magdalena) [2], Roberto Payán (Nariño) [2], La Unión (Nariño) [2], San Juanito (Meta) [2] and 79 more.
- extreme (169 municipalities): San Andrés de Tumaco (Nariño) [12], Buenaventura (Valle Del Cauca) [9], Valle del Guamuez (Putumayo) [9], Florencia (Caquetá) [8], San Vicente del Caguán (Caquetá) [8], Puerto Berrío (Antioquia) [8], Medellín (Antioquia) [6], Valdivia (Antioquia) [6], Puerto Rico (Caquetá) [6], San José del Fragua (Caquetá) [6], Uribe (Meta) [6], Solita (Caquetá) [6] and 157 more.

**PeriodRates.cnmh_forced_disappearance_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (62 municipalities): Puerto Tejada (Cauca) [4], Guapi (Cauca) [4], Caloto (Cauca) [4], Curillo (Caquetá) [4], Cáceres (Antioquia) [3], Puerto Carreño (Vichada) [2], Juradó (Chocó) [2], Medio San Juan (Chocó) [2], Tadó (Chocó) [2], Barrancas (La Guajira) [2], Fundación (Magdalena) [2], Puerto Concordia (Meta) [2] and 50 more.
- extreme (185 municipalities): San Andrés de Tumaco (Nariño) [12], Puerto Berrío (Antioquia) [11], Buenaventura (Valle Del Cauca) [11], San Vicente del Caguán (Caquetá) [9], Valle del Guamuez (Putumayo) [9], Florencia (Caquetá) [8], Puerto Santander (Norte De Santander) [8], Medellín (Antioquia) [6], Arauca (Arauca) [6], Valdivia (Antioquia) [6], Policarpa (Nariño) [6], Tarazá (Antioquia) [6] and 173 more.

**PeriodRates.cnmh_kidnapping_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (70 municipalities): Miranda (Cauca) [7], Sipí (Chocó) [4], Florencia (Cauca) [4], Medio San Juan (Chocó) [3], San José del Palmar (Chocó) [3], Unguía (Chocó) [3], Ciénaga (Magdalena) [3], Barbosa (Antioquia) [2], Nóvita (Chocó) [2], Santa Bárbara (Santander) [2], Tadó (Chocó) [2], Altamira (Huila) [2] and 58 more.
- extreme (121 municipalities): Tame (Arauca) [12], Ocaña (Norte De Santander) [11], San Andrés de Tumaco (Nariño) [11], Saravena (Arauca) [10], Convención (Norte De Santander) [10], Arauca (Arauca) [10], Policarpa (Nariño) [8], Florencia (Caquetá) [8], Quibdó (Chocó) [8], Teorama (Norte De Santander) [8], Buenaventura (Valle Del Cauca) [8], Arauquita (Arauca) [8] and 109 more.

**PeriodRates.cnmh_kidnapping_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (29 municipalities): Cértegui (Chocó) [4], Florencia (Cauca) [3], Padilla (Cauca) [2], El Castillo (Meta) [2], San José del Palmar (Chocó) [2], Cota (Cundinamarca) [2], Guachené (Cauca) [2], Nariño (Nariño) [2], Saldaña (Tolima) [2], Regidor (Bolívar) [2], Tubará (Atlántico) [2], La Llanada (Nariño) [1] and 17 more.
- extreme (176 municipalities): Tame (Arauca) [12], San Andrés de Tumaco (Nariño) [11], Buenaventura (Valle Del Cauca) [11], Ocaña (Norte De Santander) [11], Saravena (Arauca) [10], Quibdó (Chocó) [10], Teorama (Norte De Santander) [10], Arauquita (Arauca) [10], Florencia (Caquetá) [8], Cumbitara (Nariño) [8], Policarpa (Nariño) [8], Arauca (Arauca) [8] and 164 more.

**PeriodRates.cnmh_landmines_and_explosive_remnants_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (35 municipalities): Santa Rosa (Bolívar) [7], Miranda (Cauca) [4], Puerto Santander (ANM) (Amazonas) [4], Sácama (Casanare) [4], Villa Rica (Cauca) [2], Santiago (Norte De Santander) [2], La Tebaida (Quindío) [2], Chalán (Sucre) [2], Guadalupe (Antioquia) [2], Morroa (Sucre) [2], Medio San Juan (Chocó) [2], Útica (Cundinamarca) [2] and 23 more.
- extreme (148 municipalities): San Andrés de Tumaco (Nariño) [13], Arauquita (Arauca) [13], Tame (Arauca) [11], Tarazá (Antioquia) [11], Teorama (Norte De Santander) [11], Mesetas (Meta) [10], Tibú (Norte De Santander) [10], Puerto Asís (Putumayo) [10], Ituango (Antioquia) [10], Anorí (Antioquia) [10], Valdivia (Antioquia) [10], Hacarí (Norte De Santander) [9] and 136 more.

**PeriodRates.cnmh_landmines_and_explosive_remnants_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (29 municipalities): Puerto Asís (Putumayo) [4], Santa Rosa (Bolívar) [4], Samaniego (Nariño) [3], Miranda (Cauca) [3], Tierralta (Córdoba) [2], La Llanada (Nariño) [2], Santiago (Norte De Santander) [2], Concepción (Antioquia) [2], Útica (Cundinamarca) [2], Chalán (Sucre) [2], San José del Palmar (Chocó) [2], Los Patios (Norte De Santander) [2] and 17 more.
- extreme (145 municipalities): San Andrés de Tumaco (Nariño) [13], Tarazá (Antioquia) [13], Anorí (Antioquia) [12], Ituango (Antioquia) [11], Teorama (Norte De Santander) [11], Valdivia (Antioquia) [11], Hacarí (Norte De Santander) [9], Arauquita (Arauca) [9], Dabeiba (Antioquia) [9], Tibú (Norte De Santander) [8], Chaparral (Tolima) [8], La Montañita (Caquetá) [8] and 133 more.

**PeriodRates.cnmh_massacre_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (128 municipalities): Caucasia (Antioquia) [6], Villa del Rosario (Norte De Santander) [6], Valdivia (Antioquia) [6], Mesetas (Meta) [4], San Pablo (Bolívar) [4], Mercaderes (Cauca) [4], Piamonte (Cauca) [4], San José de Uré (Córdoba) [4], Viotá (Cundinamarca) [4], Andes (Antioquia) [4], Amalfi (Antioquia) [4], El Charco (Nariño) [4] and 116 more.
- extreme (29 municipalities): San Andrés de Tumaco (Nariño) [8], Puerto Asís (Putumayo) [4], San José de Cúcuta (Norte De Santander) [4], Granada (Antioquia) [2], Yopal (Casanare) [2], Tame (Arauca) [2], Jamundí (Valle Del Cauca) [2], Buenaventura (Valle Del Cauca) [2], Tibú (Norte De Santander) [2], Leiva (Nariño) [2], Barbacoas (Nariño) [2], Vistahermosa (Meta) [2] and 17 more.

**PeriodRates.cnmh_massacre_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- extreme (199 municipalities): San Andrés de Tumaco (Nariño) [10], Policarpa (Nariño) [8], Valdivia (Antioquia) [8], Caucasia (Antioquia) [8], Villa del Rosario (Norte De Santander) [7], Puerto Asís (Putumayo) [6], Segovia (Antioquia) [6], Montelíbano (Córdoba) [6], San Miguel (Putumayo) [6], Puerto Rico (Meta) [6], Suárez (Cauca) [6], Zaragoza (Antioquia) [6] and 187 more.

**PeriodRates.cnmh_recruitment_of_children_and_adolescents_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (71 municipalities): Briceño (Antioquia) [4], Curillo (Caquetá) [4], Nariño (Nariño) [4], Samaniego (Nariño) [4], Argelia (Cauca) [4], San Andrés de Tumaco (Nariño) [4], El Bagre (Antioquia) [4], La Victoria (ANM) (Amazonas) [4], Buenaventura (Valle Del Cauca) [3], Sandoná (Nariño) [2], Tadó (Chocó) [2], Neiva (Huila) [2] and 59 more.
- extreme (91 municipalities): Apartadó (Antioquia) [10], Cartagena del Chairá (Caquetá) [8], Barbacoas (Nariño) [8], Puerto Asís (Putumayo) [8], San Vicente del Caguán (Caquetá) [6], San Andrés de Tumaco (Nariño) [6], Tame (Arauca) [6], Vistahermosa (Meta) [6], San Pablo (Bolívar) [6], Toribío (Cauca) [6], Puerto Guzmán (Putumayo) [6], Chaparral (Tolima) [6] and 79 more.

**PeriodRates.cnmh_recruitment_of_children_and_adolescents_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (58 municipalities): Briceño (Antioquia) [4], Curillo (Caquetá) [4], La Victoria (ANM) (Amazonas) [4], Buenaventura (Valle Del Cauca) [3], La Argentina (Huila) [2], Pital (Huila) [2], Villavicencio (Meta) [2], Puerto Concordia (Meta) [2], Albán (Nariño) [2], Nariño (Nariño) [2], Olaya Herrera (Nariño) [2], Policarpa (Nariño) [2] and 46 more.
- extreme (106 municipalities): Apartadó (Antioquia) [10], San Vicente del Caguán (Caquetá) [8], El Bagre (Antioquia) [8], Cartagena del Chairá (Caquetá) [8], San Andrés de Tumaco (Nariño) [8], Barbacoas (Nariño) [8], Uribe (Meta) [8], Puerto Asís (Putumayo) [8], Puerto Guzmán (Putumayo) [6], Planadas (Tolima) [6], Toribío (Cauca) [6], Tame (Arauca) [6] and 94 more.

**PeriodRates.cnmh_selective_killing_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (5 municipalities): Rosas (Cauca), phase:santos_2_implementation: 3 observed, 0.23 expected at the rate of its rurality category; Villa Rica (Cauca), phase:santos_2_implementation: 2 observed, 0.2 expected at the rate of its rurality category; Gachancipá (Cundinamarca), phase:santos_2_negotiation: 2 observed, 0.17 expected at the rate of its rurality category; Puerto Santander (Norte De Santander), phase:santos_2_implementation: 2 observed, 0.17 expected at the rate of its rurality category; Pijao (Quindío), phase:santos_2_negotiation: 2 observed, 0.17 expected at the rate of its rurality category.
- extreme (245 municipalities): San Andrés de Tumaco (Nariño) [13], San José de Cúcuta (Norte De Santander) [13], Barrancabermeja (Santander) [13], Tame (Arauca) [13], Puerto Asís (Putumayo) [12], Quibdó (Chocó) [12], Valle del Guamuez (Putumayo) [11], Saravena (Arauca) [11], Puerto Berrío (Antioquia) [11], Corinto (Cauca) [11], Tibú (Norte De Santander) [10], San Pablo (Bolívar) [10] and 233 more.

**PeriodRates.cnmh_selective_killing_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (4 municipalities): Rosas (Cauca), phase:santos_2_implementation: 3 observed, 0.26 expected at the rate of its rurality category; Gachancipá (Cundinamarca), phase:santos_2_negotiation: 2 observed, 0.19 expected at the rate of its rurality category; Santuario (Risaralda), phase:santos_2_implementation: 3 observed, 0.29 expected at the rate of its rurality category; Vijes (Valle Del Cauca), government:petro: 2 observed, 0.18 expected at the rate of its rurality category; Vijes (Valle Del Cauca), phase:petro: 2 observed, 0.18 expected at the rate of its rurality category.
- extreme (269 municipalities): San José de Cúcuta (Norte De Santander) [13], Buenaventura (Valle Del Cauca) [13], Tame (Arauca) [13], Barrancabermeja (Santander) [13], San Andrés de Tumaco (Nariño) [13], Puerto Asís (Putumayo) [12], Quibdó (Chocó) [12], Puerto Berrío (Antioquia) [11], Saravena (Arauca) [11], Corinto (Cauca) [11], Valle del Guamuez (Putumayo) [11], Aguachica (Cesar) [11] and 257 more.

**PeriodRates.cnmh_sexual_violence_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (35 municipalities): Padilla (Cauca) [5], Puerto Santander (ANM) (Amazonas) [4], Unión Panamericana (Chocó) [2], Puerto Rondón (Arauca) [2], Buenaventura (Valle Del Cauca) [2], Tibú (Norte De Santander) [2], Sardinata (Norte De Santander) [2], Puerto Santander (Norte De Santander) [2], San Andrés de Tumaco (Nariño) [2], Providencia (Nariño) [2], Olaya Herrera (Nariño) [2], El Peñol (Nariño) [2] and 23 more.
- extreme (101 municipalities): San Andrés de Tumaco (Nariño) [11], Quibdó (Chocó) [11], Buenaventura (Valle Del Cauca) [11], Valle del Guamuez (Putumayo) [10], San Miguel (Putumayo) [10], Policarpa (Nariño) [10], Medio Atrato (Chocó) [9], Tarazá (Antioquia) [9], Dibulla (La Guajira) [8], Puerto Asís (Putumayo) [8], Riohacha (La Guajira) [8], Cumbitara (Nariño) [8] and 89 more.

**PeriodRates.cnmh_sexual_violence_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (26 municipalities): Puerto Santander (ANM) (Amazonas) [4], Padilla (Cauca) [4], Atrato (Chocó) [3], Turbo (Antioquia) [2], Puerto Rondón (Arauca) [2], Guática (Risaralda) [2], Sardinata (Norte De Santander) [2], Ragonvalia (Norte De Santander) [2], Puerto Santander (Norte De Santander) [2], San Andrés de Tumaco (Nariño) [2], Providencia (Nariño) [2], Olaya Herrera (Nariño) [2] and 14 more.
- extreme (122 municipalities): Valle del Guamuez (Putumayo) [11], Quibdó (Chocó) [11], Buenaventura (Valle Del Cauca) [11], San Andrés de Tumaco (Nariño) [11], San Miguel (Putumayo) [10], Puerto Asís (Putumayo) [10], Policarpa (Nariño) [10], Medio Atrato (Chocó) [9], Tarazá (Antioquia) [9], Cumbitara (Nariño) [8], Riohacha (La Guajira) [8], Dibulla (La Guajira) [8] and 110 more.

**PeriodRates.cnmh_terrorist_attack_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (77 municipalities): Patía (Cauca) [6], El Zulia (Norte De Santander) [4], Calamar (Guaviare) [4], Ituango (Antioquia) [4], Corinto (Cauca) [4], Puerto Asís (Putumayo) [4], Apartadó (Antioquia) [4], Miranda (Cauca) [4], Florida (Valle Del Cauca) [4], Timbiquí (Cauca) [4], Inzá (Cauca) [4], Argelia (Cauca) [4] and 65 more.
- extreme (19 municipalities): Argelia (Cauca) [4], Cáceres (Antioquia) [2], El Tarra (Norte De Santander) [2], Saravena (Arauca) [2], Fortul (Arauca) [2], Arauca (Arauca) [2], Riofrío (Valle Del Cauca) [2], Pradera (Valle Del Cauca) [2], Jamundí (Valle Del Cauca) [2], Buenaventura (Valle Del Cauca) [2], San Andrés de Tumaco (Nariño) [2], San Rafael (Antioquia) [2] and 7 more.

**PeriodRates.cnmh_terrorist_attack_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (19 municipalities): Patía (Cauca) [4], San Rafael (Antioquia) [4], Apartadó (Antioquia) [2], Santa Bárbara (Nariño) [2], Valle del Guamuez (Putumayo) [2], Puerto Asís (Putumayo) [2], Saravena (Arauca) [2], El Zulia (Norte De Santander) [2], Túquerres (Nariño) [2], Taminango (Nariño) [2], San Juan de Arama (Meta) [2], Samaniego (Nariño) [2] and 7 more.
- extreme (38 municipalities): Bogotá, D.C. (Bogotá, D.C.) [4], Apartadó (Antioquia) [2], Cali (Valle Del Cauca) [2], Vistahermosa (Meta) [2], Roberto Payán (Nariño) [2], San Andrés de Tumaco (Nariño) [2], San José de Cúcuta (Norte De Santander) [2], Convención (Norte De Santander) [2], San Calixto (Norte De Santander) [2], Tibú (Norte De Santander) [2], Buenaventura (Valle Del Cauca) [2], Maicao (La Guajira) [2] and 26 more.

## INDEPAZ

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | indepaz_massacre_events | 0 | 6 | 0 | 0 | 74 | 42 |
| PeriodRates | indepaz_massacre_victims | 0 | 6 | 0 | 0 | 14 | 188 |

**PeriodRates.indepaz_massacre_events**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (36 municipalities): Puerto Rondón (Arauca) [4], Andes (Antioquia) [2], Landázuri (Santander) [2], Colón (Nariño) [2], Leiva (Nariño) [2], Los Andes (Nariño) [2], Policarpa (Nariño) [2], Ábrego (Norte De Santander) [2], Circasia (Quindío) [2], Ambalema (Tolima) [2], Ciudad Bolívar (Antioquia) [2], Alcalá (Valle Del Cauca) [2] and 24 more.
- extreme (21 municipalities): Betania (Antioquia) [2], Samaniego (Nariño) [2], Puerto Leguízamo (Putumayo) [2], Puerto Asís (Putumayo) [2], Toro (Valle Del Cauca) [2], Cartago (Valle Del Cauca) [2], Guadalajara de Buga (Valle Del Cauca) [2], Ansermanuevo (Valle Del Cauca) [2], San José de Cúcuta (Norte De Santander) [2], San Andrés de Tumaco (Nariño) [2], Ipiales (Nariño) [2], Salgar (Antioquia) [2] and 9 more.

**PeriodRates.indepaz_massacre_victims**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (7 municipalities): Tarso (Antioquia) [2], Norcasia (Caldas) [2], Agua de Dios (Cundinamarca) [2], San Antonio del Tequendama (Cundinamarca) [2], Colón (Nariño) [2], Los Andes (Nariño) [2], Puerto Rondón (Arauca) [2].
- extreme (81 municipalities): Guadalajara de Buga (Valle Del Cauca) [4], San Andrés de Tumaco (Nariño) [4], Balboa (Cauca) [4], Maicao (La Guajira) [4], Cartago (Valle Del Cauca) [4], Jamundí (Valle Del Cauca) [4], Mercaderes (Cauca) [4], Santander de Quilichao (Cauca) [4], San José de Cúcuta (Norte De Santander) [4], Ábrego (Norte De Santander) [4], Puerto Asís (Putumayo) [4], Ciudad Bolívar (Antioquia) [4] and 69 more.

## Medicina Legal

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| ViolenceCases | domestic_violence | 0 | 0 | 0 | 0 | 3 | 9 |
| ViolenceCases | homicide | 0 | 2 | 0 | 0 | 0 | 11 |
| ViolenceCases | partner_violence | 0 | 0 | 0 | 0 | 13 | 9 |
| ViolenceCases | sexual_violence | 0 | 0 | 0 | 0 | 10 | 24 |
| ViolenceCases | suicide | 0 | 0 | 0 | 0 | 6 | 94 |
| ViolenceCases | violence_children | 0 | 0 | 0 | 0 | 0 | 6 |

**ViolenceCases.domestic_violence**

- small_base (2 municipalities): Turbo (Antioquia) [2], La Calera (Cundinamarca) [1].
- extreme (5 municipalities): Uribia (La Guajira) [3], Buenaventura (Valle Del Cauca) [3], Apartadó (Antioquia) [1], Yopal (Casanare) [1], Cumaribo (Vichada) [1].

**ViolenceCases.homicide**

- missing (1 municipalities): Mapiripana (ANM) (Guainía), 2020: no population behind the rate; Mapiripana (ANM) (Guainía), 2025: no population behind the rate.
- extreme (10 municipalities): Tarazá (Antioquia) [2], Anorí (Antioquia) [1], Briceño (Antioquia) [1], Remedios (Antioquia) [1], San Andrés de Cuerquía (Antioquia) [1], Argelia (Cauca) [1], Puerto Santander (Norte De Santander) [1], La Victoria (Valle Del Cauca) [1], Puerto Rondón (Arauca) [1], El Retorno (Guaviare) [1].

**ViolenceCases.partner_violence**

- small_base (9 municipalities): Cota (Cundinamarca) [3], La Calera (Cundinamarca) [2], Sopó (Cundinamarca) [2], Caucasia (Antioquia) [1], Sabanagrande (Atlántico) [1], Santo Tomás (Atlántico) [1], Usiacurí (Atlántico) [1], Tabio (Cundinamarca) [1], Tocancipá (Cundinamarca) [1].
- extreme (5 municipalities): Uribia (La Guajira) [3], Apartadó (Antioquia) [2], Manaure (La Guajira) [2], Chía (Cundinamarca) [1], Cumaribo (Vichada) [1].

**ViolenceCases.sexual_violence**

- small_base (10 municipalities): Cogua (Cundinamarca) [1], Sopó (Cundinamarca) [1], Tabio (Cundinamarca) [1], Tocancipá (Cundinamarca) [1], La Pedrera (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], Puerto Arica (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1], Barrancominas (Guainía) [1], La Guadalupe (ANM) (Guainía) [1].
- extreme (6 municipalities): San Andrés de Tumaco (Nariño) [8], Ipiales (Nariño) [5], Cumaribo (Vichada) [5], Manaure (La Guajira) [3], Apartadó (Antioquia) [2], Ayapel (Córdoba) [1].

**ViolenceCases.suicide**

- small_base (5 municipalities): Nemocón (Cundinamarca) [2], Iza (Boyacá) [1], Sutatausa (Cundinamarca) [1], Vetas (Santander) [1], La Salina (Casanare) [1].
- extreme (54 municipalities): Uribia (La Guajira) [6], Soledad (Atlántico) [5], Cumaribo (Vichada) [4], Mitú (Vaupés) [4], Puerto Gaitán (Meta) [4], Pasto (Nariño) [3], Riosucio (Chocó) [3], Cereté (Córdoba) [3], Magangué (Bolívar) [3], El Tambo (Cauca) [3], Necoclí (Antioquia) [3], Arauca (Arauca) [2] and 42 more.

**ViolenceCases.violence_children**

- extreme (4 municipalities): Uribia (La Guajira) [3], Chocontá (Cundinamarca) [1], Cucunubá (Cundinamarca) [1], Paime (Cundinamarca) [1].
