from django.urls import path
from .views import landing, register, login_view, logout_view, premium_content_view, upgrade, qr_sunday_content, domingo_detail, domingo_list

urlpatterns = [
    path('qr/domingos/', domingo_list, name='domingo_list'),
    path('qr/adviento/1-esperanza/', qr_sunday_content, name='qr_adviento_esperanza'),
    path('qr/domingo/<slug:slug>/', domingo_detail, name='domingo_detail'),
    path('', landing, name='landing'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('premium/', premium_content_view, name='premium_content'),
    path('upgrade/', upgrade, name='upgrade'),
]
