from django.shortcuts import render
from admin.views.base import BaseView

class Overview(BaseView):
    """总览"""

    def index(self,request):
        return render(request,"admin/overview.html",self.context)



