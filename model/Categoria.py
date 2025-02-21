class Categoria:
    def __init__(self, nome: str, descricao: str) -> None:
        """Classe Categoria

        Args:
            nome (str): Nome da Categoiria
            descricao (str): Descrição da Categoria
        """
        self.nome = nome
        self.descricao = descricao

    @property
    def nome(self) -> str:
        """Retorna o nome da Categoria

        Returns:
            str: Nome da Categoria
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Altera o nome da Categoria

        Args:
            nome (str): Nome da Categoria
        """
        self._nome = nome

    @property
    def descricao(self) -> str:
        """Retorna a descrição da Categoria

        Returns:
            str: Descrição da Categoria
        """
        return self._descricao

    @descricao.setter
    def descricao(self, descricao: str) -> None:
        """Altera a descrição da Categoria

        Args:
            descricao (str): Descrição da Categoria
        """
        self._descricao = descricao
