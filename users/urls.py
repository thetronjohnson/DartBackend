from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewset,basename='products')
# router.register(r'customer/login', views.CustomerLogin,basename='customer-login')
# router.register(r'shopkeeper/login', views.ShopKeeperLogin,basename='shopkeeper-login')
# router.register(r'rider/login', views.RiderLogin,basename='rider-login')
# router.register(r'customer/signup', views.CustomerRegistration,basename='customer-signup')
# router.register(r'shopkeeper/signup', views.ShopKeeperRegistration,basename='shopkeeper-signup')
# router.register(r'rider/signup', views.RiderRegistration,basename='rider-signup')

urlpatterns = router.urls

urlpatterns += [
    url('customer/signup', views.CustomerRegistration.as_view()),
    url('customer/login', views.CustomerRegistration.as_view()),
    url('rider/signup', views.RiderRegistration.as_view()),
    url('rider/login', views.RiderRegistration.as_view()),
    url('shopkeeper/signup', views.ShopKeeperRegistration.as_view()),
    url('shopkeeper/login', views.ShopKeeperRegistration.as_view()),
]
