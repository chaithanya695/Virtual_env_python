from django.contrib import admin

# Register your models here.
from app1.models import Teachers

# # Register your models here.
class teacher_admin(admin.ModelAdmin):
    list_display=['teacher_id','teacher_name','teacher_salary','teacher_email','teaching_subject']
admin.site.register(Teachers,teacher_admin)
