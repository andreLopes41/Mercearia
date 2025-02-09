from model.Produto import Produto
from model.Categoria import Categoria
from repository.produto_repository import ProdutoRepository

class ProdutoController:
    def __init__(self) -> None:
        """Inicializa o controlador de Produto
        Cria uma instância do Repository de produto
        """
        self.repository = ProdutoRepository()
    
    def criar_produto(self, nome : str, preco : float, categoria : Categoria) -> None:
        """Adiciona um novo produto ao sistema

        Args:
            nome (str): Nome do produto
            preco (float): Preço do produto
            categoria (Categoria): Categoria do produto

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o preço for menor ou igual a zero
            ValueError: Se já existir um produto com este nome
        """
        if not nome or not categoria:
            raise ValueError("Nome e categoria são obrigatórios")
            
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero") 

        try:
            produtos : list = self.listar_produtos()
        except ValueError:
            produtos = []

        if any(pro["nome"] == nome for pro in produtos):
            raise ValueError("Já existe um produto com este nome")
            
        novo_produto : Produto = Produto(nome, preco, categoria)
        self.repository.create(novo_produto)
    
    def listar_produtos(self) -> list:
        """Retorna a lista de todos os produtos cadastrados

        Returns:
            list: Lista de dicionários contendo os dados dos produtos

        Raises:
            ValueError: Se não existirem produtos cadastrados
        """
        produtos : list = self.repository.read()
        if not produtos:
            raise ValueError('Não há produtos cadastrados')
        return produtos
    
    def buscar_produto(self, nome : str) -> dict:
        """Busca um produto pelo nome

        Args:
            nome (str): Nome do produto a ser buscado

        Returns:
            dict: Dicionário com os dados do produto

        Raises:
            ValueError: Se o nome não for informado
            ValueError: Se o produto não for encontrado
        """
        if not nome:
            raise ValueError("Nome do produto é obrigatório")
            
        produtos : list = self.repository.read()
        for produto in produtos:
            if produto["nome"].lower() == nome.lower():
                return produto
        raise ValueError("Produto não encontrado")
    
    def buscar_produtos_por_categoria(self, categoria : Categoria) -> list:
        """Busca todos os produtos de uma determinada categoria

        Args:
            categoria (Categoria): Categoria para filtrar os produtos

        Returns:
            list: Lista de dicionários contendo os produtos da categoria

        Raises:
            ValueError: Se a categoria não for informada
        """
        if not categoria:
            raise ValueError("Categoria é obrigatória")
            
        produtos : list = self.repository.read()
        return [pro for pro in produtos if pro["categoria"] == categoria]
    
    def buscar_produtos_por_faixa_preco(self, preco_min : float, preco_max : float) -> list:
        """Busca produtos dentro de uma faixa de preço

        Args:
            preco_min (float): Preço mínimo da faixa
            preco_max (float): Preço máximo da faixa

        Returns:
            list: Lista de dicionários contendo os produtos na faixa de preço

        Raises:
            ValueError: Se os preços forem negativos
            ValueError: Se o preço mínimo for maior que o máximo
        """
        if preco_min < 0 or preco_max < 0:
            raise ValueError("Preços não podem ser negativos")
            
        if preco_min > preco_max:
            raise ValueError("Preço mínimo não pode ser maior que o preço máximo")
            
        produtos : list = self.repository.read()
        return [pro for pro in produtos if preco_min <= pro["preco"] <= preco_max]
    
    def atualizar_produto(self, nome: str, preco: float, categoria: Categoria) -> None:
        """Atualiza os dados de um produto existente

        Args:
            nome (str): Nome do produto
            preco (float): Novo preço do produto
            categoria (Categoria): Nova categoria do produto

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o preço for menor ou igual a zero
            ValueError: Se o produto não for encontrado
        """
        if not nome or not categoria:
            raise ValueError("Nome e categoria são obrigatórios")
            
        if preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
            
        self.buscar_produto(nome)
        
        produto_atualizado : Produto = Produto(nome, preco, categoria)
        self.repository.update(produto_atualizado)
    
    def atualizar_preco(self, nome : str, novo_preco : float) -> None:
        """Atualiza apenas o preço de um produto

        Args:
            nome (str): Nome do produto
            novo_preco (float): Novo preço do produto

        Raises:
            ValueError: Se o preço for menor ou igual a zero
            ValueError: Se o produto não for encontrado
        """
        if novo_preco <= 0:
            raise ValueError("Preço deve ser maior que zero")
            
        produto_atual : Produto = self.buscar_produto(nome)
        self.atualizar_produto(
            nome,
            novo_preco,
            produto_atual["categoria"]
        )
    
    def excluir_produto(self, nome : str) -> None:
        """Remove um produto do sistema

        Args:
            nome (str): Nome do produto a ser removido

        Raises:
            ValueError: Se o nome não for informado
            ValueError: Se o produto não for encontrado
        """
        if not nome:
            raise ValueError("Nome do produto é obrigatório")
            
        self.buscar_produto(nome)
        
        produto : Produto = Produto(nome, 0, None)
        self.repository.delete(produto)