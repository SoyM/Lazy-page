-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 2017-12-19 15:34:36
-- 服务器版本： 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `red`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add device esp status', 1, 'add_deviceespstatus'),
(2, 'Can change device esp status', 1, 'change_deviceespstatus'),
(3, 'Can delete device esp status', 1, 'delete_deviceespstatus'),
(4, 'Can add account', 2, 'add_account'),
(5, 'Can change account', 2, 'change_account'),
(6, 'Can delete account', 2, 'delete_account'),
(7, 'Can add paper', 3, 'add_paper'),
(8, 'Can change paper', 3, 'change_paper'),
(9, 'Can delete paper', 3, 'delete_paper'),
(10, 'Can add device mi led', 4, 'add_devicemiled'),
(11, 'Can change device mi led', 4, 'change_devicemiled'),
(12, 'Can delete device mi led', 4, 'delete_devicemiled'),
(13, 'Can add device esp config', 5, 'add_deviceespconfig'),
(14, 'Can change device esp config', 5, 'change_deviceespconfig'),
(15, 'Can delete device esp config', 5, 'delete_deviceespconfig'),
(16, 'Can add log entry', 6, 'add_logentry'),
(17, 'Can change log entry', 6, 'change_logentry'),
(18, 'Can delete log entry', 6, 'delete_logentry'),
(19, 'Can add group', 7, 'add_group'),
(20, 'Can change group', 7, 'change_group'),
(21, 'Can delete group', 7, 'delete_group'),
(22, 'Can add user', 8, 'add_user'),
(23, 'Can change user', 8, 'change_user'),
(24, 'Can delete user', 8, 'delete_user'),
(25, 'Can add permission', 9, 'add_permission'),
(26, 'Can change permission', 9, 'change_permission'),
(27, 'Can delete permission', 9, 'delete_permission'),
(28, 'Can add content type', 10, 'add_contenttype'),
(29, 'Can change content type', 10, 'change_contenttype'),
(30, 'Can delete content type', 10, 'delete_contenttype'),
(31, 'Can add session', 11, 'add_session'),
(32, 'Can change session', 11, 'change_session'),
(33, 'Can delete session', 11, 'delete_session');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$iK8NXWgnvIBS$JKyWBj9vOW/q0cRyMOvfc9Y3pKdIOiNy6i1IaIVVHQc=', '2017-12-18 16:15:57.564352', 1, 'SoyM', '', '', 'huangxinjiang1996@qq.com', 1, 1, '2017-12-07 00:00:00.000000');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'red', 'deviceespstatus'),
(2, 'red', 'account'),
(3, 'red', 'paper'),
(4, 'red', 'devicemiled'),
(5, 'red', 'deviceespconfig'),
(6, 'admin', 'logentry'),
(7, 'auth', 'group'),
(8, 'auth', 'user'),
(9, 'auth', 'permission'),
(10, 'contenttypes', 'contenttype'),
(11, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2017-12-18 16:09:53.286547'),
(2, 'auth', '0001_initial', '2017-12-18 16:09:55.840490'),
(3, 'admin', '0001_initial', '2017-12-18 16:09:56.417388'),
(4, 'admin', '0002_logentry_remove_auto_add', '2017-12-18 16:09:56.429196'),
(5, 'contenttypes', '0002_remove_content_type_name', '2017-12-18 16:09:56.658216'),
(6, 'auth', '0002_alter_permission_name_max_length', '2017-12-18 16:09:56.825453'),
(7, 'auth', '0003_alter_user_email_max_length', '2017-12-18 16:09:56.949048'),
(8, 'auth', '0004_alter_user_username_opts', '2017-12-18 16:09:56.969063'),
(9, 'auth', '0005_alter_user_last_login_null', '2017-12-18 16:09:57.076639'),
(10, 'auth', '0006_require_contenttypes_0002', '2017-12-18 16:09:57.079641'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2017-12-18 16:09:57.090808'),
(12, 'auth', '0008_alter_user_username_max_length', '2017-12-18 16:09:57.298009'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2017-12-18 16:09:57.418058'),
(14, 'red', '0001_initial', '2017-12-18 16:09:57.510625'),
(15, 'red', '0002_devicemiled', '2017-12-18 16:09:57.608561'),
(16, 'red', '0003_deviceespconfig_deviceespstatus', '2017-12-18 16:09:57.742656'),
(17, 'red', '0004_auto_20171215_2000', '2017-12-18 16:09:57.758167'),
(18, 'red', '0005_account', '2017-12-18 16:09:57.877752'),
(19, 'sessions', '0001_initial', '2017-12-18 16:09:58.181768');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('26ie2fxcb31ravszon9uanq5ck44e8p1', 'YTNlYTI1NjBkMmMwMzM2ZTUyZjk2ZmVhODMyNGQzNDU0NzIwOWM0Njp7Il9hdXRoX3VzZXJfaGFzaCI6IjJiMDU2MWU5NTg3MDQ3MjMyMTVhZTE4M2Q2YmVlNTIyYjAyOWUxMDciLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-01-01 16:15:57.591927');

-- --------------------------------------------------------

--
-- 表的结构 `red_account`
--

DROP TABLE IF EXISTS `red_account`;
CREATE TABLE IF NOT EXISTS `red_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(15) NOT NULL,
  `mode` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `red_deviceespconfig`
--

DROP TABLE IF EXISTS `red_deviceespconfig`;
CREATE TABLE IF NOT EXISTS `red_deviceespconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ssid_main` varchar(50) NOT NULL,
  `pwd_main` varchar(50) NOT NULL,
  `ssid_2` varchar(50) NOT NULL,
  `pwd_2` varchar(50) NOT NULL,
  `ssid_3` varchar(50) NOT NULL,
  `pwd_3` varchar(50) NOT NULL,
  `led_power` tinyint(1) NOT NULL,
  `led_bright` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 表的结构 `red_deviceespstatus`
--

DROP TABLE IF EXISTS `red_deviceespstatus`;
CREATE TABLE IF NOT EXISTS `red_deviceespstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `temperature` int(11) NOT NULL,
  `humidity` int(11) NOT NULL,
  `mq` int(11) NOT NULL,
  `ssid` varchar(60) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `red_deviceespstatus`
--

INSERT INTO `red_deviceespstatus` (`id`, `temperature`, `humidity`, `mq`, `ssid`) VALUES
(1, 25, 60, 21, 'ASUS');

-- --------------------------------------------------------

--
-- 表的结构 `red_devicemiled`
--

DROP TABLE IF EXISTS `red_devicemiled`;
CREATE TABLE IF NOT EXISTS `red_devicemiled` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` varchar(2000) NOT NULL,
  `update_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `red_devicemiled`
--

INSERT INTO `red_devicemiled` (`id`, `data`, `update_date`) VALUES
(1, '{\"power\": \"on\",\"bright\": 100}', '2017-12-18 00:00:00.000000'),
(2, '{\"power\": \"off\",\"bright\": 100}', '2017-12-19 00:00:00.000000');

-- --------------------------------------------------------

--
-- 表的结构 `red_paper`
--

DROP TABLE IF EXISTS `red_paper`;
CREATE TABLE IF NOT EXISTS `red_paper` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(140) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
