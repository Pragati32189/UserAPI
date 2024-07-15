from django.urls import path
from . import views

# urlpatterns =[
#     path('users/<int:pk>', UserDetail.as_view(), name='user-detail')
# ]

urlpatterns = [
    path('all_users/', views.all_user, name='all_user'),
    path('one_user/<int:id>/', views.one_user, name='user-detail'),
    path('create_user/', views.user_create, name='user_create'),
    path('update_user/<int:id>/', views.user_update, name='user-update'),
    path('delete_user/<int:id>/', views.user_delete, name='user-delete')
]