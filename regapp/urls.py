from django.urls import path
from regapp import views
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path("register/",views.RegistrationView.as_view(),name="signup"),
    path('login/',views.LoginView.as_view(), name='token'),

] 
