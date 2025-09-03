from django.db import models

# Define a database model called "Task"
class Task(models.Model):
    # Priority options for tasks (used in the priority field below)
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
        ('Normal', 'Normal')
    ]
    # Task title or description (up to 255 characters)
    task = models.CharField(max_length=255)
    # Boolean field to check if the task is completed or not
    completed = models.BooleanField(default=False)
    # Priority of the task, restricted to the choices above
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Normal')
    # Optional due date for the task (can be left empty in DB and forms)
    due_date = models.DateField(null=True, blank=True)
    # Category or tag for the task (default is "General")
    category = models.CharField(max_length=100, default='General')
    
    # String representation of the object
    # This makes the task's name appear instead of <task object (1)>
    def __str__(self):
        return self.task