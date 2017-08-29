from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from admin.views.base import BaseView

class Admin(BaseView):

    def login(self,request):
        request.session['login'] = False
        if request.method == "GET":
            return render(request,'admin/admin/login.html')
        elif request.method == "POST":
            input = {}
            input['user'] = request.POST.get("user")
            input['password'] = request.POST.get("password")
            if input['user'] == 'wdcxc' and input['password'] == 'wdcxc!':
                request.session['login'] = True
                request.session['login_user'] = input['user']
                return HttpResponseRedirect(redirect_to='/admin/overview/index')  
            else:
                return render(request,'admin/admin/login.html',{'error':'账号或密码错误'})

    def logout(self,request):
        request.session.clear()
        return HttpResponseRedirect(redirect_to='/admin/admin/login')
    
