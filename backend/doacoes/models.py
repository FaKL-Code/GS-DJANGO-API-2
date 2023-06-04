from django.db import models
from django.urls import reverse_lazy

VOLUME = ((
    ('PEQUENO', 'Pequeno'),
    ('MEDIO', 'Médio'),
    ('GRANDE', 'Grande'),
))


class Doacao(models.Model):
    doador = models.CharField(max_length=50)
    volume = models.CharField(
        max_length=20, choices=VOLUME, null=False, blank=False)
    is_done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doador}"

    class Meta:
        verbose_name = "Doacao"
        verbose_name_plural = "Doacoes"

    def get_absolute_url(self):
        return reverse_lazy('doacoes:doacoes_detail', kwargs={'pk': self.pk})
