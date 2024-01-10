from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.addProduct, name = 'add_product'),
    path('edit/<int:id>', views.editEntry, name = 'edit_product'),
    path('delete/<int:id>', views.deleteEntry, name = 'delete_entry')
] 