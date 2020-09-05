import random
from dependency_injector import providers, containers
from unittest import mock

# import services and classes from other python files
from services import PaymentService, AbstractPayServiceProvider, GoolePayServiceProvider, ApplePayServiceProvider, \
    AliPayServiceProvider
from containers import Container

container = Container()
container.payment_service_factory.override(mock.Mock())

# service = container.service_factory()
# assert isinstance(service.payment_service_provider, mock.Mock)
#
# print(service.service_provider_name())
# print(service.payment_service_provider)

