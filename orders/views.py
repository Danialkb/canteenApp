from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.choices import StatusChoices
from orders.models import Order
from orders.serializers import OrderSerializer, OrderGetSerializer, OrderUpdateSerializer
from utils.permissions import IsCustomer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsCustomer,)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'my_orders':
            return OrderGetSerializer
        if self.action == 'update':
            return OrderUpdateSerializer
        return OrderSerializer

    @action(detail=False, methods=["GET"])
    def my_orders(self, request, *args, **kwargs):
        orders = self.queryset.filter(customer=request.user, status=StatusChoices.Waiting)
        serializer = self.get_serializer(orders, many=True)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance, is_new = Order.objects.get_or_create(food_id=serializer.data["food"], customer_id=request.user.id)
        if not is_new:
            instance.amount += 1
            instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=["GET"])
    def send_user_orders(self, request, *args, **kwargs):
        orders = Order.objects.filter(status="Waiting", customer_id=request.user.id)

        for order in orders:
            order.status = "Processing"

        Order.objects.bulk_update(orders,  fields=["status"])

        return Response({"detail": "ok"}, status=status.HTTP_200_OK)
