from django.shortcuts import render ,redirect
from django.http import HttpResponse
from blog.models import Post , article
from django.contrib.auth.decorators import login_required
from . import forms
def index (request) :
    ret = '<body>'
    all_posts = Post.objects.all()
    for post in all_posts:
        ret = ret + '<p>' + post.text +'</p>'
    ret = ret + '</body>'
    return HttpResponse(ret)
def article_list (request):
    Articles = article.objects.all().order_by('date')
    return render(request , 'articles/article_list.html' , {'Articles':Articles})
# Create your views here.
def article_detail(request,slug): 
    # return HttpResponse(slug)
    Article = article.objects.get(slug=slug)
    return render(request , 'articles/article_detail.html' ,{'article' : Article})
@login_required(login_url = '/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.Create_Article(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect ('articles')
    else :
        form = forms.Create_Article()
    return render(request , "articles/article_create.html" , {'form' : form })
