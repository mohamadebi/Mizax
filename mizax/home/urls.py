from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = "home"),
    path('detail/<int:place_id>/',views.detail, name = "detail"),
<<<<<<< HEAD
    path('delete/<int:place_id>/',views.delete),
=======
    path('delete/<int:place_id>/', views.delete, name="delete"),
    path('update/<int:place_id>/', views.update, name="update"),
    path('create/',views.create , name = 'create'),
>>>>>>> 1be7fbe ( update_delete)
]