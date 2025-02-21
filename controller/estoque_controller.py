from model.Estoque import Estoque
from model.Produto import Produto
from repository.estoque_repository import EstoqueRepository


class EstoqueController:
    def __init__(self) -> None:
        """Inicializa o controlador de Estoque
        Cria uma instância do Repository de estoque
        """
        self.repository = EstoqueRepository()

    def adicionar_produto_estoque(
        self, produto: Produto, quantidade: int
    ) -> None:
        """Adiciona um produto ao estoque ou atualiza sua quantidade se já existir

        Args:
            produto (Produto): Produto a ser adicionado
            quantidade (int): Quantidade a ser adicionada

        Raises:
            ValueError: Se o produto não for informado
            ValueError: Se a quantidade for negativa
        """

        if not produto:
            raise ValueError('Produto é obrigatório')

        if quantidade < 0:
            raise ValueError('Quantidade não pode ser negativa')

        estoque_atual: list = self.listar_estoque()
        for item in estoque_atual:
            if item['produto'] == produto:
                nova_quantidade = item['quantidade'] + quantidade
                return self.atualizar_quantidade(produto, nova_quantidade)

        novo_estoque: Estoque = Estoque(produto, quantidade)
        self.repository.create(novo_estoque)

    def listar_estoque(self) -> list:
        """Retorna a lista de todos os produtos em estoque

        Returns:
            list: Lista de dicionários contendo produtos e suas quantidades
        """

        return self.repository.read()

    def buscar_produto_estoque(self, produto: Produto) -> Produto:
        """Busca um produto no estoque

        Args:
            produto (Produto): Produto a ser buscado

        Returns:
            dict: Dicionário com os dados do produto em estoque

        Raises:
            ValueError: Se o produto não for informado
            ValueError: Se o produto não for encontrado no estoque
        """

        if not produto:
            raise ValueError('Produto é obrigatório')

        estoque: list = self.repository.read()
        for item in estoque:
            if item['produto'] == produto:
                return item
        raise ValueError('Produto não encontrado no estoque')

    def atualizar_quantidade(
        self, produto: Produto, nova_quantidade: int
    ) -> None:
        """Atualiza a quantidade de um produto no estoque

        Args:
            produto (Produto): Produto a ser atualizado
            nova_quantidade (int): Nova quantidade do produto

        Raises:
            ValueError: Se o produto não for informado
            ValueError: Se a quantidade for negativa
            ValueError: Se o produto não for encontrado no estoque
        """

        if not produto:
            raise ValueError('Produto é obrigatório')

        if nova_quantidade < 0:
            raise ValueError('Quantidade não pode ser negativa')

        self.buscar_produto_estoque(produto)

        estoque_atualizado: Estoque = Estoque(produto, nova_quantidade)
        self.repository.update(estoque_atualizado)

    def remover_produto_estoque(self, produto: Produto) -> None:
        """Remove um produto do estoque

        Args:
            produto (Produto): Produto a ser removido

        Raises:
            ValueError: Se o produto não for informado
            ValueError: Se o produto não for encontrado no estoque
        """

        if not produto:
            raise ValueError('Produto é obrigatório')

        self.buscar_produto_estoque(produto)

        estoque: Estoque = Estoque(produto, 0)
        self.repository.delete(estoque)

    def baixar_estoque(self, produto: Produto, quantidade: int) -> None:
        """Reduz a quantidade de um produto no estoque

        Args:
            produto (Produto): Produto a ter quantidade reduzida
            quantidade (int): Quantidade a ser reduzida

        Raises:
            ValueError: Se a quantidade for negativa
            ValueError: Se o produto não for encontrado no estoque
            ValueError: Se não houver quantidade suficiente em estoque
        """

        if quantidade < 0:
            raise ValueError('Quantidade não pode ser negativa')

        item_estoque: Produto = self.buscar_produto_estoque(produto)
        if item_estoque['quantidade'] < quantidade:
            raise ValueError('Quantidade insuficiente em estoque')

        nova_quantidade: int = item_estoque['quantidade'] - quantidade
        self.atualizar_quantidade(produto, nova_quantidade)

    def verificar_disponibilidade(
        self, produto: Produto, quantidade: int
    ) -> bool:
        """Verifica se há quantidade suficiente de um produto em estoque

        Args:
            produto (Produto): Produto a ser verificado
            quantidade (int): Quantidade desejada

        Returns:
            bool: True se houver quantidade suficiente, False caso contrário
        """

        try:
            item_estoque = self.buscar_produto_estoque(produto)
            return item_estoque['quantidade'] >= quantidade
        except ValueError:
            return False
