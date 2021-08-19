from comments.models import Comment
from django.contrib import admin


@admin.register(Comment)
class ComentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post', 'created_at']
