from django.shortcuts import render
from .models import Blog

def all_blog_posts(request):
    """ A view to show all the blog posts, including search queries """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
