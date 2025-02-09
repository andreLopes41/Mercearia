class Caixa:
    
    def __init__(self, saldo : float) -> None:
        """Classe Caixa

        Args:
            saldo (float): Saldo do Caixa
        """
        self.saldo = saldo
    
    def get_saldo(self) -> float:
        """Retorna o saldo do Caixa

        Returns:
            float: Saldo do Caixa
        """
        return self.saldo
    
    def set_saldo(self, saldo : float) -> None:
        """Altera o saldo do Caixa

        Args:
            saldo (float): Saldo do Caixa
        """
        self.saldo = saldo

    def depositar(self, valor : float) -> None:
        """Incrementa o valor do Caixa 

        Args:
            valor (float): Valor a ser adicionado no Caixa
        """
        self.saldo += valor

    def sacar(self, valor : float) -> None:
        """Decrementa o valor do Caixa 

        Args:
            valor (float): Valor a ser retirado do Caixa
        """
        self.saldo -= valor
