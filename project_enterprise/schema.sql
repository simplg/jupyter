CREATE DATABASE  IF NOT EXISTS `simplon` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `simplon`;
-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: simplon
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carreer_plan`
--

DROP TABLE IF EXISTS `carreer_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carreer_plan` (
  `cap_id` int NOT NULL AUTO_INCREMENT,
  `cap_plan` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cap_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `certification`
--

DROP TABLE IF EXISTS `certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `certification` (
  `cert_id` int NOT NULL AUTO_INCREMENT,
  `cert_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cert_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `ctr_id` int NOT NULL AUTO_INCREMENT,
  `ctr_name` varchar(42) DEFAULT NULL,
  PRIMARY KEY (`ctr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `database`
--

DROP TABLE IF EXISTS `database`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `database` (
  `db_id` int NOT NULL AUTO_INCREMENT,
  `db_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`db_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `education`
--

DROP TABLE IF EXISTS `education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `education` (
  `edu_id` int NOT NULL AUTO_INCREMENT,
  `edu_title` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`edu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employment_sector`
--

DROP TABLE IF EXISTS `employment_sector`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment_sector` (
  `sec_id` int NOT NULL AUTO_INCREMENT,
  `sec_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employment_status`
--

DROP TABLE IF EXISTS `employment_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employment_status` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `emp_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `how_many_companies`
--

DROP TABLE IF EXISTS `how_many_companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `how_many_companies` (
  `mcp_id` int NOT NULL AUTO_INCREMENT,
  `mcp_many_companies` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`mcp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `job_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `largest_city`
--

DROP TABLE IF EXISTS `largest_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `largest_city` (
  `pop_id` int NOT NULL AUTO_INCREMENT,
  `pop_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `looking_job`
--

DROP TABLE IF EXISTS `looking_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `looking_job` (
  `look_id` int NOT NULL AUTO_INCREMENT,
  `look_job` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`look_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `other_database`
--

DROP TABLE IF EXISTS `other_database`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `other_database` (
  `db_id` int NOT NULL,
  `sgi_id` int NOT NULL,
  PRIMARY KEY (`db_id`,`sgi_id`),
  KEY `sgi_id` (`sgi_id`),
  CONSTRAINT `other_database_ibfk_1` FOREIGN KEY (`db_id`) REFERENCES `database` (`db_id`),
  CONSTRAINT `other_database_ibfk_2` FOREIGN KEY (`sgi_id`) REFERENCES `sondage_item` (`sgi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `other_duties`
--

DROP TABLE IF EXISTS `other_duties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `other_duties` (
  `job_id` int NOT NULL,
  `sgi_id` int NOT NULL,
  PRIMARY KEY (`job_id`,`sgi_id`),
  KEY `sgi_id` (`sgi_id`),
  CONSTRAINT `other_duties_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `job` (`job_id`),
  CONSTRAINT `other_duties_ibfk_2` FOREIGN KEY (`sgi_id`) REFERENCES `sondage_item` (`sgi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sondage`
--

DROP TABLE IF EXISTS `sondage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sondage` (
  `sdg_id` int NOT NULL AUTO_INCREMENT,
  `sdg_year` smallint DEFAULT NULL,
  PRIMARY KEY (`sdg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sondage_item`
--

DROP TABLE IF EXISTS `sondage_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sondage_item` (
  `sgi_id` int NOT NULL AUTO_INCREMENT,
  `timestamp` datetime DEFAULT NULL,
  `salary_usd` decimal(10,2) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `years_with_db` smallint DEFAULT NULL,
  `manage_staff` tinyint(1) DEFAULT NULL,
  `years_with_job` smallint DEFAULT NULL,
  `other_people` int DEFAULT NULL,
  `company_employee` int DEFAULT NULL,
  `database_servers` int DEFAULT NULL,
  `eduction_computer` tinyint(1) DEFAULT NULL,
  `hours_worked` int DEFAULT NULL,
  `telecommute` int DEFAULT NULL,
  `newest_version` varchar(50) DEFAULT NULL,
  `oldest_version` varchar(50) DEFAULT NULL,
  `gender` enum('male','female','other','na') DEFAULT NULL,
  `sdg_id` int DEFAULT NULL,
  `ctr_id` int DEFAULT NULL,
  `primary_db_id` int DEFAULT NULL,
  `emp_id` int DEFAULT NULL,
  `job_id` int DEFAULT NULL,
  `mcp_id` int DEFAULT NULL,
  `edu_id` int DEFAULT NULL,
  `cert_id` int DEFAULT NULL,
  `pop_id` int DEFAULT NULL,
  `sec_id` int DEFAULT NULL,
  `look_id` int DEFAULT NULL,
  `cap_id` int DEFAULT NULL,
  PRIMARY KEY (`sgi_id`),
  KEY `sdg_id` (`sdg_id`),
  KEY `ctr_id` (`ctr_id`),
  KEY `primary_db_id` (`primary_db_id`),
  KEY `emp_id` (`emp_id`),
  KEY `job_id` (`job_id`),
  KEY `mcp_id` (`mcp_id`),
  KEY `edu_id` (`edu_id`),
  KEY `cert_id` (`cert_id`),
  KEY `pop_id` (`pop_id`),
  KEY `sec_id` (`sec_id`),
  KEY `look_id` (`look_id`),
  KEY `cap_id` (`cap_id`),
  CONSTRAINT `sondage_item_ibfk_1` FOREIGN KEY (`sdg_id`) REFERENCES `sondage` (`sdg_id`),
  CONSTRAINT `sondage_item_ibfk_10` FOREIGN KEY (`sec_id`) REFERENCES `employment_sector` (`sec_id`),
  CONSTRAINT `sondage_item_ibfk_11` FOREIGN KEY (`look_id`) REFERENCES `looking_job` (`look_id`),
  CONSTRAINT `sondage_item_ibfk_12` FOREIGN KEY (`cap_id`) REFERENCES `carreer_plan` (`cap_id`),
  CONSTRAINT `sondage_item_ibfk_2` FOREIGN KEY (`ctr_id`) REFERENCES `country` (`ctr_id`),
  CONSTRAINT `sondage_item_ibfk_3` FOREIGN KEY (`primary_db_id`) REFERENCES `database` (`db_id`),
  CONSTRAINT `sondage_item_ibfk_4` FOREIGN KEY (`emp_id`) REFERENCES `employment_status` (`emp_id`),
  CONSTRAINT `sondage_item_ibfk_5` FOREIGN KEY (`job_id`) REFERENCES `job` (`job_id`),
  CONSTRAINT `sondage_item_ibfk_6` FOREIGN KEY (`mcp_id`) REFERENCES `how_many_companies` (`mcp_id`),
  CONSTRAINT `sondage_item_ibfk_7` FOREIGN KEY (`edu_id`) REFERENCES `education` (`edu_id`),
  CONSTRAINT `sondage_item_ibfk_8` FOREIGN KEY (`cert_id`) REFERENCES `certification` (`cert_id`),
  CONSTRAINT `sondage_item_ibfk_9` FOREIGN KEY (`pop_id`) REFERENCES `largest_city` (`pop_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `tas_id` int NOT NULL AUTO_INCREMENT,
  `tas_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `task_performed`
--

DROP TABLE IF EXISTS `task_performed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_performed` (
  `tas_id` int NOT NULL,
  `sgi_id` int NOT NULL,
  PRIMARY KEY (`tas_id`,`sgi_id`),
  KEY `sgi_id` (`sgi_id`),
  CONSTRAINT `task_performed_ibfk_1` FOREIGN KEY (`tas_id`) REFERENCES `task` (`tas_id`),
  CONSTRAINT `task_performed_ibfk_2` FOREIGN KEY (`sgi_id`) REFERENCES `sondage_item` (`sgi_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-31 14:18:41
