from collections import defaultdict
import enum

grades = {"A": 4, "B": 3, "C":2, "D":1, "F":0, "I": 0}

class Course:
    def __init__(self, courseId, year, semester):
        self.courseID = courseId
        self.year = year
        self.semester = semester
        self.teacher = None
        self.students = []

    def assignTeacher(self, teacher):
        self.teacher = teacher

    def addStudent(self, student):
        if student not in self.students:
            self.students.append(student)
        else:
            print("student already exists")

    def getTeacher(self):
        return self.teacher

    def getStudents(self):
        return self.students


class Teacher:
    def __init__(self, id):
        self.id = id


class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courseGrade = {}
        self.courses = []

    def enrollIntoCourse(self, courseID, year, semester):
        c = courseID+":"+year+":"+semester
        self.courses.append(c)
        self.courseGrade[c] = "I"

    def assignGrade(self, courseID, year, semester, grade):
        c = courseID + ":" + year + ":" + semester
        if c not in self.courseGrade:
            print("student not enrolled in course")
        else:
            self.courseGrade[c] = grade

    def getGrade(self, courseID, year, semester):
        c = courseID + ":" + year + ":" + semester
        if c not in self.courseGrade:
            print("student not enrolled in course")
        else:
            return self.courseGrade[c]

    def calculateGPA(self, year, semester):
        gpa = 0.0
        count = 0
        for k,v in self.courseGrade.items():
            c, y, s = k.split(":")
            if y == year and s == semester and v != "I":
                gpa += grades.get(v)
                count+=1
        return gpa/count

    def getCourseGradeInfo(self, year, semester):
        ret = []
        for k,v in self.courseGrade.items():
            c, y, s = k.split(":")
            if y == year and s == semester:
                ret.append((c, v))
        return ret


class School:
    def __init__(self):
        self.courses = defaultdict(Course)
        self.teachers = defaultdict(Teacher)
        self.student = defaultdict(Student)

    def createTeacher(self, id):
        self.teachers[id] = Teacher(id)

    def createStudent(self, id, name):
        self.student[id] = Student(id, name)

    def createCourse(self, courseID, year, semester):
        c = Course(courseID, year, semester)
        self.courses[courseID+year+semester] = c

    def assignTeacherToCourse(self, courseID, year, semester, teacher):
        course = self.courses.get(courseID+year+semester, None)
        if course == None:
            print("no course found")
        else:
            teacher = self.teachers.get(teacher, None)
            if teacher == None:
                print("teacher not found")
            else:
                course.assignTeacher(teacher)

    def addStudentToCourse(self, courseID, year, semester, studentID):
        course = self.courses.get(courseID + year + semester, None)
        if course == None:
            print("no course found")
        else:
            student = self.student.get(studentID, None)
            if student == None:
                print("Student not found")
            else:
                course.addStudent(studentID)
                student.enrollIntoCourse(courseID, year, semester)

'''
for a course get Teacher
'''

    def getTeacher(self, courseID, year, semester):
        course = self.courses.get(courseID + year + semester, None)
        if course == None:
            print("no course found")
        else:
            return course.getTeacher()


'''
•	For a given student and course offering, return the grade
'''

    def getGradeForStudentInCourse(self, courseID, year, semester, studentID):
        course = self.courses.get(courseID + year + semester, None)
        if course == None:
            print("no course found")
        else:
            student = self.student.get(studentID, None)
            if(student == None):
                print("Student not found")
            else:
                return student.getGrade(courseID, year, semester)

    """
    •	For a given student, year, and semester, return a grade point average (ex: 3.49)
    """
    def getGPAForStudentInYearAndSemester(self, year, semester, studentID):
        student = self.student.get(studentID, None)
        if (student == None):
            print("Student not found")
        else:
            return student.calculateGPA(year, semester)

    """
    •	For a given student, year, and semester, return a list of courses and the grades that the given student received in those courses
    """
    def getStudentCourseGradeInfo(self, year, semester, studentID):
        student = self.student.get(studentID, None)
        if (student == None):
            print("Student not found")
        else:
            return student.getCourseGradeInfo(year, semester)


