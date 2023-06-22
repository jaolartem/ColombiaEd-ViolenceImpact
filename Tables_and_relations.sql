    CREATE SCHEMA IF NOT EXISTS RelationsAndConclusions;
    
    USE RelationsAndConclusions;
    
    CREATE TABLE `Municipalities` (
    `id` INTEGER PRIMARY KEY,
    `Name_municipalities` VARCHAR(255),
    `Municipalities_id` INTEGER UNIQUE,
    `Name_departments` VARCHAR(255),
    `COD_DEPAR` INTEGER
  );

  CREATE TABLE `PopulationANDYearInformation` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER UNIQUE,
    `population` INTEGER UNIQUE,
    `year` YEAR UNIQUE
  );

  CREATE TABLE `Helt_level` (
    `Id` INTEGER PRIMARY KEY,
    `Helt_level_level` VARCHAR(255)
  );

  CREATE TABLE `Education_level` (
    `Id` INTEGER PRIMARY KEY,
    `Education_level` VARCHAR(255)
  );

  CREATE TABLE `VulnerableGroups` (
    `id` INTEGER PRIMARY KEY,
    `group_name` VARCHAR(255)
  );

  CREATE TABLE `Racial_Ancenstry` (
    `id` INTEGER PRIMARY KEY,
    `Racial_name` VARCHAR(255)
  );

  CREATE TABLE `books_for_family` (
    `id` INTEGER PRIMARY KEY,
    `number_of_books_readed` VARCHAR(255)
  );

  CREATE TABLE `Stu_read_for_pleasure` (
    `id` INTEGER PRIMARY KEY,
    `hours_of_reading` VARCHAR(255)
  );

  CREATE TABLE `Stu_internet_dedication` (
    `id` INTEGER PRIMARY KEY,
    `hours_of_dedication` VARCHAR(255)
  );

  CREATE TABLE `Saber_reference` (
    `id` INTEGER PRIMARY KEY,
    `Student_ID` VARCHAR(255) UNIQUE,
    `date_of_test` DATE,
    `students_tested` INTEGER UNIQUE,
    `municipality_where_stu_reside` INTEGER,
     INDEX idx_date_of_test (date_of_test),
     INDEX idx_students_tested (students_tested)
  );

  CREATE TABLE `HealthCenters` (
    `id` INTEGER PRIMARY KEY,
    `health_center_id` INTEGER UNIQUE,
    `health_center_name` VARCHAR(255),
    `care_level` VARCHAR(255),
    `Municipalities_id` INTEGER
  );

  CREATE TABLE `EducationalCenters` (
    `id` INTEGER PRIMARY KEY,
    `educational_center_id` INTEGER UNIQUE,
    `educational_center_name` VARCHAR(255),
    `teaching_level` INTEGER,
    `Municipalities_id` INTEGER
  );

  CREATE TABLE `RacialAncestryHomicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `Racial_group_id` INTEGER,
    `occurrences` INTEGER,
    `population` INTEGER,
    `subin_homicide` FLOAT,
    `year` YEAR,
    INDEX Iindx_subin_homicide (subin_homicide)
  );

  CREATE TABLE `RacialAncestrySuicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `Racial_group_id` INTEGER,
    `occurrences` INTEGER,
    `population` INTEGER,
    `subin_suicide` FLOAT,
    `year` YEAR,
    INDEX Iindx_subin_suicide (subin_suicide)
  );

  CREATE TABLE `VulnerableGroupsHomicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `vulnerable_group_id` INTEGER,
    `occurrences` INTEGER,
    `subin_vulnerable_groups_homicide` FLOAT,
    `year` YEAR,
    INDEX Iindxsubin_vulnerable_groups_homicide (subin_vulnerable_groups_homicide)
  );

  CREATE TABLE `VulnerableGroupsSuicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `vulnerable_group_id` INTEGER,
    `occurrences` INTEGER,
    `subin_vulnerable_groups_suicide` FLOAT,
    `year` YEAR,
    INDEX Iindxsubin_vulnerable_groups_suicide (subin_vulnerable_groups_suicide)
  );

  CREATE TABLE `ethnic_Influencer`  (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `date_of_test` DATE,
    `have_Ethia` BOOLEAN,
    `cases` INTEGER,
    `students_tested` INTEGER,
    `ethnic_Influencer_indicator` FLOAT,
    INDEX idx_ethnic_Influencer_indicato (ethnic_Influencer_indicator)
  );

  CREATE TABLE `books_for_family_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `books_for_family` INTEGER,
    `date_of_test` DATE,
    `students_tested` INTEGER,
    `books_for_family_indicator` FLOAT,
    INDEX idx_books_for_family_indicator (books_for_family_indicator)
  );

  CREATE TABLE `Stu_read_for_pleasure_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `hours_of_reading` INTEGER,
    `date_of_test` DATE,
    `students_tested` INTEGER,
    `Stu_read_for_pleasure_indicator` FLOAT,
    INDEX idx_Stu_read_for_pleasure_indicator (Stu_read_for_pleasure_indicator)
  );

  CREATE TABLE `stu_internet_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `hours_of_dedication` INTEGER,
    `date_of_test` DATE,
    `students_tested` INTEGER,
    `Stu_internet_influence_indicator` FLOAT,
    INDEX idx_Stu_internet_influence_indicator (Stu_internet_influence_indicator)
  );

  CREATE TABLE `CulturalInfluence` (
    `iid` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `ethnic_Influencer_indicator` FLOAT,
    `books_for_family_indicator` FLOAT,
    `Stu_internet_influence_indicator` FLOAT,
    `Stu_read_for_pleasure_indicator` FLOAT,
    `subin_cultural_influence` FLOAT,
    INDEX Iindx_subin_cultural_influence (subin_cultural_influence)
  );

  CREATE TABLE `CulturalViolenceIndex` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER NOT NULL,
    `year` year,
    `subin_Ancestry_homicide` FLOAT,
    `subin_Ancestry_suicide` FLOAT,
    `subin_vulnerable_groups_homicide` FLOAT,
    `subin_vulnerability_suicide` FLOAT,
    `subin_cultural_influence` FLOAT,
    `cultural_violence_index` FLOAT,
    INDEX Iindx_cultural_violence_index (cultural_violence_index)
  );

  CREATE TABLE `HealthAccess` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `year` YEAR,
    `first_level_centers_per_100k` FLOAT,
    `second_level_centers_per_100k` FLOAT,
    `third_level_centers_per_100k` FLOAT,
    `subin_health` FLOAT
  );

  CREATE TABLE `EducationAccess` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `year` year,
    `basic_education_centers_per_100k` FLOAT,
    `middle_education_centers_per_100k` FLOAT,
    `technical_professional_centers_per_100k` FLOAT,
    `university_centers_per_100k` FLOAT,
    `subin_education` FLOAT
  );

  CREATE TABLE `Inequality` (
    `municipality_id` INTEGER PRIMARY KEY,
    `gini_index` FLOAT
  );

  CREATE TABLE `Poverty` (
    `municipality_id` INTEGER PRIMARY KEY,
    `multidimensional_poverty_index` FLOAT,
    `monetary_poverty_index` FLOAT,
    `extreme_monetary_poverty_index` FLOAT,
    `unsatisfied_basic_needs_index` FLOAT,
    `subin_poverty` FLOAT
  );

  CREATE TABLE `VidegamesconsoleOwnershipcases` (
    `id` INTEGER PRIMARY KEY,
    `date_of_test` DATE,
    `municipality_id` INTEGER,
    `Student_ID` VARCHAR(255),
    `VidegamesconsoleOwnershipcases` BOOLEAN
  );

  CREATE TABLE `VidegamesconsoleOwnership_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `date_of_test` DATE,
    `count_cases_true` INTEGER,
    `count_cases_false` INTEGER,
    `subin_VidegamesconsoleOwnership` FLOAT
  );

  CREATE TABLE `CarOwnershipcases` (
    `id` INTEGER PRIMARY KEY,
    `date_of_test` DATE,
    `municipality_id` INTEGER,
    `Student_ID` VARCHAR(255),
    `carOwnershipcases` BOOLEAN
  );

  CREATE TABLE `CarOwnership_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `date_of_test` DATE,
    `count_cases_true` INTEGER,
    `count_cases_false` INTEGER,
    `subin_carOwnership` FLOAT
  );

  CREATE TABLE `WashingMachineOwnership` (
    `id` INTEGER PRIMARY KEY,
    `date_of_test` DATE,
    `municipality_id` INTEGER,
    `Student_ID` VARCHAR(255),
    `WashingMachineOwnershipcases` BOOLEAN
  );

  CREATE TABLE `WashingMachineOwnership_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `date_of_test` DATE,
    `count_cases_true` INTEGER,
    `count_cases_false` INTEGER,
    `subin_washing_machine` FLOAT
  );

  CREATE TABLE `InternetAccess` (
    `id` INTEGER PRIMARY KEY,
    `date_of_test` DATE,
    `municipality_id` INTEGER,
    `Student_ID` VARCHAR(255),
    `Internet_access` BOOLEAN
  );

  CREATE TABLE `InternetAccess_influence` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `date_of_test` DATE,
    `count_cases_true` INTEGER,
    `count_cases_false` INTEGER,
    `subin_Internet_access` FLOAT
  );

  CREATE TABLE `FloorType` (
    `id` INTEGER PRIMARY KEY,
    `FloorType` VARCHAR(255)
  );

  CREATE TABLE `FloorType_Municipalities` (
    `id` INTEGER PRIMARY KEY,
    `date_of_test` DATE,
    `municipality_id` INTEGER,
    `Student_ID` VARCHAR(255),
    `FloorType` INTEGER
  );

  CREATE TABLE `FloorType_subindicator` (
    `id` INTEGER PRIMARY KEY,
    `municipality_id` INTEGER,
    `case` int,
    `count_case` int,
    `FloorType_subindicator` FLOAT
  );

  CREATE TABLE `RoomPerBedroom` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
     `year` YEAR,
    `measurement` INTEGER,
    `subin_room_per_bedroom` INTEGER
  );

  CREATE TABLE `WorkStatus` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
     `year` YEAR,
    `measurement` BOOLEAN,
    `subin_work_status` INTEGER
  );

  CREATE TABLE `WorkHours` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
     `year` YEAR,
    `measurement` INTEGER,
    `subin_work_hours` INTEGER
  );

  CREATE TABLE `structutural_influencers` (
    `id` INTEGER PRIMARY KEY,
    `subin_room_per_bedroom` FLOAT,
    `subin_videgames_console` FLOAT,
    `subin_work_status` FLOAT,
    `subin_work_hours` FLOAT,
    `subin_washing_machine` FLOAT,
    `subin_floor_type` FLOAT,
    `subin_Internet_access` FLOAT,
    `subin_stuctural_influencers` FLOAT
  );

  CREATE TABLE `StructuralViolenceIndex` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `subin_education_access` FLOAT,
    `subin_health_access` FLOAT,
    `subin_inequality` FLOAT,
    `subin_poverty` FLOAT,
    `subin_structural_influencers` FLOAT,
    `structural_violence_index` FLOAT
  );

  CREATE TABLE `GenderInformation` (
    `id` INTEGER PRIMARY KEY,
    `gender_name` VARCHAR(255),
    `Municipalities_id` FLOAT,
    `population_by_gender` FLOAT,
    `year` YEAR
  );

  CREATE TABLE `PartnerHomicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `gender_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `homicide_rate_per_100k` FLOAT,
    `subin_partner_homicide` FLOAT
  );

  CREATE TABLE `RomanticSuicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `gender_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `suicide_rate_per_100k` FLOAT,
    `subin_romantic_suicide` FLOAT
  );

  CREATE TABLE `GenderVulnerabilityHomicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `vulnerability_factor_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `homicide_rate_per_100k` FLOAT,
    `subin_vulnerability_homicide` FLOAT
  );

  CREATE TABLE `GenderVulnerabilitySuicideViolence` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `vulnerability_factor_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `suicide_rate_per_100k` FLOAT,
    `subin_vulnerability_suicide` FLOAT
  );

  CREATE TABLE `GenderHomicideRate` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `gender_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `homicide_rate_per_100k` FLOAT,
    `subin_gender_homicide` FLOAT
  );

  CREATE TABLE `DomesticViolenceRate` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `gender_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `domestic_violence_rate_per_100k` FLOAT,
    `subin_domestic_violence` FLOAT
  );

  CREATE TABLE `IcfesResultsAnalysis` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `gender_id` INTEGER,
    `year` YEAR,
    `average_math_score` FLOAT,
    `average_natural_sciences_score` FLOAT,
    `average_social_and_citizenship_score` FLOAT,
    `average_languages_score` FLOAT,
    `average_foreign_language_score` FLOAT,
    `average_global_score` FLOAT,
    `subin_global_score` FLOAT
  );

  CREATE TABLE `GenderViolenceIndex` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `subin_partner_homicide` FLOAT,
    `subin_romantic_suicide` FLOAT,
    `subin_vulnerability_homicide` FLOAT,
    `subin_vulnerability_suicide` FLOAT,
    `subin_gender_homicide` FLOAT,
    `subin_domestic_violence` FLOAT,
    `gender_violence_index` FLOAT
  );

  CREATE TABLE `PhysicalViolenceInformation` (
    `id` INTEGER PRIMARY KEY,
    `physical_violence_type` VARCHAR(255),
    `Municipalities_id` INTEGER,
    `cases` INTEGER,
    `year` YEAR
  );

  CREATE TABLE `HomicideRate` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `homicide_rate_per_100k` INTEGER,
    `subin_homicide` INTEGER
  );

  CREATE TABLE `SuicideRate` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `suicide_rate_per_100k` FLOAT,
    `subin_suicide` INTEGER
  );

  CREATE TABLE `DomesticViolenceNonGenderBAsedRate` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `domestic_violence_rate_per_100k` INTEGER,
    `subin_domestic_violence` INTEGER
  );

  CREATE TABLE `ViolenceAgainstChildrenAndYouth` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `violence_against_children_and_youth_rate_per_100k` INTEGER,
    `subin_violence_against_children_and_youth` INTEGER
  );

  CREATE TABLE `ChildAbuse` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `cases` INTEGER,
    `child_abuse_rate_per_100k` INTEGER,
    `subin_child_abuse` INTEGER
  );

  CREATE TABLE `PhysicalViolenceIndex` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` YEAR,
    `subin_homicide` INTEGER,
    `subin_suicide` INTEGER,
    `subin_domestic_violence` INTEGER,
    `subin_violence_against_children_and_youth` INTEGER,
    `subin_child_abuse` INTEGER,
    `physical_violence_index` INTEGER
  );

  CREATE TABLE `FinalViolenceIndex` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` year,
    `subin_structural_violence` INTEGER,
    `subin_cultural_violence` INTEGER,
    `subin_gender_violence` INTEGER,
    `subin_physical_violence` INTEGER,
    `final_violence_index` INTEGER
  );

  CREATE TABLE `IcfesTestResults` (
    `id` INTEGER PRIMARY KEY,
    `Municipalities_id` INTEGER,
    `year` year,
    `final_violence_index` INTEGER,
    `math_performance` INTEGER,
    `natural_sciences_performance` INTEGER,
    `social_and_citizenship_performance` INTEGER,
    `languages_performance` INTEGER,
    `foreign_language_performance` INTEGER,
    `global_performance` INTEGER
  );

  ALTER TABLE `PopulationANDYearInformation` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `Saber_reference` ADD FOREIGN KEY (`municipality_where_stu_reside`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `HealthCenters` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `EducationalCenters` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `RacialAncestryHomicideViolence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `RacialAncestryHomicideViolence` ADD FOREIGN KEY (`Racial_group_id`) REFERENCES `Racial_Ancenstry` (`id`);

  ALTER TABLE `RacialAncestryHomicideViolence` ADD FOREIGN KEY (`population`) REFERENCES `PopulationANDYearInformation` (`population`);

  ALTER TABLE `RacialAncestryHomicideViolence` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `RacialAncestrySuicideViolence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `RacialAncestrySuicideViolence` ADD FOREIGN KEY (`Racial_group_id`) REFERENCES `Racial_Ancenstry` (`id`);

  ALTER TABLE `RacialAncestrySuicideViolence` ADD FOREIGN KEY (`population`) REFERENCES `PopulationANDYearInformation` (`population`);

  ALTER TABLE `RacialAncestrySuicideViolence` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `VulnerableGroupsHomicideViolence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `VulnerableGroupsHomicideViolence` ADD FOREIGN KEY (`vulnerable_group_id`) REFERENCES `VulnerableGroups` (`id`);

  ALTER TABLE `VulnerableGroupsHomicideViolence` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `VulnerableGroupsSuicideViolence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `VulnerableGroupsSuicideViolence` ADD FOREIGN KEY (`vulnerable_group_id`) REFERENCES `VulnerableGroups` (`id`);

  ALTER TABLE `VulnerableGroupsSuicideViolence` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `ethnic_Influencer` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `ethnic_Influencer` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `ethnic_Influencer` ADD FOREIGN KEY (`students_tested`) REFERENCES `Saber_reference` (`students_tested`);

  ALTER TABLE `books_for_family_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Saber_reference` (`municipality_where_stu_reside`);

  ALTER TABLE `books_for_family_influence` ADD FOREIGN KEY (`books_for_family`) REFERENCES `books_for_family` (`id`);

  ALTER TABLE `books_for_family_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `books_for_family_influence` ADD FOREIGN KEY (`students_tested`) REFERENCES `Saber_reference` (`students_tested`);

  ALTER TABLE `Stu_read_for_pleasure_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Saber_reference` (`municipality_where_stu_reside`);

  ALTER TABLE `Stu_read_for_pleasure_influence` ADD FOREIGN KEY (`hours_of_reading`) REFERENCES `Stu_read_for_pleasure` (`id`);

  ALTER TABLE `Stu_read_for_pleasure_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `Stu_read_for_pleasure_influence` ADD FOREIGN KEY (`students_tested`) REFERENCES `Saber_reference` (`students_tested`);

  ALTER TABLE `stu_internet_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Saber_reference` (`municipality_where_stu_reside`);

  ALTER TABLE `stu_internet_influence` ADD FOREIGN KEY (`hours_of_dedication`) REFERENCES `Stu_internet_dedication` (`id`);

  ALTER TABLE `stu_internet_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `stu_internet_influence` ADD FOREIGN KEY (`students_tested`) REFERENCES `Saber_reference` (`students_tested`);

  ALTER TABLE `CulturalInfluence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`id`);

  ALTER TABLE `CulturalInfluence` ADD FOREIGN KEY (`ethnic_Influencer_indicator`) REFERENCES `ethnic_Influencer` (`ethnic_Influencer_indicator`);

  ALTER TABLE `CulturalInfluence` ADD FOREIGN KEY (`books_for_family_indicator`) REFERENCES `books_for_family_influence` (`books_for_family_indicator`);

  ALTER TABLE `CulturalInfluence` ADD FOREIGN KEY (`Stu_internet_influence_indicator`) REFERENCES `stu_internet_influence` (`Stu_internet_influence_indicator`);

  ALTER TABLE `CulturalInfluence` ADD FOREIGN KEY (`Stu_read_for_pleasure_indicator`) REFERENCES `Stu_read_for_pleasure_influence` (`Stu_read_for_pleasure_indicator`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`subin_Ancestry_homicide`) REFERENCES `RacialAncestryHomicideViolence` (`subin_homicide`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`subin_Ancestry_suicide`) REFERENCES `RacialAncestrySuicideViolence` (`subin_suicide`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`subin_vulnerable_groups_homicide`) REFERENCES `VulnerableGroupsHomicideViolence` (`subin_vulnerable_groups_homicide`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`subin_vulnerability_suicide`) REFERENCES `VulnerableGroupsSuicideViolence` (`subin_vulnerable_groups_suicide`);

  ALTER TABLE `CulturalViolenceIndex` ADD FOREIGN KEY (`subin_cultural_influence`) REFERENCES `CulturalInfluence` (`subin_cultural_influence`);

  ALTER TABLE `HealthAccess` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `HealthAccess` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `EducationAccess` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `EducationAccess` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `Inequality` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `Poverty` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `VidegamesconsoleOwnershipcases` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `VidegamesconsoleOwnershipcases` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `VidegamesconsoleOwnershipcases` ADD FOREIGN KEY (`Student_ID`) REFERENCES `Saber_reference` (`Student_ID`);

  ALTER TABLE `VidegamesconsoleOwnership_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `VidegamesconsoleOwnership_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `CarOwnershipcases` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `CarOwnershipcases` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `CarOwnershipcases` ADD FOREIGN KEY (`Student_ID`) REFERENCES `Saber_reference` (`Student_ID`);

  ALTER TABLE `CarOwnership_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `CarOwnership_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `WashingMachineOwnership` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `WashingMachineOwnership` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `WashingMachineOwnership` ADD FOREIGN KEY (`Student_ID`) REFERENCES `Saber_reference` (`Student_ID`);

  ALTER TABLE `WashingMachineOwnership_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `WashingMachineOwnership_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `InternetAccess` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `InternetAccess` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `InternetAccess` ADD FOREIGN KEY (`Student_ID`) REFERENCES `Saber_reference` (`Student_ID`);

  ALTER TABLE `InternetAccess_influence` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `InternetAccess_influence` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `FloorType_Municipalities` ADD FOREIGN KEY (`date_of_test`) REFERENCES `Saber_reference` (`date_of_test`);

  ALTER TABLE `FloorType_Municipalities` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `FloorType_Municipalities` ADD FOREIGN KEY (`Student_ID`) REFERENCES `Saber_reference` (`Student_ID`);

  ALTER TABLE `FloorType_Municipalities` ADD FOREIGN KEY (`FloorType`) REFERENCES `FloorType` (`id`);

  ALTER TABLE `FloorType_subindicator` ADD FOREIGN KEY (`municipality_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `FloorType_subindicator` ADD FOREIGN KEY (`case`) REFERENCES `FloorType` (`id`);

  ALTER TABLE `RoomPerBedroom` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `WorkStatus` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `WorkHours` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_room_per_bedroom`) REFERENCES `RoomPerBedroom` (`subin_room_per_bedroom`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_videgames_console`) REFERENCES `VidegamesconsoleOwnership_influence` (`subin_VidegamesconsoleOwnership`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_work_status`) REFERENCES `WorkStatus` (`subin_work_status`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_work_hours`) REFERENCES `WorkHours` (`subin_work_hours`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_washing_machine`) REFERENCES `WashingMachineOwnership_influence` (`subin_washing_machine`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_floor_type`) REFERENCES `FloorType_subindicator` (`FloorType_subindicator`);

  ALTER TABLE `structutural_influencers` ADD FOREIGN KEY (`subin_Internet_access`) REFERENCES `InternetAccess_influence` (`subin_Internet_access`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`year`) REFERENCES `PopulationANDYearInformation` (`year`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`subin_education_access`) REFERENCES `EducationAccess` (`subin_education`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`subin_health_access`) REFERENCES `HealthAccess` (`subin_health`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`subin_inequality`) REFERENCES `Inequality` (`gini_index`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`subin_poverty`) REFERENCES `Poverty` (`subin_poverty`);

  ALTER TABLE `StructuralViolenceIndex` ADD FOREIGN KEY (`subin_structural_influencers`) REFERENCES `structutural_influencers` (`subin_stuctural_influencers`);

  ALTER TABLE `GenderInformation` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `PartnerHomicideViolence` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `PartnerHomicideViolence` ADD FOREIGN KEY (`gender_id`) REFERENCES `GenderInformation` (`id`);

  ALTER TABLE `RomanticSuicideViolence` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `RomanticSuicideViolence` ADD FOREIGN KEY (`gender_id`) REFERENCES `GenderInformation` (`id`);

  ALTER TABLE `GenderVulnerabilityHomicideViolence` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `GenderVulnerabilityHomicideViolence` ADD FOREIGN KEY (`vulnerability_factor_id`) REFERENCES `VulnerableGroups` (`id`);

  ALTER TABLE `GenderVulnerabilitySuicideViolence` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `GenderVulnerabilitySuicideViolence` ADD FOREIGN KEY (`vulnerability_factor_id`) REFERENCES `VulnerableGroups` (`id`);

  ALTER TABLE `GenderHomicideRate` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `GenderHomicideRate` ADD FOREIGN KEY (`gender_id`) REFERENCES `GenderInformation` (`id`);

  ALTER TABLE `DomesticViolenceRate` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `DomesticViolenceRate` ADD FOREIGN KEY (`gender_id`) REFERENCES `GenderInformation` (`id`);

  ALTER TABLE `IcfesResultsAnalysis` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `IcfesResultsAnalysis` ADD FOREIGN KEY (`gender_id`) REFERENCES `GenderInformation` (`id`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_partner_homicide`) REFERENCES `PartnerHomicideViolence` (`subin_partner_homicide`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_romantic_suicide`) REFERENCES `RomanticSuicideViolence` (`subin_romantic_suicide`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_vulnerability_homicide`) REFERENCES `GenderVulnerabilityHomicideViolence` (`subin_vulnerability_homicide`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_vulnerability_suicide`) REFERENCES `GenderVulnerabilitySuicideViolence` (`subin_vulnerability_suicide`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_gender_homicide`) REFERENCES `GenderHomicideRate` (`subin_gender_homicide`);

  ALTER TABLE `GenderViolenceIndex` ADD FOREIGN KEY (`subin_domestic_violence`) REFERENCES `DomesticViolenceRate` (`subin_domestic_violence`);

  ALTER TABLE `PhysicalViolenceInformation` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `HomicideRate` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `SuicideRate` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `DomesticViolenceNonGenderBAsedRate` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `ViolenceAgainstChildrenAndYouth` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `ChildAbuse` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`subin_homicide`) REFERENCES `HomicideRate` (`subin_homicide`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`subin_suicide`) REFERENCES `SuicideRate` (`subin_suicide`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`subin_domestic_violence`) REFERENCES `DomesticViolenceRate` (`subin_domestic_violence`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`subin_violence_against_children_and_youth`) REFERENCES `ViolenceAgainstChildrenAndYouth` (`subin_violence_against_children_and_youth`);

  ALTER TABLE `PhysicalViolenceIndex` ADD FOREIGN KEY (`subin_child_abuse`) REFERENCES `ChildAbuse` (`subin_child_abuse`);

  ALTER TABLE `FinalViolenceIndex` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `FinalViolenceIndex` ADD FOREIGN KEY (`subin_structural_violence`) REFERENCES `StructuralViolenceIndex` (`structural_violence_index`);

  ALTER TABLE `FinalViolenceIndex` ADD FOREIGN KEY (`subin_cultural_violence`) REFERENCES `CulturalViolenceIndex` (`cultural_violence_index`);

  ALTER TABLE `FinalViolenceIndex` ADD FOREIGN KEY (`subin_gender_violence`) REFERENCES `GenderViolenceIndex` (`gender_violence_index`);

  ALTER TABLE `FinalViolenceIndex` ADD FOREIGN KEY (`subin_physical_violence`) REFERENCES `PhysicalViolenceIndex` (`physical_violence_index`);

  ALTER TABLE `IcfesTestResults` ADD FOREIGN KEY (`Municipalities_id`) REFERENCES `Municipalities` (`Municipalities_id`);

  ALTER TABLE `IcfesTestResults` ADD FOREIGN KEY (`final_violence_index`) REFERENCES `FinalViolenceIndex` (`final_violence_index`);



