from rest_framework import viewsets, generics, permissions
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_profile(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
