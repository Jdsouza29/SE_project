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
    constraint phone_Check check(phone like '^[789]\d{9}$'),
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
    constraint phone_Check_ad check(ad_phone like '^[789]\d{9}$'),
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
    constraint prim_key_room primary key (R_ID),
    constraint For_key_room foreign key (A_ID) references admn(A_ID)
);

create table booking_record(
    BR_ID int auto_increment not null,
    U_ID int not null,
    R_ID int not null,
    Book_date date not null,
    Book_start_time time not null,
    Book_stop_time time not null,
    project int,
    A_V int,
    white_board_util int,
    mic_speaker int,
    Camera int,
    AC int,
    constraint prim_key_bok primary key (BR_ID),
    constraint For_key_book1 foreign key (U_ID) references User(U_ID),
    constraint For_key_book2 foreign key (R_ID) references room(R_ID)
);

create table id(
    BR_ID int not null,
    U_ID int not null,
    R_ID int not null,
    constraint prim_key_id primary key (BR_ID,U_ID,R_ID),
    constraint For_key_id1 foreign key (BR_ID) references booking_record(BR_ID),
    constraint For_key_id2 foreign key (U_ID) references User(U_ID),
    constraint For_key_id3 foreign key (R_ID) references room(R_ID)
);


create table que(
    Q_ID int auto_increment not null,
    U_ID int not null,
    R_ID int not null,
    Book_date date not null,
    Book_start_time time not null,
    Book_stop_time time not null,
    project int,
    A_V int,
    white_board_util int,
    mic_speaker int,
    Camera int,
    AC int,
    que_no int,
    constraint prim_key_que1 primary key (Q_ID),
    constraint For_key_que1 foreign key (U_ID) references User(U_ID),
    constraint For_key_que2 foreign key (R_ID) references room(R_ID)
);
