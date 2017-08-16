from django.shortcuts import render

def index(request):
    return render(request,"jdcrawler/index.html",context={})
