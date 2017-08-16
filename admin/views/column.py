from django.shortcuts import render
from admin.views.base import BaseView

class Column(BaseView):
    """栏目管理"""

    def index(self,request):
        return render(request,"admin/column/index.html",self.context)
