from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
# Create your views here.
from .models import Article


@login_required
def article_detail_view(request, id=None):
    # if(request.GET):
    print(bool(request.GET))
    # print(request.GET['q'])
    print(request.method == "GET")
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "article_obj": article_obj
    }
    return render(request, "articles/detail.html", context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm(request.POST or None)
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_obj = Article.objects.create(title=title, content=content)
        context['object'] = article_obj
        context['created'] = True
    return render(request, 'articles/create.html', context)

# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if(request.method == "POST"):
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_obj = Article.objects.create(title=title,content=content)
#             context['object'] = article_obj
#             context['created'] = True
#     return render(request,'articles/create.html',context)
