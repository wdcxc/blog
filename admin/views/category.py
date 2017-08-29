from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from admin.views.base import BaseView
from admin.models import CategoryModel

class Category(BaseView):
    """栏目管理"""

    def index(self,request):
        input = {}
        input['page'] = request.GET.get("page")
        categories = CategoryModel.objects.all().order_by("-grade","-add_time")
        paginator = Paginator(categories,8)
        try:
            self.context['categories'] = paginator.page(input['page'])
        except PageNotAnInteger:
            self.context['categories'] = paginator.page(1)
        except EmptyPage:
            self.context['categories'] = paginator.page(paginator.num_pages)
        return render(request,"admin/category/index.html",self.context)

    def change_grade(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['type'] = request.POST.get("type")
        category = CategoryModel.objects.get(id=input['id'])
        if input['type'] == "increase":
            category.grade = category.grade + 1
        else:
            category.grade = category.grade - 1
        category.save()
        return JsonResponse({'code':200,'msg':'更新category等级成功','data':{'id':category.id,'grade':category.grade}})

    def change_show(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['show'] = request.POST.get("show")
        category = CategoryModel.objects.get(id=input['id'])
        category.show = input['show']
        category.save()
        return JsonResponse({'code':200,'msg':'更新category显示属性成功','data':{'id':category.id,'show':category.show}})

    def change_show_in_header(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['show_in_header'] = request.POST.get("show_in_header")
        category = CategoryModel.objects.get(id=input['id'])
        category.show_in_header = input['show_in_header']
        category.save()
        return JsonResponse({'code':200,'msg':'更新category首页头部显示属性成功','data':{'id':category.id,'show_in_header':category.show_in_header}})
