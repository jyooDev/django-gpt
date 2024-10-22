from django.urls import path
from .views import MessageListView

urlpatterns = [
    path('<conversation_id>/', MessageListView.as_view(), name="message_list")
   ]