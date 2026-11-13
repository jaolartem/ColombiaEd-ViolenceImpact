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
DROP SCHEMA IF EXISTS `Territorial_Context`;
DROP SCHEMA IF EXISTS `State_Action`;
DROP SCHEMA IF EXISTS `Research_Design`;

CREATE SCHEMA `RelationsAndConclusions` DEFAULT CHARACTER SET utf8mb4;   -- place, population, time, sources, final index
CREATE SCHEMA `Physical_violence`       DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Structural_Violence`     DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Cultural_violence`       DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `GENDER_VIOLENCE`         DEFAULT CHARACTER SET utf8mb4;
CREATE SCHEMA `Student_Context`         DEFAULT CHARACTER SET utf8mb4;   -- what students report; never in an index
CREATE SCHEMA `Education_Outcomes`      DEFAULT CHARACTER SET utf8mb4;   -- Saber 11, Saber Pro, MEN, scholarships
CREATE SCHEMA `Territorial_Context`     DEFAULT CHARACTER SET utf8mb4;   -- DNP TerriData: every indicator per municipality
CREATE SCHEMA `State_Action`            DEFAULT CHARACTER SET utf8mb4;   -- the State as a network: entities, norms, coding
CREATE SCHEMA `Research_Design`         DEFAULT CHARACTER SET utf8mb4;   -- decision log, typology, case selection


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
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`),
    FOREIGN KEY (`school_id`)       REFERENCES `Education_Outcomes`.`Schools` (`id`)
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

CREATE TABLE `Education_Outcomes`.`CertifiedEntities` (    -- ETC: who runs public education (Law 715 of 2001)
    `id`              INT          NOT NULL PRIMARY KEY,      -- MEN's ETC code
    `name`            VARCHAR(120) NOT NULL,
    `kind`            ENUM('municipality', 'department') NOT NULL,   -- a certified municipality, or a department
    `department_id`   INT          NOT NULL,
    `municipality_id` INT          NULL,                      -- for a certified municipality, itself
    FOREIGN KEY (`department_id`)   REFERENCES `RelationsAndConclusions`.`Departments` (`id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`EducationAuthority` (   -- which ETC runs each municipality's schools, by year
    `municipality_id` INT      NOT NULL,
    `year`            SMALLINT NOT NULL,
    `entity_id`       INT      NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`entity_id`)       REFERENCES `Education_Outcomes`.`CertifiedEntities` (`id`)
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
-- Territorial_Context: DNP TerriData (python -m panel.dnp), every indicator DNP publishes per municipality
-- =====================================================================================================

CREATE TABLE `Territorial_Context`.`TerriDataIndicators` (
    `code`        CHAR(9)      NOT NULL PRIMARY KEY,         -- DNP's nine-digit indicator code
    `dimension`   VARCHAR(255) NOT NULL,
    `subcategory` VARCHAR(255) NULL,
    `name`        VARCHAR(255) NOT NULL,                     -- as DNP publishes it
    `unit`        VARCHAR(255) NULL
);

CREATE TABLE `Territorial_Context`.`TerriDataSources` (
    `id`   INT          NOT NULL PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `Territorial_Context`.`TerriDataCategories` (    -- the labels text indicators take, once each
    `id`             INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `indicator_code` CHAR(9)      NOT NULL,                  -- 010010007 rurality: Rural, Intermedio, ...
    `label`          VARCHAR(255) NOT NULL,
    UNIQUE KEY (`indicator_code`, `label`),
    FOREIGN KEY (`indicator_code`) REFERENCES `Territorial_Context`.`TerriDataIndicators` (`code`)
);

CREATE TABLE `Territorial_Context`.`MunicipalIndicators` (   -- only rows that passed validation (panel.dnp)
    `municipality_id` INT      NOT NULL,
    `indicator_code`  CHAR(9)  NOT NULL,
    `year`            SMALLINT NOT NULL,
    `month`           TINYINT  NOT NULL,                     -- 0 when the indicator is yearly or has no date
    `value`           DOUBLE   NULL,
    `category_id`     INT      NULL,                         -- for text indicators
    `source_id`       INT      NULL,
    PRIMARY KEY (`municipality_id`, `indicator_code`, `year`, `month`),
    KEY (`indicator_code`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_code`)  REFERENCES `Territorial_Context`.`TerriDataIndicators` (`code`),
    FOREIGN KEY (`category_id`)     REFERENCES `Territorial_Context`.`TerriDataCategories` (`id`),
    FOREIGN KEY (`source_id`)       REFERENCES `Territorial_Context`.`TerriDataSources` (`id`)
);

CREATE TABLE `Territorial_Context`.`DepartmentalIndicators` (  -- department totals: DANE's departmental Gini, ...
    `department_id`  INT      NOT NULL,
    `indicator_code` CHAR(9)  NOT NULL,
    `year`           SMALLINT NOT NULL,
    `month`          TINYINT  NOT NULL,
    `value`          DOUBLE   NULL,
    `category_id`    INT      NULL,
    `source_id`      INT      NULL,
    PRIMARY KEY (`department_id`, `indicator_code`, `year`, `month`),
    FOREIGN KEY (`department_id`)  REFERENCES `RelationsAndConclusions`.`Departments` (`id`),
    FOREIGN KEY (`indicator_code`) REFERENCES `Territorial_Context`.`TerriDataIndicators` (`code`),
    FOREIGN KEY (`category_id`)    REFERENCES `Territorial_Context`.`TerriDataCategories` (`id`),
    FOREIGN KEY (`source_id`)      REFERENCES `Territorial_Context`.`TerriDataSources` (`id`)
);


-- CUIPO (python -m panel.fiscal): each municipality's budget execution as reported to CGN and CGR, 2023 on.
-- Year-end closes (period YYYY1201) and the latest quarter. Before 2023: TerriData, dimension Finanzas publicas.

CREATE TABLE `Territorial_Context`.`CuipoAccounts` (          -- the income account tree
    `code`  VARCHAR(60)  NOT NULL PRIMARY KEY,                -- 1.1.02.06.001.01 = SGP, participation for education
    `name`  VARCHAR(255) NOT NULL,
    `depth` TINYINT      NOT NULL                             -- 1 = total income; each level adds up the next
);

CREATE TABLE `Territorial_Context`.`CuipoFundingSources` (
    `code` VARCHAR(60)  NOT NULL PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `Territorial_Context`.`CuipoSectors` (
    `code` VARCHAR(40)  NOT NULL PRIMARY KEY,
    `name` VARCHAR(255) NOT NULL
);

CREATE TABLE `Territorial_Context`.`MunicipalIncome` (       -- pesos collected, cumulative to the period
    `municipality_id` INT          NOT NULL,
    `period`          INT          NOT NULL,                  -- YYYYMMDD of the cut: 20241201 is the 2024 close
    `account`         VARCHAR(60)  NOT NULL,
    `funding_source`  VARCHAR(60)  NOT NULL,
    `collected`       DOUBLE       NULL,
    PRIMARY KEY (`municipality_id`, `period`, `account`, `funding_source`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`account`)         REFERENCES `Territorial_Context`.`CuipoAccounts` (`code`),
    FOREIGN KEY (`funding_source`)  REFERENCES `Territorial_Context`.`CuipoFundingSources` (`code`)
);

CREATE TABLE `Territorial_Context`.`MunicipalSpending` (     -- pesos, cumulative to the period
    `municipality_id` INT          NOT NULL,
    `period`          INT          NOT NULL,
    `sector`          VARCHAR(40)  NOT NULL,                  -- 'NO APLICA' is spending that is not investment
    `funding_source`  VARCHAR(60)  NOT NULL,
    `commitments`     DOUBLE       NULL,
    `obligations`     DOUBLE       NULL,
    `payments`        DOUBLE       NULL,
    PRIMARY KEY (`municipality_id`, `period`, `sector`, `funding_source`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`sector`)          REFERENCES `Territorial_Context`.`CuipoSectors` (`code`),
    FOREIGN KEY (`funding_source`)  REFERENCES `Territorial_Context`.`CuipoFundingSources` (`code`)
);


-- =====================================================================================================
-- Data quality (python -m panel.quality), the validation step of each source. Original values are never overwritten.
-- =====================================================================================================

CREATE TABLE `RelationsAndConclusions`.`SmoothedValues` (   -- empirical Bayes, toward the department
    `source_table`    VARCHAR(80)  NOT NULL,
    `column_name`     VARCHAR(80)  NOT NULL,                -- for PeriodRates, the measure
    `municipality_id` INT          NOT NULL,
    `period`          VARCHAR(40)  NOT NULL,                -- 'government:duque', '20172', ...
    `raw_value`       DOUBLE       NULL,
    `smoothed_value`  DOUBLE       NULL,
    `weight`          DOUBLE       NULL,                    -- share of the municipality's own value kept (0-1)
    `reference`       DOUBLE       NULL,                    -- the department's value it is pulled toward
    PRIMARY KEY (`source_table`, `column_name`, `municipality_id`, `period`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`DataQualityFlags` (   -- each source checked against its own rules
    `id`              INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `source`          VARCHAR(40)  NOT NULL,                -- Sources.code: dane, icfes, men, police, cnmh, indepaz, medicina_legal, dnp, cuipo
    `source_table`    VARCHAR(80)  NOT NULL,
    `column_name`     VARCHAR(80)  NOT NULL,                -- for PeriodRates and ViolenceCases, the measure
    `municipality_id` INT          NOT NULL,
    `period`          VARCHAR(40)  NOT NULL,
    `kind`            ENUM('error', 'missing', 'inconsistent', 'break', 'small_base', 'extreme') NOT NULL,
    -- error: a value the measure does not allow; not used.
    -- missing: no value, for a known reason.
    -- inconsistent: the source contradicts itself.
    -- break: a jump between years larger than the thing measured can make.
    -- small_base: atypical only because few people stand behind it; the smoothed value is used.
    -- extreme: atypical after weighing its base; a real case, kept as it is.
    `value`           DOUBLE       NULL,
    `smoothed_value`  DOUBLE       NULL,
    `median`          DOUBLE       NULL,                    -- of the column in that period (national rate for sparse counts)
    `robust_z`        DOUBLE       NULL,
    `note`            VARCHAR(200) NULL,
    KEY (`source`, `source_table`, `column_name`, `kind`),
    KEY (`municipality_id`),
    FOREIGN KEY (`source`)          REFERENCES `RelationsAndConclusions`.`Sources` (`code`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- State_Action: the State as a network. Entities, the norms that inscribe them, and what the norms say.
--
-- Rules of this schema (owner's decision, see Research_Design.Decisions):
--   every thing is its own table, and everything said of it depends only on its key (third normal form);
--   every relation between two things is its own connection table and holds nothing else (fourth
--   normal form): no list, no second fact, no repeated column;
--   relations that change in time carry their validity (valid_from, valid_to);
--   what a norm says is stored literally (NormExcerpts) and every coding points to the excerpt it rests on.
-- =====================================================================================================

CREATE TABLE `State_Action`.`GovernmentLevels` (            -- national, departmental, municipal, school
    `id`   TINYINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(20) NOT NULL UNIQUE,
    `name` VARCHAR(60) NOT NULL
);

CREATE TABLE `State_Action`.`EntityKinds` (                 -- ministry, agency, governorship, mayoralty, ETC, school, court ...
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(40)  NOT NULL UNIQUE,
    `name` VARCHAR(120) NOT NULL
);

CREATE TABLE `State_Action`.`StateEntities` (               -- every entity that can hold a responsibility
    `id`       INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name`     VARCHAR(255) NOT NULL,
    `kind_id`  SMALLINT     NOT NULL,
    `level_id` TINYINT      NOT NULL,
    FOREIGN KEY (`kind_id`)  REFERENCES `State_Action`.`EntityKinds` (`id`),
    FOREIGN KEY (`level_id`) REFERENCES `State_Action`.`GovernmentLevels` (`id`)
);

CREATE TABLE `State_Action`.`EntityJurisdictions` (         -- connection: entity - territory, in time
    `entity_id`       INT  NOT NULL,
    `municipality_id` INT  NOT NULL,
    `valid_from`      DATE NOT NULL,
    `valid_to`        DATE NULL,
    PRIMARY KEY (`entity_id`, `municipality_id`, `valid_from`),
    FOREIGN KEY (`entity_id`)       REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `State_Action`.`EntityFunctions` (             -- education, security, justice, transitional justice, reparation ...
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(40)  NOT NULL UNIQUE,
    `name` VARCHAR(120) NOT NULL
);

CREATE TABLE `State_Action`.`EntityFunctionAssignments` (   -- connection: entity - function, in time
    `entity_id`   INT      NOT NULL,
    `function_id` SMALLINT NOT NULL,
    `valid_from`  DATE     NOT NULL,
    `valid_to`    DATE     NULL,
    PRIMARY KEY (`entity_id`, `function_id`, `valid_from`),
    FOREIGN KEY (`entity_id`)   REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`function_id`) REFERENCES `State_Action`.`EntityFunctions` (`id`)
);

CREATE TABLE `State_Action`.`EntitySuccessions` (           -- connection: entity - the entity that replaced it
    `predecessor_id` INT  NOT NULL,
    `successor_id`   INT  NOT NULL,
    `on_date`        DATE NOT NULL,
    PRIMARY KEY (`predecessor_id`, `successor_id`),
    FOREIGN KEY (`predecessor_id`) REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`successor_id`)   REFERENCES `State_Action`.`StateEntities` (`id`)
);

CREATE TABLE `State_Action`.`NormTypes` (                   -- constitution, law, decree, resolution, CONPES, PND, agreement ...
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(40)  NOT NULL UNIQUE,
    `name` VARCHAR(120) NOT NULL
);

CREATE TABLE `State_Action`.`Norms` (
    `id`            INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `type_id`       SMALLINT     NOT NULL,
    `number`        VARCHAR(40)  NULL,
    `issued_on`     DATE         NOT NULL,
    `title`         VARCHAR(500) NOT NULL,
    `source_url`    VARCHAR(500) NULL,                       -- SUIN-Juriscol, Funcion Publica, DNP ...
    `government_id` INT          NULL,
    UNIQUE KEY (`type_id`, `number`, `issued_on`),
    FOREIGN KEY (`type_id`)       REFERENCES `State_Action`.`NormTypes` (`id`),
    FOREIGN KEY (`government_id`) REFERENCES `RelationsAndConclusions`.`Governments` (`id`)
);

CREATE TABLE `State_Action`.`NormIssuers` (                 -- connection: norm - entity that issues it (a joint resolution has several)
    `norm_id`   INT NOT NULL,
    `entity_id` INT NOT NULL,
    PRIMARY KEY (`norm_id`, `entity_id`),
    FOREIGN KEY (`norm_id`)   REFERENCES `State_Action`.`Norms` (`id`),
    FOREIGN KEY (`entity_id`) REFERENCES `State_Action`.`StateEntities` (`id`)
);

CREATE TABLE `State_Action`.`NormProvisions` (              -- article, paragraph, numeral: the unit that is read
    `id`        INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `norm_id`   INT          NOT NULL,
    `parent_id` INT          NULL,                           -- a numeral inside its article
    `label`     VARCHAR(60)  NOT NULL,                       -- 'Art. 20', 'Par. 1', 'Num. 2'
    `text`      MEDIUMTEXT   NOT NULL,
    UNIQUE KEY (`norm_id`, `label`, `parent_id`),
    FOREIGN KEY (`norm_id`)   REFERENCES `State_Action`.`Norms` (`id`),
    FOREIGN KEY (`parent_id`) REFERENCES `State_Action`.`NormProvisions` (`id`)
);

CREATE TABLE `State_Action`.`NormAmendments` (              -- connection: a provision - the provision that amends or repeals it
    `provision_id`  INT NOT NULL,
    `amended_by_id` INT NOT NULL,
    `kind`          ENUM('amends', 'repeals', 'adds', 'regulates') NOT NULL,
    PRIMARY KEY (`provision_id`, `amended_by_id`),
    FOREIGN KEY (`provision_id`)  REFERENCES `State_Action`.`NormProvisions` (`id`),
    FOREIGN KEY (`amended_by_id`) REFERENCES `State_Action`.`NormProvisions` (`id`)
);

CREATE TABLE `State_Action`.`NormExcerpts` (                -- the literal piece of a provision a coding rests on
    `id`           INT        NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `provision_id` INT        NOT NULL,
    `start_char`   INT        NOT NULL,                      -- position in NormProvisions.text
    `end_char`     INT        NOT NULL,
    `text`         TEXT       NOT NULL,                      -- the excerpt as written in the norm
    UNIQUE KEY (`provision_id`, `start_char`, `end_char`),
    FOREIGN KEY (`provision_id`) REFERENCES `State_Action`.`NormProvisions` (`id`)
);

-- What the norms say, coded. Each coded unit is its own thing; each link between them is its own table.

CREATE TABLE `State_Action`.`Coders` (                      -- who coded: the researcher, the assistant, a second reader
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `name` VARCHAR(120) NOT NULL,
    `kind` ENUM('human', 'ai') NOT NULL
);

CREATE TABLE `State_Action`.`ObjectiveTypes` (              -- the typology of objectives (the owner's thesis, or another)
    `id`          SMALLINT     NOT NULL PRIMARY KEY,
    `code`        VARCHAR(40)  NOT NULL UNIQUE,
    `name`        VARCHAR(120) NOT NULL,
    `definition`  TEXT         NOT NULL
);

CREATE TABLE `State_Action`.`Objectives` (                  -- a desired future state
    `id`           INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `statement`    TEXT         NOT NULL,
    `type_id`      SMALLINT     NULL,
    `horizon_year` SMALLINT     NULL,
    FOREIGN KEY (`type_id`) REFERENCES `State_Action`.`ObjectiveTypes` (`id`)
);

CREATE TABLE `State_Action`.`Problems` (                    -- a socially relevant problem: a fact and its explanation
    `id`          INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `fact`        TEXT NOT NULL,                             -- the uncomfortable fact (the power goes out)
    `explanation` TEXT NOT NULL                              -- why it happens, as this framing says (a transformer failed)
);

CREATE TABLE `State_Action`.`SocialGroups` (                -- for whom a fact is uncomfortable
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(60)  NOT NULL UNIQUE,
    `name` VARCHAR(160) NOT NULL
);

CREATE TABLE `State_Action`.`Responsibilities` (            -- what an entity must do, and where it stops
    `id`        INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `entity_id` INT  NOT NULL,
    `action`    TEXT NOT NULL,
    `scope`     TEXT NULL,                                   -- how far it reaches
    `boundary`  TEXT NULL,                                   -- where another entity's starts
    FOREIGN KEY (`entity_id`) REFERENCES `State_Action`.`StateEntities` (`id`)
);

CREATE TABLE `State_Action`.`ResourceTypes` (               -- money, staff, time, authority, information, infrastructure
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(40)  NOT NULL UNIQUE,
    `name` VARCHAR(120) NOT NULL
);

CREATE TABLE `State_Action`.`Resources` (                   -- what is assigned: its kind, how much, from whom, to whom
    `id`             INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `type_id`        SMALLINT     NOT NULL,
    `description`    TEXT         NOT NULL,
    `amount`         DOUBLE       NULL,
    `unit`           VARCHAR(60)  NULL,                      -- pesos of a year, posts, months, ...
    `from_entity_id` INT          NULL,
    `to_entity_id`   INT          NULL,
    FOREIGN KEY (`type_id`)        REFERENCES `State_Action`.`ResourceTypes` (`id`),
    FOREIGN KEY (`from_entity_id`) REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`to_entity_id`)   REFERENCES `State_Action`.`StateEntities` (`id`)
);

-- Connections. The coder is part of every key, so two readings of the same excerpt can be compared.

CREATE TABLE `State_Action`.`ExcerptObjectives` (
    `excerpt_id` INT NOT NULL, `objective_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`excerpt_id`, `objective_id`, `coder_id`),
    FOREIGN KEY (`excerpt_id`)   REFERENCES `State_Action`.`NormExcerpts` (`id`),
    FOREIGN KEY (`objective_id`) REFERENCES `State_Action`.`Objectives` (`id`),
    FOREIGN KEY (`coder_id`)     REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ExcerptProblems` (
    `excerpt_id` INT NOT NULL, `problem_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`excerpt_id`, `problem_id`, `coder_id`),
    FOREIGN KEY (`excerpt_id`) REFERENCES `State_Action`.`NormExcerpts` (`id`),
    FOREIGN KEY (`problem_id`) REFERENCES `State_Action`.`Problems` (`id`),
    FOREIGN KEY (`coder_id`)   REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ExcerptResponsibilities` (
    `excerpt_id` INT NOT NULL, `responsibility_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`excerpt_id`, `responsibility_id`, `coder_id`),
    FOREIGN KEY (`excerpt_id`)        REFERENCES `State_Action`.`NormExcerpts` (`id`),
    FOREIGN KEY (`responsibility_id`) REFERENCES `State_Action`.`Responsibilities` (`id`),
    FOREIGN KEY (`coder_id`)          REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ExcerptResources` (
    `excerpt_id` INT NOT NULL, `resource_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`excerpt_id`, `resource_id`, `coder_id`),
    FOREIGN KEY (`excerpt_id`)  REFERENCES `State_Action`.`NormExcerpts` (`id`),
    FOREIGN KEY (`resource_id`) REFERENCES `State_Action`.`Resources` (`id`),
    FOREIGN KEY (`coder_id`)    REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ExcerptEntityEvents` (         -- connection: excerpt - an entity it creates, abolishes, certifies ...
    `excerpt_id` INT NOT NULL, `entity_id` INT NOT NULL,
    `event`      ENUM('creates', 'abolishes', 'merges', 'renames', 'certifies', 'decertifies', 'assigns_function') NOT NULL,
    `coder_id`   SMALLINT NOT NULL,
    PRIMARY KEY (`excerpt_id`, `entity_id`, `event`, `coder_id`),
    FOREIGN KEY (`excerpt_id`) REFERENCES `State_Action`.`NormExcerpts` (`id`),
    FOREIGN KEY (`entity_id`)  REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`coder_id`)   REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ObjectiveProblems` (           -- connection: objective - the problem it answers
    `objective_id` INT NOT NULL, `problem_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`objective_id`, `problem_id`, `coder_id`),
    FOREIGN KEY (`objective_id`) REFERENCES `State_Action`.`Objectives` (`id`),
    FOREIGN KEY (`problem_id`)   REFERENCES `State_Action`.`Problems` (`id`),
    FOREIGN KEY (`coder_id`)     REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ObjectiveResources` (          -- connection: objective - a resource assigned to it
    `objective_id` INT NOT NULL, `resource_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`objective_id`, `resource_id`, `coder_id`),
    FOREIGN KEY (`objective_id`) REFERENCES `State_Action`.`Objectives` (`id`),
    FOREIGN KEY (`resource_id`)  REFERENCES `State_Action`.`Resources` (`id`),
    FOREIGN KEY (`coder_id`)     REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ResponsibilityObjectives` (    -- connection: responsibility - the objective it serves
    `responsibility_id` INT NOT NULL, `objective_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`responsibility_id`, `objective_id`, `coder_id`),
    FOREIGN KEY (`responsibility_id`) REFERENCES `State_Action`.`Responsibilities` (`id`),
    FOREIGN KEY (`objective_id`)      REFERENCES `State_Action`.`Objectives` (`id`),
    FOREIGN KEY (`coder_id`)          REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ProblemGroups` (               -- connection: problem - a group for whom the fact is uncomfortable
    `problem_id` INT NOT NULL, `group_id` SMALLINT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`problem_id`, `group_id`, `coder_id`),
    FOREIGN KEY (`problem_id`) REFERENCES `State_Action`.`Problems` (`id`),
    FOREIGN KEY (`group_id`)   REFERENCES `State_Action`.`SocialGroups` (`id`),
    FOREIGN KEY (`coder_id`)   REFERENCES `State_Action`.`Coders` (`id`)
);

CREATE TABLE `State_Action`.`ProblemFramers` (              -- connection: problem - the entity whose explanation it is
    `problem_id` INT NOT NULL, `entity_id` INT NOT NULL, `coder_id` SMALLINT NOT NULL,
    PRIMARY KEY (`problem_id`, `entity_id`, `coder_id`),
    FOREIGN KEY (`problem_id`) REFERENCES `State_Action`.`Problems` (`id`),
    FOREIGN KEY (`entity_id`)  REFERENCES `State_Action`.`StateEntities` (`id`),
    FOREIGN KEY (`coder_id`)   REFERENCES `State_Action`.`Coders` (`id`)
);


-- =====================================================================================================
-- Research_Design: the decisions taken, the municipal typology and the cases chosen from it
-- =====================================================================================================

CREATE TABLE `Research_Design`.`DecisionTopics` (           -- objective, frame, data, cleaning, model, method, design
    `id`   SMALLINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(40)  NOT NULL UNIQUE,
    `name` VARCHAR(120) NOT NULL
);

CREATE TABLE `Research_Design`.`Decisions` (                -- the decision log: what was decided, by whom, why
    `id`            INT      NOT NULL PRIMARY KEY,
    `decided_on`    DATE     NOT NULL,
    `topic_id`      SMALLINT NOT NULL,
    `decision`      TEXT     NOT NULL,
    `reason`        TEXT     NULL,
    `decided_by`    ENUM('researcher', 'assistant', 'both') NOT NULL,   -- assistant: proposed by the AI and accepted
    `superseded_by` INT      NULL,
    FOREIGN KEY (`topic_id`)      REFERENCES `Research_Design`.`DecisionTopics` (`id`),
    FOREIGN KEY (`superseded_by`) REFERENCES `Research_Design`.`Decisions` (`id`)
);

CREATE TABLE `Research_Design`.`DecisionObjects` (          -- connection: decision - a table, module or document it governs
    `decision_id` INT          NOT NULL,
    `object_name` VARCHAR(120) NOT NULL,                    -- 'panel.quality', 'Education_Outcomes.StudentScores', 'README'
    PRIMARY KEY (`decision_id`, `object_name`),
    FOREIGN KEY (`decision_id`) REFERENCES `Research_Design`.`Decisions` (`id`)
);

CREATE TABLE `Research_Design`.`TypologyRuns` (             -- one grouping of municipalities: method, base year, variables
    `id`          INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method`      VARCHAR(60)  NOT NULL,                     -- k-medoids, Ward, latent profiles ...
    `base_year`   SMALLINT     NOT NULL,
    `run_on`      DATE         NOT NULL,
    `decision_id` INT          NULL,
    FOREIGN KEY (`decision_id`) REFERENCES `Research_Design`.`Decisions` (`id`)
);

CREATE TABLE `Research_Design`.`TypologyVariables` (        -- connection: run - a variable it groups by
    `run_id`   INT          NOT NULL,
    `variable` VARCHAR(120) NOT NULL,                        -- 'TerriData 010010007', 'Census2018Municipal.ipm', ...
    PRIMARY KEY (`run_id`, `variable`),
    FOREIGN KEY (`run_id`) REFERENCES `Research_Design`.`TypologyRuns` (`id`)
);

CREATE TABLE `Research_Design`.`TypologyGroups` (           -- the groups a run produced, with the name the researcher gives them
    `id`     INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `run_id` INT          NOT NULL,
    `label`  VARCHAR(120) NOT NULL,
    `profile` TEXT        NULL,
    FOREIGN KEY (`run_id`) REFERENCES `Research_Design`.`TypologyRuns` (`id`)
);

CREATE TABLE `Research_Design`.`TypologyMemberships` (      -- connection: municipality - its group in a run
    `group_id`        INT NOT NULL,
    `municipality_id` INT NOT NULL,
    PRIMARY KEY (`group_id`, `municipality_id`),
    FOREIGN KEY (`group_id`)        REFERENCES `Research_Design`.`TypologyGroups` (`id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Research_Design`.`CaseRoles` (                -- typical (medoid), deviant, twin (nearest neighbour)
    `id`   TINYINT     NOT NULL PRIMARY KEY,
    `code` VARCHAR(20) NOT NULL UNIQUE,
    `name` VARCHAR(80) NOT NULL
);

CREATE TABLE `Research_Design`.`CaseSelections` (           -- connection: group - a municipality chosen as a case, with its role
    `group_id`        INT     NOT NULL,
    `municipality_id` INT     NOT NULL,
    `role_id`         TINYINT NOT NULL,
    `reason`          TEXT    NULL,
    PRIMARY KEY (`group_id`, `municipality_id`, `role_id`),
    FOREIGN KEY (`group_id`)        REFERENCES `Research_Design`.`TypologyGroups` (`id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`role_id`)         REFERENCES `Research_Design`.`CaseRoles` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`MunicipalLineage` (  -- connection: a municipality - the one it was split from
    `daughter_id` INT      NOT NULL,
    `mother_id`   INT      NOT NULL,
    `created_in`  SMALLINT NOT NULL,                         -- first year with its own population
    `evidence`    ENUM('inferred_population', 'divipola') NOT NULL,   -- inferred until DANE's DIVIPOLA confirms it
    PRIMARY KEY (`daughter_id`, `mother_id`),
    FOREIGN KEY (`daughter_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`mother_id`)   REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
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
    (9, 'icetex', 'Instituto Colombiano de Credito Educativo y Estudios Tecnicos en el Exterior', 'administrative', 'https://www.datos.gov.co', 'Student credits'),
    (10, 'dnp', 'Departamento Nacional de Planeacion', 'administrative', 'https://terridata.dnp.gov.co', 'TerriData: territorial statistics per municipality and department'),
    (11, 'cuipo', 'Contraloria General de la Republica and Contaduria General de la Nacion', 'administrative', 'https://www.datos.gov.co', 'CUIPO: budget execution of territorial entities');

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

INSERT INTO `State_Action`.`GovernmentLevels` VALUES
    (1, 'national', 'National'), (2, 'departmental', 'Departmental'), (3, 'municipal', 'Municipal'), (4, 'school', 'School');

INSERT INTO `State_Action`.`EntityKinds` VALUES
    (1, 'presidency', 'Presidency of the Republic'), (2, 'ministry', 'Ministry'), (3, 'administrative_department', 'Administrative department (DNP, DANE ...)'),
    (4, 'agency', 'Agency or unit (ART, ICFES, ICETEX, Victims Unit ...)'), (5, 'governorship', 'Departmental government'),
    (6, 'mayoralty', 'Municipal government'), (7, 'education_secretariat', 'Education secretariat of a certified entity (ETC)'),
    (8, 'school', 'Official school'), (9, 'court', 'Court or tribunal'), (10, 'congress', 'Congress'),
    (11, 'control_body', 'Control body (Comptroller, Procurator, Ombudsman)'), (12, 'security_force', 'Military or police force'),
    (13, 'transitional_justice', 'Transitional justice body (JEP, Truth Commission, Search Unit)');

INSERT INTO `State_Action`.`EntityFunctions` VALUES
    (1, 'education', 'Education'), (2, 'security', 'Security and public order'), (3, 'justice', 'Justice'),
    (4, 'transitional_justice', 'Transitional justice'), (5, 'victims', 'Attention and reparation to victims'),
    (6, 'planning', 'Planning and budget'), (7, 'territorial_development', 'Territorial development (PDET, rural reform)'),
    (8, 'social_protection', 'Social protection'), (9, 'evaluation', 'Evaluation and measurement'), (10, 'control', 'Fiscal and disciplinary control');

INSERT INTO `State_Action`.`NormTypes` VALUES
    (1, 'constitution', 'Constitution'), (2, 'legislative_act', 'Legislative act (constitutional amendment)'), (3, 'law', 'Law'),
    (4, 'development_plan', 'National Development Plan (law and its bases)'), (5, 'decree', 'Decree'), (6, 'resolution', 'Resolution'),
    (7, 'conpes', 'CONPES document'), (8, 'ruling', 'Court ruling'), (9, 'agreement', 'Agreement (the 2016 Final Agreement ...)'),
    (10, 'sector_plan', 'Sector plan (ten-year education plans ...)');

INSERT INTO `State_Action`.`ResourceTypes` VALUES
    (1, 'money', 'Money'), (2, 'staff', 'People: posts, teachers, officials'), (3, 'time', 'Time: deadlines, terms'),
    (4, 'authority', 'Authority: a competence or a power'), (5, 'information', 'Information: systems, records, measurement'),
    (6, 'infrastructure', 'Infrastructure: buildings, roads, connectivity');

INSERT INTO `State_Action`.`Coders` VALUES (1, 'Researcher', 'human'), (2, 'Claude (assistant)', 'ai');

INSERT INTO `Research_Design`.`DecisionTopics` VALUES
    (1, 'objective', 'Objective and questions'), (2, 'frame', 'Theoretical frame'), (3, 'data', 'Data sources'),
    (4, 'cleaning', 'Cleaning and validation'), (5, 'model', 'Data model'), (6, 'method', 'Method of analysis'), (7, 'design', 'Research design');

INSERT INTO `Research_Design`.`CaseRoles` VALUES
    (1, 'typical', 'Typical case: the medoid of its group'), (2, 'deviant', 'Deviant case: like its group, different outcome'),
    (3, 'twin', 'Twin: nearest neighbour in material and administrative conditions');
