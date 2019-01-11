SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

/*Database: `detection`*/

/*Table structure for table `students`*/

CREATE TABLE `students` ( 
	`StudentID` int(6) NOT NULL,
	`Name` varchar(50) NOT NULL,
	PRIMARY KEY(`StudentID`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `users`*/

CREATE TABLE `users` (
  `UserID` int(6) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Usertype` varchar(50) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`UserID`));

/*Table structure for table `logs`*/

CREATE TABLE `logs` (
	`StudentID` int(6) NOT NULL,
	`Name` varchar(20) NOT NULL,
	`TimeMatched` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`UserID` int(6) NOT NULL,
	`UserWorking` varchar(50) NOT NULL,
	FOREIGN KEY (`StudentID`) REFERENCES students (`StudentID`),
	FOREIGN KEY (`UserID`) REFERENCES users (`UserID`));

