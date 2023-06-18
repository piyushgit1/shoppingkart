from django.urls import path

from .views import register, login, logout, activate, dashboard, forgotPassword, resetpassword_validate, resetPassword

urlpatterns = [
    path('register/', register , name= 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
    path('activate/<uidb64>/<token>', activate, name = 'activate'),
    path('dashboard/', dashboard, name= 'dashboard'),
    path('forgotPassword/', forgotPassword, name= "forgotPassword"),
    path('restpassword_validate/<uidb64>/<token>/', resetpassword_validate, name= "resetpassword_validate"),
    path('restPassword/',resetPassword, name= 'resetPassword')

]