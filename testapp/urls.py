from django.urls import path
from .views import delete_comment

urlpatterns = [
    path('delete/<int:sms_id>/', delete_comment, name='delete_comment'),
]