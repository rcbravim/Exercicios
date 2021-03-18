/*
 Navicat Premium Data Transfer

 Source Server         : banco-raphael2
 Source Server Type    : MySQL
 Source Server Version : 80022
 Source Host           : localhost:3306
 Source Schema         : banco-raphael2

 Target Server Type    : MySQL
 Target Server Version : 80022
 File Encoding         : 65001

 Date: 13/01/2021 09:29:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `add_zipcode` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_street` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_number` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `add_city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_region` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `add_status` tinyint(1) NOT NULL DEFAULT 0,
  `add_date_create` datetime(0) NOT NULL,
  `add_date_update` datetime(0) NOT NULL,
  `add_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_address_users`(`user_id`) USING BTREE,
  CONSTRAINT `fk_address_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of address
-- ----------------------------
INSERT INTO `address` VALUES (2, 9, '29070-000', 'Rua Professora ...', '405', 'Vitória', 'ES', 'BRA', 'Sudeste', 1, '2021-01-12 18:20:30', '2021-01-12 18:20:30', NULL);
INSERT INTO `address` VALUES (3, 10, '29070-444', 'Rua Professora ...', '405', 'Vitória', 'ES', 'BRA', 'Sudeste', 1, '2021-01-12 18:21:31', '2021-01-12 18:21:31', NULL);
INSERT INTO `address` VALUES (4, 11, '29070-444', 'Rua Professora ...', '405', 'Vitória', 'ES', 'BRA', 'Sudeste', 1, '2021-01-12 18:21:54', '2021-01-12 18:21:54', NULL);

-- ----------------------------
-- Table structure for documents
-- ----------------------------
DROP TABLE IF EXISTS `documents`;
CREATE TABLE `documents`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `doc_document` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `doc_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `doc_nationality` varchar(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `doc_status` tinyint(1) NOT NULL DEFAULT 0,
  `doc_date_create` datetime(0) NOT NULL,
  `doc_date_update` datetime(0) NOT NULL,
  `doc_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id`) USING BTREE,
  INDEX `fk_documents_users`(`user_id`) USING BTREE,
  CONSTRAINT `fk_documents_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of documents
-- ----------------------------
INSERT INTO `documents` VALUES (6, 9, '103.645.687-04', 'CPF', 'BRA', 1, '2021-01-12 18:20:30', '2021-01-12 18:20:30', NULL);
INSERT INTO `documents` VALUES (7, 10, '555.645.687-04', 'CPF', 'BRA', 1, '2021-01-12 18:21:31', '2021-01-12 18:21:31', NULL);
INSERT INTO `documents` VALUES (8, 11, '2222.645.687-04', 'CPF', 'BRA', 1, '2021-01-12 18:21:54', '2021-01-12 18:21:54', NULL);

-- ----------------------------
-- Table structure for genders
-- ----------------------------
DROP TABLE IF EXISTS `genders`;
CREATE TABLE `genders`  (
  `id` tinyint(1) NOT NULL AUTO_INCREMENT,
  `gen_description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `gen_status` tinyint(1) NOT NULL DEFAULT 0,
  `gen_date_create` datetime(0) NOT NULL,
  `gen_date_update` datetime(0) NOT NULL,
  `gen_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of genders
-- ----------------------------
INSERT INTO `genders` VALUES (1, 'M', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', NULL);
INSERT INTO `genders` VALUES (2, 'F', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', NULL);

-- ----------------------------
-- Table structure for items
-- ----------------------------
DROP TABLE IF EXISTS `items`;
CREATE TABLE `items`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `user_id` int(0) NOT NULL,
  `ite_description` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ite_status` tinyint(1) NOT NULL DEFAULT 0,
  `ite_date_create` datetime(0) NOT NULL,
  `ite_date_update` datetime(0) NOT NULL,
  `ite_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id`) USING BTREE,
  INDEX `fk_items_user`(`user_id`) USING BTREE,
  CONSTRAINT `fk_items_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of items
-- ----------------------------

-- ----------------------------
-- Table structure for regions
-- ----------------------------
DROP TABLE IF EXISTS `regions`;
CREATE TABLE `regions`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `reg_state` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `reg_initials` varchar(2) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `reg_region` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `reg_status` tinyint(1) NOT NULL,
  `reg_date_create` datetime(0) NOT NULL,
  `reg_date_update` datetime(0) NOT NULL,
  `reg_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 28 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of regions
-- ----------------------------
INSERT INTO `regions` VALUES (1, 'Amazonas', 'AM', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (2, 'Pará', 'PA', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (3, 'Roraima', 'RR', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (4, 'Amapá', 'AP', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (5, 'Rondônia', 'RO', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (6, 'Acre', 'AC', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (7, 'Tocantins', 'TO', 'Norte', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (8, 'Piauí', 'PI', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (9, 'Maranhão', 'MA', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (10, 'Pernambuco', 'PE', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (11, 'Rio Grande do Norte', 'RN', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (12, 'Paraíba', 'PB', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (13, 'Ceará', 'CE', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (14, 'Bahia', 'BA', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (15, 'Alagoas', 'AL', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (16, 'Sergipe', 'SE', 'Nordeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (17, 'Mato Grosso', 'MT', 'Centro Oeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (18, 'Mato Grosso do Sul', 'MS', 'Centro Oeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (19, 'Goiás', 'GO', 'Centro Oeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (20, 'Distrito Federal', 'DF', 'Centro Oeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (21, 'São Paulo', 'SP', 'Sudeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (22, 'Rio de Janeiro', 'RJ', 'Sudeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (23, 'Espírito Santo', 'ES', 'Sudeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (24, 'Minas Gerais', 'MG', 'Sudeste', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (25, 'Rio Grande do Sul', 'RS', 'Sul', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (26, 'Paraná', 'PN', 'Sul', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);
INSERT INTO `regions` VALUES (27, 'Santa Catarina', 'SC', 'Sul', 1, '2021-01-09 14:05:39', '2021-01-09 14:05:39', NULL);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `use_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `use_birth` datetime(0) NOT NULL,
  `gender_id` tinyint(1) NULL DEFAULT NULL,
  `use_status` tinyint(1) NOT NULL DEFAULT 0,
  `use_date_create` datetime(0) NOT NULL,
  `use_date_update` datetime(0) NOT NULL,
  `use_date_delete` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `id`(`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (9, 'Raphael Costa Bravim', '1986-02-08 00:00:00', 1, 1, '2021-01-12 18:20:30', '2021-01-12 18:20:30', NULL);
INSERT INTO `users` VALUES (10, 'Julio Silva', '1980-05-10 00:00:00', 1, 1, '2021-01-12 18:21:31', '2021-01-12 18:21:31', NULL);
INSERT INTO `users` VALUES (11, 'Camila Alves', '1984-12-03 00:00:00', 2, 1, '2021-01-12 18:21:54', '2021-01-12 18:21:54', NULL);

SET FOREIGN_KEY_CHECKS = 1;
