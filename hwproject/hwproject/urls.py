"""hwproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import homeapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.login, name ='login'),
    path('home/', homeapp.views.home, name ='home'),
    path('signup/', accounts.views.signup, name='signup'),
    path('search/', homeapp.views.search, name ='search'),
    path('detail/<int:id>', homeapp.views.detail, name="detail"),
    path('new/<int:id>', homeapp.views.new, name ='new'),
    path('create/<int:id>',homeapp.views.create, name = 'create'),
    path('update/<int:id>', homeapp.views.update, name ='update'),
    path('delete/<int:id>', homeapp.views.delete, name ='delete'),
    path('db/', homeapp.views.db, name="db")
]
