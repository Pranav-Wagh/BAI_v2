from django.urls import path
from BAI_app_v2 import views

app_name = 'BAI_app_v2'

urlpatterns = [
    path('signup/',views.signup,name = 'signup'),
    path('user_login/',views.user_login,name="user_login"),
    path('form1/',views.form1,name="form1"),
    path('form2/',views.form2,name="form2"),
]