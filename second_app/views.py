from django.shortcuts import render, redirect

# Create your views here.
from second_app.forms import BookForm
from second_app.models import Book


def index(req):
    book = Book.objects.all()
    context = {
        'book':book.order_by('title')
    }
    return render(req, 'second_app/index.html', context)


def create_book(request):
    if request.method == 'GET':
        context = {
        'form': BookForm
        }
        return render (request, 'second_app/create_book.html', context)

    else:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secondary_index')
        else:

            context = {'form': form}
        return render (request, 'second_app/create_book.html', context)


def edit_book(request, pk):
    obj = Book.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'obj':obj,
            'form':BookForm(instance = obj)
        }
        return render(request, 'second_app/edit_book.html', context)
    else:
        form = BookForm(request.POST, instance = obj)
        if form.is_valid():
            form.save()
        return redirect('secondary_index')


def delete_book(req, pk):
    obj = Book.objects.get(pk = pk)
    if req.method == 'GET':
        context={
            'obj':obj,
            'form':BookForm(instance = obj)
        }
        return render(req, 'second_app/delete_book.html', context)
    else:
        obj.delete()
        return redirect('secondary_index')


def delete_view(req, pk):
    obj = Book.objects.get(pk= pk)
    if req.method == 'POST':
        context ={
            'obj':obj,
            'form':BookForm(instance = obj)
        }
        return render(req, 'second_app/delete_book.html', context)
    else:
        obj.delete()
        return redirect('secondary_index')





