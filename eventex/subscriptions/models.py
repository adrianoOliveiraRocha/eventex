from django.db import models
from eventex.subscriptions.validators import validate_cpf
from django.shortcuts import resolve_url as r


class Subscription(models.Model):
    name = models.CharField(max_length=100, verbose_name='nome')
    cpf = models.CharField(max_length=11, verbose_name='CPF',
                           validators=[validate_cpf])
    email = models.EmailField(verbose_name='e-mail', blank=True)
    phone = models.CharField(max_length=20, verbose_name='telefone',
                             blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='criado em')
    paid = models.BooleanField(default=False, verbose_name='pago')

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('subscriptions:detail', self.pk)
