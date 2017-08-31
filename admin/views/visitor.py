from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.forms.models import model_to_dict
from admin.views.base import BaseView
from admin.models import VisitorModel,VisitedRecordModel

class Visitor(BaseView):
    """ 访客管理 """

    def index(self,request):
        input = {}
        input['page'] = request.GET.get("page")
        _visitors = VisitorModel.objects.all()
        visitors = []
        for visitor in _visitors:
            add_time = visitor.add_time
            visited_records = VisitedRecordModel.objects.filter(visitor=visitor)
            visitor = model_to_dict(visitor)
            visitor['add_time'] = add_time
            visitor['latest_visited_record'] = visited_records.order_by("-visited_time")[0]
            visitor['visited_records_num'] = visited_records.count() 
            visitors.append(visitor)

        paginator = Paginator(visitors,10)
        try:
            self.context['visitors'] = paginator.page(input['page'])
        except PageNotAnInteger:
            self.context['visitors'] = paginator.page(1)
        except EmptyPage:
            self.context['visitors'] = paginator.page(paginator.num_pages)
        return render(request,"admin/visitor/index.html",self.context)

    def change_forbidden_visit(self,request):
        input = {}
        input['id'] = request.POST.get("id")
        input['forbidden_visit'] = request.POST.get("forbidden_visit")
        visitor = VisitorModel.objects.get(id=input['id'])
        visitor.forbidden_visit = input['forbidden_visit']
        visitor.save()
        return JsonResponse({'code':200,'msg':'更新访客禁止访问属性成功','data':{'id':visitor.id,'forbidden_visit':visitor.forbidden_visit}})

