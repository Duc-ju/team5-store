from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(BookItem)
admin.site.register(BookImg)
