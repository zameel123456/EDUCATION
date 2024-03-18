from django.urls import path
from.import views
app_name='dashboard'

urlpatterns=[
    path('',views.home,name="home"),
    path('course',views.course,name="course"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('newhomepage',views.newhomepage,name="newhomepage"),
    path('logout/',views.logout,name='logout'),
  
]