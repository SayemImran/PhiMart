from rest_framework.response import Response
from product.models import Product, Category, ProductImage, Review
from product.serializers import ProductSerializer, CategorySerializer,ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
from rest_framework.permissions import DjangoModelPermissions
from product.permissions import IsReviewAuthorOrReadonly
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import IsAdminUser, IsAuthenticated,AllowAny

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter ]
    filterset_class = ProductFilter
    search_fields = ['name','description']
    ordering_fields = ['price','updated_at']
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve all products")
    def list(self, request, *args, **kwargs):
        """Retrieve all the products"""
        return super().list(request, *args, **kwargs)
    @swagger_auto_schema(operation_summary="Create product (Admin only)")
    def create(self, request, *args, **kwargs):
        """Only authenticated users can add update and delete products"""
        return super().create(request, *args, **kwargs)
class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly] 
    def get_queryset(self):
        return ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_pk')
        serializer.save(product_id=product_id)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count = Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)    

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))
    
    def get_serializer_context(self):
        return {'product_id':self.kwargs.get('product_pk')}