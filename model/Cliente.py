from model.Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, cpf : str, nome : str, valor_gasto : float) -> None:
        """Classe Cliente

        Args:
            cpf (str): Cpf do Cliente
            nome (str): Nome do Cliente
            valor_gasto (float): Valor gasto pelo Cliente
        """
        super().__init__(cpf, nome)
        self.valor_gasto = valor_gasto

    def get_valor_gasto(self) -> float:
        """Retorna o valor gasto pelo Cliente

        Returns:
            float: Valor gasto pelo Cliente
        """
        return self.valor_gasto
    
    def set_valor_gasto(self, valor_gasto : float) -> None:
        """Altera o valor gasto pelo Cliente

        Args:
            valor_gasto (float): Valor gasto pelo Cliente
        """
        self.valor_gasto = valor_gasto