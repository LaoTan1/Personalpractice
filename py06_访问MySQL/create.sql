create database python charset utf8;
use python;

CREATE TABLE t_user
(
  id       int primary key auto_increment,
  username varchar(200) unique not null,
  password varchar(200),
  age      int,
  heinght  double
) engine = Innodb
  charset utf8;
