-- -------------
-- jd database
-- ------------

create database jd_data charset utf8;

use jd_data;

-- ----------------------------
-- Table jd_action
-- ----------------------------
DROP TABLE IF EXISTS `jd_action`;
CREATE TABLE `jd_action` (
  `action_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `sku_id` bigint(20) not NULL DEFAULT '0' COMMENT '商品id',
  `time` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `mode_id` int(10) not NULL DEFAULT '0' COMMENT '点击模块',
  `type` int(10) not NULL DEFAULT '0' COMMENT '点击类型id',
  `cate` int(4) not NULL DEFAULT '0' COMMENT '产品类型od',
  `brand` int(4) not NULL DEFAULT '0' COMMENT '品牌id',
  PRIMARY KEY (`action_id`),
  UNIQUE KEY (`sku_id`),
  UNIQUE KEY (`cate`),
  UNIQUE KEY (`type`),
  UNIQUE KEY (`brand`),
  UNIQUE KEY (`time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='京东行为数据表';