from django.contrib import admin
from .models import Library, Rack, BookItem
# Register your models here.
admin.site.register(Library)
admin.site.register(Rack)
admin.site.register(BookItem)