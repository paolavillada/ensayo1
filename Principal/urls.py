from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    #proceso de login y registro y envio de recuperar contraseña para cliente
    url(r'Registro/Cliente', include('usuario.urls')),
    url(r'Inicio_Sesion/Cliente', LoginView.as_view(template_name='Inicio_Sesion.html'),name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="olvidoContrase.html"),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html") ,name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),

    path('', include('inicio.urls')),
    path('Cuenta/', include('cliente.urls')),
    path('Cuenta/Root', include('root.urls')),
    path('Cuenta/', include('Cu_Admin.urls')),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
