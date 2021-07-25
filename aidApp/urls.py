from django.urls import path
from .views import CommentView, support_view, support_success_view


urlpatterns = [
    path('comment/', CommentView.as_view(), name = "comment"),
    path('support/', support_view, name = "support-view"),
    path('support-success/', support_success_view, name = "support-success"),
    
]

