"""Fresh_Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from django.views.generic.base import RedirectView
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from .settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, IndexCategoryViewSet
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewSet, LeavingMessageViewSet, AddressViewSet
from trade.views import ShoppingCartViewSet, OrderViewSet, AliPayView

# Create a router and register our viewsets with it.

router = DefaultRouter()

# 配置goods的路由
router.register(r'goods', GoodsListViewSet, basename='goods')

# 配置categories的路由
router.register(r'categorys', CategoryViewSet, basename='categorys')

# 配置短信验证码路由
router.register(r'codes', SmsCodeViewSet, basename='codes')

# 配置注册路由
router.register(r'users', UserViewSet, basename='users')

# 配置收藏路由
router.register(r'userfavs', UserFavViewSet, basename='userfavs')

# 配置留言路由
router.register(r'messages', LeavingMessageViewSet, basename='messages')

# 配置收货地址路由
router.register(r'address', AddressViewSet, basename='address')

# 配置购物车路由
router.register(r'shopcarts', ShoppingCartViewSet, basename='shopcarts')

# 配置下订单路由
router.register(r'orders', OrderViewSet, basename='orders')

# 配置轮播图路由
router.register(r'banners', BannerViewSet, basename='banners')

# 配置首页商品系列路由
router.register(r'indexgoods', IndexCategoryViewSet, basename='indexgoods')

urlpatterns = [
       url(r'^xadmin/', xadmin.site.urls),
       url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
       # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

       # 商品列表页
       url(r'^', include(router.urls)),

       # 文档路由
       url(r'docs/', include_docs_urls(title='生鲜电商')),

       # DRF自带认证路由
       url(r'^api-token-auth/', views.obtain_auth_token, name='api_token_auth'),

       # JWT认证路由
       url(r'^login/', obtain_jwt_token),

       # 支付宝结果返回接口
       url(r'^alipay/return/', AliPayView.as_view(), name='alipay'),

       # 配置favicon路由
       url(r'^favicon\.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
]