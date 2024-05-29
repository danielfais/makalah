from django.urls import re_path
from django.contrib import admin


from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^admin/', admin.site.urls),

]
