from django.contrib import admin

# Register your models here.
from todo_app.models import Todos, Categories, Person


admin.site.register(Todos)
admin.site.register(Categories)
admin.site.register(Person)