from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('', include('food_categories.urls')),
    path('', include('foods.urls')),
]
