from django.shortcuts import render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from admin.models import ArticleModel,TagModel,CategoryModel,DateArchiveModel,VisitorModel,VisitedRecordModel,CommentModel
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json

def init_context():
    """初始化模板显示变量"""

    context = {}
    context['all_tags'] = TagModel.objects.filter(show=True).order_by("-grade","-add_time")
    context['all_categories'] = CategoryModel.objects.filter(show=True,).order_by("-grade","-add_time")
    context['hot_articles'] = ArticleModel.objects.filter(open_to_public=True).order_by("-read_num","-add_time")[:5]
    context['date_archive_years'] = DateArchiveModel.objects.filter(grade=DateArchiveModel.DATE_GRADE_YEAR).order_by("-date")
    context['categories_in_header'] = CategoryModel.objects.filter(show_in_header=True).order_by("-grade","-add_time")
    return context

def index(request):
    """首页"""
    
    context = init_context()
    input = {}
    input['page'] = request.GET.get("page")
    articles = articles_append_meta(ArticleModel.objects.filter(open_to_public=True).order_by('-add_time'))
    context['articles'] = get_paginator_articles(articles=articles,page=input['page'],page_size=8)
    if request_from_mobile(request):
        return render(request,'app/mobile/index.html',context)
    else:
        return render(request,'app/index.html',context)

def article(request):
    """文章详情"""
    
    input = {}
    input['id']=request.GET.get("id")
    context = init_context()
    article = ArticleModel.objects.get(id=input['id'])
    article.read_num += 1
    article.save()
    visitor = VisitorModel.objects.get_or_create(IP=request.META['REMOTE_ADDR'])[0]
    VisitedRecordModel(visitor=visitor,article=article).save()
    context['article'] = articles_append_meta([article])[0]
    context['visitor'] = visitor
    context['comments'] = article.comments.all()
    if request_from_mobile(request):
        return render(request,'app/mobile/article.html',context)
    else:
        return render(request,'app/article.html',context)

def tag(request):
    """标签"""

    input = {}
    input['tag_id'] = request.GET.get("id")
    input['page'] = request.GET.get("page")
    context = init_context()
    selected_tag = TagModel.objects.get(id=input['tag_id'],show=True)
    context['selected_tag'] = selected_tag
    articles = selected_tag.articles.filter(open_to_public=True).order_by("-add_time")
    context['articles'] = get_paginator_articles(articles=articles_append_meta(articles),page=input['page'],page_size=8)
    return render(request,'app/tag.html',context)

def category(request):
    """文章分类"""

    input = {}
    input['page'] = request.GET.get("page")
    input['category_id'] = request.GET.get("id")
    context = init_context()
    selected_category = CategoryModel.objects.get(id=input['category_id'],show=True)
    context['selected_category'] = selected_category
    articles = selected_category.articles.filter(open_to_public=True).order_by("-add_time")
    context['articles'] = get_paginator_articles(articles=articles_append_meta(articles),page=input['page'],page_size=8)
    if request_from_mobile(request):
        return render(request,'app/mobile/category.html',context)
    else:
        return render(request,'app/category.html',context)

def date_archive(request):
    """日期归档"""

    input = {}
    input['page'] = request.GET.get("page")
    input['year'] = request.GET.get("year")
    input['month'] = request.GET.get("month",default=None)
    context = init_context()
    context['selected_archive_date'] = {"year":input['year'],"month":input['month']}
    if input['month'] is None:
        articles = DateArchiveModel.objects.get(grade=DateArchiveModel.DATE_GRADE_YEAR,date=input['year']).articles.filter(open_to_public=True).order_by("-add_time")
    else:
        articles = DateArchiveModel.objects.get(grade=DateArchiveModel.DATE_GRADE_MONTH,date=input['month']).articles.filter(open_to_public=True).order_by("-add_time")
    context['articles'] = get_paginator_articles(articles=articles_append_meta(articles),page=input['page'],page_size=8)
    return render(request,'app/date_archive.html',context)

def movie(request):
    """电影资源分享首页"""

    input = {}
    input['search_name'] = request.GET.get("search_name")
    context = {}
    context['movies'] = search_movies(name=input['search_name'])
    return render(request,'app/movie.html',context)

def add_comment(request):
    """新增评论"""

    input = {}
    input['article_id'] = request.POST.get("article_id")
    input['comment_id'] = request.POST.get("comment_id")
    input['visitor_id'] = request.POST.get("visitor_id")
    input['comment_content'] = request.POST.get("comment_content")
    visitor = VisitorModel.objects.get(id=input['visitor_id'])
    comment = CommentModel(content=input['comment_content'],visitor=visitor)
    if input['article_id']:
        comment.save()
        article = ArticleModel.objects.get(id=input['article_id'])
        article.comments.add(comment)
    if input['comment_id']:
        replied_comment = CommentModel.objects.get(id=input['comment_id'])
        comment.grade = replied_comment.grade + 1
        comment.save()
        replied_comment.reply_comments.add(comment)
        article = replied_comment.article 
        article.comments.add(comment)
    return JsonResponse({'code':200,'msg':'发表评论成功','data':{'comment_id':comment.id}})

def get_comment(request):
    """获取评论"""

    input = {}
    input['comment_id'] = request.POST.get("comment_id")
    input['article_id'] = request.POST.get("article_id")
    if input['comment_id']:
        comment = CommentModel.objects.get(id=input['comment_id'])
        if comment.reply_comments:
            comment_ids = [str(comment.id) for comment in comment.reply_comments.order_by("-add_time").all()]
        else:
            comment_ids = None 
        add_time = comment.add_time.strftime("%Y-%m-%d %H:%M:%S")
        visitor = model_to_dict(comment.visitor);
        comment = model_to_dict(comment)
        comment['add_time'] = add_time
        del comment['reply_comments']
        return JsonResponse({'code':200,'msg':'获取评论成功','data':{'comment':json.dumps(comment),'visitor':json.dumps(visitor),'comment_ids':comment_ids}})
    elif input['article_id']:
        article = ArticleModel.objects.get(id=input['article_id'])
        if article.comments:
            comment_ids = [str(comment.id) for comment in article.comments.filter(grade=0).order_by("-add_time").all()]
        else:
            comment_ids = None
        return JsonResponse({'code':200,'msg':'获取评论成功','data':{'comment_ids':comment_ids}})
        
def articles_append_meta(articles):
    """添加文章附加的可显示的属性，包括 tag category """
    
    res = []
    for article in articles:
        show_tags = article.tags.filter(show=True).order_by("-grade","-add_time")
        show_categories = article.categories.filter(show=True).order_by("-grade","add_time")
        add_time = article.add_time
        article = model_to_dict(article)
        article['show_tags'] = show_tags
        article['show_categories'] = show_categories
        article['add_time'] = add_time
        res.append(article)
    return res

def request_from_mobile(request):
    """判断请求是不是来自移动端"""

    print(request.META['HTTP_USER_AGENT'])
    if 'nsukey' in request.GET:
        return True
    mobile_characters = ['mobile','Mobile','iPhone','iPad','MicroMessenger']
    for character in mobile_characters:
        if character in request.META['HTTP_USER_AGENT']:
            return True
    return False

def get_paginator_articles(articles,page,page_size=8):
    """获取分页化的文章列表"""
    
    paginator = Paginator(articles,page_size)
    try:
       paginator_articles = paginator.page(page)  
    except PageNotAnInteger:
       paginator_articles = paginator.page(1)
    except EmptyPage:
       paginator_articles = paginator.page(paginator.num_pages)
    return paginator_articles

def search_movies(name):
    print(name)
