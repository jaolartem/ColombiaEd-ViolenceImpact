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
| Census2018Municipal | dep_dependency_rate | 0 | 0 | 0 | 0 | 0 | 16 |
| Census2018Municipal | dep_early_childhood_care_barriers | 0 | 0 | 0 | 0 | 0 | 39 |
| Census2018Municipal | dep_health_access_barriers | 0 | 0 | 0 | 0 | 0 | 1 |
| Census2018Municipal | dep_illiteracy | 0 | 0 | 0 | 0 | 0 | 9 |
| Census2018Municipal | dep_inadequate_excreta_disposal | 0 | 0 | 0 | 0 | 0 | 4 |
| Census2018Municipal | dep_informal_work | 0 | 0 | 0 | 0 | 0 | 5 |
| Census2018Municipal | dep_low_educational_attainment | 0 | 0 | 0 | 0 | 0 | 16 |
| Census2018Municipal | dep_no_health_insurance | 0 | 0 | 0 | 0 | 0 | 25 |
| Census2018Municipal | dep_no_improved_water | 0 | 0 | 0 | 0 | 0 | 4 |
| Census2018Municipal | dep_school_lag | 0 | 0 | 0 | 0 | 0 | 12 |
| Census2018Municipal | dep_school_non_attendance | 0 | 0 | 0 | 0 | 0 | 4 |
| Census2018Municipal | dwellings_occupied | 0 | 0 | 25 | 0 | 0 | 20 |
| Census2018Municipal | ipm | 0 | 0 | 0 | 0 | 0 | 16 |
| Census2018Municipal | ipm_vs_nbi | 0 | 0 | 0 | 0 | 0 | 3 |
| Census2018Municipal | nbi | 0 | 0 | 0 | 0 | 0 | 16 |
| Census2018Municipal | nbi_economic_dependency | 0 | 0 | 0 | 0 | 0 | 3 |
| Census2018Municipal | nbi_misery | 0 | 0 | 0 | 0 | 0 | 1 |
| Census2018Municipal | nbi_overcrowding | 0 | 0 | 0 | 0 | 0 | 7 |
| Census2018Municipal | nbi_school_non_attendance | 0 | 0 | 0 | 0 | 0 | 11 |
| Census2018Municipal | share_electricity | 0 | 0 | 14 | 0 | 0 | 17 |
| Census2018Municipal | share_garbage | 0 | 0 | 0 | 0 | 0 | 25 |
| Census2018Municipal | share_internet | 0 | 0 | 0 | 0 | 0 | 2 |
| Census2018Municipal | share_no_electricity_service | 0 | 0 | 0 | 0 | 0 | 15 |
| Census2018Municipal | share_sewer | 0 | 0 | 0 | 0 | 0 | 37 |
| Census2018Municipal | share_stratum | 0 | 138 | 0 | 0 | 0 | 0 |
| Census2018Municipal | share_stratum_1 | 0 | 0 | 0 | 0 | 0 | 4 |
| Census2018Municipal | share_stratum_1_2 | 0 | 0 | 0 | 0 | 0 | 21 |
| Census2018Municipal | share_stratum_3 | 0 | 0 | 0 | 0 | 0 | 53 |
| Census2018Municipal | share_stratum_4 | 0 | 0 | 0 | 0 | 0 | 102 |
| Census2018Municipal | share_water | 0 | 0 | 0 | 0 | 0 | 15 |
| Population | population | 0 | 241 | 0 | 44 | 0 | 0 |

**Census2018Municipal.dep_dependency_rate**

- extreme (16 municipalities): Sucre (Cauca) [1], Alto Baudó (Chocó) [1], La Chorrera (ANM) (Amazonas) [1], La Pedrera (ANM) (Amazonas) [1], La Victoria (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], Barrancominas (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Morichal (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1] and 4 more.

**Census2018Municipal.dep_early_childhood_care_barriers**

- extreme (39 municipalities): Guapi (Cauca) [1], La Guadalupe (ANM) (Guainía) [1], Puerto Arica (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1], Tarapacá (ANM) (Amazonas) [1], Barrancominas (Guainía) [1], Mapiripana (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], Miriti - Paraná (ANM) (Amazonas) [1], Pana Pana (ANM) (Guainía) [1] and 27 more.

**Census2018Municipal.dep_health_access_barriers**

- extreme (1 municipalities): Chaguaní (Cundinamarca) [1].

**Census2018Municipal.dep_illiteracy**

- extreme (9 municipalities): Envigado (Antioquia) [1], Sabaneta (Antioquia) [1], Bogotá, D.C. (Bogotá, D.C.) [1], Cajicá (Cundinamarca) [1], Chía (Cundinamarca) [1], Funza (Cundinamarca) [1], Mosquera (Cundinamarca) [1], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1].

**Census2018Municipal.dep_inadequate_excreta_disposal**

- extreme (4 municipalities): Soplaviento (Bolívar) [1], Mosquera (Nariño) [1], Santa Bárbara (Nariño) [1], Puerto Colombia (ANM) (Guainía) [1].

**Census2018Municipal.dep_informal_work**

- extreme (5 municipalities): La Victoria (ANM) (Amazonas) [1], Puerto Colombia (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1], Yavaraté (ANM) (Vaupés) [1].

**Census2018Municipal.dep_low_educational_attainment**

- extreme (16 municipalities): Envigado (Antioquia) [1], Sabaneta (Antioquia) [1], Puerto Colombia (Atlántico) [1], Bogotá, D.C. (Bogotá, D.C.) [1], Tunja (Boyacá) [1], Cajicá (Cundinamarca) [1], Chía (Cundinamarca) [1], Cota (Cundinamarca) [1], Funza (Cundinamarca) [1], Mosquera (Cundinamarca) [1], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1] and 4 more.

**Census2018Municipal.dep_no_health_insurance**

- extreme (25 municipalities): López de Micay (Cauca) [1], Tarapacá (ANM) (Amazonas) [1], Yavaraté (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1], Taraira (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Mitú (Vaupés) [1], Morichal (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1] and 13 more.

**Census2018Municipal.dep_no_improved_water**

- extreme (4 municipalities): San Jacinto (Bolívar) [1], Istmina (Chocó) [1], La Tola (Nariño) [1], Mosquera (Nariño) [1].

**Census2018Municipal.dep_school_lag**

- extreme (12 municipalities): Murindó (Antioquia) [1], Alto Baudó (Chocó) [1], Magüí (Nariño) [1], La Victoria (ANM) (Amazonas) [1], Barrancominas (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Morichal (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1], Yavaraté (ANM) (Vaupés) [1].

**Census2018Municipal.dep_school_non_attendance**

- extreme (4 municipalities): La Victoria (ANM) (Amazonas) [1], Pana Pana (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1].

**Census2018Municipal.dwellings_occupied**

- inconsistent (25 municipalities): Tuchín (Córdoba) [1], Puerto Nariño (Amazonas) [1], Yavaraté (ANM) (Vaupés) [1], Papunahua (ANM) (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Morichal (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Barrancominas (Guainía) [1] and 13 more.
- extreme (20 municipalities): Medellín (Antioquia) [1], Bello (Antioquia) [1], La Guadalupe (ANM) (Guainía) [1], La Victoria (ANM) (Amazonas) [1], Cali (Valle Del Cauca) [1], Ibagué (Tolima) [1], Bucaramanga (Santander) [1], Pereira (Risaralda) [1], San José de Cúcuta (Norte De Santander) [1], Villavicencio (Meta) [1], Santa Marta (Magdalena) [1], Soacha (Cundinamarca) [1] and 8 more.

**Census2018Municipal.ipm**

- extreme (16 municipalities): Envigado (Antioquia) [1], Sabaneta (Antioquia) [1], Alto Baudó (Chocó) [1], Uribia (La Guajira) [1], La Pedrera (ANM) (Amazonas) [1], La Victoria (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], Mapiripana (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Morichal (ANM) (Guainía) [1] and 4 more.

**Census2018Municipal.ipm_vs_nbi**

- extreme (3 municipalities): San Jacinto (Bolívar), 2018: IPM 60.3 against NBI 93.4; NBI's largest component: services; Quibdó (Chocó), 2018: IPM 44.4 against NBI 72.8; NBI's largest component: services; Istmina (Chocó), 2018: IPM 55.1 against NBI 84.0; NBI's largest component: services.

**Census2018Municipal.nbi**

- extreme (16 municipalities): Clemencia (Bolívar) [1], San Jacinto (Bolívar) [1], Istmina (Chocó) [1], Uribia (La Guajira) [1], La Tola (Nariño) [1], Magüí (Nariño) [1], La Victoria (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], San Felipe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1] and 4 more.

**Census2018Municipal.nbi_economic_dependency**

- extreme (3 municipalities): Sabaneta (Antioquia) [1], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [1].

**Census2018Municipal.nbi_misery**

- extreme (1 municipalities): Pacoa (ANM) (Vaupés) [1].

**Census2018Municipal.nbi_overcrowding**

- extreme (7 municipalities): Alto Baudó (Chocó) [1], Manaure (La Guajira) [1], Uribia (La Guajira) [1], Miriti - Paraná (ANM) (Amazonas) [1], Morichal (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1], Cumaribo (Vichada) [1].

**Census2018Municipal.nbi_school_non_attendance**

- extreme (11 municipalities): Cubará (Boyacá) [1], Pueblo Bello (Cesar) [1], Dibulla (La Guajira) [1], Uribia (La Guajira) [1], Pueblo Rico (Risaralda) [1], La Victoria (ANM) (Amazonas) [1], Pana Pana (ANM) (Guainía) [1], Morichal (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1], Taraira (Vaupés) [1], Papunahua (ANM) (Vaupés) [1].

**Census2018Municipal.share_electricity**

- inconsistent (14 municipalities): Frontino (Antioquia) [1], Milán (Caquetá) [1], Solano (Caquetá) [1], Pueblo Bello (Cesar) [1], Alto Baudó (Chocó) [1], Bagadó (Chocó) [1], Juradó (Chocó) [1], Lloró (Chocó) [1], Puerto Gaitán (Meta) [1], Puerto Santander (ANM) (Amazonas) [1], La Guadalupe (ANM) (Guainía) [1], Mitú (Vaupés) [1] and 2 more.
- extreme (17 municipalities): Medio Atrato (Chocó) [1], San Felipe (ANM) (Guainía) [1], Yavaraté (ANM) (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Morichal (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Sipí (Chocó) [1], Tarapacá (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1] and 5 more.

**Census2018Municipal.share_garbage**

- extreme (25 municipalities): Medellín (Antioquia) [1], Chía (Cundinamarca) [1], Puerto Colombia (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Mapiripana (ANM) (Guainía) [1], Miriti - Paraná (ANM) (Amazonas) [1], Cali (Valle Del Cauca) [1], Zapayán (Magdalena) [1], Pedraza (Magdalena) [1], Mosquera (Cundinamarca) [1], Madrid (Cundinamarca) [1], Funza (Cundinamarca) [1] and 13 more.

**Census2018Municipal.share_internet**

- extreme (2 municipalities): Envigado (Antioquia) [1], Sabaneta (Antioquia) [1].

**Census2018Municipal.share_no_electricity_service**

- extreme (15 municipalities): Medio Atrato (Chocó) [1], Sipí (Chocó) [1], Uribia (La Guajira) [1], La Victoria (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1], Mapiripana (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], Morichal (ANM) (Guainía) [1] and 3 more.

**Census2018Municipal.share_sewer**

- extreme (37 municipalities): Itagüí (Antioquia) [1], Algarrobo (Magdalena) [1], Remolino (Magdalena) [1], Sitionuevo (Magdalena) [1], Zapayán (Magdalena) [1], Zona Bananera (Magdalena) [1], La Tola (Nariño) [1], Mosquera (Nariño) [1], Francisco Pizarro (Nariño) [1], Santa Bárbara (Nariño) [1], La Virginia (Risaralda) [1], Sucre (Sucre) [1] and 25 more.

**Census2018Municipal.share_stratum**

- missing (138 municipalities): Murindó (Antioquia) [1], Nunchía (Casanare) [1], El Carmen (Norte De Santander) [1], Sardinata (Norte De Santander) [1], Tibú (Norte De Santander) [1], Cravo Norte (Arauca) [1], Chámeza (Casanare) [1], Hato Corozal (Casanare) [1], Orocué (Casanare) [1], Puerto Leguízamo (Putumayo) [1], Recetor (Casanare) [1], Sácama (Casanare) [1] and 126 more.

**Census2018Municipal.share_stratum_1**

- extreme (4 municipalities): Envigado (Antioquia) [1], Sabaneta (Antioquia) [1], La Guadalupe (ANM) (Guainía) [1], Pacoa (ANM) (Vaupés) [1].

**Census2018Municipal.share_stratum_1_2**

- extreme (21 municipalities): Murindó (Antioquia) [1], Mapiripana (ANM) (Guainía) [1], Yavaraté (ANM) (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Morichal (ANM) (Guainía) [1], Pana Pana (ANM) (Guainía) [1], Cacahual (ANM) (Guainía) [1], La Guadalupe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1], San Felipe (ANM) (Guainía) [1], Tarapacá (ANM) (Amazonas) [1], Medio Atrato (Chocó) [1] and 9 more.

**Census2018Municipal.share_stratum_3**

- extreme (53 municipalities): Medellín (Antioquia) [1], Funza (Cundinamarca) [1], Girardot (Cundinamarca) [1], La Mesa (Cundinamarca) [1], Madrid (Cundinamarca) [1], Mosquera (Cundinamarca) [1], Soacha (Cundinamarca) [1], Sopó (Cundinamarca) [1], Santa Marta (Magdalena) [1], Villavicencio (Meta) [1], Restrepo (Meta) [1], Armenia (Quindío) [1] and 41 more.

**Census2018Municipal.share_stratum_4**

- extreme (102 municipalities): Medellín (Antioquia) [1], San José de Cúcuta (Norte De Santander) [1], Pereira (Risaralda) [1], Salento (Quindío) [1], Circasia (Quindío) [1], Calarcá (Quindío) [1], Armenia (Quindío) [1], Villa del Rosario (Norte De Santander) [1], Pamplona (Norte De Santander) [1], Ocaña (Norte De Santander) [1], Los Patios (Norte De Santander) [1], Chinácota (Norte De Santander) [1] and 90 more.

**Census2018Municipal.share_water**

- extreme (15 municipalities): Norosí (Bolívar) [1], San Jacinto (Bolívar) [1], Santa Catalina (Bolívar) [1], Istmina (Chocó) [1], Uribia (La Guajira) [1], La Tola (Nariño) [1], Magüí (Nariño) [1], Mosquera (Nariño) [1], La Pedrera (ANM) (Amazonas) [1], Miriti - Paraná (ANM) (Amazonas) [1], San Felipe (ANM) (Guainía) [1], Puerto Colombia (ANM) (Guainía) [1] and 3 more.

**Population.population**

- missing (56 municipalities): Mapiripana (ANM) (Guainía) [23], Norosí (Bolívar) [13], Tuchín (Córdoba) [13], San José de Uré (Córdoba) [13], Guachené (Cauca) [12], Coveñas (Sucre) [7], Medio San Juan (Chocó) [6], Nuevo Belén de Bajirá (Chocó) [6], Río Iró (Chocó) [6], Carmen del Darién (Chocó) [6], Nueva Granada (Magdalena) [5], Cértegui (Chocó) [5] and 44 more.
- break (37 municipalities): Río Quito (Chocó) [3], Istmina (Chocó) [2], Carmen del Darién (Chocó) [2], Río Viejo (Bolívar) [2], Santa Ana (Magdalena) [2], Medio Atrato (Chocó) [2], Ciénaga (Magdalena) [1], Riosucio (Chocó) [1], Tadó (Chocó) [1], Aracataca (Magdalena) [1], Cerro de San Antonio (Magdalena) [1], Santa Bárbara (Antioquia) [1] and 25 more.

## ICFES

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| MunicipalScoresMicro | global_z | 0 | 0 | 0 | 0 | 55 | 292 |
| MunicipalScoresMicro | math_z | 0 | 0 | 0 | 0 | 104 | 320 |
| MunicipalScoresMicro | students | 0 | 0 | 0 | 826 | 0 | 0 |
| MunicipalStudentContext | share_car | 0 | 0 | 0 | 0 | 59 | 51 |
| MunicipalStudentContext | share_computer | 0 | 0 | 0 | 0 | 145 | 81 |
| MunicipalStudentContext | share_internet | 0 | 0 | 0 | 0 | 24 | 102 |
| MunicipalStudentContext | share_mother_higher_ed | 0 | 0 | 0 | 0 | 193 | 125 |
| MunicipalStudentContext | share_mother_primary_or_less | 0 | 0 | 0 | 0 | 65 | 89 |
| MunicipalStudentContext | share_stratum_1_2 | 0 | 0 | 0 | 0 | 418 | 126 |
| MunicipalStudentContext | share_washing_machine | 0 | 0 | 0 | 0 | 220 | 49 |
| SaberProByMunicipality | citizenship | 0 | 0 | 0 | 0 | 189 | 202 |
| SaberProByMunicipality | critical_reading | 0 | 0 | 0 | 0 | 171 | 261 |
| SaberProByMunicipality | english | 0 | 0 | 0 | 0 | 115 | 249 |
| SaberProByMunicipality | quantitative_reasoning | 0 | 0 | 0 | 0 | 156 | 310 |
| SaberProByMunicipality | written_communication | 0 | 0 | 0 | 0 | 201 | 449 |

**MunicipalScoresMicro.global_z**

- small_base (43 municipalities): Cartagena de Indias (Bolívar) [3], San José de Miranda (Santander) [3], Envigado (Antioquia) [2], Circasia (Quindío) [2], Sabaneta (Antioquia) [2], La Estrella (Antioquia) [2], Bogotá, D.C. (Bogotá, D.C.) [2], Sipí (Chocó) [2], Páramo (Santander) [2], Tenjo (Cundinamarca) [2], Cabrera (Santander) [1], La Tebaida (Quindío) [1] and 31 more.
- extreme (64 municipalities): Cota (Cundinamarca) [31], Sopó (Cundinamarca) [16], Albania (La Guajira) [15], Cajicá (Cundinamarca) [15], Chía (Cundinamarca) [15], Puerto Colombia (Atlántico) [14], La Calera (Cundinamarca) [14], Salento (Quindío) [13], Floridablanca (Santander) [12], Barranquilla (Atlántico) [12], Villamaría (Caldas) [11], Retiro (Antioquia) [10] and 52 more.

**MunicipalScoresMicro.math_z**

- small_base (88 municipalities): Circasia (Quindío) [4], Cota (Cundinamarca) [3], Salento (Quindío) [3], San José de Miranda (Santander) [2], Norosí (Bolívar) [2], Cepitá (Santander) [2], Gámbita (Santander) [2], Iza (Boyacá) [2], Paicol (Huila) [2], Barranquilla (Atlántico) [2], Sabaneta (Antioquia) [2], Retiro (Antioquia) [2] and 76 more.
- extreme (121 municipalities): Cota (Cundinamarca) [23], Albania (La Guajira) [15], Floridablanca (Santander) [13], La Calera (Cundinamarca) [13], Sopó (Cundinamarca) [13], Cajicá (Cundinamarca) [12], Puerto Colombia (Atlántico) [12], Villamaría (Caldas) [11], Salento (Quindío) [11], Chía (Cundinamarca) [10], Barranquilla (Atlántico) [8], Retiro (Antioquia) [6] and 109 more.

**MunicipalScoresMicro.students**

- break (404 municipalities): Ipiales (Nariño) [10], Florida (Valle Del Cauca) [9], Apartadó (Antioquia) [8], Espinal (Tolima) [8], El Cerrito (Valle Del Cauca) [7], Tuluá (Valle Del Cauca) [7], Itagüí (Antioquia) [7], Garzón (Huila) [7], Arauca (Arauca) [6], Hispania (Antioquia) [6], Funza (Cundinamarca) [6], Toledo (Antioquia) [6] and 392 more.

**MunicipalStudentContext.share_car**

- small_base (42 municipalities): Puerto Santander (ANM) (Amazonas) [3], Pacoa (ANM) (Vaupés) [3], La Pedrera (ANM) (Amazonas) [3], Barrancominas (Guainía) [2], Palmar (Santander) [2], El Encanto (ANM) (Amazonas) [2], Miriti - Paraná (ANM) (Amazonas) [2], Sativasur (Boyacá) [2], Yavaraté (ANM) (Vaupés) [2], La Victoria (Boyacá) [2], Mapiripana (ANM) (Guainía) [2], San Felipe (ANM) (Guainía) [2] and 30 more.
- extreme (25 municipalities): La Calera (Cundinamarca) [7], Tenjo (Cundinamarca) [6], Cota (Cundinamarca) [5], Villamaría (Caldas) [3], Sopó (Cundinamarca) [3], Salento (Quindío) [2], Albania (La Guajira) [2], Quibdó (Chocó) [2], San José del Guaviare (Guaviare) [2], Cajicá (Cundinamarca) [2], Patía (Cauca) [2], Bolívar (Cauca) [2] and 13 more.

**MunicipalStudentContext.share_computer**

- small_base (72 municipalities): Medio Atrato (Chocó) [8], Yavaraté (ANM) (Vaupés) [7], Puerto Santander (ANM) (Amazonas) [7], El Encanto (ANM) (Amazonas) [7], Alto Baudó (Chocó) [6], Sipí (Chocó) [5], El Litoral del San Juan (Chocó) [4], San Calixto (Norte De Santander) [4], Mapiripana (ANM) (Guainía) [4], Santa Bárbara (Nariño) [3], Regidor (Bolívar) [3], Mosquera (Nariño) [3] and 60 more.
- extreme (43 municipalities): Envigado (Antioquia) [8], Sabaneta (Antioquia) [8], La Calera (Cundinamarca) [4], La Estrella (Antioquia) [4], Cota (Cundinamarca) [4], Chía (Cundinamarca) [4], Tuchín (Córdoba) [3], Tenjo (Cundinamarca) [3], Mosquera (Cundinamarca) [3], Timbiquí (Cauca) [3], Puerto Colombia (Atlántico) [3], Villamaría (Caldas) [2] and 31 more.

**MunicipalStudentContext.share_internet**

- small_base (18 municipalities): Gachantivá (Boyacá) [2], Medio Atrato (Chocó) [2], Pacoa (ANM) (Vaupés) [2], Morichal (ANM) (Guainía) [2], San Felipe (ANM) (Guainía) [2], La Pedrera (ANM) (Amazonas) [2], Puerto Tejada (Cauca) [1], Vetas (Santander) [1], El Encanto (ANM) (Amazonas) [1], Pachavita (Boyacá) [1], Miriti - Paraná (ANM) (Amazonas) [1], Puerto Santander (ANM) (Amazonas) [1] and 6 more.
- extreme (32 municipalities): Sabaneta (Antioquia) [10], La Estrella (Antioquia) [9], Envigado (Antioquia) [9], Chía (Cundinamarca) [8], Cota (Cundinamarca) [7], Bogotá, D.C. (Bogotá, D.C.) [6], Bucaramanga (Santander) [6], Copacabana (Antioquia) [5], Itagüí (Antioquia) [4], Floridablanca (Santander) [4], La Calera (Cundinamarca) [4], Puerto Colombia (Atlántico) [3] and 20 more.

**MunicipalStudentContext.share_mother_higher_ed**

- small_base (125 municipalities): Tarapacá (ANM) (Amazonas) [4], Yavaraté (ANM) (Vaupés) [4], Tutazá (Boyacá) [4], La Victoria (Boyacá) [4], Chivatá (Boyacá) [4], Miriti - Paraná (ANM) (Amazonas) [4], Puerto Santander (ANM) (Amazonas) [4], Medio Atrato (Chocó) [3], Cepitá (Santander) [3], Palmar (Santander) [3], El Encanto (ANM) (Amazonas) [3], La Pedrera (ANM) (Amazonas) [3] and 113 more.
- extreme (43 municipalities): Envigado (Antioquia) [10], Cota (Cundinamarca) [10], Puerto Colombia (Atlántico) [10], La Estrella (Antioquia) [9], La Calera (Cundinamarca) [9], Tenjo (Cundinamarca) [8], Tunja (Boyacá) [7], Retiro (Antioquia) [7], Sabaneta (Antioquia) [7], Chía (Cundinamarca) [6], Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [4], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [3] and 31 more.

**MunicipalStudentContext.share_mother_primary_or_less**

- small_base (32 municipalities): Puerto Santander (ANM) (Amazonas) [7], Yavaraté (ANM) (Vaupés) [5], Sipí (Chocó) [5], Medio Atrato (Chocó) [5], Mapiripana (ANM) (Guainía) [4], El Encanto (ANM) (Amazonas) [4], Tarapacá (ANM) (Amazonas) [3], Guavatá (Santander) [2], Cepitá (Santander) [2], Carcasí (Santander) [2], La Chorrera (ANM) (Amazonas) [2], Jordán (Santander) [2] and 20 more.
- extreme (39 municipalities): Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [10], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [10], Envigado (Antioquia) [7], Palmar de Varela (Atlántico) [7], Sabaneta (Antioquia) [6], Puerto Colombia (Atlántico) [6], Cota (Cundinamarca) [4], Soplaviento (Bolívar) [2], Barrancominas (Guainía) [2], Mapiripana (ANM) (Guainía) [2], Patía (Cauca) [2], El Cerrito (Valle Del Cauca) [2] and 27 more.

**MunicipalStudentContext.share_stratum_1_2**

- small_base (240 municipalities): Itagüí (Antioquia) [4], La Estrella (Antioquia) [4], Manizales (Caldas) [4], Cota (Cundinamarca) [4], Floridablanca (Santander) [4], Tunja (Boyacá) [4], Tenjo (Cundinamarca) [4], Mosquera (Cundinamarca) [4], Rionegro (Antioquia) [4], Bucaramanga (Santander) [4], Dosquebradas (Risaralda) [4], Marinilla (Antioquia) [4] and 228 more.
- extreme (50 municipalities): Retiro (Antioquia) [11], Envigado (Antioquia) [11], La Ceja (Antioquia) [8], Sabaneta (Antioquia) [8], La Estrella (Antioquia) [7], Marinilla (Antioquia) [6], Entrerríos (Antioquia) [4], Cota (Cundinamarca) [4], Tenjo (Cundinamarca) [4], Uribia (La Guajira) [3], Barrancominas (Guainía) [3], Pacoa (ANM) (Vaupés) [3] and 38 more.

**MunicipalStudentContext.share_washing_machine**

- small_base (97 municipalities): El Encanto (ANM) (Amazonas) [9], Puerto Santander (ANM) (Amazonas) [9], Yavaraté (ANM) (Vaupés) [8], La Pedrera (ANM) (Amazonas) [8], La Chorrera (ANM) (Amazonas) [7], Tarapacá (ANM) (Amazonas) [6], San Felipe (ANM) (Guainía) [6], Mapiripana (ANM) (Guainía) [6], Gama (Cundinamarca) [6], Jambaló (Cauca) [5], López de Micay (Cauca) [4], El Litoral del San Juan (Chocó) [4] and 85 more.
- extreme (30 municipalities): Providencia (Archipiélago De San Andrés, Providencia Y Santa Catalina) [7], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [7], Jambaló (Cauca) [3], Totoró (Cauca) [3], Envigado (Antioquia) [2], San José del Guaviare (Guaviare) [2], Timbiquí (Cauca) [2], Jamundí (Valle Del Cauca) [1], Yavaraté (ANM) (Vaupés) [1], Pacoa (ANM) (Vaupés) [1], Mitú (Vaupés) [1], La Chorrera (ANM) (Amazonas) [1] and 18 more.

**SaberProByMunicipality.citizenship**

- small_base (148 municipalities): El Dorado (Meta) [3], Campohermoso (Boyacá) [3], Herrán (Norte De Santander) [3], Panqueba (Boyacá) [3], Caicedo (Antioquia) [3], Jordán (Santander) [3], López de Micay (Cauca) [2], Santa Sofía (Boyacá) [2], Río Viejo (Bolívar) [2], San Fernando (Bolívar) [2], Vetas (Santander) [2], Santa Helena del Opón (Santander) [2] and 136 more.
- extreme (78 municipalities): Unión Panamericana (Chocó) [7], Bahía Solano (Chocó) [7], Alto Baudó (Chocó) [7], Medio San Juan (Chocó) [6], El Cantón del San Pablo (Chocó) [6], Bojayá (Chocó) [6], Bajo Baudó (Chocó) [6], Juradó (Chocó) [6], Nuquí (Chocó) [6], Río Quito (Chocó) [6], Riosucio (Chocó) [6], Nóvita (Chocó) [5] and 66 more.

**SaberProByMunicipality.critical_reading**

- small_base (136 municipalities): Aguada (Santander) [3], Jordán (Santander) [3], Solano (Caquetá) [3], Pajarito (Boyacá) [3], Campamento (Antioquia) [3], Recetor (Casanare) [3], Cepitá (Santander) [2], Hatillo de Loba (Bolívar) [2], Charta (Santander) [2], Puerto Concordia (Meta) [2], Río Viejo (Bolívar) [2], Leiva (Nariño) [2] and 124 more.
- extreme (72 municipalities): Medio San Juan (Chocó) [8], Unguía (Chocó) [8], Juradó (Chocó) [8], Istmina (Chocó) [8], El Cantón del San Pablo (Chocó) [8], Bojayá (Chocó) [8], Bahía Solano (Chocó) [8], Bagadó (Chocó) [8], Alto Baudó (Chocó) [8], Río Quito (Chocó) [8], Riosucio (Chocó) [8], Nuquí (Chocó) [8] and 60 more.

**SaberProByMunicipality.english**

- small_base (100 municipalities): Concordia (Antioquia) [4], Cómbita (Boyacá) [3], Lejanías (Meta) [2], Santa Bárbara (Nariño) [2], El Litoral del San Juan (Chocó) [2], San Eduardo (Boyacá) [2], Maceo (Antioquia) [2], Medio Atrato (Chocó) [2], Río Viejo (Bolívar) [2], La Tola (Nariño) [2], La Capilla (Boyacá) [2], El Peñón (Bolívar) [2] and 88 more.
- extreme (80 municipalities): Cota (Cundinamarca) [10], Puerto Colombia (Atlántico) [9], Envigado (Antioquia) [8], Medio San Juan (Chocó) [7], Unión Panamericana (Chocó) [7], Retiro (Antioquia) [7], El Cantón del San Pablo (Chocó) [7], Río Quito (Chocó) [7], Bojayá (Chocó) [6], Bahía Solano (Chocó) [6], Nuquí (Chocó) [6], Riosucio (Chocó) [6] and 68 more.

**SaberProByMunicipality.quantitative_reasoning**

- small_base (127 municipalities): Santa Bárbara (Nariño) [5], Santa Rosa (Cauca) [3], Angelópolis (Antioquia) [2], Gachantivá (Boyacá) [2], El Peñón (Bolívar) [2], Chimá (Santander) [2], Cepitá (Santander) [2], Balboa (Risaralda) [2], Campohermoso (Boyacá) [2], Chiscas (Boyacá) [2], Guacamayas (Boyacá) [2], Arroyohondo (Bolívar) [2] and 115 more.
- extreme (76 municipalities): Alto Baudó (Chocó) [10], Unión Panamericana (Chocó) [10], Bojayá (Chocó) [10], Río Quito (Chocó) [10], Bajo Baudó (Chocó) [10], Nuquí (Chocó) [10], Nóvita (Chocó) [10], Bahía Solano (Chocó) [10], Bagadó (Chocó) [10], Atrato (Chocó) [9], Condoto (Chocó) [9], Cértegui (Chocó) [9] and 64 more.

**SaberProByMunicipality.written_communication**

- small_base (165 municipalities): La Tola (Nariño) [4], Tópaga (Boyacá) [4], Campohermoso (Boyacá) [3], Los Córdobas (Córdoba) [3], El Dorado (Meta) [3], Labateca (Norte De Santander) [2], Charta (Santander) [2], Albania (Caquetá) [2], Palmar (Santander) [2], Santa Lucía (Atlántico) [2], Zapayán (Magdalena) [2], Cabrera (Santander) [2] and 153 more.
- extreme (268 municipalities): Lloró (Chocó) [8], Bojayá (Chocó) [8], Nóvita (Chocó) [8], Río Quito (Chocó) [8], Unión Panamericana (Chocó) [8], Cértegui (Chocó) [7], Acandí (Chocó) [7], Alto Baudó (Chocó) [7], Bagadó (Chocó) [6], Juradó (Chocó) [6], Nuquí (Chocó) [6], Atrato (Chocó) [6] and 256 more.

## MEN

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| EnrolmentAndDropout | approval | 0 | 0 | 0 | 4 | 0 | 295 |
| EnrolmentAndDropout | dropout | 0 | 0 | 0 | 0 | 0 | 33 |
| EnrolmentAndDropout | dropout_upper_secondary | 0 | 0 | 0 | 59 | 0 | 33 |
| EnrolmentAndDropout | net_enrolment | 0 | 0 | 2,190 | 453 | 0 | 241 |
| EnrolmentAndDropout | net_enrolment_upper_secondary | 0 | 0 | 31 | 191 | 0 | 478 |
| EnrolmentAndDropout | repetition | 0 | 0 | 0 | 1 | 0 | 92 |

**EnrolmentAndDropout.approval**

- break (3 municipalities): Norosí (Bolívar), 2020: 83.7 the year before; Unión Panamericana (Chocó), 2020: 91.5 the year before; Unión Panamericana (Chocó), 2021: 53.0 the year before; Pana Pana (ANM) (Guainía), 2023: 58.2 the year before.
- extreme (150 municipalities): Puerto Arica (ANM) (Amazonas) [8], La Tola (Nariño) [7], Tarapacá (ANM) (Amazonas) [6], Ancuya (Nariño) [5], La Victoria (ANM) (Amazonas) [5], Miriti - Paraná (ANM) (Amazonas) [5], Mosquera (Nariño) [5], Cumbal (Nariño) [5], Cabrera (Santander) [5], Pupiales (Nariño) [4], Santa Bárbara (Nariño) [4], Cuaspud Carlosama (Nariño) [4] and 138 more.

**EnrolmentAndDropout.dropout**

- extreme (29 municipalities): Papunahua (ANM) (Vaupés) [2], Puerto Arica (ANM) (Amazonas) [2], La Victoria (ANM) (Amazonas) [2], San Eduardo (Boyacá) [2], Gama (Cundinamarca) [1], Taraira (Vaupés) [1], Cabrera (Santander) [1], Providencia (Nariño) [1], Ospina (Nariño) [1], Nariño (Nariño) [1], Sipí (Chocó) [1], Bagadó (Chocó) [1] and 17 more.

**EnrolmentAndDropout.dropout_upper_secondary**

- break (29 municipalities): Magüí (Nariño) [3], Aguachica (Cesar) [2], Pailitas (Cesar) [2], Morichal (ANM) (Guainía) [2], Útica (Cundinamarca) [2], Funza (Cundinamarca) [2], Tamalameque (Cesar) [2], San Martín (Cesar) [2], San Diego (Cesar) [2], San Alberto (Cesar) [2], La Paz (Cesar) [2], Río de Oro (Cesar) [2] and 17 more.
- extreme (31 municipalities): Morichal (ANM) (Guainía) [2], Magüí (Nariño) [2], Aguachica (Cesar) [1], Pelaya (Cesar) [1], Pana Pana (ANM) (Guainía) [1], Miriti - Paraná (ANM) (Amazonas) [1], Útica (Cundinamarca) [1], Funza (Cundinamarca) [1], Tamalameque (Cesar) [1], San Martín (Cesar) [1], San Diego (Cesar) [1], San Alberto (Cesar) [1] and 19 more.

**EnrolmentAndDropout.net_enrolment**

- inconsistent (433 municipalities): La Calera (Cundinamarca) [13], Bahía Solano (Chocó) [13], Fúquene (Cundinamarca) [13], Corozal (Sucre) [13], San Gil (Santander) [13], Istmina (Chocó) [13], Puente Nacional (Santander) [13], Retiro (Antioquia) [13], Soracá (Boyacá) [13], Sogamoso (Boyacá) [13], Barrancabermeja (Santander) [13], Turmequé (Boyacá) [13] and 421 more.
- break (265 municipalities): Concepción (Antioquia) [4], Cértegui (Chocó) [3], Santa Rosa (Cauca) [3], Palmar (Santander) [3], San Benito (Santander) [3], San Gil (Santander) [3], El Paso (Cesar) [3], Curumaní (Cesar) [3], Chiriguaná (Cesar) [3], Becerril (Cesar) [3], Guamal (Meta) [3], Coloso (Sucre) [3] and 253 more.
- extreme (186 municipalities): Papunahua (ANM) (Vaupés) [7], La Victoria (ANM) (Amazonas) [7], Villa de San Diego de Ubaté (Cundinamarca) [5], Paipa (Boyacá) [4], Taraira (Vaupés) [3], Suaita (Santander) [3], Talaigua Nuevo (Bolívar) [3], Rionegro (Santander) [3], Zona Bananera (Magdalena) [2], Vegachí (Antioquia) [2], Barranquilla (Atlántico) [2], San Sebastián de Buenavista (Magdalena) [2] and 174 more.

**EnrolmentAndDropout.net_enrolment_upper_secondary**

- inconsistent (10 municipalities): Cota (Cundinamarca) [9], Turmequé (Boyacá) [6], Quetame (Cundinamarca) [4], Fúquene (Cundinamarca) [3], Puerto Colombia (Atlántico) [2], Soracá (Boyacá) [2], Puente Nacional (Santander) [2], Panqueba (Boyacá) [1], Soatá (Boyacá) [1], Restrepo (Meta) [1].
- break (133 municipalities): Berbeo (Boyacá) [3], Albán (Nariño) [3], Nilo (Cundinamarca) [3], Caloto (Cauca) [3], La Macarena (Meta) [2], San Juanito (Meta) [2], Restrepo (Meta) [2], González (Cesar) [2], Gámbita (Santander) [2], Bituima (Cundinamarca) [2], El Guacamayo (Santander) [2], Cabrera (Santander) [2] and 121 more.
- extreme (93 municipalities): Magüí (Nariño) [14], Santa Bárbara (Nariño) [14], Medio Atrato (Chocó) [14], El Litoral del San Juan (Chocó) [13], Cumaribo (Vichada) [12], San Felipe (ANM) (Guainía) [12], Alto Baudó (Chocó) [12], Barrancominas (Guainía) [11], Tenjo (Cundinamarca) [11], Puerto Santander (ANM) (Amazonas) [11], Pacoa (ANM) (Vaupés) [10], Montecristo (Bolívar) [10] and 81 more.

**EnrolmentAndDropout.repetition**

- break (1 municipalities): Norosí (Bolívar), 2021: 5.9 the year before.
- extreme (70 municipalities): Cabrera (Cundinamarca) [4], Puerto Colombia (ANM) (Guainía) [3], Aguada (Santander) [3], La Victoria (ANM) (Amazonas) [3], Papunahua (ANM) (Vaupés) [3], Chiscas (Boyacá) [2], Gachantivá (Boyacá) [2], San Juanito (Meta) [2], Providencia (Nariño) [2], Yalí (Antioquia) [2], San Francisco (Cundinamarca) [2], San Cayetano (Cundinamarca) [2] and 58 more.

## Police

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | police_domestic_violence | 0 | 14 | 0 | 0 | 152 | 77 |
| PeriodRates | police_homicide | 0 | 14 | 0 | 0 | 120 | 4 |
| PeriodRates | police_massacre_events | 0 | 6 | 0 | 0 | 148 | 26 |
| PeriodRates | police_massacre_victims | 0 | 6 | 0 | 0 | 24 | 204 |
| PeriodRates | police_sexual_violence | 0 | 14 | 0 | 0 | 152 | 125 |
| PoliceDailyCases | police_domestic_violence | 0 | 0 | 0 | 273 | 0 | 0 |
| PoliceDailyCases | police_homicide | 0 | 0 | 0 | 16 | 0 | 0 |
| PoliceDailyCases | police_sexual_violence | 0 | 0 | 0 | 82 | 0 | 0 |

**PeriodRates.police_domestic_violence**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (52 municipalities): Yavaraté (ANM) (Vaupés) [7], Papunahua (ANM) (Vaupés) [7], Morichal (ANM) (Guainía) [7], Pana Pana (ANM) (Guainía) [7], Cacahual (ANM) (Guainía) [7], La Guadalupe (ANM) (Guainía) [7], Puerto Colombia (ANM) (Guainía) [7], Puerto Alegría (ANM) (Amazonas) [7], La Victoria (ANM) (Amazonas) [7], Cepitá (Santander) [5], Pacoa (ANM) (Vaupés) [5], San Jacinto del Cauca (Bolívar) [5] and 40 more.
- extreme (27 municipalities): Cumaribo (Vichada) [7], Carmen del Darién (Chocó) [7], Bojayá (Chocó) [5], Olaya Herrera (Nariño) [5], Uribia (La Guajira) [5], Manaure (La Guajira) [4], Barrancominas (Guainía) [4], Zapayán (Magdalena) [4], Alto Baudó (Chocó) [3], Roberto Payán (Nariño) [3], Magüí (Nariño) [3], Santa Bárbara (Nariño) [2] and 15 more.

**PeriodRates.police_homicide**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (60 municipalities): Murindó (Antioquia) [2], Santa Lucía (Atlántico) [2], Río Quito (Chocó) [2], Zapayán (Magdalena) [2], Cabrera (Santander) [2], Enciso (Santander) [2], Galán (Santander) [2], Jordán (Santander) [2], Palmar (Santander) [2], San Joaquín (Santander) [2], San Miguel (Santander) [2], Vetas (Santander) [2] and 48 more.
- extreme (3 municipalities): Policarpa (Nariño) [2], Briceño (Antioquia) [1], Tarazá (Antioquia) [1].

**PeriodRates.police_massacre_events**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (71 municipalities): Mercaderes (Cauca) [4], El Águila (Valle Del Cauca) [4], Venecia (Antioquia) [4], El Peñol (Nariño) [2], La Playa (Norte De Santander) [2], Policarpa (Nariño) [2], Mallama (Nariño) [2], La Florida (Nariño) [2], El Rosario (Nariño) [2], Amalfi (Antioquia) [2], Santuario (Risaralda) [2], Colón (Nariño) [2] and 59 more.
- extreme (13 municipalities): Abejorral (Antioquia) [2], Balboa (Cauca) [2], Corinto (Cauca) [2], Guachené (Cauca) [2], Miranda (Cauca) [2], Puerto Gaitán (Meta) [2], Ipiales (Nariño) [2], El Carmen (Norte De Santander) [2], Ansermanuevo (Valle Del Cauca) [2], Cartago (Valle Del Cauca) [2], Toro (Valle Del Cauca) [2], Puerto Guzmán (Putumayo) [2] and 1 more.

**PeriodRates.police_massacre_victims**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (12 municipalities): Chita (Boyacá) [2], Belén de Los Andaquíes (Caquetá) [2], La Jagua de Ibirico (Cesar) [2], Lloró (Chocó) [2], Íquira (Huila) [2], El Peñol (Nariño) [2], La Florida (Nariño) [2], Mallama (Nariño) [2], La Playa (Norte De Santander) [2], La Celia (Risaralda) [2], Versalles (Valle Del Cauca) [2], Saravena (Arauca) [2].
- extreme (92 municipalities): Morales (Cauca) [4], Mercaderes (Cauca) [4], Puerto Rico (Caquetá) [4], Buenos Aires (Cauca) [4], Cartagena del Chairá (Caquetá) [4], Guadalajara de Buga (Valle Del Cauca) [4], Cartago (Valle Del Cauca) [4], El Águila (Valle Del Cauca) [4], Balboa (Cauca) [4], Puerto Guzmán (Putumayo) [4], Colón (Nariño) [2], Puerto Gaitán (Meta) [2] and 80 more.

**PeriodRates.police_sexual_violence**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (62 municipalities): Yavaraté (ANM) (Vaupés) [7], Pana Pana (ANM) (Guainía) [7], San Felipe (ANM) (Guainía) [7], Puerto Colombia (ANM) (Guainía) [7], La Guadalupe (ANM) (Guainía) [7], La Victoria (ANM) (Amazonas) [7], Papunahua (ANM) (Vaupés) [7], Morichal (ANM) (Guainía) [7], Pacoa (ANM) (Vaupés) [5], Mapiripana (ANM) (Guainía) [5], Puerto Arica (ANM) (Amazonas) [5], Zapayán (Magdalena) [4] and 50 more.
- extreme (46 municipalities): Uribia (La Guajira) [7], Alto Baudó (Chocó) [7], Barrancominas (Guainía) [6], Manaure (La Guajira) [6], Carmen del Darién (Chocó) [6], Olaya Herrera (Nariño) [5], Medio Baudó (Chocó) [5], Bajo Baudó (Chocó) [5], Marinilla (Antioquia) [4], Mosquera (Nariño) [4], El Litoral del San Juan (Chocó) [4], Puerto Escondido (Córdoba) [4] and 34 more.

**PoliceDailyCases.police_domestic_violence**

- break (241 municipalities): San Bernardo del Viento (Córdoba) [3], Zipaquirá (Cundinamarca) [3], Soacha (Cundinamarca) [2], Maicao (La Guajira) [2], San Antero (Córdoba) [2], San Andrés Sotavento (Córdoba) [2], Melgar (Tolima) [2], Planeta Rica (Córdoba) [2], San Juan Nepomuceno (Bolívar) [2], Icononzo (Tolima) [2], Montelíbano (Córdoba) [2], Aquitania (Boyacá) [2] and 229 more.

**PoliceDailyCases.police_homicide**

- break (16 municipalities): Briceño (Antioquia) [1], Girardota (Antioquia) [1], Remedios (Antioquia) [1], Santa Rosa de Osos (Antioquia) [1], Segovia (Antioquia) [1], Vegachí (Antioquia) [1], Baranoa (Atlántico) [1], Toribío (Cauca) [1], Ayapel (Córdoba) [1], La Apartada (Córdoba) [1], Planeta Rica (Córdoba) [1], Valencia (Córdoba) [1] and 4 more.

**PoliceDailyCases.police_sexual_violence**

- break (81 municipalities): Zipaquirá (Cundinamarca) [2], Medellín (Antioquia) [1], Riohacha (La Guajira) [1], San José de Cúcuta (Norte De Santander) [1], La Unión (Nariño) [1], Acacías (Meta) [1], Villavicencio (Meta) [1], Guamal (Magdalena) [1], Fundación (Magdalena) [1], Ciénaga (Magdalena) [1], Quibdó (Chocó) [1], Funza (Cundinamarca) [1] and 69 more.

## CNMH

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | cnmh_act_of_war_events | 0 | 14 | 0 | 0 | 146 | 1,272 |
| PeriodRates | cnmh_act_of_war_victims | 0 | 14 | 0 | 0 | 127 | 1,227 |
| PeriodRates | cnmh_attack_on_a_town_events | 0 | 14 | 0 | 0 | 52 | 14 |
| PeriodRates | cnmh_attack_on_a_town_victims | 0 | 14 | 0 | 0 | 2 | 24 |
| PeriodRates | cnmh_damage_to_civilian_property_events | 0 | 14 | 0 | 0 | 296 | 678 |
| PeriodRates | cnmh_damage_to_civilian_property_victims | 0 | 14 | 0 | 0 | 98 | 40 |
| PeriodRates | cnmh_forced_disappearance_events | 0 | 14 | 0 | 0 | 257 | 694 |
| PeriodRates | cnmh_forced_disappearance_victims | 0 | 14 | 0 | 0 | 205 | 784 |
| PeriodRates | cnmh_kidnapping_events | 0 | 14 | 0 | 0 | 375 | 674 |
| PeriodRates | cnmh_kidnapping_victims | 0 | 14 | 0 | 0 | 143 | 883 |
| PeriodRates | cnmh_landmines_and_explosive_remnants_events | 0 | 14 | 0 | 0 | 204 | 846 |
| PeriodRates | cnmh_landmines_and_explosive_remnants_victims | 0 | 14 | 0 | 0 | 152 | 790 |
| PeriodRates | cnmh_massacre_events | 0 | 14 | 0 | 0 | 470 | 106 |
| PeriodRates | cnmh_massacre_victims | 0 | 14 | 0 | 0 | 0 | 703 |
| PeriodRates | cnmh_recruitment_of_children_and_adolescents_events | 0 | 14 | 0 | 0 | 280 | 475 |
| PeriodRates | cnmh_recruitment_of_children_and_adolescents_victims | 0 | 14 | 0 | 0 | 216 | 520 |
| PeriodRates | cnmh_selective_killing_events | 0 | 14 | 0 | 0 | 84 | 1,240 |
| PeriodRates | cnmh_selective_killing_victims | 0 | 14 | 0 | 0 | 61 | 1,424 |
| PeriodRates | cnmh_sexual_violence_events | 0 | 14 | 0 | 0 | 196 | 625 |
| PeriodRates | cnmh_sexual_violence_victims | 0 | 14 | 0 | 0 | 144 | 697 |
| PeriodRates | cnmh_terrorist_attack_events | 0 | 14 | 0 | 0 | 173 | 44 |
| PeriodRates | cnmh_terrorist_attack_victims | 0 | 14 | 0 | 0 | 44 | 74 |

**PeriodRates.cnmh_act_of_war_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (78 municipalities): Sácama (Casanare) [5], La Tola (Nariño) [5], Paya (Boyacá) [4], Calamar (Guaviare) [4], San José del Palmar (Chocó) [4], Recetor (Casanare) [4], Tutazá (Boyacá) [4], Florencia (Cauca) [3], Toledo (Antioquia) [3], Juradó (Chocó) [3], Murindó (Antioquia) [3], Pisba (Boyacá) [3] and 66 more.
- extreme (281 municipalities): Convención (Norte De Santander) [13], Teorama (Norte De Santander) [13], El Tarra (Norte De Santander) [13], Fortul (Arauca) [13], Valdivia (Antioquia) [13], Corinto (Cauca) [13], Tame (Arauca) [13], Tibú (Norte De Santander) [13], Ituango (Antioquia) [12], Argelia (Cauca) [12], Toribío (Cauca) [12], El Tambo (Cauca) [12] and 269 more.

**PeriodRates.cnmh_act_of_war_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (71 municipalities): Sácama (Casanare) [4], Nóvita (Chocó) [4], San José del Palmar (Chocó) [4], Labranzagrande (Boyacá) [4], El Carmen (Norte De Santander) [3], San Calixto (Norte De Santander) [3], Acandí (Chocó) [3], Cerrito (Santander) [2], Cértegui (Chocó) [2], Juradó (Chocó) [2], Sipí (Chocó) [2], Colombia (Huila) [2] and 59 more.
- extreme (325 municipalities): Teorama (Norte De Santander) [13], Tame (Arauca) [13], El Tambo (Cauca) [12], Ituango (Antioquia) [12], Calamar (Guaviare) [12], Tibú (Norte De Santander) [12], San Vicente del Caguán (Caquetá) [11], La Macarena (Meta) [11], San José del Guaviare (Guaviare) [11], Uribe (Meta) [11], Toribío (Cauca) [10], Convención (Norte De Santander) [10] and 313 more.

**PeriodRates.cnmh_attack_on_a_town_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (21 municipalities): Caldono (Cauca) [6], Toribío (Cauca) [4], San Calixto (Norte De Santander) [4], Caloto (Cauca) [4], Córdoba (Bolívar) [2], Santacruz (Nariño) [2], Francisco Pizarro (Nariño) [2], Los Andes (Nariño) [2], La Llanada (Nariño) [2], Cumbal (Nariño) [2], Quibdó (Chocó) [2], Suárez (Cauca) [2] and 9 more.
- extreme (7 municipalities): Argelia (Cauca) [2], El Tambo (Cauca) [2], Sipí (Chocó) [2], Teruel (Huila) [2], Vistahermosa (Meta) [2], Samaniego (Nariño) [2], Casabianca (Tolima) [2].

**PeriodRates.cnmh_attack_on_a_town_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (1 municipalities): Los Andes (Nariño), government:uribe_1: 1 observed, 0.01 expected at the national rate; Los Andes (Nariño), phase:uribe_1: 1 observed, 0.01 expected at the national rate.
- extreme (12 municipalities): Marulanda (Caldas) [2], Caloto (Cauca) [2], Corinto (Cauca) [2], Toribío (Cauca) [2], Sipí (Chocó) [2], Vistahermosa (Meta) [2], Cumbal (Nariño) [2], La Llanada (Nariño) [2], Francisco Pizarro (Nariño) [2], Samaniego (Nariño) [2], Santacruz (Nariño) [2], Ibagué (Tolima) [2].

**PeriodRates.cnmh_damage_to_civilian_property_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (141 municipalities): Calamar (Guaviare) [5], Piamonte (Cauca) [5], Hatillo de Loba (Bolívar) [4], Bucarasica (Norte De Santander) [4], Puerto Rico (Meta) [4], Arenal (Bolívar) [4], Pisba (Boyacá) [4], El Carmen de Atrato (Chocó) [4], Pelaya (Cesar) [4], La Gloria (Cesar) [4], San Andrés de Cuerquía (Antioquia) [4], Padilla (Cauca) [4] and 129 more.
- extreme (171 municipalities): Valdivia (Antioquia) [12], Tame (Arauca) [11], Arauquita (Arauca) [11], San Andrés de Tumaco (Nariño) [10], Corinto (Cauca) [10], El Tarra (Norte De Santander) [9], Caldono (Cauca) [9], Fortul (Arauca) [9], Saravena (Arauca) [9], Tibú (Norte De Santander) [9], Teorama (Norte De Santander) [9], Caloto (Cauca) [9] and 159 more.

**PeriodRates.cnmh_damage_to_civilian_property_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (43 municipalities): Condoto (Chocó) [4], Tame (Arauca) [4], Valdivia (Antioquia) [4], Tibú (Norte De Santander) [4], Algeciras (Huila) [4], San José de Cúcuta (Norte De Santander) [4], Briceño (Antioquia) [2], El Castillo (Meta) [2], Riohacha (La Guajira) [2], Hatonuevo (La Guajira) [2], Fundación (Magdalena) [2], Tenerife (Magdalena) [2] and 31 more.
- extreme (19 municipalities): Barbacoas (Nariño) [4], Granada (Antioquia) [2], Puerto Guzmán (Putumayo) [2], Puerto Caicedo (Putumayo) [2], Tolú Viejo (Sucre) [2], Teorama (Norte De Santander) [2], San José de Cúcuta (Norte De Santander) [2], Santa Bárbara (Nariño) [2], Puerres (Nariño) [2], Íquira (Huila) [2], San Carlos (Antioquia) [2], Quibdó (Chocó) [2] and 7 more.

**PeriodRates.cnmh_forced_disappearance_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (127 municipalities): Segovia (Antioquia) [4], Valdivia (Antioquia) [4], Calamar (Guaviare) [4], Cáceres (Antioquia) [4], Toribío (Cauca) [4], Curillo (Caquetá) [4], Puerto Guzmán (Putumayo) [4], Caloto (Cauca) [4], Solano (Caquetá) [4], La Montañita (Caquetá) [4], El Litoral del San Juan (Chocó) [3], Puerto Leguízamo (Putumayo) [3] and 115 more.
- extreme (220 municipalities): San Andrés de Tumaco (Nariño) [12], Valle del Guamuez (Putumayo) [9], Puerto Berrío (Antioquia) [8], Florencia (Caquetá) [8], San Vicente del Caguán (Caquetá) [8], Cáceres (Antioquia) [8], Buenaventura (Valle Del Cauca) [8], Tarazá (Antioquia) [6], Ricaurte (Nariño) [6], Policarpa (Nariño) [6], El Charco (Nariño) [6], Cumbitara (Nariño) [6] and 208 more.

**PeriodRates.cnmh_forced_disappearance_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (105 municipalities): Cáceres (Antioquia) [4], Toribío (Cauca) [4], Curillo (Caquetá) [4], Puerto Guzmán (Putumayo) [4], Solano (Caquetá) [4], Valdivia (Antioquia) [4], El Litoral del San Juan (Chocó) [3], El Doncello (Caquetá) [3], La Montañita (Caquetá) [3], Tame (Arauca) [3], Caloto (Cauca) [3], Albania (La Guajira) [2] and 93 more.
- extreme (241 municipalities): San Andrés de Tumaco (Nariño) [12], San Vicente del Caguán (Caquetá) [11], Buenaventura (Valle Del Cauca) [11], Puerto Berrío (Antioquia) [11], Valle del Guamuez (Putumayo) [9], Cáceres (Antioquia) [8], Florencia (Caquetá) [8], Puerto Santander (Norte De Santander) [8], El Tambo (Cauca) [6], Curillo (Caquetá) [6], San José del Fragua (Caquetá) [6], Puerto Rico (Caquetá) [6] and 229 more.

**PeriodRates.cnmh_kidnapping_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (167 municipalities): Morales (Bolívar) [6], Piamonte (Cauca) [6], Hacarí (Norte De Santander) [5], Alto Baudó (Chocó) [5], Mutatá (Antioquia) [5], Simití (Bolívar) [4], Norosí (Bolívar) [4], Santa Rosa (Cauca) [4], Totoró (Cauca) [4], González (Cesar) [4], Río de Oro (Cesar) [4], Tamalameque (Cesar) [4] and 155 more.
- extreme (200 municipalities): Tame (Arauca) [12], El Tarra (Norte De Santander) [11], Arauquita (Arauca) [11], Saravena (Arauca) [10], Convención (Norte De Santander) [10], Arauca (Arauca) [10], Santa Bárbara (Nariño) [8], Policarpa (Nariño) [8], Teorama (Norte De Santander) [8], Corinto (Cauca) [8], Fortul (Arauca) [8], El Carmen (Norte De Santander) [8] and 188 more.

**PeriodRates.cnmh_kidnapping_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (73 municipalities): Mutatá (Antioquia) [5], Curillo (Caquetá) [4], Medio San Juan (Chocó) [4], Florencia (Cauca) [4], Tadó (Chocó) [3], Unguía (Chocó) [3], Cértegui (Chocó) [3], El Carmen (Norte De Santander) [3], San José del Palmar (Chocó) [3], Murillo (Tolima) [2], El Rosario (Nariño) [2], Carurú (Vaupés) [2] and 61 more.
- extreme (254 municipalities): Teorama (Norte De Santander) [12], Tame (Arauca) [12], El Tarra (Norte De Santander) [11], Arauca (Arauca) [10], Convención (Norte De Santander) [10], Quibdó (Chocó) [10], Arauquita (Arauca) [10], Hacarí (Norte De Santander) [10], Saravena (Arauca) [10], Cumbitara (Nariño) [8], Tibú (Norte De Santander) [8], Policarpa (Nariño) [8] and 242 more.

**PeriodRates.cnmh_landmines_and_explosive_remnants_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (104 municipalities): El Carmen (Norte De Santander) [7], Puerto Rondón (Arauca) [7], Mapiripán (Meta) [6], Baraya (Huila) [5], Policarpa (Nariño) [4], Támara (Casanare) [4], Uribe (Meta) [3], Zambrano (Bolívar) [3], Roberto Payán (Nariño) [3], La Playa (Norte De Santander) [3], Vistahermosa (Meta) [3], Puerto Concordia (Meta) [3] and 92 more.
- extreme (185 municipalities): Ituango (Antioquia) [13], Hacarí (Norte De Santander) [13], Teorama (Norte De Santander) [13], Tame (Arauca) [13], Arauquita (Arauca) [13], Anorí (Antioquia) [12], Tibú (Norte De Santander) [12], Valdivia (Antioquia) [12], Fortul (Arauca) [11], Tarazá (Antioquia) [11], El Tarra (Norte De Santander) [10], Sácama (Casanare) [10] and 173 more.

**PeriodRates.cnmh_landmines_and_explosive_remnants_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (86 municipalities): La Playa (Norte De Santander) [6], Policarpa (Nariño) [6], Támara (Casanare) [4], Guapi (Cauca) [3], Mapiripán (Meta) [3], Unguía (Chocó) [3], Convención (Norte De Santander) [3], El Carmen (Norte De Santander) [3], Carmen del Darién (Chocó) [2], Pailitas (Cesar) [2], Cabrera (Cundinamarca) [2], Guayabetal (Cundinamarca) [2] and 74 more.
- extreme (189 municipalities): Tarazá (Antioquia) [13], Valdivia (Antioquia) [12], Anorí (Antioquia) [12], Teorama (Norte De Santander) [12], Hacarí (Norte De Santander) [11], Ituango (Antioquia) [11], Dabeiba (Antioquia) [10], Tibú (Norte De Santander) [10], Argelia (Cauca) [9], San Andrés de Tumaco (Nariño) [9], Arauquita (Arauca) [9], Fortul (Arauca) [9] and 177 more.

**PeriodRates.cnmh_massacre_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (178 municipalities): Policarpa (Nariño) [8], Mercaderes (Cauca) [6], San Rafael (Antioquia) [6], Montecristo (Bolívar) [6], San Miguel (Putumayo) [6], Suárez (Cauca) [6], Cáceres (Antioquia) [6], Barbacoas (Nariño) [6], Hato Corozal (Casanare) [6], Villa del Rosario (Norte De Santander) [5], Mosquera (Nariño) [4], Puerto Rico (Meta) [4] and 166 more.
- extreme (48 municipalities): Remedios (Antioquia) [4], Miraflores (Guaviare) [4], Riosucio (Chocó) [4], Valdivia (Antioquia) [4], Tame (Arauca) [4], Granada (Antioquia) [2], Leiva (Nariño) [2], Maicao (La Guajira) [2], San Juan del Cesar (La Guajira) [2], El Castillo (Meta) [2], Puerto Rico (Meta) [2], San Juan de Arama (Meta) [2] and 36 more.

**PeriodRates.cnmh_massacre_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- extreme (241 municipalities): San Andrés de Tumaco (Nariño) [10], Valdivia (Antioquia) [8], Montecristo (Bolívar) [8], Remedios (Antioquia) [8], Tame (Arauca) [8], Cáceres (Antioquia) [8], Suárez (Cauca) [8], Policarpa (Nariño) [8], Mercaderes (Cauca) [6], Segovia (Antioquia) [6], Zaragoza (Antioquia) [6], San Rafael (Antioquia) [6] and 229 more.

**PeriodRates.cnmh_recruitment_of_children_and_adolescents_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (119 municipalities): Murindó (Antioquia) [6], Puerto Rondón (Arauca) [6], Anorí (Antioquia) [4], Cantagallo (Bolívar) [4], Solano (Caquetá) [4], Olaya Herrera (Nariño) [4], Río Iró (Chocó) [4], Condoto (Chocó) [4], La Victoria (ANM) (Amazonas) [4], Briceño (Antioquia) [4], La Salina (Casanare) [4], Montecristo (Bolívar) [4] and 107 more.
- extreme (146 municipalities): Argelia (Cauca) [10], Puerto Asís (Putumayo) [8], Cartagena del Chairá (Caquetá) [8], Barbacoas (Nariño) [8], Uribe (Meta) [8], San Vicente del Caguán (Caquetá) [6], Planadas (Tolima) [6], Arauquita (Arauca) [6], Curillo (Caquetá) [6], La Montañita (Caquetá) [6], Solita (Caquetá) [6], El Tambo (Cauca) [6] and 134 more.

**PeriodRates.cnmh_recruitment_of_children_and_adolescents_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (96 municipalities): Anorí (Antioquia) [4], Morichal (ANM) (Guainía) [4], Solano (Caquetá) [4], Puerto Rondón (Arauca) [4], La Salina (Casanare) [4], Sácama (Casanare) [4], Condoto (Chocó) [4], Medio Atrato (Chocó) [4], Morales (Bolívar) [4], La Victoria (ANM) (Amazonas) [4], Río Iró (Chocó) [4], Murindó (Antioquia) [4] and 84 more.
- extreme (156 municipalities): San Vicente del Caguán (Caquetá) [8], Argelia (Cauca) [8], Cartagena del Chairá (Caquetá) [8], El Bagre (Antioquia) [8], Barbacoas (Nariño) [8], Uribe (Meta) [8], Arauquita (Arauca) [6], Puerto Rico (Meta) [6], Apartadó (Antioquia) [6], Vistahermosa (Meta) [6], La Montañita (Caquetá) [6], Chaparral (Tolima) [6] and 144 more.

**PeriodRates.cnmh_selective_killing_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (46 municipalities): Briceño (Antioquia) [5], Puerto Rondón (Arauca) [5], Toledo (Antioquia) [4], Sácama (Casanare) [4], Cravo Norte (Arauca) [3], Lloró (Chocó) [3], Bahía Solano (Chocó) [3], Mesetas (Meta) [3], Elías (Huila) [2], Mallama (Nariño) [2], Puerto Santander (Norte De Santander) [2], Pijao (Quindío) [2] and 34 more.
- extreme (326 municipalities): Corinto (Cauca) [13], Tame (Arauca) [13], San Andrés de Tumaco (Nariño) [13], San Pablo (Bolívar) [12], Tibú (Norte De Santander) [12], Ituango (Antioquia) [12], Barrancabermeja (Santander) [11], Algeciras (Huila) [11], Saravena (Arauca) [11], Puerto Berrío (Antioquia) [11], Valle del Guamuez (Putumayo) [11], Fortul (Arauca) [11] and 314 more.

**PeriodRates.cnmh_selective_killing_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (39 municipalities): Puerto Rondón (Arauca) [5], Baraya (Huila) [3], Cravo Norte (Arauca) [3], Albania (Caquetá) [2], Juradó (Chocó) [2], California (Santander) [2], Elías (Huila) [2], Hobo (Huila) [2], Solita (Caquetá) [2], Policarpa (Nariño) [2], Paya (Boyacá) [2], Norcasia (Caldas) [2] and 27 more.
- extreme (361 municipalities): Tame (Arauca) [13], Corinto (Cauca) [13], San Andrés de Tumaco (Nariño) [13], Remedios (Antioquia) [12], Puerto Asís (Putumayo) [12], Algeciras (Huila) [12], San Pablo (Bolívar) [12], Ituango (Antioquia) [12], San José del Guaviare (Guaviare) [12], Tibú (Norte De Santander) [12], Barrancabermeja (Santander) [11], Puerto Berrío (Antioquia) [11] and 349 more.

**PeriodRates.cnmh_sexual_violence_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (104 municipalities): El Cantón del San Pablo (Chocó) [5], Curillo (Caquetá) [5], San José del Palmar (Chocó) [5], Río Quito (Chocó) [4], La Tola (Nariño) [4], Miraflores (Guaviare) [4], Teorama (Norte De Santander) [3], Norosí (Bolívar) [3], Roberto Payán (Nariño) [3], La Llanada (Nariño) [3], Lloró (Chocó) [3], Nóvita (Chocó) [3] and 92 more.
- extreme (182 municipalities): Tarazá (Antioquia) [11], Barbacoas (Nariño) [10], Valle del Guamuez (Putumayo) [10], San Miguel (Putumayo) [10], Policarpa (Nariño) [10], Quibdó (Chocó) [9], San Vicente del Caguán (Caquetá) [9], Buenaventura (Valle Del Cauca) [9], Medio Atrato (Chocó) [9], San Andrés de Tumaco (Nariño) [9], Riosucio (Chocó) [8], Cumbitara (Nariño) [8] and 170 more.

**PeriodRates.cnmh_sexual_violence_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (83 municipalities): El Cantón del San Pablo (Chocó) [4], Dolores (Tolima) [3], San José del Palmar (Chocó) [3], La Llanada (Nariño) [3], Mosquera (Nariño) [3], Norosí (Bolívar) [3], Curillo (Caquetá) [3], San Andrés de Cuerquía (Antioquia) [3], Roncesvalles (Tolima) [2], Río Iró (Chocó) [2], Puerto Santander (ANM) (Amazonas) [2], Sipí (Chocó) [2] and 71 more.
- extreme (199 municipalities): Barbacoas (Nariño) [11], Tarazá (Antioquia) [11], Valle del Guamuez (Putumayo) [11], San Miguel (Putumayo) [10], Policarpa (Nariño) [10], Dibulla (La Guajira) [9], San Andrés de Tumaco (Nariño) [9], Medio Atrato (Chocó) [9], Quibdó (Chocó) [9], Buenaventura (Valle Del Cauca) [9], San Vicente del Caguán (Caquetá) [9], Riosucio (Chocó) [8] and 187 more.

**PeriodRates.cnmh_terrorist_attack_events**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (75 municipalities): Florida (Valle Del Cauca) [4], Calamar (Guaviare) [4], Ituango (Antioquia) [4], Inzá (Cauca) [4], Puerto Asís (Putumayo) [4], Patía (Cauca) [4], Corinto (Cauca) [4], Arauquita (Arauca) [4], El Zulia (Norte De Santander) [4], Miranda (Cauca) [4], Timbiquí (Cauca) [4], Tibú (Norte De Santander) [4] and 63 more.
- extreme (19 municipalities): Argelia (Cauca) [6], Balboa (Cauca) [4], Cáceres (Antioquia) [2], El Tarra (Norte De Santander) [2], Saravena (Arauca) [2], Fortul (Arauca) [2], Arauca (Arauca) [2], Riofrío (Valle Del Cauca) [2], Jamundí (Valle Del Cauca) [2], Buenaventura (Valle Del Cauca) [2], Samaniego (Nariño) [2], San Andrés de Tumaco (Nariño) [2] and 7 more.

**PeriodRates.cnmh_terrorist_attack_victims**

- missing (6 municipalities): Nuevo Belén de Bajirá (Chocó) [4], Norosí (Bolívar) [2], Guachené (Cauca) [2], San José de Uré (Córdoba) [2], Tuchín (Córdoba) [2], Mapiripana (ANM) (Guainía) [2].
- small_base (20 municipalities): San Rafael (Antioquia) [4], Patía (Cauca) [4], Taminango (Nariño) [2], Valle del Guamuez (Putumayo) [2], Puerto Asís (Putumayo) [2], Tame (Arauca) [2], Saravena (Arauca) [2], Jamundí (Valle Del Cauca) [2], El Zulia (Norte De Santander) [2], Túquerres (Nariño) [2], Santa Bárbara (Nariño) [2], El Paujíl (Caquetá) [2] and 8 more.
- extreme (36 municipalities): Bogotá, D.C. (Bogotá, D.C.) [4], Apartadó (Antioquia) [2], San Calixto (Norte De Santander) [2], Puerto Rico (Meta) [2], Vistahermosa (Meta) [2], Roberto Payán (Nariño) [2], San Andrés de Tumaco (Nariño) [2], San José de Cúcuta (Norte De Santander) [2], Convención (Norte De Santander) [2], Tibú (Norte De Santander) [2], Neiva (Huila) [2], Buenaventura (Valle Del Cauca) [2] and 24 more.

## INDEPAZ

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| PeriodRates | indepaz_massacre_events | 0 | 6 | 0 | 0 | 180 | 54 |
| PeriodRates | indepaz_massacre_victims | 0 | 6 | 0 | 0 | 34 | 250 |

**PeriodRates.indepaz_massacre_events**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (80 municipalities): Solano (Caquetá) [4], El Retorno (Guaviare) [4], Policarpa (Nariño) [4], Mallama (Nariño) [4], Ciudad Bolívar (Antioquia) [4], Piamonte (Cauca) [4], El Águila (Valle Del Cauca) [4], Puerto Rondón (Arauca) [4], San José del Fragua (Caquetá) [4], Venecia (Antioquia) [4], Leiva (Nariño) [2], Roberto Payán (Nariño) [2] and 68 more.
- extreme (25 municipalities): Santander de Quilichao (Cauca) [4], Balboa (Cauca) [4], Betania (Antioquia) [2], Puerto Leguízamo (Putumayo) [2], Toro (Valle Del Cauca) [2], Guadalajara de Buga (Valle Del Cauca) [2], Ansermanuevo (Valle Del Cauca) [2], Ábrego (Norte De Santander) [2], San José de Cúcuta (Norte De Santander) [2], San Andrés de Tumaco (Nariño) [2], Samaniego (Nariño) [2], Puerto Gaitán (Meta) [2] and 13 more.

**PeriodRates.indepaz_massacre_victims**

- missing (2 municipalities): Nuevo Belén de Bajirá (Chocó), government:duque: no population behind the rate; Nuevo Belén de Bajirá (Chocó), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:duque: no population behind the rate; Mapiripana (ANM) (Guainía), government:petro: no population behind the rate; Mapiripana (ANM) (Guainía), phase:duque: no population behind the rate; Mapiripana (ANM) (Guainía), phase:petro: no population behind the rate.
- small_base (17 municipalities): Angostura (Antioquia) [2], Medio San Juan (Chocó) [2], La Playa (Norte De Santander) [2], El Carmen (Norte De Santander) [2], Mallama (Nariño) [2], La Florida (Nariño) [2], Guamal (Meta) [2], Palestina (Huila) [2], Lloró (Chocó) [2], Venecia (Antioquia) [2], San Antonio del Tequendama (Cundinamarca) [2], Agua de Dios (Cundinamarca) [2] and 5 more.
- extreme (110 municipalities): Ábrego (Norte De Santander) [4], Policarpa (Nariño) [4], Piamonte (Cauca) [4], Santander de Quilichao (Cauca) [4], Balboa (Cauca) [4], Puerto Rondón (Arauca) [4], El Águila (Valle Del Cauca) [4], Mercaderes (Cauca) [4], Guadalajara de Buga (Valle Del Cauca) [4], Jamundí (Valle Del Cauca) [4], Ciudad Bolívar (Antioquia) [4], Tibú (Norte De Santander) [4] and 98 more.

## Medicina Legal

| Table | Column | error | missing | inconsistent | break | small_base | extreme |
|---|---|---:|---:|---:|---:|---:|---:|
| ViolenceCases | domestic_violence | 0 | 0 | 0 | 0 | 0 | 32 |
| ViolenceCases | homicide | 0 | 2 | 0 | 0 | 0 | 62 |
| ViolenceCases | partner_violence | 0 | 0 | 0 | 0 | 0 | 33 |
| ViolenceCases | sexual_violence | 0 | 0 | 0 | 0 | 0 | 85 |
| ViolenceCases | suicide | 0 | 0 | 0 | 0 | 10 | 69 |
| ViolenceCases | violence_children | 0 | 0 | 0 | 0 | 0 | 4 |

**ViolenceCases.domestic_violence**

- extreme (14 municipalities): Uribia (La Guajira) [9], Manaure (La Guajira) [5], Tierralta (Córdoba) [3], El Tambo (Cauca) [2], Páez (Cauca) [2], Piendamó - Tunía (Cauca) [2], Mitú (Vaupés) [2], Bolívar (Cauca) [1], Planeta Rica (Córdoba) [1], San Marcos (Sucre) [1], San José del Guaviare (Guaviare) [1], Puerto Carreño (Vichada) [1] and 2 more.

**ViolenceCases.homicide**

- missing (1 municipalities): Mapiripana (ANM) (Guainía), 2020: no population behind the rate; Mapiripana (ANM) (Guainía), 2025: no population behind the rate.
- extreme (41 municipalities): Puerto Santander (Norte De Santander) [4], Tarazá (Antioquia) [4], Argelia (Cauca) [3], Puerto Rondón (Arauca) [3], Briceño (Antioquia) [3], Uribia (La Guajira) [2], Corinto (Cauca) [2], Tibú (Norte De Santander) [2], Valdivia (Antioquia) [2], San José del Palmar (Chocó) [2], Segovia (Antioquia) [2], Ituango (Antioquia) [2] and 29 more.

**ViolenceCases.partner_violence**

- extreme (11 municipalities): Uribia (La Guajira) [11], Manaure (La Guajira) [6], Cumaribo (Vichada) [4], Tierralta (Córdoba) [3], Páez (Cauca) [2], Barbacoas (Nariño) [2], Bolívar (Cauca) [1], Inzá (Cauca) [1], Silvia (Cauca) [1], Riosucio (Chocó) [1], Mitú (Vaupés) [1].

**ViolenceCases.sexual_violence**

- extreme (44 municipalities): Cumaribo (Vichada) [10], San Andrés de Tumaco (Nariño) [5], Barbacoas (Nariño) [5], Riosucio (Chocó) [5], Uribia (La Guajira) [4], Toribío (Cauca) [4], Páez (Cauca) [3], Puerto Carreño (Vichada) [3], Ipiales (Nariño) [3], Manaure (La Guajira) [3], Morales (Cauca) [2], Inzá (Cauca) [2] and 32 more.

**ViolenceCases.suicide**

- small_base (7 municipalities): Sativasur (Boyacá) [4], Panqueba (Boyacá) [1], Sativanorte (Boyacá) [1], Lourdes (Norte De Santander) [1], Cabrera (Santander) [1], Jordán (Santander) [1], Vetas (Santander) [1].
- extreme (51 municipalities): Mitú (Vaupés) [7], Cumaribo (Vichada) [4], Soledad (Atlántico) [4], San Andrés (Archipiélago De San Andrés, Providencia Y Santa Catalina) [3], Uribia (La Guajira) [3], Carurú (Vaupés) [2], Maicao (La Guajira) [2], Montería (Córdoba) [1], Cereté (Córdoba) [1], Pueblo Rico (Risaralda) [1], Floridablanca (Santander) [1], San Miguel (Santander) [1] and 39 more.

**ViolenceCases.violence_children**

- extreme (4 municipalities): Guarne (Antioquia) [1], Cachipay (Cundinamarca) [1], Cucunubá (Cundinamarca) [1], Arauca (Arauca) [1].
