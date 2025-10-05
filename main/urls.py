from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, create_product, show_product, register, login_user, logout_user, edit_product, delete_product, create_product_ajax, update_product_ajax, delete_product_ajax, login_user_ajax, register_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('create_product/', create_product, name='create_product'),
    path('product/<str:product_id>/', show_product, name='show_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<str:product_id>/edit/', edit_product, name='edit_product'),
    path('product/<str:product_id>/delete/', delete_product, name='delete_product'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('edit-product-ajax/<str:product_id>/', update_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<str:product_id>/', delete_product_ajax, name='delete_product_ajax'),
    path('login-ajax/', login_user_ajax, name='login_user_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
]