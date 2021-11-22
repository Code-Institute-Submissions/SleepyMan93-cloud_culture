from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blog_posts(request):
    """ A view to show all the blog posts, including search queries """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, blog_id):
    """ A view to render individual blog posts or return 404 error page """

    post = get_object_or_404(Blog, pk=blog_id)

    context = {
        'post': blog,
    }

    return render(request, 'blog/blog_post.html', context)
