from django.urls import path

from likeapp.views import LikeArticleView

app_name = 'likeapp'

urlpatterns = [
    path('articles/<int:article_pk>', LikeArticleView.as_view(), name='article_like')
]