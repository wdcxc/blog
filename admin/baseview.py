from django.shortcuts import render
from django.views import View

class BaseView(View):
    """后台管理类"""

    def __init__(self):
        """初始化"""
        self.context = {}
        self.context["path"] = {}
        _path = request.path_info.split("/")[1:]
        self.context["path"]["app"] = _path[0]
        self.context["path"]["module"] = _path[1]
        self.context["path"]["action"] = _path[-1]

    
