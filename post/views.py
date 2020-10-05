from django.shortcuts import render, redirect
from .forms import CreateForm
from django.views.decorators.http import require_POST

from .models import Post

def post_list(request):
    context = {
        'post_list': Post.objects.all(),
    }
    return render(request, 'post/post_list.html', context)


def post_create(request):
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # post_listに移行
            return redirect('post:post_list')
    else:
        form = CreateForm()
    return render(request, 'post/post_create.html', {'form': form})


# Create your views here.
