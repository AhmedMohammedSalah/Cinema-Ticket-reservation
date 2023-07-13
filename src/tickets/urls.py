"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tickets import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register ('guests',views.Viewsets_guest)
urlpatterns = [
    # 1 
    path('jsonresponsenomodel/',views.no_rest_no_model),
    # 2
    path('jsonresponsefrommodel/',views.no_rest_from_model),
    # 3
    path('rest/fbvlist/',views.fbv_list ),
    # 4 
    path('rest/fbvpk/<pk>/',views.fbv_pk ),
    
    # Class Based View 
    path('rest/cbv/',views.CBV_list.as_view()),
    # 
    path('rest/cbv/<pk>/',views.CBV_pk.as_view()),
     
    # Mixins 
    path('rest/mixins/',views.Mixins_list.as_view()),
    # 
    path('rest/mixins/<pk>/',views.Mixins_pk.as_view()),
    #Generics 
    path('rest/generics/',views.Generics_list.as_view()),
    # 
    path('rest/generics/<pk>/',views.Generics_pk.as_view()),
    # Viewsets
    path('rest/viewsets/',include(router.urls)),
    
]
