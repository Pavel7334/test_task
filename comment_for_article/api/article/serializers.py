from rest_framework.serializers import ModelSerializer

from comment_for_article.api.comment.serializers import CommentSerializer
from comment_for_article.models import Article


class ArticleSerializer(ModelSerializer):
    """Вывод статей"""

    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'name', 'description', 'created_at', 'comments')
