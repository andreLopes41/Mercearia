from model.Cliente import Cliente
from model.Funcionario import Funcionario
from model.Produto import Produto
from datetime import datetime


class Venda:
    def __init__(
        self,
        produto: Produto,
        quantidade: int,
        comprador: Cliente,
        vendedor: Funcionario,
        data: datetime,
    ):
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
        self.valor = self.produto.preco * self.quantidade

    @property
    def produto(self) -> Produto:
        """Retorna o Produto da Venda

        Returns:
            Produto: Objeto de Produto
        """
        return self._produto

    @produto.setter
    def produto(self, produto: Produto) -> None:
        """Altera o Produto da Venda

        Args:
            produto (Produto): Objeto de Produto
        """
        self._produto = produto

    @property
    def quantidade(self) -> int:
        """Retorna a quantidade vendida do Produto

        Returns:
            int: Quantidade vendida do Produto
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int) -> None:
        """Altera a quantidade vendida do Produto

        Args:
            quantidade (int): Quantidade vendida do Produto
        """
        self._quantidade = quantidade

    @property
    def comprador(self) -> Cliente:
        """Retorna o comprador

        Returns:
            Cliente: Objeto de Cliente
        """
        return self._comprador

    @comprador.setter
    def comprador(self, comprador: Cliente) -> None:
        """Altera o comprador

        Args:
            comprador (Cliente): Objeto de Cliente
        """
        self._comprador = comprador

    @property
    def vendedor(self) -> Funcionario:
        """Retorna o Vendedor

        Returns:
            Funcionario: Objeto de Funcionário
        """
        return self._vendedor

    @vendedor.setter
    def vendedor(self, vendedor: Funcionario) -> None:
        """Altera o Vendedor

        Args:
            vendedor (Funcionario): Objeto de Funcionário
        """
        self._vendedor = vendedor

    @property
    def data(self) -> datetime:
        """Retorna a data da Venda no formato (Y-m-d h:m:s)

        Returns:
            datetime: Data da venda
        """
        return self._data

    @data.setter
    def data(self, data: datetime) -> None:
        """Altera a data da Venda no formato (Y-m-d h:m:s)

        Args:
            data (datetime): Data da venda
        """
        self._data = data

    @property
    def valor(self) -> float:
        """Retorna o valor total da Venda

        Returns:
            float: Valor total da Venda
        """
        return self._valor

    @valor.setter
    def valor(self, valor: float) -> None:
        """Altera o valor total da Venda

        Args:
            valor (float): Valor total da Venda
        """
        self._valor = valor
