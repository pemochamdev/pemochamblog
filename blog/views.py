from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Blog, Category,Comment

def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):

    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }
    return render(request, 'blog/blog_detail.html', context)
