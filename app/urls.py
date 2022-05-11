from django.urls import path
from app import views

urlpatterns = [
    # トップページに遷移
    path('', views.IndexView.as_view(), name='index'),
    # 商品ページに遷移
    path('detail/<str:isbn>', views.DetailView.as_view(), name='detail'), 
]