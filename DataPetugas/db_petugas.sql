-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 15 Feb 2016 pada 10.35
-- Versi Server: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_petugas`
--
CREATE DATABASE IF NOT EXISTS `db_petugas` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `db_petugas`;

-- --------------------------------------------------------

--
-- Struktur dari tabel `petugas`
--

CREATE TABLE IF NOT EXISTS `petugas` (
  `petugas_kode` varchar(10) NOT NULL,
  `petugas_nama` varchar(30) NOT NULL,
  `petugas_tgl_lahir` date NOT NULL,
  `petugas_alamat` varchar(30) NOT NULL,
  `petugas_no_hp` varchar(15) NOT NULL,
  PRIMARY KEY (`petugas_kode`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `petugas`
--

INSERT INTO `petugas` (`petugas_kode`, `petugas_nama`, `petugas_tgl_lahir`, `petugas_alamat`, `petugas_no_hp`) VALUES
('0001', 'Andi Herman', '1991-10-09', 'JL. Pahlawan No.19 RT.07\n', '082165338712');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
