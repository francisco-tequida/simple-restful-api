from django.contrib.auth.models import User


def get_admin_emails() -> list:
    """function to get administrators' email

    Returns:
        typing[list]: list of strings containing all administrators' email
    """

    return User.objects.filter(is_staff=True).values_list('email', flat=True)
