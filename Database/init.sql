CREATE DATABASE atadosapi;
USE atadosapi;

CREATE TABLE voluntary (
    id integer primary key auto_increment,
    name varchar(50) not null,
    surname varchar(50) not null,
    district varchar(200) not null,
    city varchar(60) not null
);

CREATE TABLE actions (
    id integer primary key auto_increment,
    name varchar(100) not null,
    district varchar(100) not null,
    address varchar(100) not null,
    city varchar(60) not null,
    description varchar(100) not null
);

