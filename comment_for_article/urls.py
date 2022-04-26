# from django.urls import path
#
# from comment_for_article.views import ArticleListAPIView, CommentCreateListAPIView, CommentRetrieveDestroyAPIView, \
#     ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView
#
# urlpatterns = [
#     path('article_list/', ArticleListAPIView.as_view(), name='articles_list'),
#     path('comment/', CommentCreateListAPIView.as_view(), name='comments_list'),
#     path('comment/<int:pk>', CommentRetrieveDestroyAPIView.as_view(), name='comments_destroy_list'),
#     path('article/', ArticleListCreateAPIView.as_view(), name='articles_create_list'),
#     path('article/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='articles_update_destroy_list')
# ]