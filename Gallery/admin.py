from django.contrib import admin
from .models import Gallery_Main, Gallery_Detail


class GalleryMainAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    list_filter = ["date"]


class GalleryDetailAdmin(admin.ModelAdmin):
    list_display = ("image_alt", "image_group")
    search_fields = ("image_alt", "image_group__title")
    list_filter = ["image_group__title"]


admin.site.register(Gallery_Main, GalleryMainAdmin)
admin.site.register(Gallery_Detail, GalleryDetailAdmin)
