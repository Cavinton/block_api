# Register your models here.
from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'description', 'created_at')
    list_filter = ('created_at',)  #фильтрация по дате создания
    search_fields = ('title',)  #создает поисковик по названию


admin.site.register(Post, PostAdmin)