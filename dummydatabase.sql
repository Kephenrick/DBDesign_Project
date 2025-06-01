-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 01, 2025 at 03:24 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dummydatabase`
--

-- --------------------------------------------------------

--
-- Table structure for table `msguest`
--

CREATE TABLE `msguest` (
  `GuestID` int(11) NOT NULL,
  `GuestName` varchar(100) DEFAULT NULL,
  `GuestPass` varchar(100) DEFAULT NULL,
  `PhoneNum` varchar(30) DEFAULT NULL,
  `Gender` enum('Male','Female') DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `msguest`
--

INSERT INTO `msguest` (`GuestID`, `GuestName`, `GuestPass`, `PhoneNum`, `Gender`, `Email`) VALUES
(1, 'Arif', '12345', '081234567891', 'Male', 'arif@gmail.com'),
(2, 'Dewi', '12345', '081234567892', 'Female', 'dewi@gmail.com'),
(3, 'Rifki', '12345', '081234567893', 'Male', 'rifki@gmail.com'),
(4, 'Sinta', '12345', '081234567894', 'Female', 'sinta@gmail.com'),
(5, 'Putri', '12345', '081234567895', 'Female', 'putri@gmail.com'),
(6, 'Arif', '12345', '081234567891', 'Male', 'arif@gmail.com'),
(7, 'Dewi', '12345', '081234567892', 'Female', 'dewi@gmail.com'),
(8, 'Rifki', '12345', '081234567893', 'Male', 'rifki@gmail.com'),
(9, 'Sinta', '12345', '081234567894', 'Female', 'sinta@gmail.com'),
(10, 'Putri', '12345', '081234567895', 'Female', 'putri@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `mslocation`
--

CREATE TABLE `mslocation` (
  `LocationID` int(11) NOT NULL,
  `Location` varchar(20) DEFAULT NULL,
  `LocationName` varchar(100) DEFAULT NULL,
  `LocationAddress` varchar(100) DEFAULT NULL,
  `LocationDescription` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mslocation`
--

INSERT INTO `mslocation` (`LocationID`, `Location`, `LocationName`, `LocationAddress`, `LocationDescription`) VALUES
(1, 'PIK', 'Mercury PIK', 'Jl. Pantai Indah Kapuk, Kamal Muara Penjaringan, North Jakarta, 14470', 'Mercury PIK is a midscale hotel located conveniently at Pantai In Korea, the most popular area in North Jakarta. With direct connection to Avenir PIK Mall, it offers 240 facilities including an All Day Dining restaurant, 5 meeting rooms, outdoor swimming pool, spa and fitness centre.'),
(2, 'Lampung', 'Mercury Lampung Grand', 'Jl. Raden Intan, 88, Pelita Enggal, 35117, Bandar Lampung', 'Located on the hillside of Lampung Bay, Bandar Lampung is the capital as well as the largest city of the Province. It is a bustling city with fast growing economy as well as a sea holiday destination and the best entry point to Sumatra. Enjoy the unparalleled view at our Rooftop Bar & Lounge, indulge yourself with our delicious restaurant specialties, or relax at our Swimming Pool and Fitness.');

-- --------------------------------------------------------

--
-- Table structure for table `msreservation`
--

CREATE TABLE `msreservation` (
  `ReservationID` int(11) NOT NULL,
  `PaymentType` varchar(100) DEFAULT NULL,
  `PaymentStatus` enum('Complete','Pending') DEFAULT NULL,
  `CheckIn` date DEFAULT NULL,
  `CheckOut` date DEFAULT NULL,
  `GuestID` int(11) DEFAULT NULL,
  `StaffID` int(11) DEFAULT NULL,
  `RoomID` int(11) DEFAULT NULL,
  `LocationID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `msreservation`
--

INSERT INTO `msreservation` (`ReservationID`, `PaymentType`, `PaymentStatus`, `CheckIn`, `CheckOut`, `GuestID`, `StaffID`, `RoomID`, `LocationID`) VALUES
(7, 'BankMega', 'Complete', '2025-05-05', '2025-05-09', 1, 1, 1, 1),
(8, 'Paypal', 'Complete', '2025-06-01', '2025-06-05', 2, 1, 1, 1),
(9, 'BCA', 'Complete', '2025-06-02', '2025-06-06', 3, 2, 2, 2),
(10, 'BankMega', 'Complete', '2025-06-07', '2025-06-22', 2, 1, 3, 1),
(11, 'BCA', 'Complete', '2025-06-04', '2025-06-08', 4, 3, 1, 2),
(12, 'Paypal', 'Complete', '2025-06-05', '2025-06-09', 4, 4, 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `msroom`
--

CREATE TABLE `msroom` (
  `RoomID` int(11) NOT NULL,
  `RoomType` varchar(45) DEFAULT NULL,
  `RoomPrice` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `msroom`
--

INSERT INTO `msroom` (`RoomID`, `RoomType`, `RoomPrice`) VALUES
(1, 'Single', 1000000),
(2, 'Double', 1500000),
(3, 'Suite', 2000000),
(4, 'Deluxe', 2500000),
(5, 'Single', 1000000),
(6, 'Double', 1500000),
(7, 'Suite', 2000000),
(8, 'Deluxe', 2500000);

-- --------------------------------------------------------

--
-- Table structure for table `msstaff`
--

CREATE TABLE `msstaff` (
  `StaffID` int(11) NOT NULL,
  `StaffName` varchar(100) DEFAULT NULL,
  `StaffPass` varchar(100) DEFAULT NULL,
  `StaffContact` varchar(30) DEFAULT NULL,
  `StaffPosition` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `msstaff`
--

INSERT INTO `msstaff` (`StaffID`, `StaffName`, `StaffPass`, `StaffContact`, `StaffPosition`) VALUES
(1, 'Andi', '12345', '081300000001', 'Receptionist'),
(2, 'Dina', '12345', '081300000002', 'Manager'),
(3, 'Rudi', '12345', '081300000003', 'Front Desk'),
(4, 'Mira', '12345', '081300000004', 'Housekeeping'),
(5, 'Tono', '12345', '081300000005', 'Concierge'),
(6, 'Andi', '12345', '081300000001', 'Receptionist'),
(7, 'Dina', '12345', '081300000002', 'Manager'),
(8, 'Rudi', '12345', '081300000003', 'Front Desk'),
(9, 'Mira', '12345', '081300000004', 'Housekeeping'),
(10, 'Tono', '12345', '081300000005', 'Concierge');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `msguest`
--
ALTER TABLE `msguest`
  ADD PRIMARY KEY (`GuestID`);

--
-- Indexes for table `mslocation`
--
ALTER TABLE `mslocation`
  ADD PRIMARY KEY (`LocationID`);

--
-- Indexes for table `msreservation`
--
ALTER TABLE `msreservation`
  ADD PRIMARY KEY (`ReservationID`),
  ADD KEY `GuestID` (`GuestID`),
  ADD KEY `StaffID` (`StaffID`),
  ADD KEY `RoomID` (`RoomID`),
  ADD KEY `LocationID` (`LocationID`);

--
-- Indexes for table `msroom`
--
ALTER TABLE `msroom`
  ADD PRIMARY KEY (`RoomID`);

--
-- Indexes for table `msstaff`
--
ALTER TABLE `msstaff`
  ADD PRIMARY KEY (`StaffID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `msguest`
--
ALTER TABLE `msguest`
  MODIFY `GuestID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `mslocation`
--
ALTER TABLE `mslocation`
  MODIFY `LocationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `msreservation`
--
ALTER TABLE `msreservation`
  MODIFY `ReservationID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `msroom`
--
ALTER TABLE `msroom`
  MODIFY `RoomID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `msstaff`
--
ALTER TABLE `msstaff`
  MODIFY `StaffID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `msreservation`
--
ALTER TABLE `msreservation`
  ADD CONSTRAINT `msreservation_ibfk_1` FOREIGN KEY (`GuestID`) REFERENCES `msguest` (`GuestID`),
  ADD CONSTRAINT `msreservation_ibfk_2` FOREIGN KEY (`StaffID`) REFERENCES `msstaff` (`StaffID`),
  ADD CONSTRAINT `msreservation_ibfk_3` FOREIGN KEY (`RoomID`) REFERENCES `msroom` (`RoomID`),
  ADD CONSTRAINT `msreservation_ibfk_4` FOREIGN KEY (`LocationID`) REFERENCES `mslocation` (`LocationID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
