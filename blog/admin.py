from django.contrib import admin
from .models import Blog, Author, Entry

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass
