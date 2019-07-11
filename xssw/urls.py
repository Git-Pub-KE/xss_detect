from django.conf.urls import url
from django.urls import path
from xssw import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   url(r'^$',views.get,name='get'),
   url(r'^about/',views.about,name='about')
   
]

urlpatterns +=staticfiles_urlpatterns()
