from django.contrib import admin
# import your model
from collection.models import podcast_show

class PdbAdmin(admin.ModelAdmin):
    model = podcast_show
    list_display = ('name', 'description','tag_list')
    prepopulated_fields = {'slug': ('name',)}
    
    def get_queryset(self, request):
        return super(PdbAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, podcast_show):
        return u", ".join(o.name for o in podcast_show.tags.all())
    

# Register your models here.
admin.site.register(podcast_show, PdbAdmin)
