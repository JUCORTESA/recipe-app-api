"""
URL mappings for the user API
"""
from django.urls import path
from user import views

# will be used for the reverse function in test as the name in url_patterns
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
