from django.contrib import admin
from example.models import Post

@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
