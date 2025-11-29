create database employee_coffeeshop_db;

use employee_coffeeshop_db;

drop table if exists employees;
create table if not exists employees(
    id int primary key auto_increment,
    fullname varchar(255),
    age int,
    email varchar(255),
    address varchar(255),
    phone_number varchar(255),
    cccd_code varchar(255)
);

select * from employees;