-- --------------------------------------------------------
-- Host:                         192.168.200.68
-- Server version:               10.0.28-MariaDB-2+b1 - Raspbian testing-staging
-- Server OS:                    debian-linux-gnueabihf
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for prayer_request
CREATE DATABASE IF NOT EXISTS `prayer_request` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `prayer_request`;

-- Dumping structure for table prayer_request.category
CREATE TABLE IF NOT EXISTS `category` (
  `Category_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`Category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

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
  KEY `FK_users_comments` (`User_id`),
  CONSTRAINT `FK_prayer_request_comments` FOREIGN KEY (`Prayer_request_id`) REFERENCES `prayer_request` (`Prayer_Request_id`),
  CONSTRAINT `FK_users_comments` FOREIGN KEY (`User_id`) REFERENCES `users` (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.prayer_request
CREATE TABLE IF NOT EXISTS `prayer_request` (
  `Prayer_Request_id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(22) NOT NULL DEFAULT '0',
  `Description` varchar(1000) DEFAULT NULL,
  `IsAnswered` tinyint(1) NOT NULL DEFAULT '0',
  `Add_By` varchar(50) DEFAULT NULL,
  `Category_id` int(11) DEFAULT NULL,
  `Date_Added` date NOT NULL,
  `Date_Answered` date DEFAULT NULL,
  PRIMARY KEY (`Prayer_Request_id`),
  KEY `FK_prayer_request_category` (`Category_id`),
  CONSTRAINT `FK_prayer_request_category` FOREIGN KEY (`Category_id`) REFERENCES `category` (`Category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table prayer_request.users
CREATE TABLE IF NOT EXISTS `users` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_name` varchar(50) NOT NULL,
  `Email_address` varchar(50) NOT NULL,
  `First_name` varchar(50) NOT NULL,
  `Last_name` varchar(50) NOT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
