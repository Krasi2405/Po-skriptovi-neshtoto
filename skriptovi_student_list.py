import re
import copy
import os
import operator

class Subject:

	def __init__(self, name):
		self.name = name
		self.grades = [];
		
	def add_grade(self, grade):
		self.grades.append(grade)
	
class Student:

	def __init__(self, name, age, subject_list):
		self.name = name
		self.age = age
		self.subject_list = copy.deepcopy(subject_list)
		
	def get_info(self):
		info = "Name: {}, Age: {}\n".format(student.name, student.age)
		for subject in self.subject_list:
			info += "{}\n".format(subject.name)
			for grade in subject.grades:
				info += "  {}".format(grade)
			info += "\n"	
			
		return info
		
	def add_subject(self, name):
		self.subject_list.append(Subject(name)) 
	
	def remove_subject(self, name):
		for subject in self.subject_list:
			if subject.name == name:
				self.subject_list.remove(subject)
		
def print_choices():
	print("Press 0 to print all students\nPress 1 to print a student's info\nPress 2 to add a student\nPress 3 to remove a student\nPress 4 to grade a student\nPress 5 to add a subject\nPress 6 to remove a subject\nPress 7 to exit the program\n");
	
def sort_student_list(student_list):
	student_list.sort(key = lambda student: student.age, reverse = True)
	student_list.sort(key = lambda student: student.name) 
	
subject_list = []
student_list = []
response = ""

try:
	student_info = open("student_info.txt", "r+")
	info = student_info.read()
	student_info.close()
	a = re.findall("(?P<name>\w+)\|(?P<age>\d+)", info)
	for x in a:
		student = Student(a[a.index(x)][0], int(a[a.index(x)][1]), subject_list)
		student_list.append(student)
	
		
except FileNotFoundError:
	pass

while True:
		
	print(response)
	print_choices()
	choice = input("What would you like to do?")
	
	if choice == "0":
		response = ""
		for student in student_list:
			response += "Name: {}, Age: {}, Number: {}\n".format(student.name, student.age, student_list.index(student) + 1)
			
	elif choice == "1":
		number = int(input("Which student would you like to check out by number?"))
		for student in student_list:
			if student_list.index(student) + 1 == number:
				response = student.get_info()
				break
			response = "Student number {} does not exist".format(number)
				
	elif choice == "2":
		name = input("What is the student's name?")
		age = int(input("What is the student's age?"))
		student_list.append(Student(name, age, subject_list))
		sort_student_list(student_list)
		response = "Student {} has been successfully added.\n".format(name)
		
	elif choice == "3":
		number = int(input("What is the student's number?"))
		for student in student_list:
			if student_list.index(student) + 1 == number:
				student_list.remove(student)
				sort_student_list(student_list)
				response = "Student {} has been successfully removed.\n".format(name)
				break
			response = "Student {} could not be found.\n".format(name)
			
	elif choice == "4":
		number = int(input("Which student would you like to grade by number?"))
		subject_name = input("Which subject would you like to grade him in?")
		grade = int(input("What is the student's grade?"))
		for student in student_list:
			if student_list.index(student) + 1 == number:
				for subject in student.subject_list:
					if subject.name == subject_name:
						subject.add_grade(grade)
						response = "{} No{} has been successfully graded {} at {}.".format(student.name, number, grade, subject_name)
				break
			response = "Subject {} or Student No {} could not be found.".format(subject_name, number)	
	
	elif choice == "5":
		subject_name = input("Which subject would you like to add?")
		subject_list.append(Subject(subject_name))
		for student in student_list:
			student.add_subject(subject_name)
		response = "Subject {} has been added".format(subject_name)
			
	elif choice == "6":
		subject_name = input("Which subject would you like to remove?")
		for subject in subject_list:
			if subject.name == subject_name:
				subject_list.remove(subject)
				for student in student_list:
					student.remove_subject(subject_name)
				response = "Subject {} has been successfully removed.".format(subject_name)
				break
			response = "Subject {} could not be found.".format(subject_name)
		
	elif choice == "7":
		choice = input("Would you like to save current detals?")
		if choice == "yes":
			try:
				os.remove("student_info.txt")
			except:
				pass
			student_info_to_save = open("student_info.txt", "w")
			for student in student_list:
				student_info_to_save.write("{}|{}".format(student.name, student.age))
			student_info_to_save.close()
		else:
			try:
				os.remove("student_info.txt")
			except:
				pass
		break
	