create database library;

create table login(
id int primary key auto_increment,
username varchar(25),
password varchar(20));

create table books(
bid int primary key,
bname varchar(25),
author varchar(25),
status varchar(25));

create table issue(
bid int primary key,
sid int,
sname varchar(25),
idate date,
edate date);