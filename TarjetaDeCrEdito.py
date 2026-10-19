from abc import ABC, abstractmethod

class TarjetaCredito(ABC):
    def __init__(self, numero: str, titular: str):
        self.numero = numero
        self.titular = titular

    @abstractmethod
    def calcular_cashback(self, monto: float) -> float:
        """Método abstracto que será implementado de forma polimórfica en las subclases."""
        pass


class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
      
        cashback = monto * 0.02
        print(f"[Gold] Compra de ${monto:,.2f} -> Cashback generado (2%): ${cashback:,.2f}")
        return cashback


class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
       
        cashback = monto * 0.05
        print(f"[Black] Compra de ${monto:,.2f} -> Cashback generado (5%): ${cashback:,.2f}")
        return cashback



def procesar_cashback(tarjeta: TarjetaCredito, monto_compra: float):
    """Función que procesa el cálculo independientemente de si es Gold o Black (Polimorfismo)."""
    tarjeta.calcular_cashback(monto_compra)


if __name__ == "__main__":
    
    tarjeta_g = TarjetaGold("1234-5678-9876", "Carlos Mendoza")
    tarjeta_b = TarjetaBlack("9876-5432-1234", "Ana Rodríguez")

    monto_transaccion = 500000.0

    print("--- Procesando Tarjeta Gold ---")
    procesar_cashback(tarjeta_g, monto_transaccion)

    print("\n--- Procesando Tarjeta Black ---")
    procesar_cashback(tarjeta_b, monto_transaccion)