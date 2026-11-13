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

**Population.population**

- missing (56 municipalities): Mapiripana (ANM) (Guainía) [23], Norosí (Bolívar) [13], Tuchín (Córdoba) [13], San José de Uré (Córdoba) [13], Guachené (Cauca) [12], Coveñas (Sucre) [7], Medio San Juan (Chocó) [6], Nuevo Belén de Bajirá (Chocó) [6], Río Iró (Chocó) [6], Carmen del Darién (Chocó) [6], Nueva Granada (Magdalena) [5], Cértegui (Chocó) [5] and 44 more.
- break (37 municipalities): Río Quito (Chocó) [3], Istmina (Chocó) [2], Carmen del Darién (Chocó) [2], Río Viejo (Bolívar) [2], Santa Ana (Magdalena) [2], Medio Atrato (Chocó) [2], Ciénaga (Magdalena) [1], Riosucio (Chocó) [1], Tadó (Chocó) [1], Aracataca (Magdalena) [1], Cerro de San Antonio (Magdalena) [1], Santa Bárbara (Antioquia) [1] and 25 more.

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
| EnrolmentAndDropout | approval | 0 | 0 | 0 | 4 | 0 | 300 |
| EnrolmentAndDropout | dropout | 0 | 0 | 0 | 0 | 0 | 35 |
| EnrolmentAndDropout | dropout_upper_secondary | 0 | 0 | 0 | 59 | 0 | 40 |
| EnrolmentAndDropout | net_enrolment | 0 | 0 | 2,190 | 453 | 0 | 226 |
| EnrolmentAndDropout | net_enrolment_upper_secondary | 0 | 0 | 31 | 191 | 0 | 252 |
| EnrolmentAndDropout | repetition | 0 | 0 | 0 | 1 | 0 | 191 |

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
