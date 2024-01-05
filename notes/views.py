from rest_framework import viewsets, generics, filters
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # Require authentication

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set author on creation
    
    @action(detail=False, methods=['GET'], name='Share Note')
    def share(self, request, pk):
        note = self.get_object()
        user_to_share_with = get_object_or_404(User, username=request.data.get('username'))
        note.shared_with.add(user_to_share_with)
        note.save()
        return Response({'message': 'Note shared successfully.'})
    


class SearchNotesView(generics.ListAPIView):
    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        user = self.request.user
        query = self.request.query_params.get('q', None)
        if query is None:
            return Note.objects.none()  # return an empty queryset if no query parameter

        authored_notes = Note.objects.filter(Q(author=user) & (Q(title__icontains=query) | Q(content__icontains=query)))
        shared_notes = Note.objects.filter(Q(shared_with=user) & (Q(title__icontains=query) | Q(content__icontains=query)))
        return authored_notes.union(shared_notes)