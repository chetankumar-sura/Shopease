from django.urls import path
from .views import home, category1, category2, category3, contact
# from . import views
urlpatterns = [
    path('', home, name='home'),
    path('electronics/', category1, name='category1'),
    path('fashion/', category2, name='category2'),
    path('groceries/', category3, name='category3'),
    path('contact/',  contact, name='contact'),
]

