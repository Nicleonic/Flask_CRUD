-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 10 mars 2024 à 11:27
-- Version du serveur : 10.4.22-MariaDB
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `cryptodb`
--

-- --------------------------------------------------------

--
-- Structure de la table `cipher`
--

CREATE TABLE `cipher` (
  `utilisateur` varchar(50) NOT NULL,
  `e` int(11) NOT NULL,
  `n` int(11) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `cipher`
--

INSERT INTO `cipher` (`utilisateur`, `e`, `n`, `password`) VALUES
('Abdala', 13, 257, 'BachLord48'),
('Hangi', 5, 327, 'htmlCss22'),
('Mado', 3, 33, 'madonaDressvuch23'),
('Mr. Robot', 7, 47, 'w123@#');

-- --------------------------------------------------------

--
-- Structure de la table `etudiant`
--

CREATE TABLE `etudiant` (
  `matricule` varchar(10) NOT NULL,
  `nom` varchar(25) NOT NULL,
  `postnom` varchar(25) NOT NULL,
  `dateNaissance` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `etudiant`
--

INSERT INTO `etudiant` (`matricule`, `nom`, `postnom`, `dateNaissance`) VALUES
('3ew', 'Cinquante-deux', 'Vingt-cinq', '2024-02-22'),
('a22', 'kljslksa [Updated]', 'lklsjlsa', '2024-02-21'),
('aa', 'ddd', 'dd', '2024-03-02'),
('ae23', 'Dani', 'Hangi', '2024-03-02'),
('aws24', 'Aphiwe', 'Naledi', '2024-02-27'),
('i93dskj', 'Clear', 'View', '2024-02-29'),
('jkh32', 'Justin [jdk]', 'Timberblake', '2024-02-22'),
('KAN28', 'Kanaila', 'Madona', '2024-03-09'),
('lkhlkhlsa', 'Hanna [updated]', 'Baker [updated]', '2024-02-21'),
('M14', 'Mariam [updated]', 'Kalonda', '2024-02-29'),
('MDLKAN23', 'Kanila', 'Madona', '2024-02-01'),
('nmbs98', 'ClearView', 'Ghana', '2024-02-29'),
('QNA53', 'Anthony', 'Bourbon', '2024-02-21'),
('ss2', 'xe', 'dc', '2024-02-28');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `cipher`
--
ALTER TABLE `cipher`
  ADD PRIMARY KEY (`utilisateur`);

--
-- Index pour la table `etudiant`
--
ALTER TABLE `etudiant`
  ADD PRIMARY KEY (`matricule`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
