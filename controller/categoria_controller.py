from model.Categoria import Categoria
from repository.categoria_repository import CategoriaRepository


class CategoriaController:
    def __init__(self) -> None:
        """Inicializa o controlador de Categorias
        Cria uma instância do Repository de categorias
        """
        self.repository = CategoriaRepository()

    def criar_categoria(self, nome: str, descricao: str) -> None:
        """Cria uma nova categoria

        Args:
            nome (str): Nome da categoria
            descricao (str): Descrição da categoria

        Raises:
            ValueError: Se o nome ou descrição estiverem vazios
            ValueError: Se já existir uma categoria com o mesmo nome
        """
        if not nome or not descricao:
            raise ValueError('Nome e descrição são obrigatórios')

        try:
            categorias: list = self.listar_categorias()
        except ValueError:
            categorias = []

        if any(cat['nome'] == nome for cat in categorias):
            raise ValueError('Já existe uma categoria com este nome')

        nova_categoria: Categoria = Categoria(nome, descricao)
        self.repository.create(nova_categoria)

    def listar_categorias(self) -> list:
        """Retorna a lista de todas as categorias

        Returns:
            list: Lista de dicionários contendo as categorias

        Raises:
            ValueError: Se não existirem categorias cadastradas
        """
        categorias: list = self.repository.read()
        if not categorias:
            raise ValueError('Não há categorias cadastradas.')
        return categorias

    def buscar_categoria(self, nome: str) -> Categoria:
        """Busca uma categoria pelo nome

        Args:
            nome (str): Nome da categoria a ser buscada

        Returns:
            dict: Dicionário com os dados da categoria

        Raises:
            ValueError: Se a categoria não for encontrada
        """
        categorias: list = self.repository.read()
        for categoria in categorias:
            if categoria['nome'] == nome:
                return categoria
        raise ValueError('Categoria não encontrada')

    def atualizar_categoria(self, nome: str, nova_descricao: str) -> None:
        """Atualiza a descrição de uma categoria existente

        Args:
            nome (str): Nome da categoria a ser atualizada
            nova_descricao (str): Nova descrição da categoria

        Raises:
            ValueError: Se o nome ou nova descrição estiverem vazios
            ValueError: Se a categoria não for encontrada
        """
        if not nome or not nova_descricao:
            raise ValueError('Nome e nova descrição são obrigatórios')

        self.buscar_categoria(nome)

        categoria_atualizada: Categoria = Categoria(nome, nova_descricao)
        self.repository.update(categoria_atualizada)

    def excluir_categoria(self, nome: str) -> None:
        """Exclui uma categoria pelo nome

        Args:
            nome (str): Nome da categoria a ser excluída

        Raises:
            ValueError: Se o nome estiver vazio
            ValueError: Se a categoria não for encontrada
        """
        if not nome:
            raise ValueError('Nome da categoria é obrigatório')

        self.buscar_categoria(nome)

        categoria: Categoria = Categoria(nome, '')
        self.repository.delete(categoria)
