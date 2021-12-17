# settings(проверка) -> urls(перенапровление, привязка) ->

import rest_framework.pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from product.filters import ProductsFilter
from product.models import Product, Category, Comment
from product.permissions import IsAdmin, IsAuthor
from product.serializer import ProductSerializer, ProductsListSerializer, CategorySerializer, CommentSerializer


class ProductViewSet(ModelViewSet): #ModelViewSet - отвечает за update, delete и.т.д
    queryset = Product.objects.all() #получение всех данных
    serializer_class = ProductSerializer #преобразование данных JSON
    # permission_classes = [IsAdmin] #ограниичение доступа
    # pagination_class = rest_framework.pagination.PageNumberPagination
    paginate_by = 5
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductsFilter
    search_fields = ['name']
    order_fields = ['name', 'price']

    # def get_permissions(self):
    #     if self.action == 'comment':
    #         return []
    #     return [IsAdmin()]
    # api/v1/products/1/comment
    # @action(['POST'], detail=True)
    # def comment(self, request, pk):
    #     product = self.get_object()
    #     data = {'product': product.id}
    #     data.update(request.data)
    #     serializer = CommentSerializer(data=data)
    #     serializer.is_valid(raise_exeption=True)
    #     serializer.save()
    #     return Response('Комментарий успешно создан', status=201)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    # pagination_class = rest_framework.pagination.PageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filterset_class = ProductsFilter
    search_fields = ['name']
    ordering_fields = ['name', 'price']

    @action (['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object() 
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class CreateCommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class UpdateCommentView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

class DeleteCommentView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor | IsAdmin]

class CommentViewSet(CreateModelMixin,
                     UpdateModelMixin,
                     DestroyModelMixin,
                     GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]


# TODO: Авторизация
# TODO: Фильтрация продуктов
# TODO: Поиск по продуктам
# TODO: ПАгинация
# TODO: Заказы
# TODO: Тесты
# TODO: git
# TODO: документация



# class MainView(GenericView)
