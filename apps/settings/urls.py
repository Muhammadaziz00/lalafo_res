from django.urls import path

from apps.settings.views import PostAPIView,PostCreateAPIView,PostUpdateAPIView,PostDestroyAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name="api_settings"),
    path('posts/create/', PostCreateAPIView.as_view(), name="api_settings_create"),
    path('posts/update/<int:pk>/', PostUpdateAPIView.as_view(), name="api_settings_update"),
    path('posts/destroy/<int:pk>/', PostDestroyAPIView.as_view(), name="api_settings_destroy"),

]