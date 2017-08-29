from django.shortcuts import render
from django.db.models import Count
from admin.views.base import BaseView
from admin.models import ArticleModel,TagModel,CategoryModel

class Overview(BaseView):
    """总览"""

    def index(self,request):
        try:
            articles = ArticleModel.objects
            self.context['articles'] = { 
                'count':articles.count(),
                'open_articles_num':articles.filter(open_to_public=True).count,
                'latest_article':articles.order_by("-add_time")[0],
                'hotest_article':articles.order_by("-read_num")[0],
            }
            tags = TagModel.objects
            self.context['tags'] = {
                'count':tags.count(),
                'show_tags_num':tags.filter(show=True).count(),
                'latest_tag':tags.order_by("-add_time")[0],
                'most_articles_tag':tags.annotate(related_articles_num=Count('article')).order_by("-related_articles_num")[0]
            }
            categories = CategoryModel.objects
            self.context['categories'] = {
                'count':categories.count(),
                'show_categories_num':categories.filter(show=True).count(),
                'latest_category':categories.order_by("-add_time")[0],
                'most_articles_category':categories.annotate(related_articles_num=Count('article')).order_by("-related_articles_num")[0]
            }
        except Exception as e:
            print(e)
        return render(request,"admin/overview/index.html",self.context)



