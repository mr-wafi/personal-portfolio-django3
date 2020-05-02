from django.shortcuts import render, get_object_or_404#if there is no page avalible then we will call this method
from .models import Blog
def all_blogs(request):
    blogs = Blog.objects.all()#if you want just to show the recent one so use object.order_by(-date)this will show the recent one
    #and if you want to limit it then object.order_by(-date)[:5] this will show only 5 post
    return render(request, 'blog/all_blogs.html', {'blogs' :blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #here we are searching for the id which is comming from the url and searching it in
    #the blog table the pk mean primary key so every id is a primary key if the search found any result in blog table so it will
    #display it in the page if not it will display the 404 page not found error
    return render(request, 'blog/detail.html', {'blog':blog})
