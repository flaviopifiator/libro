from django.contrib import admin

from . import models


admin.site.register(models.Autor)
admin.site.register(models.Capitulo)
admin.site.register(models.Categoria)
admin.site.register(models.Editorial)
admin.site.register(models.Libro)

