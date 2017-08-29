import importlib
from django.conf import settings
from django.views import View
from django.http.response import HttpResponseRedirect

class BaseView(View):
    """后台管理基类"""

    def __init__(self):
        self.context = {}
        self.context["path"] = {}

    def dispatch(self,request,*args,**kwargs):
        _path = request.path_info.split("/")[1:]
        self.context["path"]["app"] = _path[0]
        self.context["path"]["module"] = _path[1]
        self.context["path"]["action"] = _path[-1]

        if self.context['path']['module'] == 'admin' or request.session.get("login",default=False) is True:
            imp_module_path = self.context["path"]["app"]+".views."+self.context["path"]["module"]
            imp_module = importlib.import_module(imp_module_path)
            imp_cls = getattr(imp_module,self.context["path"]["module"].capitalize())
            return getattr(imp_cls,self.context["path"]["action"])(self,request)
        else:
            return HttpResponseRedirect(redirect_to="/admin/admin/login")
