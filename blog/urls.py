from django.urls import path
from .views import BloglistView

app_name="Geriatrico"

urlpatterns = [
    path('', BloglistView.as_view(), name="home")
]
