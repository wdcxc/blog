from django.conf.urls import url
import jdcrawler.views as views

app_name = 'jdcrawler'

urlpatterns = [
    url(r'^index$',views.index,name='index'),
]

