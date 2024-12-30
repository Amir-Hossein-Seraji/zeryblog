from django.urls import path , re_path
from . import views



urlpatterns = [
    # path('',views.index , name = 'index'),
    path('',views.article_list , name = 'articles'),
    path('create/' , views.article_create , name = 'create'),
    path('<slug:slug>/', views.article_detail , name = 'article_detail'),
]