from model.Pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, cpf: str, nome: str, cargo: str) -> None:
        """Classe Funcionario

        Args:
            cpf (str): Cpf do Funcionario
            nome (str): Nome do Funcionario
            cargo (str): Cargo do Funcionario
        """
        super().__init__(cpf, nome)
        self.cargo = cargo

    @property
    def cargo(self) -> str:
        """Retorna o cargo do Funcionario

        Returns:
            str: Cargo do Funcionario
        """
        return self._cargo

    @cargo.setter
    def cargo(self, cargo: str) -> None:
        """Altera o cargo do Funcionario

        Args:
            cargo (str): Cargo do Funcionario
        """
        self._cargo = cargo
