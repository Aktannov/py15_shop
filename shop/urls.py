from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from order.views import CreateOrderView, UserOrdersList, UpdateOrderStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('product.urls')),
    path('api/v1/orders/', CreateOrderView.as_view()),
    path('api/v1/orders/own/', UserOrdersList.as_view()),
    path('api/v1/orders/<int:pk>', UpdateOrderStatusView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)