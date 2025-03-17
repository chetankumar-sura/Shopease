from django.urls import path
from .views import home, signup_view, login_view, logout_view, profile_view, category_products
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('category/<str:category>/', views.category_products, name='category_products'),

]




