class Caixa:
    def __init__(self, saldo: float) -> None:
        """Classe Caixa

        Args:
            saldo (float): Saldo do Caixa
        """
        self.saldo = saldo

    @property
    def saldo(self) -> float:
        """Retorna o saldo do Caixa

        Returns:
            float: Saldo do Caixa
        """
        return self._saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        """Altera o saldo do Caixa

        Args:
            saldo (float): Saldo do Caixa
        """
        self._saldo = saldo

    def depositar(self, valor: float) -> None:
        """Incrementa o valor do Caixa

        Args:
            valor (float): Valor a ser adicionado no Caixa
        """
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        """Decrementa o valor do Caixa

        Args:
            valor (float): Valor a ser retirado do Caixa
        """
        self.saldo -= valor
