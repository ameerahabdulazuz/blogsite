from django.http import HttpResponse
from django.template import loader
from .models import Post
from .models import Comment
from .models import category
from .models import myUsers


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def testuser(request):
    MyUsers = myUsers.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'MyUsers': MyUsers,
    }
    return HttpResponse(template.render(context, request))


def showblog(request):
    mymembers = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def showComment(request):
    commentS = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {
        'commentS': commentS,
    }
    return HttpResponse(template.render(context, request))


def showcategories(request):
    Category = category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'Category': Category,
    }
    return HttpResponse(template.render(context, request))


def blogdetails(request, id):
    mymemberstest = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'mymemberstest': mymemberstest,
    }
    return HttpResponse(template.render(context, request))
