from __future__ import unicode_literals

from django.db import models
YEAR_CHOICES = (
	('17', '2017'),
	('18', '2018'),
	('19', '2019'),
	('20', '2020'),
	('21', '2021'),
	('22', '2022'),)

SEMESTER_CHOICES = (
	(1, 'I'),
	(2, 'II'),
	(3, 'III'),
	(4, 'IV'),
	(5, 'V'),
	(6, 'VI'),
	(7, 'VII'),
	(8, 'VIII'),)

# class Semester(models.Model):
# 	semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)




# Create your models here.
class Program(models.Model):
	name = models.CharField(max_length=100)
	semester = models.CharField(max_length=20)

	def __str__(self):
		return self.name

# class Semester(models.Model):

# 	# program = models.ForeignKey(Program, on_delete=models.CASCADE)
# 	# semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)


class Course(models.Model):
	program = models.ForeignKey(Program, on_delete=models.CASCADE)
	semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	credit = models.IntegerField()
	pass_mark = models.FloatField()
	full_mark = models.FloatField()

	def __str__(self):
		return self.name


class ManageStudent(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	address = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	year = models.CharField(max_length=10, choices=YEAR_CHOICES)
	program = models.ForeignKey(Program, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class ManageTeacher(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	address = models.CharField(max_length=100)
	contact = models.CharField(max_length=15)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return self.name








