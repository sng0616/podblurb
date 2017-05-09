from django.forms import ModelForm
from collection.models import podcast_show

class EditForm(ModelForm):
    class Meta:
        model = podcast_show
        fields = ('name','description')