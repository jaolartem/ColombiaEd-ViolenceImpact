-- =====================================================================================================
-- Violence and education in Colombia: data model
--
-- Research logic
--   Violence is measured per municipality and year in Galtung's terms, plus gender:
--     direct (physical) violence   - homicide, suicide, intra-family violence, violence against children
--     structural violence          - avoidable deprivation: poverty, inequality, access to education/health
--     cultural violence            - violence that targets identities (ethnic, vulnerable groups,
--                                    socio-political), the observable trace of what legitimises violence
--     gender violence              - partner violence, sexual violence, homicide and suicide by sex
--   Each indicator goes cases -> rate per 100,000 -> sub-index (0-1, fixed goalposts) -> dimension
--   index -> final index, combining sub-indices with a geometric mean as in the UNDP Human Development
--   Index.
--
--   Two levels:
--     municipality - the violence indices, built ONLY from external sources (Medicina Legal, Police,
--                    DANE, MEN). Nothing reported by the students enters an index: the index explains
--                    the scores, so it cannot contain the students' own answers.
--     student      - each Saber 11 exam taker: scores and what the student reports about home and
--                    family (Student_Context). It describes the student's life, works as the student
--                    level of a multilevel model, and is compared with what DANE says of the same
--                    municipality (who reaches grade 11 is a selected group).
--
--   Time is compared by government (Uribe I to Petro) through Governments / Government_Phases.
--
-- Keys
--   Municipality.id is the DANE code as a number (5001 = Medellin). Sources write it as '5001' or
--   '05001'; as a number both are the same key. Names are never used to join.
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

CREATE SCHEMA `RelationsAndConclusions`;   -- shared dimensions: place, population, time, sources, final index
CREATE SCHEMA `Physical_violence`;
CREATE SCHEMA `Structural_Violence`;
CREATE SCHEMA `Cultural_violence`;
CREATE SCHEMA `GENDER_VIOLENCE`;
CREATE SCHEMA `Student_Context`;           -- what each student reports (ICFES questionnaire); never in an index
CREATE SCHEMA `Education_Outcomes`;        -- Saber 11 scores and MEN enrolment / dropout rates


-- =====================================================================================================
-- RelationsAndConclusions: place, population, time and sources
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
    `id`   CHAR(1)     NOT NULL PRIMARY KEY,             -- F, M, U (unknown / not reported)
    `name` VARCHAR(20) NOT NULL
);

CREATE TABLE `RelationsAndConclusions`.`Population` (     -- DANE projections, mid-year
    `municipality_id` INT     NOT NULL,
    `year`            YEAR    NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,                  -- 'U' holds the total
    `population`      INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `sex_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`Governments` (
    `id`         INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code`       VARCHAR(30)  NOT NULL UNIQUE,           -- uribe_1, uribe_2, santos_1, santos_2, duque, petro
    `president`  VARCHAR(100) NOT NULL,
    `start_date` DATE         NOT NULL,                  -- terms start on 7 August
    `end_date`   DATE         NOT NULL                   -- exclusive
);

CREATE TABLE `RelationsAndConclusions`.`Government_Phases` (   -- e.g. Santos II: negotiation / implementation
    `id`            INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `government_id` INT          NOT NULL,
    `code`          VARCHAR(40)  NOT NULL UNIQUE,
    `description`   VARCHAR(255) NULL,
    `start_date`    DATE         NOT NULL,
    `end_date`      DATE         NOT NULL,
    FOREIGN KEY (`government_id`) REFERENCES `RelationsAndConclusions`.`Governments` (`id`)
);

CREATE TABLE `RelationsAndConclusions`.`Sources` (
    `id`          INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `institution` VARCHAR(150) NOT NULL,                 -- Medicina Legal, Policia (MinDefensa), DANE, ICFES, MEN
    `dataset`     VARCHAR(40)  NULL,                     -- datos.gov.co id (vtub-3de2) or file name
    `description` VARCHAR(255) NULL,
    `preliminary` TINYINT(1)   NOT NULL DEFAULT 0
);

-- Final index: geometric mean of the four dimension indices
CREATE TABLE `RelationsAndConclusions`.`FinalViolenceIndex` (
    `municipality_id`      INT   NOT NULL,
    `year`                 YEAR  NOT NULL,
    `physical_index`       FLOAT NULL,
    `structural_index`     FLOAT NULL,
    `cultural_index`       FLOAT NULL,
    `gender_index`         FLOAT NULL,
    `final_violence_index` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Violence facts, shared by the physical, cultural and gender dimensions
--   One row per municipality, year, indicator and victim's sex. Which dimension an indicator belongs
--   to is a property of the indicator, so it lives in the catalogue, not in the fact table.
-- =====================================================================================================

CREATE TABLE `RelationsAndConclusions`.`ViolenceIndicators` (
    `id`          INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `code`        VARCHAR(40)  NOT NULL UNIQUE,          -- homicide, suicide, violence_children, domestic_violence,
                                                         -- partner_violence, sexual_violence, massacre_victims, ...
    `dimension`   ENUM('physical', 'cultural', 'gender') NOT NULL,
    `description` VARCHAR(255) NULL
);

CREATE TABLE `RelationsAndConclusions`.`ViolenceCases` (
    `municipality_id` INT     NOT NULL,
    `year`            YEAR    NOT NULL,
    `indicator_id`    INT     NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,
    `source_id`       INT     NOT NULL,
    `cases`           INT     NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `indicator_id`, `sex_id`, `source_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_id`)    REFERENCES `RelationsAndConclusions`.`ViolenceIndicators` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`),
    FOREIGN KEY (`source_id`)       REFERENCES `RelationsAndConclusions`.`Sources` (`id`)
);

-- Cases by the identity of the victim (ethnic ancestry, vulnerable group): the cultural dimension
CREATE TABLE `Cultural_violence`.`IdentityGroups` (
    `id`   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `kind` ENUM('racial_ancestry', 'vulnerable_group', 'indigenous_people', 'sexual_orientation', 'gender_identity') NOT NULL,
    `name` VARCHAR(150) NOT NULL,
    UNIQUE (`kind`, `name`)
);

CREATE TABLE `Cultural_violence`.`IdentityViolenceCases` (
    `municipality_id`   INT  NOT NULL,
    `year`              YEAR NOT NULL,
    `indicator_id`      INT  NOT NULL,                   -- homicide, suicide, socio-political homicide
    `identity_group_id` INT  NOT NULL,
    `source_id`         INT  NOT NULL,
    `cases`             INT  NOT NULL,
    PRIMARY KEY (`municipality_id`, `year`, `indicator_id`, `identity_group_id`, `source_id`),
    FOREIGN KEY (`municipality_id`)   REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`indicator_id`)      REFERENCES `RelationsAndConclusions`.`ViolenceIndicators` (`id`),
    FOREIGN KEY (`identity_group_id`) REFERENCES `Cultural_violence`.`IdentityGroups` (`id`),
    FOREIGN KEY (`source_id`)         REFERENCES `RelationsAndConclusions`.`Sources` (`id`)
);


-- =====================================================================================================
-- Dimension indices: sub-index per indicator (0-1) and the dimension's geometric mean
-- =====================================================================================================

CREATE TABLE `Physical_violence`.`PhysicalViolenceIndex` (
    `municipality_id`              INT   NOT NULL,
    `year`                         YEAR  NOT NULL,
    `subin_homicide`               FLOAT NULL,
    `subin_suicide`                FLOAT NULL,
    `subin_violence_children`      FLOAT NULL,
    `subin_domestic_violence`      FLOAT NULL,           -- other relatives and older adults
    `physical_violence_index`      FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Cultural_violence`.`CulturalViolenceIndex` (
    `municipality_id`                  INT   NOT NULL,
    `year`                             YEAR  NOT NULL,
    `subin_ancestry_homicide`          FLOAT NULL,
    `subin_ancestry_suicide`           FLOAT NULL,
    `subin_vulnerable_groups_homicide` FLOAT NULL,
    `subin_vulnerable_groups_suicide`  FLOAT NULL,
    `subin_sociopolitical_homicide`    FLOAT NULL,
    `cultural_violence_index`          FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `GENDER_VIOLENCE`.`GenderViolenceIndex` (
    `municipality_id`          INT   NOT NULL,
    `year`                     YEAR  NOT NULL,
    `subin_partner_violence`   FLOAT NULL,
    `subin_partner_homicide`   FLOAT NULL,
    `subin_sexual_violence`    FLOAT NULL,
    `subin_female_homicide`    FLOAT NULL,               -- per 100,000 women
    `subin_female_suicide`     FLOAT NULL,
    `gender_violence_index`    FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Structural_Violence: external sources only (DANE, MinSalud, MEN)
-- =====================================================================================================

CREATE TABLE `Structural_Violence`.`Poverty` (           -- census-based, one reference year per measure
    `municipality_id`         INT   NOT NULL,
    `reference_year`          YEAR  NOT NULL,
    `mpi`                     FLOAT NULL,                -- multidimensional poverty index
    `monetary_poverty`        FLOAT NULL,
    `extreme_monetary_poverty` FLOAT NULL,
    `unsatisfied_basic_needs` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `reference_year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`Inequality` (
    `municipality_id` INT   NOT NULL,
    `reference_year`  YEAR  NOT NULL,
    `gini_index`      FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `reference_year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`EducationAccess` (
    `municipality_id`                   INT   NOT NULL,
    `year`                              YEAR  NOT NULL,
    `basic_education_centers_per_100k`  FLOAT NULL,
    `middle_education_centers_per_100k` FLOAT NULL,
    `technical_centers_per_100k`        FLOAT NULL,
    `university_centers_per_100k`       FLOAT NULL,
    `net_enrolment`                     FLOAT NULL,      -- MEN
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`HealthCenters` (
    `id`              INT          NOT NULL PRIMARY KEY, -- REPS code
    `name`            VARCHAR(255) NULL,
    `care_level`      TINYINT      NULL,                 -- 1, 2, 3
    `municipality_id` INT          NOT NULL,
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`HealthAccess` (
    `municipality_id`               INT   NOT NULL,
    `year`                          YEAR  NOT NULL,
    `first_level_centers_per_100k`  FLOAT NULL,
    `second_level_centers_per_100k` FLOAT NULL,
    `third_level_centers_per_100k`  FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Structural_Violence`.`StructuralViolenceIndex` (
    `municipality_id`           INT   NOT NULL,
    `year`                      YEAR  NOT NULL,
    `subin_poverty`             FLOAT NULL,
    `subin_inequality`          FLOAT NULL,
    `subin_education_access`    FLOAT NULL,
    `subin_health_access`       FLOAT NULL,
    `structural_violence_index` FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `year`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);


-- =====================================================================================================
-- Education_Outcomes: Saber 11 and MEN
-- =====================================================================================================

CREATE TABLE `Education_Outcomes`.`ExamPeriods` (
    `id`       INT     NOT NULL PRIMARY KEY,             -- ICFES period code: 20102, 20194, 20224 ...
    `year`     YEAR    NOT NULL,
    `calendar` CHAR(1) NOT NULL,                         -- A (second semester) or B (first semester)
    `scale`    ENUM('pre_2014', 'since_2014_2') NOT NULL -- the exam changed in 2014-2; compare as z-scores
);

CREATE TABLE `Education_Outcomes`.`Schools` (
    `id`              BIGINT       NOT NULL PRIMARY KEY, -- DANE school code
    `name`            VARCHAR(255) NULL,
    `municipality_id` INT          NOT NULL,
    `sector`          ENUM('public', 'private') NULL,
    `area`            ENUM('urban', 'rural') NULL,
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`)
);

CREATE TABLE `Education_Outcomes`.`Students` (           -- one exam taker in one period
    `id`              VARCHAR(40) NOT NULL PRIMARY KEY,  -- ICFES estu_consecutivo
    `exam_period_id`  INT         NOT NULL,
    `school_id`       BIGINT      NULL,
    `municipality_id` INT         NOT NULL,              -- where the school is
    `sex_id`          CHAR(1)     NOT NULL,
    `birth_date`      DATE        NULL,
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`),
    FOREIGN KEY (`school_id`)       REFERENCES `Education_Outcomes`.`Schools` (`id`),
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
    `global_score`       FLOAT NULL,                     -- only since 2014-2
    FOREIGN KEY (`student_id`) REFERENCES `Education_Outcomes`.`Students` (`id`)
);

CREATE TABLE `Education_Outcomes`.`MunicipalScores` (    -- per municipality, period and sex
    `municipality_id` INT     NOT NULL,
    `exam_period_id`  INT     NOT NULL,
    `sex_id`          CHAR(1) NOT NULL,
    `students`        INT     NOT NULL,
    `mean_math`       FLOAT NULL,
    `mean_global`     FLOAT NULL,
    `math_z`          FLOAT NULL,                        -- against the national mean and SD of the period
    `global_z`        FLOAT NULL,
    PRIMARY KEY (`municipality_id`, `exam_period_id`, `sex_id`),
    FOREIGN KEY (`municipality_id`) REFERENCES `RelationsAndConclusions`.`Municipalities` (`id`),
    FOREIGN KEY (`exam_period_id`)  REFERENCES `Education_Outcomes`.`ExamPeriods` (`id`),
    FOREIGN KEY (`sex_id`)          REFERENCES `RelationsAndConclusions`.`Sexes` (`id`)
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


-- =====================================================================================================
-- Student_Context: what each student reports (ICFES questionnaire)
--   Every attribute depends only on the student, so they share one table. These variables describe
--   the student's life and are compared with DANE; they never feed a violence index.
-- =====================================================================================================

CREATE TABLE `Student_Context`.`EducationLevels` (
    `id`   INT          NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL UNIQUE                  -- ICFES wording: "Primaria completa", ...
);

CREATE TABLE `Student_Context`.`StudentHousehold` (
    `student_id`                 VARCHAR(40) NOT NULL PRIMARY KEY,
    `stratum`                    TINYINT    NULL,        -- 1-6, 0 = none
    `persons_in_household`       TINYINT    NULL,
    `rooms`                      TINYINT    NULL,
    `floor_type`                 VARCHAR(60) NULL,
    `has_internet`               TINYINT(1) NULL,
    `has_computer`               TINYINT(1) NULL,
    `has_car`                    TINYINT(1) NULL,
    `has_washing_machine`        TINYINT(1) NULL,
    `has_video_game_console`     TINYINT(1) NULL,
    `mother_education_level_id`  INT        NULL,
    `father_education_level_id`  INT        NULL,
    `ethnic_group`               VARCHAR(60) NULL,
    `work_hours_per_week`        VARCHAR(40) NULL,       -- ICFES reports ranges
    FOREIGN KEY (`student_id`)                REFERENCES `Education_Outcomes`.`Students` (`id`),
    FOREIGN KEY (`mother_education_level_id`) REFERENCES `Student_Context`.`EducationLevels` (`id`),
    FOREIGN KEY (`father_education_level_id`) REFERENCES `Student_Context`.`EducationLevels` (`id`)
);

CREATE TABLE `Student_Context`.`StudentCulturalCapital` (
    `student_id`             VARCHAR(40) NOT NULL PRIMARY KEY,
    `books_at_home`          VARCHAR(40) NULL,           -- ICFES reports ranges
    `reading_for_pleasure`   VARCHAR(40) NULL,
    `internet_hours_per_day` VARCHAR(40) NULL,
    FOREIGN KEY (`student_id`) REFERENCES `Education_Outcomes`.`Students` (`id`)
);

-- What the students of a municipality report, to set beside DANE
CREATE TABLE `Student_Context`.`MunicipalStudentContext` (
    `municipality_id`          INT   NOT NULL,
    `exam_period_id`           INT   NOT NULL,
    `students`                 INT   NOT NULL,
    `share_internet`           FLOAT NULL,
    `share_computer`           FLOAT NULL,
    `share_car`                FLOAT NULL,
    `share_washing_machine`    FLOAT NULL,
    `share_stratum_1_2`        FLOAT NULL,
    `share_mother_higher_ed`   FLOAT NULL,
    `mean_persons_per_room`    FLOAT NULL,
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
JOIN `RelationsAndConclusions`.`Population` p
  ON p.`municipality_id` = vc.`municipality_id` AND p.`year` = vc.`year` AND p.`sex_id` = 'U'
GROUP BY vc.`municipality_id`, vc.`year`, vi.`code`, vi.`dimension`, p.`population`;


-- =====================================================================================================
-- Reference rows
-- =====================================================================================================

INSERT INTO `RelationsAndConclusions`.`Sexes` VALUES ('F', 'Female'), ('M', 'Male'), ('U', 'Unknown / total');

INSERT INTO `RelationsAndConclusions`.`Governments` (`code`, `president`, `start_date`, `end_date`) VALUES
    ('uribe_1',  'Alvaro Uribe Velez (I)',     '2002-08-07', '2006-08-07'),
    ('uribe_2',  'Alvaro Uribe Velez (II)',    '2006-08-07', '2010-08-07'),
    ('santos_1', 'Juan Manuel Santos (I)',     '2010-08-07', '2014-08-07'),
    ('santos_2', 'Juan Manuel Santos (II)',    '2014-08-07', '2018-08-07'),
    ('duque',    'Ivan Duque Marquez',         '2018-08-07', '2022-08-07'),
    ('petro',    'Gustavo Petro Urrego',       '2022-08-07', '2026-08-07');

INSERT INTO `RelationsAndConclusions`.`Government_Phases` (`government_id`, `code`, `description`, `start_date`, `end_date`)
SELECT `id`, 'santos_2_negotiation', 'Havana talks until the final agreement', '2014-08-07', '2016-11-24'
FROM `RelationsAndConclusions`.`Governments` WHERE `code` = 'santos_2';
INSERT INTO `RelationsAndConclusions`.`Government_Phases` (`government_id`, `code`, `description`, `start_date`, `end_date`)
SELECT `id`, 'santos_2_implementation', 'From the final agreement (24 Nov 2016)', '2016-11-24', '2018-08-07'
FROM `RelationsAndConclusions`.`Governments` WHERE `code` = 'santos_2';

INSERT INTO `RelationsAndConclusions`.`ViolenceIndicators` (`code`, `dimension`, `description`) VALUES
    ('homicide',             'physical', 'Presumed homicides'),
    ('suicide',              'physical', 'Presumed suicides'),
    ('violence_children',    'physical', 'Intra-family violence against children and adolescents'),
    ('domestic_violence',    'physical', 'Intra-family violence against other relatives and older adults'),
    ('massacre_victims',     'physical', 'Victims of massacres'),
    ('partner_violence',     'gender',   'Partner violence'),
    ('sexual_violence',      'gender',   'Medico-legal examinations for presumed sexual offence'),
    ('sociopolitical_homicide', 'cultural', 'Homicides with a socio-political circumstance');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
