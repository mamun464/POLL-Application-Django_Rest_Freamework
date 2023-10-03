from django.contrib import admin
from .models import Author
from .models import Choice

admin.site.register(Author)
admin.site.register(Choice)