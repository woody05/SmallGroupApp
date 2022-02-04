-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.5.8-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for prayer_request
CREATE DATABASE IF NOT EXISTS `prayer_request` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `prayer_request`;

-- Dumping structure for table prayer_request.category
CREATE TABLE IF NOT EXISTS `category` (
  `Category_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.comments
CREATE TABLE IF NOT EXISTS `comments` (
  `Comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) NOT NULL,
  `Prayer_request_id` int(11) NOT NULL,
  `Comment` varchar(5000) NOT NULL DEFAULT '',
  `Date_Added` datetime NOT NULL,
  PRIMARY KEY (`Comment_id`),
  KEY `FK_prayer_request_comments` (`Prayer_request_id`),
  KEY `FK_users_comments` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.prayer_request
CREATE TABLE IF NOT EXISTS `prayer_request` (
  `Prayer_Request_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(22) NOT NULL DEFAULT '0',
  `Description` varchar(1000) DEFAULT NULL,
  `IsAnswered` tinyint(1) NOT NULL DEFAULT 0,
  `Category_id` int(11) DEFAULT NULL,
  `Date_Added` date NOT NULL,
  `Date_Answered` date DEFAULT NULL,
  `added_by_user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Prayer_Request_id`),
  KEY `FK_prayer_request_category` (`Category_id`),
  KEY `FK_prayer_request_users` (`added_by_user_id`),
  CONSTRAINT `FK_prayer_request_category` FOREIGN KEY (`Category_id`) REFERENCES `category` (`Category_id`),
  CONSTRAINT `FK_prayer_request_users` FOREIGN KEY (`added_by_user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(50) NOT NULL,
  `Email_address` varchar(50) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  `is_active` int(11) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `salt` varchar(50) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` enum('male','female') DEFAULT NULL,
  `recieve_email` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
