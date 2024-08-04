from __future__ import annotations
from abc import ABC, abstractmethod

# ------------------>> Interface dos estados possíveis <<------------------
class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self._order = order
    
    @abstractmethod
    def pending(self) -> None: ...
    @abstractmethod
    def approve(self) -> None: ...
    @abstractmethod
    def reject(self) -> None: ...
    
# ------------------>> Contexto - Objeto <<------------------
class Order:
    def __init__(self) -> None:
        self._state: OrderState = PaymentPending(self) # Estado inicial
        
    def pending(self) -> None:
        self._state.pending()
        
    def approve(self) -> None:
        self._state.approve()
        
    def reject(self) -> None: 
        self._state.reject()
    
# ------------------>> Classes de estados possíveis <<------------------
class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento já pendente, não fazer nada!')
        
    def approve(self) -> None:
        self._order._state = PaymentApproved(self._order)
        print('Pagamento aprovado!')
        
    def reject(self) -> None:
        self._order._state = PaymentRejected(self._order)
        print('Pagamento rejeitado!')
    
class PaymentApproved(OrderState):
    def pending(self) -> None:
        self._order._state = PaymentPending(self._order)
        print('Pagamento pendente!')
        
    def approve(self) -> None:
        print('Pagamento já foi aprovado!, Não fazer nada')
        
    def reject(self) -> None:
        self._order._state = PaymentRejected(self._order)
        print('Pagamento rejeitado!')
        
class PaymentRejected(OrderState):
    def pending(self) -> None:
        print('Pagamento rejeitado! Não fazer nada.')
    def approve(self) -> None:
        print('Pagamento rejeitado! Não fazer nada.')
    def reject(self) -> None:
        print('Pagamento rejeitado! Não fazer nada.')
        
# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    order = Order()
    order.pending()
    order.approve()
    order.reject()
    order.pending()