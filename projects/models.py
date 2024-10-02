from django.db import models
from .validators import (
    validate_profile_fields,
    validate_project_fields,
    validate_certifying_institution,
    validate_certificate_fields,
)


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField()

    def clean(self):
        validate_profile_fields(self)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    github = models.URLField()
    keyword = models.CharField(max_length=50)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="projects"
    )

    def clean(self):
        validate_project_fields(self)

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def clean(self):
        validate_certifying_institution(self)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution, on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name="certificates")

    def clean(self):
        validate_certificate_fields(self)

    def __str__(self):
        return self.name
