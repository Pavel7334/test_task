from drf_yasg.generators import OpenAPISchemaGenerator


class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        """Generate a :class:`.Swagger` object with custom tags"""

        swagger = super().get_schema(request, public)
        swagger.tags = [
            {
                "name": "article",
                "description": "Создание статьи, удаление статьи, изменение статьи, получение статьи"
            },
            {
                "name": "comment",
                "description": "Получить комментарий, создание комментария, удаление комментария"
            },
        ]

        return swagger
