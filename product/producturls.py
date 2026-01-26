from django.urls import path
from product import views
urlpatterns = [
    path('',views.ViewProduct.as_view(),name='product-lists'),
    path('<int:id>/', views.ViewSpeciificProduct.as_view(),name='product-list'),
]
