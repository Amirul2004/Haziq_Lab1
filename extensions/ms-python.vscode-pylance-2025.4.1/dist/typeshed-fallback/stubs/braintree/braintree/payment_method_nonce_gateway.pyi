from _typeshed import Incomplete

class PaymentMethodNonceGateway:
    gateway: Incomplete
    config: Incomplete
    def __init__(self, gateway) -> None: ...
    def create(self, payment_method_token, params=...): ...
    def find(self, payment_method_nonce): ...
