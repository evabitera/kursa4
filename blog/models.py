from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст")
    images = models.ImageField(upload_to="blog/images", verbose_name="Превью блога", **NULLABLE)
    blog_date = models.DateField(verbose_name="Дата публикации", **NULLABLE)
    count_views = models.IntegerField(verbose_name="Количество просмотров", default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
