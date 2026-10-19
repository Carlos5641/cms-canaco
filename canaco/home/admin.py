from django.contrib import admin
from .models import Categoria, Archivo, Perfil, Publicacion, GaleriaPublicacion, Comentario

admin.site.register(Categoria)
admin.site.register(Archivo)
admin.site.register(Perfil)
admin.site.register(Publicacion)
admin.site.register(GaleriaPublicacion)
admin.site.register(Comentario)