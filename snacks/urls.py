from django.contrib import admin
from django.urls import path
from .views import HomePageView,AboutPageView,SnacksPageView,SnackDetailPageView,CreateSnackView,DeleteSnackView,UpdateSnackView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='home'),
    path('about/', AboutPageView.as_view(),name='about'),
    path('snacks/',SnacksPageView.as_view(),name='snacks'),
    path('<int:pk>/',SnackDetailPageView.as_view(),name="snack_detail"),
    path('create/',CreateSnackView.as_view(),name="snack_create"),
    path('update/<int:pk>',UpdateSnackView.as_view(),name="snack_update"),
    path('delete/<int:pk>',DeleteSnackView.as_view(),name="snack_delete")
]