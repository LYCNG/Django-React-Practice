from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# lead Viewset
class LeadViewSet(viewssets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer