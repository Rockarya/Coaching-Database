import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate


def viewTable(rows):
    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return

def show_tables():
    print("Choose a VIEW option\n")
    print("1.  branch")
    print("2.  branch_address")
    print("3.  consists_of")
    print("4.  course")
    print("5.  online_lecture")
    print("6.  reads")
    print("7.  require")
    print("8.  sheet")
    print("9.  staff")
    print("10. staff_working_hours")
    print("11. student_family_address")
    print("12. student_family_member_name")
    print("13. students")
    print("14. study_material")
    print("15. test_score")
    print("\n")
    return

def progress():
    print("Hey!,here you will get the difference in scores of student for the 2 test_ids you will input\n")
    s_id=input("Write the rollno of student: ")
    t1_id=input("Write the test_id1: ")
    t2_id=input("Write the test_id2: ")
    query="SELECT t1.score - t2.score FROM test_score t1,test_score t2 WHERE t1.test_id='%s' AND t2.test_id='%s' AND t1.student_rollno='%s' AND t2.student_rollno='%s' " %(t1_id,t2_id,s_id,s_id)

    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")
        
    return


def project():
    inp=input("Press 1 for getting top performers of a test\nPress 2 for getting above average students\n")
    
    if inp == '1':
        t_id=input("Write the test_id: ")
        k=input("Write the number of top performers you want to list out: ")
        query="SELECT * FROM test_score WHERE test_id='%s' ORDER BY score DESC LIMIT %s " %(t_id,k)

        try:
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
            con.commit()

        except Exception as e:
            print(e)
            print("\nInvalid data\n")

    elif inp == '2':
        query="SELECT * FROM test_score WHERE score > (SELECT AVG(score) FROM test_score)"

        try:
            cur.execute(query)
            rows=cur.fetchall()
            viewTable(rows)
            con.commit()

        except Exception as e:
            print(e)

    return  

def view_it():
    show_tables();
    n = input("Enter view option: ")

    if n == '1':
        query = "SELECT * FROM branch;"
    elif n == '2':
        query = "SELECT * FROM branch_address;"
    elif n == '3':
        query = "SELECT * FROM consists_of;"
    elif n == '4':
        query = "SELECT * FROM course;"
    elif n == '5':
        query = "SELECT * FROM online_lecture;"
    elif n == '6':
        query = "SELECT * FROM reads;"
    elif n == '7':
        query = "SELECT * FROM require;"
    elif n == '8':
        query = "SELECT * FROM sheet;"
    elif n == '9':
        query = "SELECT * FROM staff;"
    elif n == '10':
        query = "SELECT * FROM staff_working_hours;"
    elif n == '11':
        query = "SELECT * FROM student_family_address;"
    elif n == '12':
        query = "SELECT * FROM student_family_member_name;"
    elif n == '13':
        query = "SELECT * FROM students;"
    elif n == '14':
        query = "SELECT * FROM study_material;"
    elif n == '15':
        query = "SELECT * FROM test_score;"
    
    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid query number\n")
        
    return

def delete():
    print("Choose a table in which you have to apply delete operation\n")
    show_tables()
    n=input("Enter table number: ")

    if n == '1':
        s=input("Enter branchcode to be deleted: ")
        query = "DELETE FROM branch WHERE branchcode='%s';" %(s)
    elif n == '2':
        s=input("Enter branch_id to be deleted: ")
        query = "DELETE FROM branch_address WHERE branch_id='%s';" %(s)
    elif n == '3':
        s1=input("Enter course_id to be deleted: ")
        s2=input("Enter branchcode to be deleted: ")
        query = "DELETE FROM consists_of WHERE branchcode='%s' AND course_id='%s';" %(s2,s1)
    elif n == '4':
        s=input("Enter course_id to be deleted: ")
        query = "DELETE FROM course WHERE course_id='%s';" %(s)
    elif n == '5':
        s1=input("Enter topic_name to be deleted: ")
        s2=input("Enter staff_id to be deleted: ")
        query = "DELETE FROM online_lecture WHERE topic_name='%s' AND staff_id='%s';" %(s1,s2)
    elif n == '6':
        s1=input("Enter rollno to be deleted: ")
        s2=input("Enter study_material_id to be deleted: ")
        query = "DELETE FROM reads WHERE rollno='%s' AND study_material_id='%s';" %(s1,s2)
    elif n == '7':
        s1=input("Enter student_rollno to be deleted: ")
        s2=input("Enter study_material_id to be deleted: ")
        s3=input("Enter course_id to be deleted: ")
        s4=input("Enter staff_id to be deleted: ")
        query = "DELETE FROM require WHERE student_rollno='%s' AND study_material_id='%s' AND course_id='%s' AND staff_id='%s';" %(s1,s2,s3,s4)
    elif n == '8':
        s=input("Enter id to be deleted: ")
        query = "DELETE FROM sheet WHERE id='%s';" %(s)
    elif n == '9':
        s=input("Enter staff_id to be deleted: ")
        query = "DELETE FROM staff WHERE staff_id='%s';" %(s)
    elif n == '10':
        s=input("Enter shift to be deleted: ")
        query = "DELETE FROM staff_working_hours WHERE shift='%s';" %(s)
    elif n == '11':
        s=input("Enter student_rollno to be deleted: ")
        query = "DELETE FROM student_family_address WHERE student_rollno='%s';" %(s)
    elif n == '12':
        s1=input("Enter rollno to be deleted: ")
        s2=input("Enter phone_no to be deleted: ")
        query = "DELETE FROM student_family_member_name WHERE rollno='%s' AND phone_no='%s';" %(s1,s2)
    elif n == '13':
        s=input("Enter rollno to be deleted: ")
        query = "DELETE FROM students WHERE rollno='%s';" %(s)
    elif n == '14':
        s=input("Enter id to be deleted: ")
        query = "DELETE FROM study_material WHERE id='%s';" %(s)
    elif n == '15':
       s1=input("Enter student_rollno to be deleted: ")
       s2=input("Enter test_id to be deleted: ")
       query = "DELETE FROM test_score WHERE student_rollno='%s' AND test_id='%s';" %(s1,s2)

    try:
        cur.execute(query)
        rows=cur.fetchall()
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")

    return  


def aggregate():
    print("Choose a option\n")
    print("1.  MIN MARKS OF A PARTICULAR TEST")
    print("2.  MAX MARKS OF A PARTICULAR TEST")
    print("3.  AVERAGE MARKS FOR A PARTICULAR TEST")

    n = input("Enter option: ")

    if n=='1':
        min_marks()
    elif n=='2':
        max_marks()
    elif n=='3':
        avg_marks()


def min_marks():
    print("Choose test_ids like: T_PHY102 , T_MATH94, T_CHEM24\n")

    inp = input("Enter test id: ")
    query="SELECT MIN(score) FROM test_score t WHERE t.test_id = '%s';" %(inp);
    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")
        
    return


def max_marks():
    print("Choose test_ids like: T_PHY102 , T_MATH94, T_CHEM24\n")

    inp = input("Enter test id: ")
    query="SELECT MAX(score) FROM test_score t WHERE t.test_id = '%s';" %(inp);
    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")
        
    return


def avg_marks():
    print("Choose test_ids like: T_PHY102 , T_MATH94, T_CHEM24\n")

    inp = input("Enter test id: ")
    query="SELECT AVG(score) FROM test_score t WHERE t.test_id = '%s';" %(inp);
    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")
        
    return


def sex_ratio():
    query = "DROP VIEW IF EXISTS V1;" 
    cur.execute(query)
    query = "CREATE VIEW V1(M) AS SELECT COUNT(gender) FROM students WHERE gender='Male';"
    cur.execute(query)
    query = "DROP VIEW IF EXISTS V2;" 
    cur.execute(query)

    query = "CREATE VIEW V2(F) AS SELECT COUNT(gender) FROM students WHERE gender='Female';"
    cur.execute(query)
    query = "SELECT F/M FROM V1,V2;"
    try:
        cur.execute(query)
        rows=cur.fetchall()
        viewTable(rows)
        con.commit()

    except Exception as e:
        print(e)
        print("\nInvalid data\n")
        
    return


def option1():
    
    print("Select something to add")
    print("1. Student")
    print("2. New Branch")
    print("3. Staff(employee)")
    print("4. Online Lecture details")
    print("5. New Course")
    print("6. Student family details")
    print("7. Study material given to a particular student")
    print("8. New study material")
    print("9. Test score")
    print("10. Requirements")
    print("11. Consists")
    print("12 or above for Logging out")

    ad = int(input("\nEnter Choice>  "))
    tmp = sp.call('clear', shell = True)
    if( ad == 1 ):
        studentAdmission();
    if( ad == 2 ):
        addBranch();
    if( ad == 3 ):
        addStaff();
    if( ad == 4 ):
        addOnlineLecture();
    if( ad == 5 ):
        addCourse();
    if( ad == 6 ):
        addFamilyMembers();
    if( ad == 7 ):
        addReads();
    if( ad == 8 ):
        addStudyMaterial();
    if( ad == 9 ):
        addTestScore();
    if( ad == 10 ):
        addRequire();
    if( ad == 11 ):
        addConsists();
    if( ad >= 12 ):
        return


def option2():
    
    print("Select something to update!")
    print("1. Student's family's address")
    print("2. Student's family member's phone no.")
    print("3. Course Fee")
    print("4. Teacher assigned to a particular course")
    print("5. Branch address and pincode")
    adda = int(input("Enter Choice>  "))
    temp = sp.call('clear', shell = True)

    if( adda == 1 ):
        updateFamilyAddress();
    if( adda == 2 ):
        updatePhone();
    if( adda == 3 ):
        updateFee();
    if( adda == 4 ):
        updateStaff();
    if( adda == 5 ):
        updateBranchAddress();
    if( adda >= 6 ):
        return


def studentAdmission():

    try:
        row = {}
        print("Enter new student's details: ")
        name = input("Full Name: ")
        row["full_name"] = name;
        row["rollno"] = input("Roll No.: ")
        row["dob"] = input("Birth Date (YYYY-MM-DD): ")
        row["gender"] = input("Gender: (Male/Female/Others): ")
        print("Course id(format: (Exam_to_appear)_subjectID)\nFor example JEE_MATH01, MED_BIO02")
        row["course_id"] = input("Please enter the course id for the course student is enrolled in: ")
        query = "INSERT INTO students(rollno, course_id, full_name, dob, gender) VALUES('%s', '%s', '%s', '%s', '%s')" % (
            row["rollno"], row["course_id"], row["full_name"], row["dob"], row["gender"])

        print(query)
        cur.execute(query)
        query = "UPDATE course SET num_of_students_enrolled = num_of_students_enrolled + 1 WHERE course_id = '%s'" % (row["course_id"])
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addBranch():

    try:
        row = {}
        print("Enter new branch details")
        row["name"] = input("Name: ")
        row["address"] = input("Address: ")
        row["pincode"] = input("Pincode(6 digit): ")
        row["branchcode"] = input("Branch code(First 3-4 letters of the city followed by 2digit no. like KOTA02): ")

        query = "INSERT INTO branch(pincode, branchcode, name, address) VALUES('%s', '%s', '%s', '%s')" % (
            row["pincode"], row["branchcode"], row["name"], row["address"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addStaff():

    try:
        row = {}
        print("Enter new Staff details")
        row["staff_id"] = input("Staff_id(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["salary"] = input("Enter salary(correct upto 2 decimals XD): ")
        row["branchcode"] = input("Branch code for the branch where employed(First 3-4 letters of the city followed by 2digit no. like KOTA02): ")
        row["name"] = input("Full name of the employee: ")
        row["working_hours"] = input("Expected working hours(no. of hours followed by 'hour' without spaces): ")

        query = "INSERT INTO staff(staff_id, salary, branchcode, name, working_hours) VALUES('%s', '%s', '%s', '%s', '%s')" % (
            row["staff_id"], row["salary"], row["branchcode"], row["name"], row["working_hours"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addOnlineLecture():
    try:

        print("Enter Online Lecture Details")
        row = {}
        row["topic_name"] = input("Topic Name: ")
        row["staff_id"] = input("Staff Id of the teacher who is tutoring the video(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["duration"] = input("Duration of the online lecture(no. of mins followed by space followed by 'min': ")

        query = "INSERT INTO online_lecture(topic_name, staff_id, duration) VALUES('%s', '%s', '%s')" % (row["topic_name"], row["staff_id"], row["duration"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addCourse():

    try:

        row = {}
        print("Enter New Course Details")
        row["coursename"] = input("Course name(name of the exam to appear): ")
        row["session"] = input("Session(YYYY): ")
        print("Course id(format: (Exam_to_appear)_subjectID)\nFor example JEE_MATH01, MED_BIO02")
        row["course_id"] = input("Course Id: ")
        row["staff_id"] = input("Staff Id of the teacher taking the course(First letter should be S followed by a non 0 int without preceding 0s): ")
        row["fee"] = input("Fee(in Rs, upto 2 decimals: ")
        # have to make a function so that we can count the no. of students in a course

        query = "INSERT INTO course(course_id, staff_id, C_name, session, fee, num_of_students_enrolled) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
            row["course_id"], row["staff_id"], row["coursename"], row["session"], row["fee"], '0')

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addFamilyMembers():

    try:

        row = {}
        print("Enter Family member details")
        row["name"] = input("Name of the Family member: ")
        row["rollno"] = input("Roll number of the student related to the family memeber(format: positive integer): ")
        row["phone_no"] = input("Phone no. of the family member: ")
        row["address"] = input("Address of the member(expected to be same as student): ")

        query = "INSERT INTO student_family_member_name(rollno, name, phone_no) VALUES('%s', '%s', '%s')" % (row["rollno"], row["name"], row["phone_no"])

        print(query)
        cur.execute(query)
        con.commit()

        query = "INSERT INTO student_family_address(student_rollno, address) VALUES('%s', '%s')" % (row["rollno"], row["address"])
        cur.execute(query)
        con.commit()
        print(query)
        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addReads():

    try:
        print("Enter the details about the study_material given to a student")
        row = {}
        row["rollno"] = input("Roll no of the student(format: +ve int): ")
        row["study_material_id"] = input("ID of the study material given to the specified student(format: X_SUBJ00): ")

        query = "INSERT INTO `reads`(rollno, study_material_id) VALUES('%s', '%s')" % (row["rollno"], row["study_material_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addStudyMaterial():

    try:

        print("Enter the details of the new study material")
        row = {}
        row["id"] = input("ID of the study material(format: X_SUBJ00): ")
        row["difficulty_level"] = input("Approximate difficulty level of the study material(Easy/Medium/Hard): ")

        query = "INSERT INTO study_material(id, difficulty_level) VALUES('%s', '%s')" % (row["id"], row["difficulty_level"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addTestScore():

    try:

        print("Enter details")
        row = {}
        row["student_rollno"] = input("Roll no of the student: ")
        row["test_id"] = input("Test id(X_SUBJ00): ")
        row["score"] = input("Score: ")

        query = "INSERT INTO test_score(student_rollno, test_id, score) VALUES('%s', '%s', '%s')" % (row["student_rollno"], row["test_id"], row["score"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def addRequire():

    try:

        print("Enter details")
        row = {}
        row["student_rollno"] = input("Student's roll no.: ")
        row["study_material_id"] = input("Id of the study material: ")
        row["course_id"] = input("Id of the course: ")
        row["staff_id"] = input("Id of the staff: ")

        query = "INSERT INTO `require`(student_rollno, study_material_id, course_id, staff_id) VALUES('%s', '%s', '%s', '%s')" % (
            row["student_rollno"], row["study_material_id"], row["course_id"], row["staff_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def addConsists():

    try:
        print("Enter details")
        row = {}
        row["course_id"] = input("Course id: ")
        row["session"] = input("Session(YYYY): ")
        row["pincode"] = input("Pincode: ")
        row["branchcode"] = input("Branch code of the branch that consists the said course: ")

        query = "INSERT INTO consists_of(course_id, session, pincode, branchcode) VALUES('%s', '%s', '%s', '%s')" % (row["course_id"], row["session"], row["pincode"], row["branchcode"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted into database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateFamilyAddress():

    try:

        # print("Roll no of the student whose address is to be changed: ")
        row = {}
        row["rollno"] = input("Roll no of the student whose address is to be changed: ")
        row["address"] = input("New address: ")

        query = "UPDATE student_family_address SET address = '%s' WHERE student_rollno = '%s'" % (row["address"], row["rollno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updatePhone():

    try:

        # print("Roll no of the student whose address is to be changed: ")
        row = {}
        row["name"] = input("Name of the family member: ")
        row["rollno"] = input("Roll no of the related student: ")
        row["phone"] = input("New phone no.: ")

        query = "UPDATE student_family_member_name SET phone_no = '%s' WHERE (rollno = '%s' AND name = '%s')" % (row["phone"], row["rollno"], row["name"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateFee():

    try:

        # print("Roll no of the student whose address is to be changed: ")
        row = {}
        row["Id"] = input("Course Id(eg. JEE_MATH01): ")
        row["fee"] = input("New Fee: ")

        query = "UPDATE course SET fee = '%s' WHERE course_id = '%s'" % (row["fee"], row["Id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateStaff():

    try:
        # print("Roll no of the student whose address is to be changed: ")
        row = {}
        row["Id"] = input("Course Id(eg. JEE_MATH01): ")
        row["New"] = input("staff_id of the new teacher assigned: ")

        query = "UPDATE course SET staff_id = '%s' WHERE course_id = '%s'" % (row["New"], row["Id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def updateBranchAddress():

    try:

        # print("Roll no of the student whose address is to be changed: ")
        row = {}
        row["branchcode"] = input("Branchcode: ")
        row["New"] = input("New address of the branch: ")
        row["new"] = input("New pincode of the branch: ")

        query = "UPDATE branch SET address = '%s', pincode = '%s' WHERE branchcode = '%s'" % (row["New"], row["new"], row["branchcode"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Database Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        view_it()
    elif(ch == 4):
        project()
    elif(ch == 5):
        progress()
    elif(ch == 6):
        delete()
    elif(ch == 7):
        aggregate()
    elif(ch == 8):
        sex_ratio()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='COACHING',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                
                print("1. Add to the database")
                print("2. Update the database") 
                print("3. Have a look on our database tables")  
                print("4. Project students based on their performance")  
                print("5. Check Progress")  
                print("6. Delete tuples")
                print("7. Calculate Aggregate")
                print("8. Sex-ratio")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch > 8:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")