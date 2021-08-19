# from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns =[
    # Portfolio
    path("",TestTemplateView.as_view(), name="bearhug_folio"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("profile/update/<int:pk>/",login_required(ProfileUpdateView.as_view()), name="profile_update"),
    path("send_message/",SendMessageView.as_view(), name="send_message"),

]


