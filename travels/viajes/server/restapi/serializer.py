from rest_framework import serializers 
from .models import Terminal, Usuario, Boleto, Asiento, Bus, Trayecto


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','url', 'nombre', 'apellido', 'identidad']

class BoletoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Boleto
        fields = ['id','url', 'usuario', 'fecha_de_compra', 'usuario']

class AsientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asiento
        fields = ['id','url', 'numero', 'boleto']

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ['id','url', 'patente','chofer','capacidad_maxima']

class TerminalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Terminal
        fields = ['id','url', 'direccion','comuna','ciudad', 'pais']


class TrayectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trayecto
        fields = ['id','url', 'fecha','origen','destino', 'bus', 'precio']

