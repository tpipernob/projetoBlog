from django.contrib import admin
from .models import *

admin.AdminSite.site_header = "Administração do Nosso Blog"
admin.AdminSite.site_title = "Nosso Blog"

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')
    list_filter = ('titulo',)
    search_fields = ('titulo', 'descricao', 'conteudo',)
    list_editable = ('descricao',)

admin.site.register(Postagem, PostagemAdmin)

