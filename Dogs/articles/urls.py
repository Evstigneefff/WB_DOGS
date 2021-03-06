from django.urls import URLPattern, path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('', views.articles, name= 'articles'),
    path('about/', views.about, name= 'about'),
    path('<int:article_id>/', views.detail, name= 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name= 'leave_comment'),
]
