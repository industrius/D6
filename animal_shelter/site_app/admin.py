from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Pet, Recall, Comment

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("get_image", "nickname", "age", "breed", "receipt_date")
    list_display_links = ("nickname",)
    list_filter = ("breed",)
    search_fields = ("nickname", "breed",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.foto.url} width="100"')

admin.site.register(Recall)
admin.site.register(Comment)