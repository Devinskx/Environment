CREATE DATABASE IF NOT EXISTS csu;
USE csu;

CREATE TABLE IF NOT EXISTS homeuser(
            u_id int primary key not null comment '成员编号',
            u_name varchar(30) not null comment '成员姓名',
            u_admin varchar(50) not null comment '成员账号',
            u_password varchar(30) not null comment '成员密码',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间',
            update_time timestamp not null default current_timestamp on update current_timestamp comment '修改时间'
            )
            engine = InnoDB
			default char set = utf8;

CREATE TABLE IF NOT EXISTS led(
            led_id int primary key not null comment 'LED编号',
            led_status int not null comment 'LED状态',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间',
            update_time timestamp not null default current_timestamp on update current_timestamp comment '修改时间'
            )
            engine = InnoDB
			default char set = utf8;

CREATE TABLE IF NOT EXISTS door(
            door_id int primary key not null comment '门编号',
            door_status int not null comment '门状态',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间',
            update_time timestamp not null default current_timestamp on update current_timestamp comment '修改时间'
            )
            engine = InnoDB
			default char set = utf8;
            
CREATE TABLE IF NOT EXISTS blower(
            blow_id int primary key not null comment '风扇编号',
            blow_status int not null comment '风扇状态',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间',
            update_time timestamp not null default current_timestamp on update current_timestamp comment '修改时间'
            )
            engine = InnoDB
			default char set = utf8;

CREATE TABLE IF NOT EXISTS environment(
            e_id int primary key not null comment '环境数据编号',
            e_temperature double not null comment '温度',
            e_humidity double not null comment '相对湿度',
			e_co2 double not null comment '二氧化碳',
            e_pm double not null comment 'PM2.5',
			e_fire int not null comment '火光',
            e_infrared int not null comment '红外线',
            e_ch4 int not null comment '甲烷',
            e_smoke int not null comment '烟雾',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间'
            )
            engine = InnoDB
			default char set = utf8;
CREATE TABLE IF NOT EXISTS enhistory(
            h_id int primary key auto_increment not null comment '环境数据编号',
            h_temperature double not null comment '温度',
            h_humidity double not null comment '相对湿度',
			h_co2 double not null comment '二氧化碳',
            h_pm double not null comment 'PM2.5',
            currenttime timestamp not null default current_timestamp comment '当前数据对应时间'
            )
            engine = InnoDB
			default char set = utf8;