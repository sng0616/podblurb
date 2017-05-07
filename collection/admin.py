from django.contrib import admin
# import your model
from collection.models import podcast_show

class PdbAdmin(admin.ModelAdmin):
    model = podcast_show
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(podcast_show, PdbAdmin)