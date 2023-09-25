create database face_recognizer;

create table face_recognizer.my_table
(
  id int,
  Name varchar(255),
  Age varchar(255),
  Address varchar(255)
  
)

insert into face_recognizer.my_table(id,Name,Age,Address)values(1,'Swaraj Sinha','21','Pune');
insert into face_recognizer.my_table(id,Name,Age,Address)values(2,'Swaraj','21','Pune');
insert into face_recognizer.my_table(id,Name,Age,Address)values(3,'Swaraj','21','Pune');
insert into face_recognizer.my_table(id,Name,Age,Address)values(4,'Aditi','21','Pune');


SELECT * from face_recognizer.my_table;



