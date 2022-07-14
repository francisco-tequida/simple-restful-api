from django.conf import settings
from typing import Dict
from django.core.mail import EmailMessage
from brands.models import Brand
from utils.users_utils import get_admin_emails


def format_previous_product_info(prev_data: Dict) -> Dict:
    """creates a dictionary using previous info from a product. This dict is used
    to provide variables to sendgrid email template.

    Args:
        curr_data (Dict): previous info of a product

    Returns:
        Dict: dict used by sendgrid
    """
    data = {
        "prev_sku": prev_data.get("sku"),
        "prev_name": prev_data.get("name"),
        "prev_price": str(prev_data.get("price")),
        "prev_brand": ""
    }
    if prev_data.get("brand"):
        data["prev_brand"] = Brand.objects.get(id=prev_data.get("brand")).name
    return data


def format_current_product_info(curr_data: Dict) -> Dict:
    """creates a dictionary using current info from a product. This dict is used
    to provide variables to sendgrid email template.

    Args:
        curr_data (Dict): current info of a product

    Returns:
        Dict: dict used by sendgrid
    """
    data = {
        "curr_sku": curr_data.get("sku"),
        "curr_name": curr_data.get("name"),
        "curr_price": str(curr_data.get("price")),
        "curr_brand": ""
    }
    if curr_data.get("brand"):
        data["curr_brand"] = Brand.objects.get(id=curr_data.get("brand")).name
    return data


def send_product_information_updated_email(prev_data: Dict, curr_data: Dict) -> None:
    """Function to send an email notifying all the administrators about the
    update of a product information.

    Args:
        prev_data (Dict): previous info of the product
        curr_data (Dict): current info of the product
    """
    admin_emails = get_admin_emails()

    msg = EmailMessage(
        from_email=settings.FROM_EMAIL,
        to=admin_emails
    )
    msg.template_id = settings.TEMPLATE_ID

    msg.dynamic_template_data = {
        **format_previous_product_info(prev_data),
        **format_current_product_info(curr_data)
    }

    msg.send(fail_silently=False)
