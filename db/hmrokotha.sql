-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hamrokotha
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add contact',1,'add_contact'),(2,'Can change contact',1,'change_contact'),(3,'Can delete contact',1,'delete_contact'),(4,'Can view contact',1,'view_contact'),(5,'Can add login',2,'add_login'),(6,'Can change login',2,'change_login'),(7,'Can delete login',2,'delete_login'),(8,'Can view login',2,'view_login'),(9,'Can add image',3,'add_image'),(10,'Can change image',3,'change_image'),(11,'Can delete image',3,'delete_image'),(12,'Can view image',3,'view_image'),(13,'Can add log entry',4,'add_logentry'),(14,'Can change log entry',4,'change_logentry'),(15,'Can delete log entry',4,'delete_logentry'),(16,'Can view log entry',4,'view_logentry'),(17,'Can add permission',5,'add_permission'),(18,'Can change permission',5,'change_permission'),(19,'Can delete permission',5,'delete_permission'),(20,'Can view permission',5,'view_permission'),(21,'Can add group',6,'add_group'),(22,'Can change group',6,'change_group'),(23,'Can delete group',6,'delete_group'),(24,'Can view group',6,'view_group'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add content type',8,'add_contenttype'),(30,'Can change content type',8,'change_contenttype'),(31,'Can delete content type',8,'delete_contenttype'),(32,'Can view content type',8,'view_contenttype'),(33,'Can add session',9,'add_session'),(34,'Can change session',9,'change_session'),(35,'Can delete session',9,'delete_session'),(36,'Can view session',9,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$390000$sAUoMkNA7PWi5zAwjCR8l4$RTBPkciAqG8TQSTxE7lEgcqLIe406RgGN6q9hNWOo/o=','2023-04-25 14:57:51.860167',1,'HamroKotha','','','',1,1,'2023-04-25 14:57:39.912122'),(2,'pbkdf2_sha256$600000$QjX2cvhxDB0dX6JfDseh9y$AxMEYGAv+iwoaDJ0y/x57zEGqrD+U/xFepQuyF6JBk8=','2023-05-15 05:33:47.681689',0,'bipin','','','bipinpoudel406@gmail.com',0,1,'2023-05-15 05:33:45.793257');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (4,'admin','logentry'),(6,'auth','group'),(5,'auth','permission'),(7,'auth','user'),(8,'contenttypes','contenttype'),(1,'home','contact'),(3,'home','image'),(2,'home','login'),(9,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-25 12:53:12.461882'),(2,'auth','0001_initial','2023-04-25 12:53:12.932296'),(3,'admin','0001_initial','2023-04-25 12:53:13.061814'),(4,'admin','0002_logentry_remove_auto_add','2023-04-25 12:53:13.079651'),(5,'admin','0003_logentry_add_action_flag_choices','2023-04-25 12:53:13.096602'),(6,'contenttypes','0002_remove_content_type_name','2023-04-25 12:53:13.227251'),(7,'auth','0002_alter_permission_name_max_length','2023-04-25 12:53:13.314019'),(8,'auth','0003_alter_user_email_max_length','2023-04-25 12:53:13.379843'),(9,'auth','0004_alter_user_username_opts','2023-04-25 12:53:13.400786'),(10,'auth','0005_alter_user_last_login_null','2023-04-25 12:53:13.478605'),(11,'auth','0006_require_contenttypes_0002','2023-04-25 12:53:13.484100'),(12,'auth','0007_alter_validators_add_error_messages','2023-04-25 12:53:13.503051'),(13,'auth','0008_alter_user_username_max_length','2023-04-25 12:53:13.576568'),(14,'auth','0009_alter_user_last_name_max_length','2023-04-25 12:53:13.646381'),(15,'auth','0010_alter_group_name_max_length','2023-04-25 12:53:13.686117'),(16,'auth','0011_update_proxy_permissions','2023-04-25 12:53:13.703079'),(17,'auth','0012_alter_user_first_name_max_length','2023-04-25 12:53:13.778403'),(18,'home','0001_initial','2023-04-25 12:53:13.806301'),(19,'home','0002_alter_contact_fullname','2023-04-25 12:53:13.849978'),(20,'home','0003_login','2023-04-25 12:53:13.873101'),(21,'home','0004_rename_login_signup','2023-04-25 12:53:13.910160'),(22,'home','0005_delete_signup','2023-04-25 12:53:13.925802'),(23,'home','0006_signup','2023-04-25 12:53:13.950730'),(24,'home','0007_login','2023-04-25 12:53:13.975664'),(25,'home','0008_remove_signup_password_remove_signup_username','2023-04-25 12:53:14.015558'),(26,'home','0009_delete_signup_alter_login_username','2023-04-25 12:53:14.064929'),(27,'home','0010_alter_login_username','2023-04-25 12:53:14.105960'),(28,'home','0011_image','2023-04-25 12:53:14.131893'),(29,'home','0012_alter_image_img','2023-04-25 12:53:14.139869'),(30,'home','0013_post_delete_image','2023-04-25 12:53:14.175543'),(31,'home','0014_image_delete_post','2023-04-25 12:53:14.208500'),(32,'home','0015_signup','2023-04-25 12:53:14.234431'),(33,'home','0016_delete_signup_alter_image_img','2023-04-25 12:53:14.252154'),(34,'home','0017_alter_image_table','2023-04-25 12:53:14.276090'),(35,'home','0018_alter_image_table','2023-04-25 12:53:14.295039'),(36,'home','0019_image_phone','2023-04-25 12:53:14.317977'),(37,'home','0020_image_desc_image_propertytype','2023-04-25 12:53:14.351076'),(38,'home','0021_alter_image_desc','2023-04-25 12:53:14.394546'),(39,'home','0022_remove_image_desc','2023-04-25 12:53:14.424335'),(40,'home','0023_image_descp','2023-04-25 12:53:14.446273'),(41,'home','0024_remove_image_descp_alter_image_propertytype','2023-04-25 12:53:14.500802'),(42,'home','0025_alter_contact_desc','2023-04-25 12:53:14.544737'),(43,'home','0026_remove_image_propertytype','2023-04-25 12:53:14.564682'),(44,'home','0027_alter_contact_desc','2023-04-25 12:53:14.576652'),(45,'home','0028_alter_contact_desc','2023-04-25 12:53:14.584630'),(46,'home','0029_image_descp_image_propertytype','2023-04-25 12:53:14.634500'),(47,'sessions','0001_initial','2023-04-25 12:53:14.676779'),(48,'home','0030_alter_image_table','2023-04-25 14:35:19.910935'),(49,'home','0031_alter_image_table','2023-04-25 14:36:33.204552'),(50,'home','0032_alter_image_phone','2023-05-13 11:50:05.170577'),(51,'home','0033_alter_image_phone','2023-05-13 11:51:24.293127');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('bc9gm14pwxqjxxk2fog5sr2ack6y1f1w','.eJxVjMsOwiAQRf-FtSHAVB4u3fcbmpkBpGogKe3K-O_apAvd3nPOfYkJt7VMW0_LNEdxEUacfjdCfqS6g3jHemuSW12XmeSuyIN2ObaYntfD_Tso2Mu3DsEjnTkmy0olIksQQbGBQTN6j6y8DpGYkABJG3aYwYIaXMjOZhTvDwq1ONk:1pyQqB:Z654cJKrSyoVPdMNW1NoSGU5la9exv_5ixiejKF4n80','2023-05-29 05:33:47.702819'),('hjhc42lq6c5ahcqpgupxe1feg2387dot','.eJxVjEEOwiAQRe_C2hCgwBSX7j0DGZhBqoYmpV0Z765NutDtf-_9l4i4rTVunZc4kTgLLU6_W8L84LYDumO7zTLPbV2mJHdFHrTL60z8vBzu30HFXr-1sRmwIDhryoCgAHBwwVKggqx90GwSFmeDgeBpLAYSeJVpzMp5Dkq8P-HwN7k:1prK75:tBs9M7RYh8B-kNmeaZ-m6Otv9eayAynBbm0HrAVM40w','2023-05-09 14:57:51.865634');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_contact`
--

DROP TABLE IF EXISTS `home_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(122) NOT NULL,
  `fullname` varchar(122) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_contact`
--

LOCK TABLES `home_contact` WRITE;
/*!40000 ALTER TABLE `home_contact` DISABLE KEYS */;
INSERT INTO `home_contact` VALUES (1,'bipinpoudel406@gmail.com','BIPIN POUDEL','because why useful message djamgo python hijack','2023-05-16'),(2,'aatreyason@yahoo.com','SB Aatreya','sdsg','2023-05-16');
/*!40000 ALTER TABLE `home_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_image`
--

DROP TABLE IF EXISTS `home_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_image` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `img` varchar(100) NOT NULL,
  `phone` int NOT NULL,
  `descp` varchar(50) NOT NULL,
  `propertytype` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_image`
--

LOCK TABLES `home_image` WRITE;
/*!40000 ALTER TABLE `home_image` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `home_login`
--

DROP TABLE IF EXISTS `home_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `home_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(122) NOT NULL,
  `password` varchar(121) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `home_login`
--

LOCK TABLES `home_login` WRITE;
/*!40000 ALTER TABLE `home_login` DISABLE KEYS */;
/*!40000 ALTER TABLE `home_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-16 12:17:54
