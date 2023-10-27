from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, 'todo/todo_list.html')
