from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def homePage(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'posts': posts})

def blogPost(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_post.html', {'post': post})
