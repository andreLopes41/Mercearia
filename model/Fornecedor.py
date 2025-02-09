from model.Categoria import Categoria

class Fornecedor:

    def __init__(self, cnpj : str, nome : str, categoria : Categoria) -> None:
        """Classe Fornecedor

        Args:
            cnpj (str): Cnpj do Fornecedor
            nome (str): Nome do Fornecedor
            categoria (Categoria): Categoria do Fornecedor
        """
        self.cnpj = cnpj
        self.nome = nome
        self.categoria = categoria

    def get_cnpj(self) -> str:
        """Retorna o cnpj do Fornecedor no formato XX.XXX.XXX/XXXX-XX

        Returns:
            str: Cnpj do Fornecedor
        """
        return self.cnpj
    
    def set_cnpj(self, cnpj : str) -> None:
        """Altera o cnpj do Fornecedor no formato XX.XXX.XXX/XXXX-XX

        Args:
            cnpj (str): Cnpj do Fornecedor
        """
        self.cnpj = cnpj

    def get_nome(self) -> str:
        """Retorna o nome do Fornecedor

        Returns:
            str: Nome do Fornecedor
        """
        return self.nome
    
    def set_nome(self, nome : str) -> None:
        """Altera o nome do Fornecedor

        Args:
            nome (str): _description_
        """
        self.nome = nome

    def get_categoria(self) -> Categoria:
        """Retorna a Categoria do Fornecedor

        Returns:
            Categoria: Objeto de Categoria
        """
        return self.categoria
    
    def set_categoria(self, categoria : Categoria) -> None:
        """Altera a Categoria do Fornecedor

        Args:
            categoria (Categoria): Objeto de Categoria
        """
        self.categoria = categoria
