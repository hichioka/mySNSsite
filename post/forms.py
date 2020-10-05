from django import forms
from .models import Post

class CreateForm(forms.ModelForm):

# subtitleを必須事項じゃなくする
    def __init__(self, *args, **kwd):
        super(CreateForm, self).__init__(*args, **kwd)
        self.fields["subtitle"].required = False

    class Meta:
        model = Post
        fields = ('title','subtitle','tec_img','desc',)
        widgets = {
            'title': forms.Textarea(
                attrs={'rows': 1, 'cols': 20, 'placeholder': '技術名称'}
            ),
        }
        widgets = {
            'subtitle': forms.Textarea(
                attrs={'rows': 1, 'cols': 20, 'placeholder': 'サブ技術名称'}
            ),
        }