from dependency_injector import providers, containers
from main import PaymentService, AbstractPayServiceProvider, GoolePayServiceProvider, ApplePayServiceProvider, \
    AliPayServiceProvider


class Container(containers.DeclarativeContainer):
    payment_service_factory = providers.AbstractFactory(AbstractPayServiceProvider)
    service_factory = providers.Factory(PaymentService, payment_service_provider=payment_service_factory)
