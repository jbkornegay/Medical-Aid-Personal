"""medicalAid1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from aidApp import views as aid_app_views
# from aidApp import feedback 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', aid_app_views.index, name = "homepage"),
    path('aid/', include('aidApp.urls')),
    path('feedback/',aid_app_views.feedbackview, name = "feedback"),
    path('new-post/', aid_app_views.createpost, name="new-post"),

    
]

