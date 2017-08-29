from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from admin.views.base import BaseView
from admin.models import TagModel

class Tag(BaseView):
    """栏目管理"""

    def index(self,request):
        input = {}
        input['page'] = request.GET.get("page")
        tags = TagModel.objects.all().order_by("-grade","-add_time")
        paginator = Paginator(tags,8)
        try:
            self.context['tags'] = paginator.page(input['page'])
        except PageNotAnInteger:
            self.context['tags'] = paginator.page(1)
        except EmptyPage:
            self.context['tags'] = paginator.page(paginator.num_pages)
        return render(request,"admin/tag/index.html",self.context)

    def change_grade(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['type'] = request.POST.get("type")
        tag = TagModel.objects.get(id=input['id'])
        if input['type'] == "increase":
            tag.grade = tag.grade + 1
        else:
            tag.grade = tag.grade - 1
        tag.save()
        return JsonResponse({'code':200,'msg':'更新tag等级成功','data':{'id':tag.id,'grade':tag.grade}})

    def change_show(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['show'] = request.POST.get("show")
        tag = TagModel.objects.get(id=input['id'])
        tag.show = input['show']
        tag.save()
        return JsonResponse({'code':200,'msg':'更新tag显示属性成功','data':{'id':tag.id,'show':tag.show}})

