from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Blog
from .forms import BlogForm

def allblogs(request):
    """Landing page of the blogs app."""
    blogs = Blog.objects.all()

    return render(request, 'blogs/allblogs.html', {'blogs': blogs})

def create(request):
    """Simple creation for a blog"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data = request.POST)
        # Validate
        if form.is_valid():
            form.save()
            # Redirect to all blogs
            return HttpResponseRedirect(reverse('allblogs'))

    return render(request, 'blogs/create.html', {'form': form})

def details(request, blog_id):
    """Read page of the blog entry."""
    blog = Blog.objects.get(id=blog_id)

    return render(request, 'blogs/details.html', {'blog': blog})

def update(request, blog_id):
    """Update the blog post"""
    # Must be passed to any conditional
    blog = Blog.objects.get(id = blog_id)

    if request.method != 'POST':
        # Assume GET
        form = BlogForm(instance = blog)
    else:
        # Assume POST
        form = BlogForm(instance = blog, data= request.POST)
        # Check validity before saving
        if form.is_valid():
            # Can the previous instance be used instead? The id is the same,
            # so it probably doens't matter.  This is technically more accurate.
            blog = form.save()
            # Redirect back to the details of the blog
            # Is form really needed here?
            context = {'blog': blog}

            return render(request, 'blogs/details.html', context)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/update.html', context)

def delete(request, blog_id):
    """Delete blog entry. Redirects to all blogs.:"""
    ### NOTES ###
    '''
    Ultimately I would want some sort of warning here to determine whether or not we
    truly want to delete the entry. I think this would be JS.
    For now, take it to a page with two options: Yes or No.
    '''
    blog = Blog.objects.get(id = blog_id)

    if request.method == 'POST':
        # Check for which input was selected. Works by checking the keys
        if '_yes' in request.POST:

            ########################
            # TEST. print to console
            # print(request.POST)
            # print()
            # returns this:
            '''
            <QueryDict: {
                'csrfmiddlewaretoken':
            ['bgYKvrOZnpnQ6NCa9cupeIyolCyzSCxgfj2FzGPnX6KyCRxkTqQ1txhCMstwGaV0'],
                '_yes': ['YES']
                }
            >
            '''
            ########################

            # Delete the entry
            blog.delete()
            return HttpResponseRedirect(reverse('allblogs'))
        else:
            # Cancel deletion, return to the detail page
            return render(request, 'blogs/details.html', {'blog': blog})

    return render(request, 'blogs/delete.html', {'blog': blog})
