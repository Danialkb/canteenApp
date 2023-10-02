from rest_framework import serializers

from foods.models import Food
from foods.serializers import FoodSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("status", )


class OrderGetSerializer(serializers.ModelSerializer):
    food = FoodSerializer()
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("status",)
