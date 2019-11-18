"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # ^$ 는 현재 폴더를 의미
    url(r'^$',views.index, name = 'polls'),
    url(r'^signin/',views.signin, name='signin' ),
    url(r'^login/',views.login, name='login' ),
    url(r'^register/',views.register, ),
    url(r'^index1/',views.index1, name = 'index1' ),
    url(r'^book/(?P<pk>[0-9]+)/$' ,views.bookdetail, name='bookdetail'),
    url(r'^rent/(?P<pk>[0-9]+)/$', views.rent, name='rent'),
    url('test1', views.test1),
    url(r'^rentlist/', views.rentlist1, name='rentlist1'),
    # url(r'^dojoin/', views.dojoin, name='dojoin'),
    # 
]
