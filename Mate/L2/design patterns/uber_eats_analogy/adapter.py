
"""
Adapter Pattern Example: Unifying different delivery partner APIs
------------------------------------------------------------------
We want a common interface `DeliveryClient` with a method `quote(order)` and `dispatch(order)`.
Two third-party SDKs exist with incompatible interfaces:
- FastShipSDK  (methods: get_price(cart), send(package))
- EcoCourierSDK(methods: estimate(order_dict), deliver(order_dict))

Adapters wrap these SDKs and present a uniform interface so the rest of the app
is decoupled from each vendor’s API quirks.

Usage:
    from adapter import DeliveryClient, FastShipAdapter, EcoCourierAdapter

    order = {"items": 3, "weight": 1.2, "destination": "Sydney"}

    clients: list[DeliveryClient] = [
        FastShipAdapter(),
        EcoCourierAdapter(),
    ]
    for c in clients:
        print(c.quote(order))
        print(c.dispatch(order))
"""
from __future__ import annotations
from typing import Protocol, Dict, Any

Order = Dict[str, Any]

class DeliveryClient(Protocol):
    def quote(self, order: Order) -> float: ...
    def dispatch(self, order: Order) -> str: ...

# --- Third-party SDKs we cannot change -------------------------------------
class FastShipSDK:
    def get_price(self, cart: Order) -> float:
        base = 5.0
        return base + 2.0 * cart.get("weight", 0)

    def send(self, package: Order) -> str:
        return f"FastShip tracking #{hash(frozenset(package.items())) & 0xffff}"

class EcoCourierSDK:
    def estimate(self, order_dict: Order) -> float:
        base = 4.0
        return base + 1.5 * order_dict.get("weight", 0)

    def deliver(self, order_dict: Order) -> str:
        return f"EcoCourier ref {abs(hash(str(order_dict))) % 100000}"

# --- Adapters ---------------------------------------------------------------
class FastShipAdapter:
    def __init__(self):
        self._sdk = FastShipSDK()

    def quote(self, order: Order) -> float:
        return self._sdk.get_price(order)

    def dispatch(self, order: Order) -> str:
        return self._sdk.send(order)

class EcoCourierAdapter:
    def __init__(self):
        self._sdk = EcoCourierSDK()

    def quote(self, order: Order) -> float:
        return self._sdk.estimate(order)

    def dispatch(self, order: Order) -> str:
        return self._sdk.deliver(order)

if __name__ == "__main__":
    order = {"items": 3, "weight": 1.2, "destination": "Sydney"}
    clients: list[DeliveryClient] = [FastShipAdapter(), EcoCourierAdapter()]
    for client in clients:
        print("Quote:", client.quote(order))
        print("Dispatch:", client.dispatch(order))
