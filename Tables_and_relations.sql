-- =====================================================================================================
-- Violence and education in Colombia: data model
--
-- Frame
--   The Saber 11 exam is read as an operator: it translates years of a student's life into a number
--   that universities, scholarships and credits know how to read, and in some places that number opens
--   a door and in others it does not. Violence is followed as a material effect (a closed road, a mine
--   on the way to school, a recruitment, a confinement, a massacre) that opens or closes those doors.
--   Nothing is assumed to explain anything in advance: the model records the associations so they can
--   be described (symmetric sociology); structure, class and power are what the description may arrive
--   at, not where it starts.
--
--   Galtung's typology is the map's legend, a way of classifying harm, not a cause:
--     physical  - homicide, suicide, intra-family violence, conflict events
--     cultural  - violence that targets an identity (ethnic, vulnerable group, socio-political)
--     gender    - partner and sexual violence, homicide and suicide of women
--     structural- avoidable deprivation (census 2018) and access to school and health
--   Each index is a geometric mean of sub-indices between fixed goalposts, as in the UNDP Human
--   Development Index. Indices are one more inscription on the map, never the explanation.
--
--   Two levels:
--     municipality - everything from external sources (Medicina Legal, Police, CNMH, INDEPAZ, DANE,
--                    MEN, MinSalud). Nothing the students report enters an index.
--     student      - each Saber 11 exam taker: scores and what the student reports about home and
--                    family (Student_Context), set beside what DANE says of the same municipality.
--                    Only those who reached grade 11 sit the exam: the gap measures who did not.
--
--   Time: every dated fact can be placed in a government (Uribe I to Petro) and in a phase of it.
--
-- Keys
--   Municipalities.id is the DANE code as a number (5001 = Medellin): '5001' and '05001' are the same
--   key. Names never join anything.
-- =====================================================================================================

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `Phisical_violence`;           -- old misspelled name
DROP SCHEMA IF EXISTS `RelationsAndConclusions`;
DROP SCHEMA IF EXISTS `Physical_violence`;
DROP SCHEMA IF EXISTS `Structural_Violence`;
DROP SCHEMA IF EXISTS `Cultural_violence`;
DROP SCHEMA IF EXISTS `GENDER_VIOLENCE`;
DROP SCHEMA IF EXISTS `Student_Context`;
DROP SCHEMA IF EXISTS `Education_Outcomes`;

CREATE SCHEMA `RelationsAndConclusions` DEFAULT CHARACTER SET utf8mb4;   -- place, population, time, sources, final index
CREATE SCHEMA `Physical_violence`       DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Structural_Violence`     DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Cultural_violence`       DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `GENDER_VIOLENCE`         DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Student_Context`         DEFAULT CHARACTER SET utf8mb4;   -- what students report; never in an index
CREATE SCHEMA `Education_Outcomes`      DEFAULT CHARACTER SET utf8mb4;   -- Saber 11, Saber Pro, MEN, scholarships


-- =====================================================================================================
-- RelationsAndConclusions: place, population, time, sources
-- =====================================================================================================

CREATE TABLE `RelationsAndConclusions`.`Departments` (
    `id`   INT          NOT NULL PRIMARY KEY,            -- DANE department code (5 = Antioquia)
    `name` VARCHAR(100) NOT NULL
);

CREATE TABLE `RelationsAndConclusions`.`Municipalities` (
    `id`            INT          NOT NULL PRIMARY KEY,   -- DANE municipality code (5001 = Medellin)
    `name`          VARCHAR(100) NOT NULL,
    `department_id` INT          NOT NULL,
    FOREIGN KEY (`department_id`) REFERENCES `RelationsAndConclusions`.`Departments` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`Sexes` (
    `id`   CHAR(1)     NOT NULL PRIMARY KEY,             -- F, M, U (unknown / not reported / total)
    `name` VARCHAR(20) NOT NULL
);

CREATE TABLE `RelationsAndConclusions`.`Population` (     -- DANE, mid-year, all areas, 1995-2042
    `municipality_id` INT  NOT NULL,
    `year`            YEAR NOT NULL,
    `population`      INT  NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`PopulationBySexAge` (   -- 5-year bands, single ages 15-19 (the exam cohort)
    `municipality_id` INT     NOT NULL,
    `year`            YEAR    NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,
    `age_from`        TINYINT NOT NULL,
    `age_to`          TINYINT NULL,                      -- NULL = and over (80+)
    `population`      INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `sex_id`, `age_from`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`Governments` (
    `id`         INT          NOT NULL PRIMARY KEY,
    `code`       VARCHAR(30)  NOT NULL UNIQUE,           -- uribe_1, uribe_2, santos_1, santos_2, duque, petro
    `president`  VARCHAR(100) NOT NULL,
    `start_date` DATE         NOT NULL,                  -- terms start on 7 August
    `end_date`   DATE         NOT NULL                   -- exclusive
);

CREATE TABLE `RelationsAndConclusions`.`Government_Phases` (
    `id`            INT          NOT NULL PRIMARY KEY,
    `government_id` INT          NOT NULL,
    `code`          VARCHAR(40)  NOT NULL UNIQUE,
    `description`   VARCHAR(255) NULL,
    `start_date`    DATE         NOT NULL,
    `end_date`      DATE         NOT NULL,
    FOREIGN KEY (`government_id`) REFERENCES `RelationsAndConclusions`.`Governments` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`Sources` (
    `id`            INT          NOT NULL PRIMARY KEY,
    `code`          VARCHAR(40)  NOT NULL UNIQUE,        -- medicina_legal, police, cnmh, indepaz, dane, icfes, men, minsalud, icetex
    `institution`   VARCHAR(200) NOT NULL,
    `kind`          ENUM('official_record', 'memory_observatory', 'press_based', 'census', 'administrative') NOT NULL,
    `url`           VARCHAR(255) NULL,
    `description`   VARCHAR(500) NULL
);

CREATE TABLE `RelationsAndConclusions`.`SourceDatasets` (   -- each dataset read, with what it covers
    `id`            INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `source_id`     INT          NOT NULL,
    `dataset`       VARCHAR(80)  NOT NULL UNIQUE,        -- datos.gov.co id, file or page
    `description`   VARCHAR(255) NULL,
    `coverage_from` DATE         NULL,
    `coverage_to`   DATE         NULL,
    `preliminary`   TINYINT(1)   NOT NULL DEFAULT 0,
    FOREIGN KEY (`source_id`) REFERENCES `RelationsAndConclusions`.`Sources` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`ViolenceIndicators` (
    `id`          INT          NOT NULL PRIMARY KEY,
    `code`        VARCHAR(40)  NOT NULL UNIQUE,
    `dimension`   ENUM('physical', 'cultural', 'gender') NOT NULL,
    `description` VARCHAR(255) NULL
);

-- Medicina Legal: cases per municipality, year, indicator and victim's sex
CREATE TABLE `RelationsAndConclusions`.`ViolenceCases` (
    `municipality_id` INT     NOT NULL,
    `year`            YEAR    NOT NULL,
    `indicator_id`    INT     NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,
    `dataset_id`      INT     NOT NULL,
    `cases`           INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `indicator_id`, `sex_id`, `dataset_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_id`)    REFERENCES `RelationsAndConclusions`.`ViolenceIndicators` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`),
    FOREIGN KEY (`dataset_id`)      REFERENCES `RelationsAndConclusions`.`SourceDatasets` (`id`)
);

-- Police: cases per municipality and day (so every case falls in its exact government)
CREATE TABLE `RelationsAndConclusions`.`PoliceDailyCases` (
    `municipality_id` INT     NOT NULL,
    `day`             DATE    NOT NULL,
    `indicator_id`    INT     NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,
    `cases`           INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `day`, `indicator_id`, `sex_id`),
    KEY `by_day` (`day`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_id`)    REFERENCES `RelationsAndConclusions`.`ViolenceIndicators` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

-- Rates per government or phase: cases over the person-years the source covers in that period
CREATE TABLE `RelationsAndConclusions`.`PeriodRates` (
    `municipality_id` INT          NOT NULL,
    `period_kind`     ENUM('government', 'phase') NOT NULL,
    `period_code`     VARCHAR(40)  NOT NULL,
    `measure`         VARCHAR(60)  NOT NULL,             -- police_homicide, cnmh_massacre_victims, ...
    `cases`           DOUBLE       NOT NULL,
    `person_years`    DOUBLE       NOT NULL,
    `rate_per_100k`   DOUBLE       NULL,
    PRIMARY KEY (`municipality_id`, `period_kind`, `period_code`, `measure`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

-- Final index: geometric mean of the dimension indices
CREATE TABLE `RelationsAndConclusions`.`FinalViolenceIndex` (
    `municipality_id`      INT   NOT NULL,
    `year`                 YEAR  NOT NULL,
    `physical_index`       FLOAT NULL,
    `cultural_index`       FLOAT NULL,
    `gender_index`         FLOAT NULL,
    `structural_index`     FLOAT NULL,               -- census 2018: the same every year
    `final_violence_index` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Physical_violence: events (CNMH, INDEPAZ, Police massacres), their links, and the physical index
-- =====================================================================================================

CREATE TABLE `Physical_violence`.`EventModalities` (
    `code` CHAR(2)      NOT NULL PRIMARY KEY,            -- MA massacre, AS selective killing, DF forced disappearance, ...
    `name` VARCHAR(100) NOT NULL
);

CREATE TABLE `Physical_violence`.`Perpetrators` (
    `id`   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(150) NOT NULL UNIQUE                  -- as the source writes it: GRUPO PARAMILITAR, GUERRILLA, ...
);

CREATE TABLE `Physical_violence`.`ViolenceEvents` (
    `id`               INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `dataset_id`       INT          NOT NULL,
    `source_event_id`  VARCHAR(60)  NOT NULL,
    `modality_code`    CHAR(2)      NOT NULL,
    `day`              DATE         NULL,
    `date_precision`   ENUM('day', 'month', 'year') NULL,
    `municipality_id`  INT          NULL,
    `victims`          FLOAT        NULL,
    `perpetrator_id`   INT          NULL,
    `displacement`     FLOAT        NULL,                -- simultaneous facts recorded by CNMH
    `confinement`      FLOAT        NULL,
    `massacre_cluster` VARCHAR(60)  NULL,                -- same value = the same massacre in several sources
    UNIQUE (`dataset_id`, `source_event_id`),
    KEY `by_place_day` (`municipality_id`, `day`),
    FOREIGN KEY (`dataset_id`)      REFERENCES `RelationsAndConclusions`.`SourceDatasets` (`id`),
    FOREIGN KEY (`modality_code`)   REFERENCES `Physical_violence`.`EventModalities` (`code`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`perpetrator_id`)  REFERENCES `Physical_violence`.`Perpetrators` (`id`)
);

CREATE TABLE `Physical_violence`.`EventLinks` (           -- triangulation: same municipality, <= 3 days (15 if month only)
    `event_a_id` INT NOT NULL,
    `event_b_id` INT NOT NULL,
    `day_gap`    INT NOT NULL,
    PRIMARY KEY (`event_a_id`, `event_b_id`),
    FOREIGN KEY (`event_a_id`) REFERENCES `Physical_violence`.`ViolenceEvents` (`id`),
    FOREIGN KEY (`event_b_id`) REFERENCES `Physical_violence`.`ViolenceEvents` (`id`)
);

CREATE TABLE `Physical_violence`.`PhysicalViolenceIndex` (
    `municipality_id`         INT   NOT NULL,
    `year`                    YEAR  NOT NULL,
    `subin_homicide`          FLOAT NULL,
    `subin_suicide`           FLOAT NULL,
    `subin_violence_children` FLOAT NULL,
    `subin_domestic_violence` FLOAT NULL,                -- other relatives and older adults
    `physical_violence_index` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Cultural_violence: violence that targets an identity
-- =====================================================================================================

CREATE TABLE `Cultural_violence`.`IdentityGroups` (
    `id`   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `kind` ENUM('racial_ancestry', 'vulnerable_group', 'indigenous_people', 'sexual_orientation',
                'gender_identity', 'circumstance') NOT NULL,
    `name` VARCHAR(200) NOT NULL,
    UNIQUE (`kind`, `name`)
);

CREATE TABLE `Cultural_violence`.`IdentityViolenceCases` (    -- Medicina Legal, homicides and suicides
    `municipality_id`   INT  NOT NULL,
    `year`              YEAR NOT NULL,
    `indicator_id`      INT  NOT NULL,
    `identity_group_id` INT  NOT NULL,
    `preliminary`       TINYINT(1) NOT NULL,
    `cases`             INT  NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `indicator_id`, `identity_group_id`),
    FOREIGN KEY (`municipality_id`)   REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_id`)      REFERENCES `RelationsAndConclusions`.`ViolenceIndicators` (`id`),
    FOREIGN KEY (`identity_group_id`) REFERENCES `Cultural_violence`.`IdentityGroups` (`id`)
);

CREATE TABLE `Cultural_violence`.`CulturalViolenceIndex` (
    `municipality_id`                  INT   NOT NULL,
    `year`                             YEAR  NOT NULL,
    `subin_ethnic_homicide`            FLOAT NULL,       -- victims of Black, Indigenous or Mulatto ancestry
    `subin_vulnerable_group_homicide`  FLOAT NULL,       -- victims from a vulnerable group
    `subin_sociopolitical_homicide`    FLOAT NULL,       -- political killing, socio-political violence, armed confrontation
    `cultural_violence_index`          FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- GENDER_VIOLENCE
-- =====================================================================================================

CREATE TABLE `GENDER_VIOLENCE`.`GenderViolenceIndex` (
    `municipality_id`        INT   NOT NULL,
    `year`                   YEAR  NOT NULL,
    `subin_partner_violence` FLOAT NULL,                 -- per 100,000 inhabitants
    `subin_sexual_violence`  FLOAT NULL,
    `subin_female_homicide`  FLOAT NULL,                 -- per 100,000 women
    `subin_female_suicide`   FLOAT NULL,
    `gender_violence_index`  FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Structural_Violence: avoidable deprivation (census 2018) and access
-- =====================================================================================================

CREATE TABLE `Structural_Violence`.`Census2018Municipal` (      -- DANE CNPV 2018; IPM (census source) and NBI
    `municipality_id`                       INT   NOT NULL PRIMARY KEY,
    `ipm`                                   FLOAT NULL,     -- % of people in multidimensional poverty
    `dep_illiteracy`                        FLOAT NULL,     -- % of people in households with each deprivation
    `dep_low_educational_attainment`        FLOAT NULL,
    `dep_early_childhood_care_barriers`     FLOAT NULL,
    `dep_health_access_barriers`            FLOAT NULL,
    `dep_dependency_rate`                   FLOAT NULL,
    `dep_critical_overcrowding`             FLOAT NULL,
    `dep_inadequate_excreta_disposal`       FLOAT NULL,
    `dep_school_non_attendance`             FLOAT NULL,
    `dep_inadequate_wall_material`          FLOAT NULL,
    `dep_inadequate_floor_material`         FLOAT NULL,
    `dep_school_lag`                        FLOAT NULL,
    `dep_no_improved_water`                 FLOAT NULL,
    `dep_no_health_insurance`               FLOAT NULL,
    `dep_child_labour`                      FLOAT NULL,
    `dep_informal_work`                     FLOAT NULL,
    `nbi`                                   FLOAT NULL,     -- % of people with unsatisfied basic needs
    `nbi_misery`                            FLOAT NULL,
    `nbi_housing`                           FLOAT NULL,
    `nbi_services`                          FLOAT NULL,
    `nbi_overcrowding`                      FLOAT NULL,
    `nbi_school_non_attendance`             FLOAT NULL,
    `nbi_economic_dependency`               FLOAT NULL,
    `dwellings_occupied`                    INT   NULL,
    `share_earth_floor`                     FLOAT NULL,     -- shares of occupied dwellings (0-1)
    `share_electricity`                     FLOAT NULL,
    `share_water`                           FLOAT NULL,
    `share_sewer`                           FLOAT NULL,
    `share_gas`                             FLOAT NULL,
    `share_garbage`                         FLOAT NULL,
    `share_internet`                        FLOAT NULL,
    `share_stratum_1`                       FLOAT NULL,     -- shares of people by energy stratum (0-1)
    `share_stratum_2`                       FLOAT NULL,
    `share_stratum_3`                       FLOAT NULL,
    `share_stratum_4`                       FLOAT NULL,
    `share_stratum_5`                       FLOAT NULL,
    `share_stratum_6`                       FLOAT NULL,
    `share_no_electricity_service`          FLOAT NULL,
    `share_stratum_1_2`                     FLOAT NULL,
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`Inequality` (    -- no municipal Gini is published yearly: documented gap, empty
    `municipality_id` INT   NOT NULL,
    `reference_year`  YEAR  NOT NULL,
    `gini_index`      FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `reference_year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`SchoolsByMunicipality` (    -- MEN directory, pre-school to secondary
    `municipality_id` INT          NOT NULL,
    `year`            YEAR         NOT NULL,
    `sector`          VARCHAR(40)  NOT NULL,             -- OFICIAL / NO OFICIAL
    `establishments`  INT          NOT NULL,
    `sites`           INT          NULL,
    `enrolment`       INT          NULL,
    PRIMARY KEY (`municipality_id`, `year`, `sector`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`HealthSites` (               -- MinSalud REPS, latest cut-off
    `municipality_id` INT          NOT NULL,
    `provider_class`  VARCHAR(120) NOT NULL,
    `legal_nature`    VARCHAR(60)  NOT NULL,
    `sites`           INT          NOT NULL,
    PRIMARY KEY (`municipality_id`, `provider_class`, `legal_nature`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`StructuralViolenceIndex` (  -- census 2018 and access
    `municipality_id`           INT   NOT NULL PRIMARY KEY,
    `subin_multidimensional_poverty` FLOAT NULL,
    `subin_unsatisfied_needs`   FLOAT NULL,
    `subin_no_internet`         FLOAT NULL,
    `subin_health_access`       FLOAT NULL,              -- fewer health sites per 100,000 = more deprivation
    `structural_violence_index` FLOAT NULL,
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Education_Outcomes: Saber 11 (both levels), MEN, and the door on the other side
-- =====================================================================================================

CREATE TABLE `Education_Outcomes`.`ExamPeriods` (
    `id`            INT     NOT NULL PRIMARY KEY,        -- ICFES period code: 20102, 20194, 20224 ...
    `year`          YEAR    NOT NULL,
    `calendar`      CHAR(1) NOT NULL,                    -- A (second semester) or B (first semester)
    `scale`         ENUM('pre_2014', 'since_2014_2') NOT NULL,
    `government_id` INT     NULL,                        -- government in office on 1 September of the year
    FOREIGN KEY (`government_id`) REFERENCES `RelationsAndConclusions`.`Governments` (`id`)
);

CREATE TABLE `Education_Outcomes`.`MunicipalScores` (    -- per municipality of the school, period and sex
    `municipality_id`    INT     NOT NULL,
    `exam_period_id`     INT     NOT NULL,
    `sex_id`             CHAR(1) NOT NULL,
    `students`           INT     NOT NULL,
    `mean_global`        FLOAT NULL,                     -- only since 2014-2
    `mean_math`          FLOAT NULL,
    `mean_critical_reading` FLOAT NULL,
    `mean_social`        FLOAT NULL,
    `mean_science`       FLOAT NULL,
    `mean_english`       FLOAT NULL,
    `math_z`             FLOAT NULL,                     -- against the national mean and SD of the period
    `global_z`           FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `exam_period_id`, `sex_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

CREATE TABLE `Education_Outcomes`.`Schools` (            -- one row per school seen in the Saber 11 microdata
    `id`              BIGINT       NOT NULL PRIMARY KEY, -- DANE school code
    `name`            VARCHAR(255) NULL,
    `municipality_id` INT          NULL,
    `sector`          VARCHAR(40)  NULL,
    `area`            VARCHAR(40)  NULL,
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`Students` (           -- one exam taker in one period (DataIcfes microdata)
    `id`              VARCHAR(40) NOT NULL PRIMARY KEY,  -- ICFES estu_consecutivo
    `exam_period_id`  INT         NOT NULL,
    `school_id`       BIGINT      NULL,
    `municipality_id` INT         NULL,                  -- where the school is
    `sex_id`          CHAR(1)     NOT NULL,
    `birth_year`      SMALLINT    NULL,
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

CREATE TABLE `Education_Outcomes`.`StudentScores` (
    `student_id`         VARCHAR(40) NOT NULL PRIMARY KEY,
    `math`               FLOAT NULL,
    `critical_reading`   FLOAT NULL,
    `social_citizenship` FLOAT NULL,
    `natural_sciences`   FLOAT NULL,
    `english`            FLOAT NULL,
    `global_score`       FLOAT NULL,                     -- ICFES's own, weighted, 0-500; only since 2014-2
    `global_mean`        FLOAT NULL,                     -- simple mean of the five tests, every period; NULL if one is missing
    FOREIGN KEY (`student_id`) REFERENCES `Education_Outcomes`.`Students` (`id`)
);

CREATE TABLE `Education_Outcomes`.`MunicipalScoresMicro` (   -- from the microdata, 2000-2022, every period
    `municipality_id` INT   NOT NULL,
    `exam_period_id`  INT   NOT NULL,
    `students`        INT   NOT NULL,
    `mean_math`       FLOAT NULL,
    `math_z`          FLOAT NULL,                        -- against the national mean and SD of the period
    `mean_global`     FLOAT NULL,                        -- ICFES's global score where it exists, else the simple mean
    `global_z`        FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `exam_period_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`)
);

CREATE TABLE `Education_Outcomes`.`EnrolmentAndDropout` (   -- MEN, per municipality and year
    `municipality_id`               INT   NOT NULL,
    `year`                          YEAR  NOT NULL,
    `net_enrolment`                 FLOAT NULL,
    `net_enrolment_upper_secondary` FLOAT NULL,
    `dropout`                       FLOAT NULL,
    `dropout_upper_secondary`       FLOAT NULL,
    `approval`                      FLOAT NULL,
    `repetition`                    FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`SaberProByMunicipality` (    -- by municipality of the school the student finished
    `municipality_id`       INT         NOT NULL,
    `periodo`               INT         NOT NULL,
    `year`                  YEAR        NOT NULL,
    `sex_id`                CHAR(1)     NOT NULL,
    `students`              INT         NOT NULL,
    `quantitative_reasoning` FLOAT NULL,
    `critical_reading`      FLOAT NULL,
    `citizenship`           FLOAT NULL,
    `english`               FLOAT NULL,
    `written_communication` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `periodo`, `sex_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

CREATE TABLE `Education_Outcomes`.`HigherEdEnrolment` (   -- MEN, by municipality where the programme is offered
    `municipality_id` INT     NOT NULL,
    `year`            YEAR    NOT NULL,
    `semester`        TINYINT NOT NULL,
    `sector_id`       TINYINT NOT NULL,
    `level_id`        TINYINT NOT NULL,
    `enrolled`        INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `semester`, `sector_id`, `level_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`GeneracionE` (
    `municipality_id` INT   NOT NULL,
    `cutoff`          DATE  NOT NULL,
    `beneficiaries`   FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `cutoff`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`IcetexCredits` (       -- ICETEX publishes the department of origin only
    `department_id` INT          NOT NULL,
    `year`          YEAR         NOT NULL,
    `sex`           VARCHAR(20)  NOT NULL,
    `level`         VARCHAR(80)  NOT NULL,
    `kind`          ENUM('new', 'renewal') NOT NULL,
    `beneficiaries` INT          NOT NULL,
    PRIMARY KEY (`department_id`, `year`, `sex`, `level`, `kind`),
    FOREIGN KEY (`department_id`) REFERENCES `RelationsAndConclusions`.`Departments` (`id`)
);


-- =====================================================================================================
-- Student_Context: what each student reports (ICFES questionnaire); never in an index
-- =====================================================================================================

CREATE TABLE `Student_Context`.`StudentHousehold` (
    `student_id`            VARCHAR(40)  NOT NULL PRIMARY KEY,
    `stratum`               TINYINT      NULL,           -- 1-6, 0 = none
    `persons_in_household`  VARCHAR(40)  NULL,           -- ICFES reports ranges
    `rooms`                 VARCHAR(40)  NULL,
    `floor_type`            VARCHAR(80)  NULL,
    `has_internet`          TINYINT(1)   NULL,
    `has_computer`          TINYINT(1)   NULL,
    `has_car`               TINYINT(1)   NULL,
    `has_washing_machine`   TINYINT(1)   NULL,
    `mother_education`      VARCHAR(100) NULL,
    `father_education`      VARCHAR(100) NULL,
    `ethnic_group`          VARCHAR(80)  NULL,
    `work_hours_per_week`   VARCHAR(40)  NULL,
    FOREIGN KEY (`student_id`) REFERENCES `Education_Outcomes`.`Students` (`id`)
);

CREATE TABLE `Student_Context`.`StudentPractices` (       -- reading, books at home, internet use
    `student_id`             VARCHAR(40) NOT NULL PRIMARY KEY,
    `books_at_home`          VARCHAR(40) NULL,
    `reading_for_pleasure`   VARCHAR(40) NULL,
    `internet_hours_per_day` VARCHAR(40) NULL,
    FOREIGN KEY (`student_id`) REFERENCES `Education_Outcomes`.`Students` (`id`)
);

CREATE TABLE `Student_Context`.`MunicipalStudentContext` (  -- what a municipality's exam takers report
    `municipality_id`          INT   NOT NULL,
    `exam_period_id`           INT   NOT NULL,
    `students`                 INT   NOT NULL,
    `share_internet`           FLOAT NULL,
    `share_computer`           FLOAT NULL,
    `share_car`                FLOAT NULL,
    `share_washing_machine`    FLOAT NULL,
    `share_stratum_1_2`        FLOAT NULL,
    `share_mother_higher_ed`   FLOAT NULL,
    `share_mother_primary_or_less` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `exam_period_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`)
);


-- =====================================================================================================
-- Views
-- =====================================================================================================

CREATE VIEW `RelationsAndConclusions`.`ViolenceRates` AS
SELECT vc.`municipality_id`, vc.`year`, vi.`code` AS `indicator`, vi.`dimension`,
       SUM(vc.`cases`) AS `cases`, p.`population`,
       SUM(vc.`cases`) / p.`population` * 100000 AS `rate_per_100k`
FROM `RelationsAndConclusions`.`ViolenceCases` vc
JOIN `RelationsAndConclusions`.`ViolenceIndicators` vi ON vi.`id` = vc.`indicator_id`
JOIN `RelationsAndConclusions`.`Population` p ON p.`municipality_id` = vc.`municipality_id` AND p.`year` = vc.`year`
GROUP BY vc.`municipality_id`, vc.`year`, vi.`code`, vi.`dimension`, p.`population`;

CREATE VIEW `RelationsAndConclusions`.`EventsByGovernment` AS
SELECT e.`municipality_id`, g.`code` AS `government`, e.`modality_code`, sd.`dataset`,
       COUNT(*) AS `events`, SUM(e.`victims`) AS `victims`
FROM `Physical_violence`.`ViolenceEvents` e
JOIN `RelationsAndConclusions`.`SourceDatasets` sd ON sd.`id` = e.`dataset_id`
JOIN `RelationsAndConclusions`.`Governments` g ON e.`day` >= g.`start_date` AND e.`day` < g.`end_date`
GROUP BY e.`municipality_id`, g.`code`, e.`modality_code`, sd.`dataset`;

CREATE VIEW `Student_Context`.`StudentsVersusCensus` AS    -- exam takers 2019 against the census 2018
SELECT c.`municipality_id`, sc.`exam_period_id`, sc.`students`,
       sc.`share_internet`    AS `students_internet`,    c.`share_internet`    AS `census_internet`,
       sc.`share_stratum_1_2` AS `students_stratum_1_2`, c.`share_stratum_1_2` AS `census_stratum_1_2`
FROM `Student_Context`.`MunicipalStudentContext` sc
JOIN `Structural_Violence`.`Census2018Municipal` c ON c.`municipality_id` = sc.`municipality_id`;


-- =====================================================================================================
-- Reference rows
-- =====================================================================================================

INSERT INTO `RelationsAndConclusions`.`Sexes` VALUES ('F', 'Female'), ('M', 'Male'), ('U', 'Unknown / total');

INSERT INTO `RelationsAndConclusions`.`Governments` VALUES
    (1, 'uribe_1',  'Alvaro Uribe Velez (I)',  '2002-08-07', '2006-08-07'),
    (2, 'uribe_2',  'Alvaro Uribe Velez (II)', '2006-08-07', '2010-08-07'),
    (3, 'santos_1', 'Juan Manuel Santos (I)',  '2010-08-07', '2014-08-07'),
    (4, 'santos_2', 'Juan Manuel Santos (II)', '2014-08-07', '2018-08-07'),
    (5, 'duque',    'Ivan Duque Marquez',      '2018-08-07', '2022-08-07'),
    (6, 'petro',    'Gustavo Petro Urrego',    '2022-08-07', '2026-08-07');

INSERT INTO `RelationsAndConclusions`.`Government_Phases` VALUES
    (1, 1, 'uribe_1',  NULL, '2002-08-07', '2006-08-07'),
    (2, 2, 'uribe_2',  NULL, '2006-08-07', '2010-08-07'),
    (3, 3, 'santos_1', NULL, '2010-08-07', '2014-08-07'),
    (4, 4, 'santos_2_negotiation',    'Havana talks until the final agreement', '2014-08-07', '2016-11-24'),
    (5, 4, 'santos_2_implementation', 'From the final agreement (24 Nov 2016)', '2016-11-24', '2018-08-07'),
    (6, 5, 'duque',    NULL, '2018-08-07', '2022-08-07'),
    (7, 6, 'petro',    NULL, '2022-08-07', '2026-08-07');

INSERT INTO `RelationsAndConclusions`.`Sources` VALUES
    (1, 'medicina_legal', 'Instituto Nacional de Medicina Legal y Ciencias Forenses', 'official_record', 'https://www.datos.gov.co', 'Forensic records of fatal and non-fatal injuries'),
    (2, 'police', 'Policia Nacional / Ministerio de Defensa', 'official_record', 'https://www.datos.gov.co', 'Crime records (SIEDCO)'),
    (3, 'cnmh', 'Centro Nacional de Memoria Historica, Observatorio de Memoria y Conflicto', 'memory_observatory', 'https://www.datos.gov.co', 'SIEVCAC: armed-conflict events from press, judicial and social-organisation sources'),
    (4, 'indepaz', 'Instituto de Estudios para el Desarrollo y la Paz', 'press_based', 'https://indepaz.org.co/informe-de-masacres-en-colombia-durante-el-2020-2021/', 'Massacre list from press and regional reports'),
    (5, 'dane', 'Departamento Administrativo Nacional de Estadistica', 'census', 'https://www.dane.gov.co', 'Population projections and the 2018 census'),
    (6, 'icfes', 'Instituto Colombiano para la Evaluacion de la Educacion', 'administrative', 'https://www.datos.gov.co', 'Saber 11 and Saber Pro'),
    (7, 'men', 'Ministerio de Educacion Nacional', 'administrative', 'https://www.datos.gov.co', 'Enrolment, dropout, schools, higher education, Generacion E'),
    (8, 'minsalud', 'Ministerio de Salud y Proteccion Social', 'administrative', 'https://www.datos.gov.co', 'REPS health providers'),
    (9, 'icetex', 'Instituto Colombiano de Credito Educativo y Estudios Tecnicos en el Exterior', 'administrative', 'https://www.datos.gov.co', 'Student credits');

INSERT INTO `RelationsAndConclusions`.`ViolenceIndicators` VALUES
    (1,  'homicide',                'physical', 'Homicides'),
    (2,  'suicide',                 'physical', 'Suicides'),
    (3,  'violence_children',       'physical', 'Intra-family violence against children and adolescents'),
    (4,  'domestic_violence',       'physical', 'Intra-family violence (Medicina Legal: other relatives and older adults; Police: all)'),
    (5,  'partner_violence',        'gender',   'Partner violence'),
    (6,  'sexual_violence',         'gender',   'Sexual violence (Medicina Legal examinations; Police offences)'),
    (7,  'sociopolitical_homicide', 'cultural', 'Homicides with a socio-political circumstance');

INSERT INTO `Physical_violence`.`EventModalities` VALUES
    ('MA', 'massacre'), ('AS', 'selective killing'), ('DF', 'forced disappearance'), ('SE', 'kidnapping'),
    ('MI', 'landmines and explosive remnants'), ('RU', 'recruitment of children and adolescents'),
    ('AP', 'attack on a town'), ('AB', 'act of war'), ('DB', 'damage to civilian property'),
    ('VS', 'sexual violence'), ('AT', 'terrorist attack');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
