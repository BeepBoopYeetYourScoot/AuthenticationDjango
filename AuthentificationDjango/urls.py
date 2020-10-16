"""AuthentificationDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from basic import views as user_views
from django.contrib.auth import views as auth_views
from api import views as api_views
from api.routers import router
from api.yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('basic.urls')),

    path('api_access_all/', router.get_api_root_view(), name='access'),
    path('api-access/', include(router.urls)),
    path('api-access/farms/<pk>/relationships/<related_field>', api_views.FarmRelationshipView.as_view(),
         name='farms-relationships'),
    path('api-access/farms/<pk>/<related_field>/', api_views.FarmViewSet.as_view({'get': 'retrieve_related'}),
         name='farms-related'),
    path('api-access/cats/<pk>/relationships/<related_field>/', api_views.CatRelationshipView.as_view(),
         name='cats-relationships'),
    path('api-access/cats/<pk>/<related_field>/', api_views.CatViewSet.as_view({'get': 'retrieve_related'}),
         name='cats-related'),
    path('api-access/owners/<pk>/relationships/<related_field>/', api_views.OwnerRelationshipView.as_view(),
         name='owners-relationships'),
    path('api-access/owners/<pk>/<related_field>/', api_views.OwnerViewSet.as_view({'get': 'retrieve_related'}),
         name='owners-related')
]

urlpatterns += doc_urls
