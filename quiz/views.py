from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Quiz, Participant
from .serializers import QuizSerializer, ParticipantSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        quiz = self.get_object()
        participants = Participant.objects.filter(quiz=quiz)
        participant_serializer = ParticipantSerializer(participants, many=True)
        return Response(participant_serializer.data)


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    @action(detail=True, methods=['post'])
    def accept_invitation(self, request, pk=None):
        participant = self.get_object()
        participant.invitation_accepted = True
        participant.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def submit_quiz(self, request, pk=None):
        participant = self.get_object()
        # Hier kannst du die Logik zum Berechnen des Scores hinzufügen
        participant.completed = True
        participant.save()
        return Response(status=status.HTTP_200_OK)
