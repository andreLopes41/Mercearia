from model.Caixa import Caixa
from repository.caixa_repository import CaixaRepository

class CaixaController:

    def __init__(self) -> None:
        """Inicializa o controlador do Caixa
        Cria uma instância do Repository e carrega os dados do caixa
        """
        self.repository = CaixaRepository()
        self.caixa = None
        self.carregar_caixa()
    
    def carregar_caixa(self) -> None:
        """Carrega os dados do caixa a partir do Repository
        """
        dados : dict = self.repository.read()
        self.caixa = Caixa(dados["saldo"])
    
    def get_saldo(self) -> float:
        """Retorna o saldo atual do caixa

        Returns:
            float: Saldo atual do caixa
        """
        return self.caixa.get_saldo()
    
    def depositar(self, valor : float) -> None:
        """Realiza um depósito no caixa

        Args:
            valor (float): Valor a ser depositado

        Raises:
            ValueError: Se o valor do depósito for menor ou igual a zero
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        
        self.caixa.depositar(valor)
        self.repository.depositar(valor)
        
    def sacar(self, valor : float) -> None:
        """Realiza um saque do caixa

        Args:
            valor (float): Valor a ser sacado

        Raises:
            ValueError: Se o valor do saque for menor ou igual a zero ou se não houver saldo suficiente
        """
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > self.caixa.get_saldo():
            raise ValueError("Saldo insuficiente")
            
        self.caixa.sacar(valor)
        self.repository.sacar(valor)

    def verificar_saldo(self, valor : float) -> bool:
        """Verifica se há saldo suficiente para uma operação

        Args:
            valor (float): Valor a ser verificado

        Returns:
            bool: True se houver saldo suficiente, False caso contrário
        """
        return self.get_saldo() >= valor

