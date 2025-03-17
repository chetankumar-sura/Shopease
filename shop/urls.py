from django.urls import path
from .views import home, category1, category2, category3
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('electronics/', category1, name='category1'),
    path('fashion/', category2, name='category2'),
    path('accessories/', category3, name='category3'),
     path('category/<str:category>/', views.category_products, name='category_products'),

]




