from django.urls import path

from . import views

app_name = 'top10'

urlpatterns = [
    path('', views.index, name='index'),
    path('tech', views.tech, name = 'tech'),
    path('post/<slug:post_slug>/', views.detail, name = 'detail'),
    path('post/<slug:post_slug>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('finance', views.finance, name = 'finance'),
    path('health', views.health, name = 'health'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('family', views.family, name='family'),
    path('business', views.business, name='business'),
    path('shopping', views.shopping, name='shopping'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('personal_growth', views.personal_growth, name='personal_growth'),
    path('register/', views.registerPage, name='register'),
    path('log-in/', views.logIn, name='log-in'),
    path('log-out/', views.logOut, name='log-out')
]