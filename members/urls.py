from django.urls import path, include
from . import views


urlpatterns = [
  
  #  path('', views.home ),
   path('addcart', views.addcart ),
   path('billing', views.billing ),
   path('index', views.index ),
   path('placeorder', views.placeorder ),
  #  path('productdetail', views.details ),
   path('step', views.step ),
   path('<str>/<name>/', views.print_name) ,
  # path('', views.print_name) ,
  path('aboutme', views.my_self  ),
  path('login',views.login_page),
  path('action_page',views.submit),
  path('logout', views.logout_view),
  path('contact',views.contact),
]
