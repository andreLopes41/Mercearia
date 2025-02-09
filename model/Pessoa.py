class Pessoa:

    def __init__(self, cpf : str, nome : str) -> None:
        """Classe Peesoa

        Args:
            cpf (str): Cpf da Pessoa no formato XXX.XXX.XXX-XX
            nome (str): Nome da Pessoa
        """
        self.cpf = cpf
        self.nome = nome
    
    def get_cpf(self) -> str:
        """Retorna o cpf da Pessoa no formato XXX.XXX.XXX-XX

        Returns:
            str: Cpf da Pessoa
        """
        return self.cpf
    
    def set_cpf(self, cpf : str) -> None:
        """Altera o cpf da Pessoa no formato XXX.XXX.XXX-XX

        Args:
            cpf (str): Cpf da Pessoa
        """
        self.cpf = cpf

    def get_nome(self) -> str:
        """Retorna o nome da Pessoa

        Returns:
            str: Nome da pessoa
        """
        return self.nome
    
    def set_nome(self, nome : str) -> None:
        """Altera o nome da Pessoa

        Args:
            nome (str): Nome da pessoa
        """
        self.nome = nome