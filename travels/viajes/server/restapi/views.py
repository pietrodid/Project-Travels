from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Asiento, Boleto, Bus, Terminal, Usuario, Trayecto
from .serializer import TerminalSerializer, UsuarioSerializer, BoletoSerializer, AsientoSerializer, BusSerializer, TrayectoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class BoletoViewSet(viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer

class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

class TerminalViewSet(viewsets.ModelViewSet):
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer

class TrayectoViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer

class TrayectoList(generics.ListAPIView):
    serializer_class = TrayectoSerializer

    def get_queryset(self):
        fecha = self.kwargs['fecha']
        return Trayecto.objects.filter(Trayecto=fecha)
    
    def get_queryset(self):
        origen = self.kwargs['origen']
        return Trayecto.objects.filter(Trayecto=origen)    
        
    def get_queryset(self):
        destino = self.kwargs['destino']
        return Trayecto.objects.filter(Trayecto=destino)     

    def get_queryset(self):
        bus = self.kwargs['bus']
        return Trayecto.objects.filter(Trayecto=bus)

    def get_queryset(self):
        precio = self.kwargs['precio']
        return Trayecto.objects.filter(Trayecto=precio)      