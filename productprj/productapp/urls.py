from django.urls import path
from .import views

urlpatterns = [
   
    path('',views.index,name='index'),
    path('accounts/login/',views.Loginpage,name='login'),
    path('accounts/sign_up/',views.sign_up,name='signup'),
    path('reset',views.Resethome,name='reset'),
    
    path('passwordreset',views.resetPassword),
    path('logout',views.Logout_view),
    path('',views.index,name='index'),
    path('display',views.display),
    path('add',views.add),
    path('delt',views.delete),
    path('update',views.update)
]
