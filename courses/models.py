from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Course(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
    )

    instructor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, limit_choices_to={'role': 'instructor'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def approve(self):
        """Approve the course (used by Approver role)."""
        self.status = 'Approved'
        self.save()

class Enrollment(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.email} enrolled in {self.course.title}'

class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('document', 'Document')])
    file = models.FileField(upload_to='course_materials/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
