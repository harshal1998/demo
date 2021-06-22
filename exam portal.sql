create database exam;
use exam;

create table registration(
rollno int primary key,
name varchar(25),
class varchar(5),
username varchar(25),
password varchar(25));

admincreate table admin(
id int primary key auto_increment,
username varchar(25),
password varchar(25));