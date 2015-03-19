-- MySQL dump 10.13  Distrib 5.6.23, for Win64 (x86_64)
--
-- Host: localhost    Database: swm_dataset1
-- ------------------------------------------------------
-- Server version	5.6.23-log

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
-- Table structure for table `journal`
--

DROP TABLE IF EXISTS `journal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `journal` (
  `journal_key` int(11) NOT NULL AUTO_INCREMENT,
  `journal_name` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`journal_key`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journal`
--

LOCK TABLES `journal` WRITE;
/*!40000 ALTER TABLE `journal` DISABLE KEYS */;
INSERT INTO `journal` VALUES (1,'Artificial Intelligence'),(2,'International Journal of Computer Vision'),(3,'Journal of Machine Learning Research'),(4,'Evolutionary Computation'),(5,'Computational Linguistics'),(6,'Computer Vision and Image Understanding'),(7,'Machine Learning'),(8,'Natural Computing'),(9,'Neural Networks'),(10,'Pattern Recognition'),(11,'Artificial Life'),(12,'Decision Support Systems'),(13,'Computational Intelligence'),(14,'Expert Systems'),(15,'Fuzzy Sets and Systems'),(16,'Machine Translation'),(17,'Pattern Recognition Letters'),(18,'Neurocomputing'),(19,'Neural Computation'),(20,'Neural Processing Letters'),(21,'Web Intelligence and Agent Systems'),(22,'Computer Supported Cooperative Work'),(23,'Natural Language Engineering'),(24,'IEEE Transactions on Image Processing'),(25,'Computer-Aided Design'),(26,'Computer Aided Geometric Design'),(27,'Graphical Models'),(28,'IEEE Transactions on Multimedia'),(29,'Speech Communication'),(30,'Discrete & Computational Geometry'),(31,'Signal Processing'),(32,'The Visual Computer'),(33,'Data Compression Conference'),(34,'Computer Graphics International'),(35,'Shape Modeling International'),(36,'Symposium on Solid and Physical Modeling'),(37,'Computer Networks'),(38,'IEEE Transactions on Wireless Communications'),(39,'Computer Communications'),(40,'IEEE Transactions on Network and Service Management'),(41,'Peer-to-Peer Networking and Applications'),(42,'Wireless Networks'),(43,'Networks'),(44,'Internet Measurement Conference'),(45,'Ad Hoc Networks'),(46,'Advanced Engineering Informatics'),(47,'GeoInformatica'),(48,'Information Systems'),(49,'Distributed and Parallel Databases'),(50,'Information and Management'),(51,'Information Retrieval'),(52,'International Journal of Geographical Information Science'),(53,'Distributed Computing'),(54,'The Journal of Supercomputing'),(55,'EuroSys'),(56,'International Conference on Supercomputing'),(57,'Cluster Computing'),(58,'European Test Symposium'),(59,'IEEE Transactions on Communications'),(60,'Parallel Computing'),(61,'MICRO'),(62,'IEEE Transactions on Information Forensics and Security'),(63,'Computers & Security'),(64,'Journal of Computer Security'),(65,'Security and Communication Networks'),(66,'USENIX Security Symposium'),(67,'Selected Areas in Cryptography'),(68,'Human computer interaction'),(69,'Interacting with Computers'),(70,'Pervasive and Mobile Computing'),(71,'Personal and Ubiquitous Computing'),(72,'Proceedings of the IEEE'),(73,'Bioinformatics'),(74,'BMC Bioinformatics'),(75,'Briefings in Bioinformatics'),(76,'PLoS Computational Biology'),(77,'IEEE Transactions on Robotics'),(78,'SCIENCE CHINA Information Sciences'),(79,'Frontiers of computer science'),(80,'Cybernetics and Systems'),(81,'IEEE Transactions on Information Technology in Biomedicine'),(82,'Medical Image Analysis'),(83,'Empirical Software Engineering'),(84,'IET Software'),(85,'Journal of Systems and Software'),(86,'Requirements Engineering'),(87,'Software and System Modeling'),(88,'Service Oriented Computing and Applications'),(89,'Software Quality Journal'),(90,'ACM Symposium on User Interface Software and Technology'),(91,'ACM Transactions on Algorithms'),(92,'Algorithmica'),(93,'Computational Complexity'),(94,'Formal Methods in System Design'),(95,'INFORMS Journal on Computing'),(96,'Mathematical Structures in Computer Science'),(97,'Theoretical Computer Science'),(98,'Discrete Applied Mathematics'),(99,'Higher-Order and Symbolic Computation'),(100,'Logical Methods in Computer Science'),(101,'IEEE Conference on Computational Complexity');
/*!40000 ALTER TABLE `journal` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-19  1:16:52
