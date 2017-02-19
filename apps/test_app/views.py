# Create a web page with blog entrys and the ability to comment underneath them
from django.shortcuts import render, redirect
from . models import Blog, Comment   # . means from same directory that we're sitting in,
                                     # then get the classes Blog and Comment

# Create your views here.
def index(request):
    context = {
    "blogs" : Blog.objects.all()  # runs query: SELECT * FROM blogs
    }
    return render(request, 'test_app/index.html', context)

def blogs(request):
    print "************************"
    print "Post Title"
    print request.POST['title']
    print "Post Blog"
    print request.POST['blog']
    print "************************"
    # using ORM, create new blog
    # Go to class Blog and then the manager of the class which is named objects. Then create and pass in variables
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])  # This will run the SQL query
    # This said - Insert into blogs (title, blog, created_at, updated_at) values (title, blog, now(), now)
    return redirect('/')

def comments(request, id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comment'],blog=blog)
    return redirect('/')
