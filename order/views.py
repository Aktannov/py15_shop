
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from order.serializer import OrderSerializer


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class UserOrdersList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # orders = Order.objects.filter(user=user) или
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class UpdateOrderStatusView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return Response('Неврный статус', status=400)
        order = Order.objects.get(pk=pk)
        order.status = status
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


# TODO: Обновление заказа
# TODO: список заказов пользователя