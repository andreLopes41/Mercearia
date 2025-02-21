from model.Produto import Produto


class Estoque:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        """Classe Estoque

        Args:
            produto (Produto): Objeto de Produto
            quantidade (int): Quantidade de Produtos no Estoque
        """
        self.produto = produto
        self.quantidade = quantidade

    @property
    def produto(self) -> Produto:
        """Retorna o Produto do Estoque

        Returns:
            Produto: Objeto de Produto
        """
        return self._produto

    @produto.setter
    def produto(self, produto: Produto) -> None:
        """Altera o Produto no Estoque

        Args:
            produto (Produto): Objeto de Produto
        """
        self._produto = produto

    @property
    def quantidade(self) -> int:
        """Retorna a quantidade do Produto no Estoque

        Returns:
            int: Quantidade de Produtos
        """
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int) -> None:
        """Altera a quantidade do Produto no Estoque

        Args:
            quantidade (int): Quantidade de Produtos
        """
        self._quantidade = quantidade
