from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post



# Create your views here.
def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})
def detail(request, id):
    post = get_object_or_404(Post, pk = id) #해당 아이디값이 있는 블로그의 오브젝트를 가져오거나 없으면 404에러
    return render(request, 'detail.html', {'post':post})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.now()
    new_post.save()

    return redirect('detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id) 
    return render(request, 'edit.html', {'post':edit_post})

def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.body = request.POST['body']
    update_post.pub_date = timezone.now()
    update_post.save()
    return redirect('detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('home')