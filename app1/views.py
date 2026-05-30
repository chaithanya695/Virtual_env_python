from django.shortcuts import render


from django.http import HttpResponse 

from app1.models import Teachers


def teacher_details(request):
    
    data=Teachers.objects.all() 

    # sending data in key and value pairs
    context={
        "data":data
    }
    return render(request,"app1_templates/home.html",context)