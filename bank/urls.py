from django.urls import path
from . import views

urlpatterns = [
    path("",views.homePage,name="HomePage"),
    path("aboutUs/",views.aboutUs,name="aboutUs"),
    path("contactUs/",views.contactUs,name="contactUs"),
    path("makeTransaction/<id>/",views.makeTransaction,name="makeTransaction"),
    path("transactionHistory/",views.transactionHistory,name="transactionHistory"),
    path("createUser/",views.createUser,name="createUser"),
    path("viewUsers/",views.viewUsers,name="viewUsers"),
]