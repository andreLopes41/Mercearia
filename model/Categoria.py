class Categoria:

    def __init__(self, nome : str, descricao : str) -> None:
        """Classe Categoria

        Args:
            nome (str): Nome da Categoiria
            descricao (str): Descrição da Categoria
        """
        self.nome = nome
        self.descricao = descricao

    def get_nome(self) -> str:
        """Retorna o nome da Categoria

        Returns:
            str: Nome da Categoria
        """
        return self.nome
    
    def set_nome(self, nome : str) -> None:
        """Altera o nome da Categoria

        Args:
            nome (str): Nome da Categoria
        """
        self.nome = nome

    def get_descricao(self) -> str:
        """Retorna a descrição da Categoria

        Returns:
            str: Descrição da Categoria
        """
        return self.descricao
    
    def set_descricao(self, descricao : str) -> None:
        """Altera a descrição da Categoria

        Args:
            descricao (str): Descrição da Categoria 
        """
        self.descricao = descricao