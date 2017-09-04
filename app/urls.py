"""wdcxcblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import app.views as app

urlpatterns = [
    url(r'^index$',app.index,name='index'),
    url(r'^article$',app.article,name='article'),
    url(r'^tag$',app.tag,name='tag'),
    url(r'^category$',app.category,name='category'),
    url(r'^date_archive$',app.date_archive,name='date_archive'),
    url(r'^movie$',app.movie,name='movie'),
    url(r'^add_comment$',app.add_comment,name='add_comment'),
    url(r'^get_comment$',app.get_comment,name='get_comment'),
]
