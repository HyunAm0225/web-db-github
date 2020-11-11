from django.urls import path
from . import views

app_name = 'namecard'

urlpatterns = [
    path('', views.NamecardLV.as_view(), name='index'),
    path('<int:pk>/', views.NamecardDV.as_view(), name='detail'),
    path('search/', views.SearchFormView.as_view(), name='search'),

    # namecard CRUD구현
    path('add/', views.NamecardCreateView.as_view(), name='add'),
    path('change/', views.NamecardChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.NamecardUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.NamecardDeleteView.as_view(), name='delete'),
]
