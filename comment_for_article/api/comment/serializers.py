from rest_framework.serializers import ListSerializer, Serializer, ModelSerializer

from comment_for_article.models import Comment


class FilterCommentListSerializer(ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentSerializer(ModelSerializer):
    """Вывод комментариев"""

    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ('id', 'parent', 'text', 'children')
