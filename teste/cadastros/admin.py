from django.contrib import admin


# importando classes
from cadastros.models import Produto, Cliente
from cadastros.models import Compra

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Produto)


