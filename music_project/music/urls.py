from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,name='index'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>',views.delete),

    path('home/',views.home,name="home"),
    path('login/',views.Login,name="login"),
    path('sign/',views.Signup,name='sign'),
    path('logoutpage/',views.logoutpage,name="logoutpage"),

]
