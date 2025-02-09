from model.Categoria import Categoria

class Produto:

    def __init__(self, nome : str, preco : float, categoria : Categoria) -> None:
        """Classe Produto

        Args:
            nome (str): Nome do Produto
            preco (float): Preço do Produto
            categoria (Categoria): Objeto de Categoria
        """
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def get_nome(self) -> str:
        """Retorna o mome do Produto

        Returns:
            str: Nome do Produto
        """
        return self.nome
    
    def set_nome(self, nome : str) -> None:
        """Altera o nome do Produto

        Args:
            nome (str): Nome do Produto
        """
        self.nome = nome

    def get_preco(self) -> float:
        """Retorna o preço do Produto

        Returns:
            float: Preço do Produto
        """
        return self.preco
    
    def set_preco(self, preco : float) -> None:
        """Altera o preço do Produto

        Args:
            preco (float): Preço do Produto
        """
        self.preco = preco

    def get_categoria(self) -> Categoria:
        """Retorna a Categoria do Produto

        Returns:
            Categoria: Objeto de Categoria
        """
        return self.categoria
    
    def set_categoria(self, categoria : Categoria) -> None:
        """Altera a Categoria do Produto

        Args:
            categoria (Categoria): Objeto de Categoria
        """
        self.categoria = categoria