from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.choices import StatusChoices
from orders.models import Order
from orders.serializers import OrderSerializer, OrderGetSerializer
from utils.permissions import IsCustomer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsCustomer, )

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'my_orders':
            return OrderGetSerializer
        return OrderSerializer

    @action(detail=False, methods=["GET"])
    def my_orders(self, request, *args, **kwargs):
        orders = self.queryset.filter(customer=request.user, status=StatusChoices.Waiting)
        serializer = self.get_serializer(orders, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
