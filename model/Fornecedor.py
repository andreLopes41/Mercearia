from model.Categoria import Categoria


class Fornecedor:
    def __init__(self, cnpj: str, nome: str, categoria: Categoria) -> None:
        """Classe Fornecedor

        Args:
            cnpj (str): Cnpj do Fornecedor
            nome (str): Nome do Fornecedor
            categoria (Categoria): Categoria do Fornecedor
        """
        self.cnpj = cnpj
        self.nome = nome
        self.categoria = categoria

    @property
    def cnpj(self) -> str:
        """Retorna o cnpj do Fornecedor no formato XX.XXX.XXX/XXXX-XX

        Returns:
            str: Cnpj do Fornecedor
        """
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj: str) -> None:
        """Altera o cnpj do Fornecedor no formato XX.XXX.XXX/XXXX-XX

        Args:
            cnpj (str): Cnpj do Fornecedor
        """
        self._cnpj = cnpj

    @property
    def nome(self) -> str:
        """Retorna o nome do Fornecedor

        Returns:
            str: Nome do Fornecedor
        """
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        """Altera o nome do Fornecedor

        Args:
            nome (str): _description_
        """
        self._nome = nome

    @property
    def categoria(self) -> Categoria:
        """Retorna a Categoria do Fornecedor

        Returns:
            Categoria: Objeto de Categoria
        """
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: Categoria) -> None:
        """Altera a Categoria do Fornecedor

        Args:
            categoria (Categoria): Objeto de Categoria
        """
        self._categoria = categoria
