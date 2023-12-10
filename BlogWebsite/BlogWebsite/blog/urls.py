from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('testuser/', views.testuser, name='testuser'),
    path('showblog/', views.showblog, name='showblog'),
    path('showblog/blogdetails/<int:id>', views.blogdetails, name='blogdetails'),
    path('showComment/', views.showComment, name='showComment'),
    path('showComment/', views.showComment, name='showComment'),
    path('showcategories/', views.showcategories, name='showcategories'),
]
