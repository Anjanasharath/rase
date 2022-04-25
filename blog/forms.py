from django import forms

from blog.models import Blog, BlogComment, BlogImage


class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("title","content")


class BlogImageForm(forms.ModelForm):
    
    class Meta:
        model = BlogImage
        fields = ("image",)
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'multiple': 'true', "required":"false"})
        }



class BlogCommentForm(forms.ModelForm):
    
    class Meta:
        model = BlogComment
        fields = ("comment",)
