/*
 Navicat Premium Data Transfer

 Source Server         : aikuai
 Source Server Type    : MySQL
 Source Server Version : 80033
 Source Host           : 192.168.100.1:3306
 Source Schema         : local

 Target Server Type    : MySQL
 Target Server Version : 80033
 File Encoding         : 65001

 Date: 11/02/2025 15:11:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account`  (
  `id` int NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `password` varbinary(255) NOT NULL,
  `user_explain` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `plugin` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
