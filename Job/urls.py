"""Job URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView


router = DefaultRouter()
router.register(r'job_detail',views.JobDetailView),
router.register(r'job_category',views.JobCategory),
router.register(r'job_description',views.DescriptionView),


urlpatterns = [
    path('',include(router.urls)),
    path('login/',TokenObtainPairView.as_view()),
    path('admin/', admin.site.urls),
    path('new_contact/',views.CreateContact),
    path('get_contact_detail/',views.ContactData)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Job Portal Admin'
admin.site.site_title = 'Job Portal Admin'