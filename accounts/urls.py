from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.addProduct, name = 'add_product'),
    path('edit/<int:id>', views.editEntry, name = 'edit_product'),
    path('delete/<int:id>', views.deleteEntry, name = 'delete_entry')
] 

print(staticfiles_urlpatterns())
urlpatterns += staticfiles_urlpatterns()