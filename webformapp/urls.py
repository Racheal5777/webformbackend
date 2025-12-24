from django.urls import path
from . import views
urlpatterns = [
    path('submit/', views.UserDetailView.as_view(), name='submit'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('view/', views.UserDetailListView.as_view(), name='view_data'),
]