from django.contrib import admin
from .models import Noticia
from .models import Pessoa
from .models import Tag
from .models import Comentario
from .models import Categoria
from .models import Foto

@admin.register(Noticia)
@admin.register(Pessoa)
@admin.register(Tag)
@admin.register(Comentario)
@admin.register(Categoria)
@admin.register(Foto)

class PessoaAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class NoticiaAdmin(admin.ModelAdmin):
    pass


# Register your models here.
