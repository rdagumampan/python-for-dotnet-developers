class PaymentService:
    def __init__(self, payment_service_provider):
        self.payment_service_provider = payment_service_provider

    def __repr__(self):
        return "Payment via {0}".format(self.payment_service_provider.name)

    def service_provider_name(self):
        return self.payment_service_provider.name


class AbstractPayServiceProvider:
    ...


class GoolePayServiceProvider(AbstractPayServiceProvider):
    name = "GooglePay"

    def __repr__(self):
        return "Pay with GooglePay"


class ApplePayServiceProvider(AbstractPayServiceProvider):
    name = "ApplePay"

    def __repr__(self):
        return "Pay with ApplePay"


class AliPayServiceProvider(AbstractPayServiceProvider):
    name = "AliPay"

    def __repr__(self):
        return "Pay with AliPay"
