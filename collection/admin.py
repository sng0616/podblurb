from django.contrib import admin
from collection.models import podcast_post, podcast_show

class PdbPost(admin.ModelAdmin):
    model = podcast_post
    list_display = ('post_title', 'post_content','tag_list')
    prepopulated_fields = {'slug': ('post_title',)}
    
    def get_queryset(self, request):
        return super(PdbPost, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, podcast_post):
        return u", ".join(o.post_title for o in podcast_post.tags.all())
    
class PdbShow(admin.ModelAdmin):
    model = podcast_show
    list_display = ('show_name','show_description','show_website','show_format')
    prepopulated_fields = {'show_slug': ('show_name',)}

    def get_queryset(self, request):
        return super(PdbShow, self).get_queryset(request).prefetch_related('show_tags')

    def show_tags_list(self, podcast_post):
        return u", ".join(o.show_name for o in podcast_show.show_tags.all())
    
# Register your models here.
admin.site.register(podcast_post, PdbPost)
admin.site.register(podcast_show, PdbShow)
