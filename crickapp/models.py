from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()

    def __str__(self):
        return '{}--{}'.format(self.name, self.price)


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=32)

         #  Create a foreign key, the foreign key will automatically add _id
    subject = models.ForeignKey(to='Subject', on_delete=True)

    def __str__(self):
        return '{}-{}'.format(self.name, self.age)


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=32)
    salary = models.CharField(max_length=32)

	 # ,Create in any class
    student = models.ManyToManyField(to='Student')

    def __str__(self):
        return '{}-{}'.format(self.name, self.age)
