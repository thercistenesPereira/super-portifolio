from django.core.exceptions import ValidationError


def validate_field_length(field_value, field_name, max_length=500):
    if not field_value or len(field_value) > max_length:
        raise ValidationError(
            f"O campo {field_name} não pode estar vazio ou ter mais de"
            f"{max_length} caracteres."
        )


def validate_profile_fields(profile):
    validate_field_length(profile.name, "name", 100)
    validate_field_length(profile.github, "github")
    validate_field_length(profile.linkedin, "linkedin")
    validate_field_length(profile.bio, "bio")


def validate_project_fields(project):
    validate_field_length(project.name, "name", 50)
    validate_field_length(project.description, "description", 500)
    validate_field_length(project.github, "github_url")
    validate_field_length(project.keyword, "keyword", 50)
    validate_field_length(project.key_skill, "key_skill", 50)


def validate_certifying_institution(institution):
    validate_field_length(institution.name, "name", 100)
    validate_field_length(institution.url, "url")


def validate_certificate_fields(certificate):
    validate_field_length(certificate.name, "name", 100)
    if not certificate.certifying_institution:
        raise ValidationError("Certifying_institution não pode estar vazio.")
    if not certificate.timestamp:
        raise ValidationError("O campo timestamp não pode estar vazio.")
    if not certificate.profiles.exists():
        raise ValidationError("O campo profiles não pode estar vazio.")
