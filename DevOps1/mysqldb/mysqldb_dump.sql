-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: 127.0.0.1    Database: Devops
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `devops_images`
--

DROP TABLE IF EXISTS `devops_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `devops_images` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `image_name` varchar(100) NOT NULL,
  `creation_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `image_path` varchar(100) DEFAULT '/home/tcs/DEVOPS/repo_iso',
  `status` varchar(100) DEFAULT 'disable',
  `ut_link` varchar(100) DEFAULT 'http://10.125.155.107:9090/view/DEVOPS/job/2.TEST_EXECUTION_UT_SO/',
  `ft_link` varchar(100) DEFAULT 'http://10.125.155.107:9090/view/DEVOPS/job/3.TEST_EXECUTION_FT_SO/',
  `Deployed_VM_IP` varchar(100) NOT NULL DEFAULT '-',
  PRIMARY KEY (`image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devops_images`
--

LOCK TABLES `devops_images` WRITE;
/*!40000 ALTER TABLE `devops_images` DISABLE KEYS */;
INSERT INTO `devops_images` VALUES (8,'devops-build-9','2015-06-01 15:11:40','/home/tcs/DEVOPS/repo_iso','disable','http://10.125.155.107:9090/job/2.TEST_EXECUTION_UT_SO/23/','http://10.125.155.107:9090/job/3.TEST_EXECUTION_FT_SO/22/','-'),(9,'devops-build-14','2015-06-01 15:35:58','/home/tcs/DEVOPS/repo_iso','running','http://10.125.155.107:9090/job/2.TEST_EXECUTION_UT_SO/24/','http://10.125.155.107:9090/job/3.TEST_EXECUTION_FT_SO/23/','10.127.150.66');
/*!40000 ALTER TABLE `devops_images` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-06-03 12:22:47
