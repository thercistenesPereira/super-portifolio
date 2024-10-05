from rest_framework import routers
from django.urls import path, include
from .views import (
    ProfileViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet,
    ProjectListCreateView,
    ProjectDetailView,
)


router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
# router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "projects/",
        ProjectListCreateView.as_view(),
        name="project-list-create",
    ),
    path(
        "projects/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail",
    ),
]
