from django.shortcuts import render

# Create your views here.
from todo_app.models import Todos


def index (req):
    context ={
        'todos':Todos.objects.all()
    }
    return render(req, 'todo/index.html', context)


