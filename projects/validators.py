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
