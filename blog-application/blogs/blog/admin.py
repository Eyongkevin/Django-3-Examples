from ast import Dict
from typing import Optional, Sequence
from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_username",
        "body",
        "publish",
        "status",
    )
    list_filter = ("status", "publish")
    search_fields: Sequence[str] = ("title", "body")
    # TODO: 'prepopulated_fields' Do not work for updates
    prepopulated_fields: Dict(str, Sequence[str]) = {"slug": ("title",)}
    raw_id_fields: Sequence[str] = ("author",)
    date_hierarchy: Optional[str] = "publish"
    ordering: Optional[Sequence[str]] = ("status", "publish")

    @admin.display(description="Author username")
    def get_username(self, obj):
        return obj.author.username
