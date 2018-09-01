from django.core.exceptions import ValidationError
from django.forms import ModelForm


from posts.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['owner']



    def clean(self):
        super().clean()  # al llamar al método clean de la superclase garantizamos la validacion de los campos del modelo


