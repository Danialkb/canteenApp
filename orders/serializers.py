from rest_framework import serializers

from foods.models import Food
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    food = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = "__all__"
