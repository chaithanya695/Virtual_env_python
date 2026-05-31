from django.db import models

class Teachers(models.Model):
    teacher_id=models.IntegerField(unique=True)
    teacher_name=models.CharField(max_length=20)
    teacher_salary=models.FloatField()
    teacher_email=models.EmailField(unique=True)

    select_subject=[
        ('TELUGU','TELUGU'),
        ('HINDI','HINDI'),
        ('ENGLISH','ENGLISH'),
        ('MATHS','MATHS'),
        ('SCIENCE','SCIENCE'),
        ('SOCIAL','SOCIAL')
    ]

    teaching_subject=models.CharField(max_length=20,choices=select_subject)


