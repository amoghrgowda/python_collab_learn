
"""
Decorator Pattern Example: Adding cross-cutting concerns to payment processing
-----------------------------------------------------------------------------
We have a `PaymentProcessor` component with a single method `pay(order)`.
Decorators can add behavior (logging, retry, currency conversion) without modifying
the original class, and they can be stacked at runtime.

Usage:
    from decorator import BaseProcessor, LoggingDecorator, RetryDecorator, CurrencyDecorator

    processor = BaseProcessor()
    wrapped = LoggingDecorator(RetryDecorator(CurrencyDecorator(processor, rate=1.5)))
    wrapped.pay({"total": 10.0, "currency": "USD"})
"""
from __future__ import annotations
from typing import Protocol, Dict, Any, Callable
import time

Order = Dict[str, Any]

class PaymentProcessor(Protocol):
    def pay(self, order: Order) -> None: ...

class BaseProcessor:
    def pay(self, order: Order) -> None:
        # Simulate a payment call
        print(f"Processed payment of {order['total']} {order.get('currency', 'AUD')}")

# --- Decorators -------------------------------------------------------------
class ProcessorDecorator:
    def __init__(self, wrappee: PaymentProcessor):
        self._wrappee = wrappee

    def pay(self, order: Order) -> None:
        self._wrappee.pay(order)

class LoggingDecorator(ProcessorDecorator):
    def pay(self, order: Order) -> None:
        print(f"[LOG] Starting payment: {order}")
        try:
            super().pay(order)
        finally:
            print("[LOG] Finished payment")

class RetryDecorator(ProcessorDecorator):
    def __init__(self, wrappee: PaymentProcessor, retries: int = 2, delay: float = 0.2,
                 should_fail: Callable[[Order], bool] | None = None):
        super().__init__(wrappee)
        self.retries = retries
        self.delay = delay
        self.should_fail = should_fail or (lambda o: False)

    def pay(self, order: Order) -> None:
        attempts = 0
        while True:
            try:
                attempts += 1
                if self.should_fail(order) and attempts <= self.retries:
                    raise RuntimeError("Transient gateway error")
                return super().pay(order)
            except RuntimeError as e:
                if attempts > self.retries:
                    print(f"[RETRY] Giving up after {attempts} attempts: {e}")
                    raise
                print(f"[RETRY] Attempt {attempts} failed: {e}. Retrying in {self.delay}s...")
                time.sleep(self.delay)

class CurrencyDecorator(ProcessorDecorator):
    def __init__(self, wrappee: PaymentProcessor, rate: float):
        super().__init__(wrappee)
        self.rate = rate  # e.g., USD->AUD conversion rate

    def pay(self, order: Order) -> None:
        if order.get("currency") and order["currency"].upper() != "AUD":
            converted = dict(order)
            converted["total"] = round(order["total"] * self.rate, 2)
            converted["currency"] = "AUD"
            return super().pay(converted)
        return super().pay(order)

if __name__ == "__main__":
    base = BaseProcessor()
    processor = LoggingDecorator(
        RetryDecorator(
            CurrencyDecorator(base, rate=1.5),
            retries=2,
            delay=0.1,
            should_fail=lambda o: o.get("total", 0) < 20,  # make small payments fail twice
        )
    )
    processor.pay({"total": 10.0, "currency": "USD"})
