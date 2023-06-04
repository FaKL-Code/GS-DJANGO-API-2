from django.contrib import admin

from backend.doacoes.models import Doacao


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_done')
    search_fields = ('doador',)
    list_filter = ('is_done',)
    date_hierarchy = 'created'
