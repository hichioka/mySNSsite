from django.shortcuts import render, redirect
from .forms import PostCreateForm
from django.views.decorators.http import require_POST

from .models import Post
from django import forms

def post_list(request):
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):#クリエイトの処理を行う
    if request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():#中身チェック
            form.save()#保存
            #ふぉーむに異常らなく成功した時にpost_listに移行
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
    #何か異常があった時は同じくpost_createに移行
    return render(request, 'post/post_create.html', {'form': form})

def post_edit(request):
    context = {
        'post_edit': Post.objects.all(),
    }
    return render(request, 'post/post_edit.html', context)

def post_remove(request):
    context = {
        'post_remove': Post.objects.all(),
    }
    return render(request, 'post/post_remove.html', context)

