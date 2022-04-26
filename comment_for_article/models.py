from django.db import models


class Article(models.Model):
    """Статья"""

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    """Комментарий"""

    text = models.TextField(blank=True, null=True, verbose_name='Текст коментария')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья', related_name='comments')
    parent = models.ForeignKey('self', verbose_name='родитель', on_delete=models.SET_NULL, blank=True, null=True,
                               related_name='children')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



