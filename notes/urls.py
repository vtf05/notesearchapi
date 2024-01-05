from .views import NoteViewSet, SearchNotesView
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('notes/<int:pk>/share/', NoteViewSet.as_view({'post': 'share'})),  # Correct URL pattern
    path('search/', SearchNotesView.as_view(), name='search_notes'),


]
