from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from quests.models import Quest
from quests.serializers import QuestSerializer


class QuestsViewSet(viewsets.ModelViewSet):
    serializer_class = QuestSerializer
    queryset = Quest.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = QuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
