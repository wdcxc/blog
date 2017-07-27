from admin.views.base import BaseView
from django.shortcuts import render

class Article(BaseView):
    """文章管理"""

    def index(self,request):
        return render(request,"admin/article/index.html",self.context)

    
    def add(self,request):
        return render(request,"admin/article/add.html",self.context)
