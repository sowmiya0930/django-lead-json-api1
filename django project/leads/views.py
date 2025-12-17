from rest_framework import viewsets
from .models import Lead
from .serializers import LeadSerializer
from rest_framework.permissions import AllowAny

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [AllowAny]  # Anyone can access API



