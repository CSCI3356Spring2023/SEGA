"""TAMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('', include('summary.urls')),
#     path('', include('createcourse.urls')),
#     path('admin/', admin.site.urls),
#     path('register/', views.register, name='register'),
# ]

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views as view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("django.contrib.auth.urls")),
    path('', view.home, name='home'),

    path('accounts/login/', view.login_view, name='login'),
    path('logout/', view.logout_view),
    path('register/', view.register, name='register'),
    path('studentregister/', view.studentregister, name='studentregister'),
    path('instructorregister/', view.instructorregister, name='instructorregister'),
]
