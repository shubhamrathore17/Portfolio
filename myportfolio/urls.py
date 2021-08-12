from django.urls import path
from .views import *
# from . import views

urlpatterns =[
    # Portfolio
    path("",TestTemplateView.as_view(), name="bearhug_folio"),
    path("send_message/",SendMessageView.as_view(), name="send_message"),

]