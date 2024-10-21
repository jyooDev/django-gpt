from django.urls import path
from .views import UserConversationListView, UserConversationDetailView

urlpatterns = [
    path('<username>/', UserConversationListView.as_view(), name="user_converstion_list"),
    path('<username>/<title_slug>/', UserConversationDetailView.as_view(), name='conversation_detail'),
   ]