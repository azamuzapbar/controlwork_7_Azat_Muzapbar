from django.db import models



class Article(models.Model):
    CHOICES = (
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    )

    title = models.CharField(verbose_name='название', max_length=200, null=False, blank=False)
    mail = models.EmailField(verbose_name='почта', max_length=200, null=False,blank=False)
    text = models.TextField(verbose_name='описание', max_length=3000, null=False, blank=False)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='дата создание')
    updated = models.DateTimeField(auto_now=True,verbose_name='Дата изменения')
    status = models.CharField(max_length=10, choices=CHOICES, default='active')

    def __str__(self):
        return f'{self.title} - {self.text} - {self.mail} - {self.status}'
