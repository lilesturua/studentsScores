from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    picture = models.ImageField(upload_to="student/", null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Score(models.Model):
    subject_name = models.CharField(max_length=100, null=True)
    student_score = models.IntegerField(null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="scores")

    def __str__(self):
        return f"{self.subject_name}: {self.student_score}"


