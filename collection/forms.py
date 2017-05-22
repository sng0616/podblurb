from django.forms import ModelForm
from collection.models import podcast_post

class EditForm(ModelForm):
    class Meta:
        model = podcast_post
        fields = ('post_title','post_content')