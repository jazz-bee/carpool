from django.urls import path
from .views import UserList, UserDetail

app_name = 'users_api'

# endpoints
# 1 to show and individual post
# 2 to show all posts
urlpatterns = [
    path('<int:pk>/', UserDetail.as_view(), name='detailcreate'),
    path('', UserList.as_view(), name='listcreate'),
]
