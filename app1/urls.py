from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('all_users_details/', views.AllUsersDetails.as_view(), name='all_users_details'),
    path('update_user/<int:pk>/', views.UpdateUserDetail.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', views.DeleteUser.as_view(), name='delete_user'),
]
