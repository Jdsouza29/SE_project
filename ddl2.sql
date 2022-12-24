drop database SE_Project;

create database SE_Project;

use SE_Project;

create table User(
    U_ID int auto_increment not null,
    Username varchar (100) not null,
    user_password varchar (100) not null, 
    U_name varchar(150) ,
    gender varchar(10) ,
    DOB date,
    phone varchar(100), 
    e_mail varchar(100),
    constraint F_M check ( gender='FEMALE' or gender='MALE'),
    constraint E_Check check(e_mail like '%@%.com'),
    constraint phone_Check check(phone like '__________'),
    constraint prim_key_user primary key (U_ID)
);

create table admn (
    A_ID int auto_increment  not null, 
    ad_username varchar(100) not null,
    ad_password varchar(100) not null, 
    Ad_name varchar (150) not null,
    Uni_key varchar(50) not null,
    ad_mail varchar(100),
    ad_phone varchar(100),
    constraint E_Check_ad check(ad_mail like '%@%.com'),
    constraint phone_Check_ad check(ad_phone like '__________'),
    constraint prim_key_ad primary key (A_ID)
);

create table room(
    R_ID int auto_increment not null,
    size int not null,
    project int,
    A_V int,
    white_board_util int,
    mic_speaker int,
    Camera int,
    AC int,
    add_date date not null,
    last_modi date,
    A_ID int not null,
    primary key (R_ID),
   foreign key (A_ID) references admn(A_ID) on delete CASCADE on update CASCADE
);

create table booking_record(
    BR_ID int auto_increment not null,
    U_ID int not null,
    R_ID int not null,
    Book_date date not null,
    Book_start_time datetime not null,
    Book_stop_time datetime not null,
    size int not null,
    project int,
    A_V int,
    white_board_util int,
    mic_speaker int,
    Camera int,
    AC int,
    PRIMARY key(BR_ID),FOREIGN KEY(U_ID)REFERENCES User(U_ID) on delete CASCADE on update CASCADE,
    foreign key (R_ID) references room(R_ID) on delete CASCADE on update CASCADE
);

create table id(
    BR_ID int not null,
    U_ID int not null,
    R_ID int not null,
    primary key (BR_ID,U_ID,R_ID),
    foreign key (BR_ID) references booking_record(BR_ID) on delete CASCADE on update CASCADE,
    foreign key (U_ID) references User(U_ID) on delete CASCADE on update CASCADE,
    foreign key (R_ID) references room(R_ID) on delete CASCADE on update CASCADE
);


create table que(
    Q_ID int auto_increment not null,
    U_ID int not null,
    R_ID int not null,
    Book_date date not null,
    Book_start_time datetime not null,
    Book_stop_time datetime not null,
    project int,
    A_V int,
    white_board_util int,
    mic_speaker int,
    Camera int,
    AC int,
    primary key (Q_ID),
    foreign key (U_ID) references User(U_ID)on delete CASCADE on update CASCADE,
    foreign key (R_ID) references room(R_ID)on delete CASCADE on update CASCADE
);



-- adding values into user table:

INSERT into User 
(Username,user_password,U_name,gender,DOB,phone,e_mail)
values
("Priya_Singh","priya@123","Priya","FEMALE","2001-11-07","9019877456","priyasingh123@gmail.com"),
("John_Roy","john@roy124","John","MALE","2002-10-17","9019172356","johnroy123@gmail.com"),
("Zain_Malik","zain@gigi","Zain","MALE","1991-05-07","9919762893","zain_official@gmail.com"),
("Brinda_Gowda","brinda_gowda@a123","Brinda","FEMALE","2000-09-06","2728534573","gowdabrinda@gmail.com"),
("Khushi_rao","123khushi","Khushi","FEMALE","1999-01-01","7378564901","khushirao@gmail.com");


INSERT into Admn 
(ad_username,ad_password,Ad_name,Uni_key,ad_phone,ad_mail)
values
("Divya_Spandana","divyaspan@1894","Divya","abcd1234","9019123499","spandanadivya@gmail.com");
INSERT into Admn 
(ad_username,ad_password,Ad_name,Uni_key,ad_phone,ad_mail)
values
("Zubair_Dilayak","Zubair@8909","Zubair","dgbcsd342","9019123432","dilayak_zubair@gmail.com");


INSERT into Room 
(size,project,A_V,white_board_util,mic_speaker,Camera,AC,add_date,last_modi,A_ID)
VALUES
(300,1,0,0,1,1,1,"2020-11-10","2022-11-21",1),
(100,1,1,1,1,0,1,"2020-11-05","2022-10-21",1),
(150,1,1,1,0,1,1,"2021-10-17","2022-09-20",2),
(500,1,0,1,0,1,0,"2022-05-12","2022-07-19",2),
(189,1,1,1,0,1,1,"2022-09-21","2022-01-18",1),
(200,1,1,1,1,0,1,"2021-01-22","2022-11-06",1),
(300,1,0,1,1,1,1,"2020-02-08","2022-10-02",2);

INSERT into booking_record 
(u_id,R_id,Book_date,Book_start_time,Book_stop_time,size,project,A_V,white_board_util,mic_speaker,Camera,AC)
values 
(1,1,"2022-11-28","10:00:00","15:00:00",300,1,0,1,1,1,1);

INSERT into Admn 
(ad_username,ad_password,Ad_name,Uni_key,ad_phone,ad_mail)
values
("abc","abc123","abc","111","9019123432","abc@gmail.com");

INSERT into User 
(Username,user_password,U_name,gender,DOB,phone,e_mail)
values
("avi","avi123","a_vi","FEMALE","2001-11-09","9019877456","avi@gmail.com");