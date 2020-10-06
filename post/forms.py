from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):

# subtitleを必須事項じゃなくする
    def __init__(self, *args, **kwd):
        super(PostCreateForm, self).__init__(*args, **kwd)
        self.fields["subtitle"].required = False
        self.fields["desc2"].required = False
        self.fields["desc3"].required = False

    class Meta:
        model = Post
        fields = ('title','subtitle','tec_img','desc1','desc2','desc3')
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

# データベースから該当のデータを持ってきて、編集する機能を入れたい

