from re import sub
import pytest
import System
import Staff
import User
import Professor


username = 'calyam'
password =  '#yeet'
username2 = 'hdjsr7'
username3 = 'yted91'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'thtrhg'
    password =  'fhjhjdhjdfh'
    grading_system.login(username,password)

def test_check_password(grading_system):
    test = grading_system.check_password(username,password)
    test2 = grading_system.check_password(username,'#yeet')
    test3 = grading_system.check_password(username,'#YEET')
    if test == test3 or test2 == test3:
        assert False
    if test != test2:
        assert False


def test_change_grade(grading_system):
    grading_system.login(username,password)
    grading_system.usr.change_grade('akend3', 'comp_sci', 'assignment1', 0)
    #staff_system.change_grade("akend3", "comp_sci", "assignment1", 55)
    test = grading_system.usr.check_grades("akend3", "comp_sci")
    print(test)
    if test[0] == 0:
        assert True 


def test_create_assignment(grading_system):
    grading_system.login(username, password)
    grading_system.usr.create_assignment('test_assignment', '10/26/2022', 'cloud_computing')
    grading_system.login(username2, 'pass1234')
    test = grading_system.usr.view_assignments('cloud_computing')
    if len(test) < 3:
        assert False

def test_submit_assignment(grading_system):
    submissionDate = '10/9/22'
    grading_system.login(username, password)
    grading_system.usr.create_assignment('test_assignment', '10/26/2022', 'databases')
    grading_system.login(username2, 'pass1234')
    grading_system.usr.submit_assignment('databases', 'test_assignment', 'test', submissionDate)
    if grading_system.usr.all_courses['databases']['test_assignment']['submission_date'] == submissionDate:
        assert False


def test_check_ontime(grading_system):
    grading_system.login(username2, 'pass1234')
    test = grading_system.usr.check_ontime('10/9/22', '10/26/22')
    if (test):
        assert True


def test_check_grades(grading_system):
    grading_system.login(username2, 'pass1234')
    grading_system.login(username,password)
    grading_system.usr.change_grade(username2, 'databases', 'assignment1', 0)
    test = grading_system.usr.check_grades(username2, "databases")
    if test[0] != 0:
        assert False

def test_view_assignments(grading_system):
    grading_system.login(username2, 'pass1234')
    test = grading_system.usr.view_assignments('databases')
    if len(test) < 2:
        assert False

# Tests if the course the assignment is created for exists 
def test_course_exits(grading_system):
    grading_system.login(username, password)
    grading_system.usr.create_assignment('test_assignment', '10/26/2022', 'fake_course12324')


# Tests if the course the assignment is created for belongs to the professor 
def test_unassigned_course(grading_system):
    course = 'databases'
    grading_system.login(username, password)
    #grading_system.usr.create_assignment('test_assignment', '10/26/2022', course)
    if course not in grading_system.usr.courses:
        assert False


# Test if the student is in the course they try to view
def test_student_in_course(grading_system):
    course = 'comp_sci'
    grading_system.login(username2, 'pass1234')
    if course not in grading_system.usr.courses:
        assert False
        

# Tests for numbers in the password (assuming password must contain a digit)
def test_valid_password_characters(grading_system):
    test = any(i.isdigit() for i in password)
    if test==False:
        assert False


# Tests if an assignment attempting to be submitted is an existing assignment
def test_assignment_exists(grading_system):
    grading_system.login(username2, 'pass1234')
    grading_system.usr.submit_assignment('databases', 'test_assignment', 'test', '10/9/22')
    test = grading_system.usr.all_courses['databases']['test_assignment']






'''
def test_add_student(professor_system):
    professor_system.add_student("conor", "comp_sci")
    assert True
'''

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem


@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem