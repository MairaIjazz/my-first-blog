from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blogs.models import Post

def index(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request, 'index.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post':post})