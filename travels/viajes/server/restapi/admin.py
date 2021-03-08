from django.contrib import admin
from .models import Usuario
from .models import Boleto
from .models import Asiento
from .models import Bus
from .models import Terminal
from .models import Trayecto 

admin.site.register(Usuario)
admin.site.register(Boleto)
admin.site.register(Asiento)
admin.site.register(Bus)
admin.site.register(Terminal)
admin.site.register(Trayecto)