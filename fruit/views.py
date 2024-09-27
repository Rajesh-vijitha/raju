from django.shortcuts import render
from django.http import HttpResponse

from fruit.models import Fruit, Places


def fruit_app_landingpage(request):
    return HttpResponse('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1 style="color:Red; text-align: center">Welcome To fruit App</h1>
</body>
</html>''')

def fruit_view(request):
    fruit1 = Fruit.objects.all()
    return render(request=request,template_name="fruits/fruit_view.html",context={"fruit1": fruit1})

def places_view(request):
    places1 = Places.objects.all()
    return render(request=request,template_name="fruits/places_view.html",context={"places1": places1})