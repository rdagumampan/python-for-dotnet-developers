import random
from dependency_injector import providers, containers

# import services and classes from other python files
from services import PaymentService, AbstractPayServiceProvider, GoolePayServiceProvider, ApplePayServiceProvider, \
    AliPayServiceProvider
from containers import Container

if __name__ == 'main':
    container = Container()

    # emulate random choice of payment service provider
    # this could be coming from configuration file
    payment_service_provider = random.choice(['googlepay', 'applepay', 'alipay'])
    if payment_service_provider == 'googlepay':
        container.payment_service_factory.override(
            providers.Factory(GoolePayServiceProvider)
        )
    elif payment_service_provider == 'applepay':
        container.payment_service_factory.override(
            providers.Factory(ApplePayServiceProvider)
        )
    elif payment_service_provider == 'alipay':
        container.payment_service_factory.override(
            providers.Factory(AliPayServiceProvider)
        )

    service = container.service_factory()
    print(service.service_provider_name())
    print(service.payment_service_provider)

# reference
# https://pypi.org/project/dependency-injector/
# https://levelup.gitconnected.com/python-dependency-injection-with-flask-injector-50773d451a32
# https://medium.com/@shivama205/dependency-injection-python-cb2b5f336dce
