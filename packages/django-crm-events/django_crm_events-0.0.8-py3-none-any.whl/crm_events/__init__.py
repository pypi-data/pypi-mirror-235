from .clickup import Clickup
from .klaviyo import Klaviyo

services = [Clickup, Klaviyo]


def get_available_services():
    return [service for service in services if service().is_available()]


def on_install(shop_data):
    for service in get_available_services():
        service().on_install(shop_data)


def on_login(shop_data, user_data):
    for service in get_available_services():
        service().on_login(shop_data, user_data)


def on_billing_plan_change(shop_data, monthly_price):
    for service in get_available_services():
        service().on_billing_plan_change(shop_data, monthly_price)


def on_uninstall(shop_data, users_data):
    for service in get_available_services():
        service().on_uninstall(shop_data, users_data)
