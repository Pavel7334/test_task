from django.urls import path

from comment_for_article.api.article.views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView
from comment_for_article.api.comment.views import CommentCreateListAPIView, CommentRetrieveDestroyAPIView

urlpatterns = [
    path('comment/', CommentCreateListAPIView.as_view(), name='comments_list'),
    path('comment/<int:pk>', CommentRetrieveDestroyAPIView.as_view(), name='comments_destroy_list'),
    path('article/', ArticleListCreateAPIView.as_view(), name='articles_create_list'),
    path('article/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='articles_update_destroy_list')
]
