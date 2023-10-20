from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.HomeView.as_view(), name="home"),
        #EN SUCESION, ESTOS SON PERFILES Y TIENDA/LISTA DE PRODUCTOS
    path('profiles/', views.ProfileView.as_view(), name="profiles"),
    path('categories/', views.CategoryView.as_view(), name="categories"),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name="category"),
        #SECCION DE CATEGORIAS, adicion, edicion y eliminacion
    path('add-categories/', views.CategoryCreatePage, name="add-categories"),
    path('edit-categories/<int:pk>', views.CategoryEditView.as_view(), name="edit-categories"),
    path('delete-categories/<int:pk>', views.CategoryDeleteView.as_view(), name="delete-categories"),
        #SECCION DE PRODUCTOS - añadir, edicion, eliminacion de producto
    path('add-products/', views.ProductCreatePage, name="add-products"),
    path('edit-products/<int:pk>', views.ProductEditView.as_view(), name="edit-products"),
    path('delete-products/<int:pk>', views.ProductDeleteView.as_view(), name="delete-products"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),
        #SECCION DE Reviews - añadir, edicion, eliminacion de review
    path('add-reviews/<int:pk>', views.ReviewCreatePage, name="add-reviews"),
    path('edit-reviews/<int:pk>', views.ReviewEditView.as_view(), name="edit-reviews"),
    path('delete-reviews/<int:pk>', views.ReviewDeleteView.as_view(), name="delete-reviews"),
    # path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name="product-detail"),		
]
