from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, ParticipantViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'participants', ParticipantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
