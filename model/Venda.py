from model.Cliente import Cliente
from model.Funcionario import Funcionario
from model.Produto import Produto
from datetime import datetime

class Venda:

    def __init__(self, produto : Produto, quantidade : int, comprador : Cliente, vendedor : Funcionario, data : datetime):
        """Classe de Venda

        Args:
            produto (Produto): Objeto de Produto
            quantidade (int): Quantidade vendida do Produto 
            comprador (Cliente): Objeto de Cliente
            vendedor (Funcionario): Objeto de Funcionario
            data (datetime): Data da realização da Venda
        """
        self.produto = produto
        self.quantidade = quantidade
        self.comprador = comprador
        self.vendedor = vendedor
        self.data = data
        self.valor = self.produto.get_preco() * self.quantidade

    def get_produto(self) -> Produto:
        """Retorna o Produto da Venda

        Returns:
            Produto: Objeto de Produto
        """
        return self.produto 
    
    def set_produto(self, produto : Produto) -> None:
        """Altera o Produto da Venda

        Args:
            produto (Produto): Objeto de Produto
        """
        self.produto = produto

    def get_quantidade(self) -> int:
        """Retorna a quantidade vendida do Produto

        Returns:
            int: Quantidade vendida do Produto
        """
        return self.quantidade  
    
    def set_quantidade(self, quantidade : int) -> None:
        """Altera a quantidade vendida do Produto

        Args:
            quantidade (int): Quantidade vendida do Produto
        """
        self.quantidade = quantidade

    def get_comprador(self) -> Cliente:
        """Retorna o comprador

        Returns:
            Cliente: Objeto de Cliente
        """
        return self.comprador   
    
    def set_comprador(self, comprador : Cliente) -> None:
        """Altera o comprador

        Args:
            comprador (Cliente): Objeto de Cliente
        """
        self.comprador = comprador

    def get_vendedor(self) -> Funcionario:
        """Retorna o Vendedor

        Returns:
            Funcionario: Objeto de Funcionário
        """
        return self.vendedor    
    
    def set_vendedor(self, vendedor : Funcionario) -> None:
        """Altera o Vendedor

        Args:
            vendedor (Funcionario): Objeto de Funcionário
        """
        self.vendedor = vendedor

    def get_data(self) -> datetime:
        """Retorna a data da Venda no formato (Y-m-d h:m:s)

        Returns:
            datetime: Data da venda
        """
        return self.data    
    
    def set_data(self, data : datetime) -> None:
        """Altera a data da Venda no formato (Y-m-d h:m:s)

        Args:
            data (datetime): Data da venda
        """
        self.data = data

    def get_valor(self) -> float:
        """Retorna o valor total da Venda

        Returns:
            float: Valor total da Venda
        """
        return self.valor

    def set_valor(self, valor : float) -> None:
        """Altera o valor total da Venda

        Args:
            valor (float): Valor total da Venda
        """
        self.valor = valor
