-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: mydata
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `register1`
--

DROP TABLE IF EXISTS `register1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register1` (
  `firstname` varchar(45) NOT NULL,
  `lastname` varchar(45) DEFAULT NULL,
  `conatctno` varchar(45) DEFAULT NULL,
  `emailid` varchar(45) NOT NULL COMMENT '\n',
  `SecurityQuestion` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `securityanswer` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`emailid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register1`
--

LOCK TABLES `register1` WRITE;
/*!40000 ALTER TABLE `register1` DISABLE KEYS */;
INSERT INTO `register1` VALUES ('Andy','roman','9876543256','Andy@909','Your hobby','Andy564','Playing'),('Andy','dosuza','9785689535','Andy123','Your city name','12','mumbai'),('Anna','Shaikh','98567444432','anna@','Your favourite game','abcd','Cricket'),('Saniya','Khan','8928790116','farookkhan123','Your city name','1234','mumbai'),('haha','hsj','88978','haha@','Your city name','7676','mumbai'),('11','khan','287289','kahanana','Your pet name','1234','dog'),('Anadiya','khan','12334567','khan','Your hobby','1234','reading'),('Anadiya','khan','9321369690','khan@','Your hobby','1111','Dancing'),('Anadiya','khan','9321369690','khananadiay45@gmail.com','Your city name','1234','mumbai'),('Anadiya','khan','9321369690','khananadiya@786','Your hobby','1234','reading'),('Anadiya','khan','9321369690','khananadiya45@gmail.com','Your hobby','1234','Reading'),('Wasina','khan','8765435678','khanwasina@90','Your hobby','9898','cooking'),('Sam','Khan','2345678912','sam@','Your hobby','1111','Playing'),('SAM','Khan','9823456734','sam@gmail.com','Your hobby','sam123','Playing'),('fhdjau','fea','426234466','sdtwrtyw','Your favourite food name','123','Biryani');
/*!40000 ALTER TABLE `register1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-02-22 21:45:28
