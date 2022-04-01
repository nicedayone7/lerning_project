from django.db import models


class Arts(models.Model):
    title = models.CharField(blank=True, max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    author = models.CharField(max_length=100, verbose_name='Автор')
    image = models.ImageField(upload_to='arts/%Y/%m/%d/', blank=True)
    creating_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    changed_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-changed_date', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True,
                            verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']