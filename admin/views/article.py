from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from admin.models import ArticleModel,TagModel,CategoryModel,DateArchiveModel
from admin.views.base import BaseView

class Article(BaseView):
    """文章管理"""

    def __init__(self):
        pass

    def index(self,request):
        input = {}
        input['search'] = request.GET.get("search")
        if input['search']:
            input['search_condition'] = request.GET.get("search_condition")
            input['search_text'] = request.GET.get("search_text")
            articles = search_articles(input['search_condition'],input['search_text'])
            self.context['search'] = True
            self.context['search_condition'] = input['search_condition']
            self.context['search_text'] = input['search_text']
        else:
            articles = ArticleModel.objects.order_by("-add_time").all()
        input['page'] = request.GET.get("page")
        paginator = Paginator(articles,8)
        try:
            self.context['articles'] = paginator.page(input['page'])
        except PageNotAnInteger:
            self.context['articles'] = paginator.page(1)
        except EmptyPage:
            self.context['articles'] = paginator.page(paginator.num_pages)
        return render(request,"admin/article/index.html",self.context)
    
    def add(self,request):
        return render(request,"admin/article/add.html",self.context)

    def do_add(self,request):
        try:
            input = {}
            input['content'] = request.POST.get('content')
            article = save_article(content=input['content'])
            return JsonResponse({'code':200,'msg':'文章保存成功','data':{'article_id':article.id}})
        except Exception as e:
            print(e)
            return JsonResponse({'code':400,'msg':'文章保存失败','data':{'error':str(e)}})

    def delete(self,request):
        try:
            input = {}
            input['id'] = request.POST.get("id")
            article = ArticleModel.objects.get(id=input['id'])
            # 删除旧标签和分类
            for tag in article.tags.all():
                article.tags.remove(tag)
                if tag.articles.count() == 0:
                    tag.delete()
            for category in article.categories.all():
                article.categories.remove(category)
                if category.articles.count() == 0:
                    category.delete()
            article.delete()
            return JsonResponse({'code':200,'msg':'文章删除成功','data':{'id':input['id']}})
        except Exception as e:
            return JsonResponse({'code':400,'msg':'文章删除失败','data':{'error':str(e)}})

    def modify(self,request):
        input = {}
        input['id'] = request.GET.get("id")
        article = ArticleModel.objects.get(id=input['id'])
        self.context['article'] = article
        return render(request,'admin/article/modify.html',self.context)

    def do_modify(self,request):
        try:
            input = {}
            input['id'] = request.POST.get('id') 
            input['content'] = request.POST.get('content')
            save_article(content=input['content'],id=input['id'])
            return JsonResponse({'code':200,'msg':'修改文章成功','data':{'id':input['id']}})
        except Exception as e:
            print(e)
            return JsonResponse({'code':400,'msg':'修改文章失败','data':{'id':input['id'],'error':str(e)}})

    def open_to_public(self,request):
        try:
            input = {}
            input['id'] = request.POST.get("id")
            input['open'] = request.POST.get("open")
            article = ArticleModel.objects.get(id=input['id'])
            article.open_to_public=input['open']
            article.save()
            return JsonResponse({'code':200,'msg':'修改成功','data':{'id':input['id'],'open':input['open']}})
        except Exception as e:
            return JsonResponse({'code':400,'msg':'修改失败','data':{'id':input['id'],'open':input['open'],'error':str(e)}})

def search_articles(condition,text):
    """ 搜索文章 """

    if condition == "title":
        articles = ArticleModel.objects.filter(title__icontains=text)
    elif condition == "content":
        articles = ArticleModel.objects.filter(content__icontains=text)
    elif condition == "tag":
        articles = TagModel.objects.get(name=text).articles
    elif condition == "category":
        articles = CategoryModel.objects.get(name=text).articles
    return articles.order_by("-add_time")

def process_article(content):
    """处理 markdown 格式文章，提取 meta 信息"""

    processed_content = {}
    lines = content.splitlines()
    begin_mark = False
    line_count = 0
    for line in lines:
        line_count += 1
        if line == "---":
            if begin_mark is False:
                begin_mark = True
            else:
                break
        else:
            key,val = line.split(":")[:2]
            processed_content[key.strip()] = val.strip()
    processed_content['meta'] = '\n'.join(lines[:line_count+1])
    processed_content['content'] = '\n'.join(lines[line_count+1:])
    return processed_content

def save_article(content=None,id=None):
    """保存新文章或修改后的文章到数据库中"""

    processed_content = process_article(content)
    if id is None:
        article = ArticleModel(title=processed_content['title'],author=processed_content['author'],content=processed_content['content'],meta=processed_content['meta'])
        article.save()
        # 文章日期归档
        date_archive_year = DateArchiveModel.objects.get_or_create(grade=DateArchiveModel.DATE_GRADE_YEAR,date=datetime.today().year)[0]
        date_archive_month = DateArchiveModel.objects.get_or_create(grade=DateArchiveModel.DATE_GRADE_MONTH,date=datetime.today().month,pre_grade=date_archive_year)[0]
        date_archive_day = DateArchiveModel.objects.get_or_create(grade=DateArchiveModel.DATE_GRADE_DAY,date=datetime.today().day,pre_grade=date_archive_month)[0]
        article.date_archives.add(date_archive_year)
        article.date_archives.add(date_archive_month)
        article.date_archives.add(date_archive_day)
    else:
        article = ArticleModel.objects.get(id=id)
        article.meta = processed_content['meta']
        article.content = processed_content['content']
        article.title = processed_content['title']
        article.author = processed_content['author']
        # 删除旧标签和分类
        for tag in article.tags.all():
            article.tags.remove(tag)
            if tag.articles.count() == 0:
                tag.delete()
        for category in article.categories.all():
            article.categories.remove(category)
            if category.articles.count() == 0:
                category.delete()
    # 添加新标签和分类
    if 'tags' in processed_content:
        for tag in processed_content['tags'].split(','):
            article.tags.add(TagModel.objects.get_or_create(name=tag.strip())[0])
    if 'categories' in processed_content:
        for category in processed_content['categories'].split(','):
            article.categories.add(CategoryModel.objects.get_or_create(name=category.strip())[0])

    article.save()
    return article

