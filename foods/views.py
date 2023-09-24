from rest_framework.viewsets import ModelViewSet

from foods.models import Food
from foods.serializers import FoodSerializer
from utils.permissions import IsManager


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = (IsManager, )
