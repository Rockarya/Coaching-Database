-- Table structure for table COACHING

DROP DATABASE IF EXISTS COACHING;
CREATE SCHEMA COACHING;
USE COACHING;

DROP TABLE IF EXISTS branch_address;
CREATE TABLE branch_address (
  branch_id varchar(10) NOT NULL,
  branch_Address varchar(500) NOT NULL,
  PRIMARY KEY (branch_id)
  
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES branch_address WRITE;
INSERT INTO branch_address
VALUES
(
	'KOTA_01',
	'10-F-12, INDIRA VIHAR, KOTA'
),(
	'NAGPUR_02',
	'12-K-9, Gumanpura, Nagpur'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS study_material;
CREATE TABLE study_material (
  id varchar(10) NOT NULL,
  difficulty_level varchar(10) NOT NULL,
  PRIMARY KEY (id)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES study_material WRITE;
INSERT INTO study_material
VALUES
(
	'S_PHY20',
	'Hard'
),(
	'T_MATH94',
	'Easy'
),(
	'T_CHEM24',
	'Medium'
),
(
	'T_PHY102',
	'Hard'
),(
	'S_MATH14',
	'Medium'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS branch;
CREATE TABLE branch (
  pincode varchar(10) NOT NULL,
  branchcode varchar(10) NOT NULL,
  name varchar(100) NOT NULL,
  address varchar(500) NOT NULL,
  PRIMARY KEY (branchcode)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES branch WRITE;
INSERT INTO branch
VALUES
(
	'324005',
	'KOTA912',
	'C.G. Tower',
	'10-F-12, INDIRA VIHAR, KOTA'
),(
	'440001',
	'NAG345',
	'M.H. Tower',
	'12-K-9, Gumanpura, Nagpur'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS staff;
CREATE TABLE staff (
  staff_id varchar(5) NOT NULL,
  salary varchar(10) NOT NULL,
  branchcode varchar(10) NOT NULL,
  name varchar(100) NOT NULL,
  working_hours varchar(10) NOT NULL,
  PRIMARY KEY (staff_id),
  
  CONSTRAINT staff_ibfk_1 FOREIGN KEY (branchcode) REFERENCES branch (branchcode)
  ON UPDATE CASCADE
  ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES staff WRITE;
INSERT INTO staff
VALUES
(
	'S1',
	'25000',
	'KOTA912',
	'Piyush Chawla',
	'7.5hour'
),(
	'S2',
	'40000',
	'NAG345',
	'Mayank Jain',
	'8.5hour'
),(
	'S3',
	'50000',
	'NAG345',
	'Kadam Jain',
	'6hour'
),(
	'S4',
	'54000',
	'KOTA912',
	'Bhavya Gupta',
	'6hour'
),(
	'S5',
	'60000',
	'NAG345',
	'Palash Sharma',
	'6hour'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS online_lecture;
CREATE TABLE online_lecture (
  topic_name varchar(100) NOT NULL,
  staff_id varchar(5) NOT NULL,
  duration varchar(100) NOT NULL,
  PRIMARY KEY (topic_name,staff_id),

  CONSTRAINT online_lecture_ibfk_1 FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE 

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES online_lecture WRITE;
INSERT INTO online_lecture
VALUES
(
	'Centre of Mass',
	'S1',
	'40 min'
),(
	'Trignometry',
	'S2',
	'35 min'
),(
	'RBD',
	'S3',
	'55 min'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS course;
CREATE TABLE course (
  course_id varchar(10) NOT NULL,
  staff_id varchar(5) NOT NULL,
  C_name varchar(100) NOT NULL,
  session varchar(100) NOT NULL,
  fee varchar(10) NOT NULL,
  num_of_students_enrolled int(10) NOT NULL,
  PRIMARY KEY (course_id),
  
  CONSTRAINT course_ibfk_1 FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES course WRITE;
INSERT INTO course
VALUES
(
	'JEE_MATH01',
	'S1',
	'JEE',
	'2019',
	'140000',
	'1095'	
),
(
	'JEE_PHY04',
	'S2',
	'JEE',
	'2019',
	'120000',
	'1292'
),(
	'MED_BIO02',
	'S3',
	'MEDICAL',
	'2020',
	'125000',
	'2056'
	),
	(
	'MED_CHEM05',
	'S4',
	'MEDICAL',
	'2020',
	'125000',
	'2056'
),(
	'JEE_CHEM03',
	'S5',
	'JEE',
	'2020',
	'124000',
	'1956'

);
UNLOCK TABLES;


DROP TABLE IF EXISTS consists_of;
CREATE TABLE consists_of (
  course_id varchar(10) NOT NULL,
  session varchar(100) NOT NULL,
  pincode varchar(10) NOT NULL,
  branchcode varchar(10) NOT NULL,
  PRIMARY KEY (course_id,branchcode),

  CONSTRAINT consists_of_ibfk_1 FOREIGN KEY (branchcode) REFERENCES branch (branchcode)
  ON UPDATE CASCADE
  ON DELETE CASCADE, 

  CONSTRAINT consists_of_ibfk_2 FOREIGN KEY (course_id) REFERENCES course (course_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES consists_of WRITE;
INSERT INTO consists_of
VALUES
(
	'JEE_PHY04',
	'2019',
	'324005',
	'KOTA912'
),
(
	'MED_BIO02',
	'2020',
	'440001',
	'NAG345'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS students;
CREATE TABLE students (
  rollno varchar(10) NOT NULL,
  course_id varchar(10) NOT NULL,        
  full_name varchar(100) NOT NULL,
  dob date NOT NULL,
  gender varchar(20) NOT NULL,
  PRIMARY KEY (rollno),

  CONSTRAINT students_ibfk_1 FOREIGN KEY (course_id) REFERENCES course (course_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE


) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES students WRITE;
INSERT INTO students
VALUES
(
	'1',
	'JEE_PHY04',
	'Atulya Bhushan',
	'2002-11-13',
	'Male'
),(
	'2',
	'JEE_MATH01',
	'kamlesh Nagarkoti',
	'2002-10-14',
	'Male'
),(
	'3',
	'MED_BIO02',
	'Pooja Sharma',
	'2003-07-18',
	'Female'
),(
	'4',
	'MED_CHEM05',
	'Rohit Sharma',
	'2001-09-01',
	'Male'
),(
	'5',
	'JEE_CHEM03',
	'Chanchal Khanna',
	'2002-03-09',
	'Female'
),(
	'6',
	'JEE_PHY04',
	'Aryan Kharbanda',
	'2002-12-23',
	'Male'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS `reads`;
CREATE TABLE `reads` (
  rollno varchar(10) NOT NULL,
  study_material_id varchar(10) NOT NULL,
  PRIMARY KEY (rollno,study_material_id),

  CONSTRAINT reads_ibfk_1 FOREIGN KEY (rollno) REFERENCES students (rollno)
  ON UPDATE CASCADE
  ON DELETE CASCADE,      

  CONSTRAINT reads_ibfk_2 FOREIGN KEY (study_material_id) REFERENCES study_material (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE   

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES `reads` WRITE;
INSERT INTO `reads`
VALUES
(
	'1','S_PHY20'
),(
	'3','T_MATH94'
),(
	'5','S_MATH14'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS student_family_address;
CREATE TABLE student_family_address (
  student_rollno varchar(10) NOT NULL,
  address varchar(500) NOT NULL,
  PRIMARY KEY (student_rollno),
  
  CONSTRAINT student_family_address_ibfk_1 FOREIGN KEY (student_rollno) REFERENCES students (rollno)
  ON UPDATE CASCADE
  ON DELETE CASCADE


) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES student_family_address WRITE;
INSERT INTO student_family_address
VALUES
(
	'1',
	'10-M-5, Parijat Colony, Kishangarh'
),(
	'2',
	'12-K-7, Talwandi, Nagpur'
),(
	'3',
	'10-F-3, Mahaveer Nagar 2, Chandigarh' 
),(
	'4',
	'12-J-2, Gumanpura, Kurukshetra'
),(
	'5',
	'11-L-4, Keshavpura, kota'
),(
	'6',
	'9-N-6, Mahaveer Nagar 3, Ranchi'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS `require`;
CREATE TABLE `require` (
  student_rollno varchar(10) NOT NULL,
  study_material_id varchar(10) NOT NULL,
  course_id varchar(10) NOT NULL,
  staff_id varchar(5) NOT NULL,

  PRIMARY KEY (student_rollno,study_material_id,course_id,staff_id),
  CONSTRAINT require_ibfk_1 FOREIGN KEY (student_rollno) REFERENCES students (rollno)
  ON UPDATE CASCADE
  ON DELETE CASCADE,

  CONSTRAINT require_ibfk_2 FOREIGN KEY (study_material_id) REFERENCES study_material (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE, 

  CONSTRAINT require_ibfk_3 FOREIGN KEY (staff_id) REFERENCES staff (staff_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE,

  CONSTRAINT require_ibfk_4 FOREIGN KEY (course_id) REFERENCES course (course_id)
  ON UPDATE CASCADE
  ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES `require` WRITE;
INSERT INTO `require`
VALUES
(
	'1',
	'S_PHY20',
	'JEE_PHY04',
	'S1'
),(
	'3',
	'T_MATH94',
	'MED_BIO02',
	'S2'
),(
	'2',
	'S_MATH14',
	'JEE_MATH01',
	'S3'
);
UNLOCK TABLES;





DROP TABLE IF EXISTS student_family_member_name;
CREATE TABLE student_family_member_name (
  rollno varchar(10) NOT NULL,
  name varchar(50) NOT NULL,
  phone_no varchar(15) NOT NULL,
  PRIMARY KEY (rollno,phone_no),

  CONSTRAINT student_family_member_name_ibfk_1 FOREIGN KEY (rollno) REFERENCES students (rollno)
  ON UPDATE CASCADE
  ON DELETE CASCADE

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES student_family_member_name WRITE;
INSERT INTO student_family_member_name
VALUES
(
	'1',
	'Sandeep Bhushan',
	'8101232505'
),(
	'2',
	'Saroj Nagarkoti',
	'9573453457'
),(
	'3',
	'Himanshu Sharma',
	'7792442457'
),(
	'4',
	'Kapil Sharma',
	'9543442315'
),(
	'5',
	'Aditya Khanna',
	'8537652908'
),(
	'6',
	'Akshay Kharbanda',
	'9766442103'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS sheet;
CREATE TABLE sheet (
  id varchar(10) NOT NULL,
  subject varchar(100) NOT NULL,
  PRIMARY KEY (id),
  
  CONSTRAINT sheet_ibfk_1 FOREIGN KEY (id) REFERENCES study_material (id)
  ON UPDATE CASCADE
  ON DELETE CASCADE 

) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES sheet WRITE;
INSERT INTO sheet
VALUES
(
	'S_PHY20',
	'PHY'
),(
	'S_MATH14',
	'MATH'
);
UNLOCK TABLES;


DROP TABLE IF EXISTS staff_working_hours;
CREATE TABLE staff_working_hours (
  shift varchar(100) NOT NULL,
  working_hours varchar(10) NOT NULL,
  PRIMARY KEY (shift)
  
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES staff_working_hours WRITE;
INSERT INTO staff_working_hours
VALUES
(
	'10am-6pm',
	'8 hour'
),
(
	'11am-8pm',
	'9 hour'
),(
	'10am-5.5pm',
	'7.5 hour'
);

UNLOCK TABLES;


DROP TABLE IF EXISTS test_score;
CREATE TABLE test_score (
  student_rollno varchar(10) NOT NULL,
  test_id varchar(10) NOT NULL,
  score int(3) NOT NULL,
  PRIMARY KEY (student_rollno, test_id),

  CONSTRAINT test_score_ibfk_1 FOREIGN KEY (student_rollno) REFERENCES students (rollno)
  ON UPDATE CASCADE
  ON DELETE CASCADE
  
) ENGINE = InnoDB DEFAULT CHARSET = utf8;
LOCK TABLES test_score WRITE;
INSERT INTO test_score
VALUES
(
	'1',
	'T_PHY102',
	'56'
),(
	'2',
	'T_MATH94',
	'44'
),(
	'4',
	'T_CHEM24',
	'99'
),(
	'3',
	'T_PHY102',
	'26'
),(
	'6',
	'T_MATH94',
	'56'
),(
	'4',
	'T_PHY102',
	'96'
),(
	'1',
	'T_MATH94',
	'92'
),(
	'3',
	'T_CHEM24',
	'59'
),(
	'2',
	'T_PHY102',
	'94'
),(
	'5',
	'T_MATH94',
	'94'
),(
	'6',
	'T_CHEM24',
	'81'
),(
	'5',
	'T_CHEM24',
	'88'
);
UNLOCK TABLES;