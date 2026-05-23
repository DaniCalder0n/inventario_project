from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [IsAuthenticated]
