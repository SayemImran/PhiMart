from django.core.exceptions import ValidationError
def validate_file_size(file):
    max_size  = 10
    max_in_size_bytes = max_size * 1024 * 1024

    if file.size > max_in_size_bytes:
        raise ValidationError(f"File size should not exceed {max_size} MB.")