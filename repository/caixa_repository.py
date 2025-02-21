import json
import os


class CaixaRepository:

    JSON_FILE = '../json/caixa.json'

    @classmethod
    def read(cls) -> dict:
        """Retorna o saldo gravado no arquivo JSON

        Returns:
            dict: saldo disponível
        """
        os.makedirs('../json', exist_ok=True)

        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            saldo: dict = {'saldo': 0}
            cls.save(saldo)
            return saldo

    @classmethod
    def depositar(cls, valor: float) -> None:
        """Adiciona o valor passado por parâmetro ao saldo no arquivo JSON

        Args:
            valor (float): valor a ser adicionado
        """
        saldo: dict = cls.read()
        saldo['saldo'] += valor
        cls.save(saldo)

    @classmethod
    def sacar(cls, valor: float) -> None:
        """Retira o valor passado por parâmetro do saldo no arquivo JSON

        Args:
            valor (float): valor a ser retirado
        """
        saldo: dict = cls.read()
        saldo['saldo'] -= valor
        cls.save(saldo)

    @classmethod
    def save(cls, saldo: dict) -> None:
        """Faz a persistência do valor do saldo em arquivo JSON

        Args:
            saldo (dict): saldo a ser persistido
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(saldo, arquivo, indent=4)
