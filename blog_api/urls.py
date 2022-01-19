from django.urls import path
from .views import PostList
from rest_framework.routers import DefaultRouter
# from .views import PostList,PostDetail
app_name='blog_api'

router = DefaultRouter()
router.register("",PostList,basename='user')
urlpatterns =  router.urls

# urlpatterns = [
#     # path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
#     path('',PostList.as_view(),name='listcreate'),
# ]

