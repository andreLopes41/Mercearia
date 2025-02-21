from model.Funcionario import Funcionario
import json
import os


class FuncionarioRepository:

    JSON_FILE = '../json/funcionario.json'

    @classmethod
    def create(cls, funcionario: Funcionario) -> None:
        """Cria um novo Funcionario

        Args:
            funcionario (Funcionario): Objeto Funcionario
        """

        funcionarios: list = cls.read()

        funcionarios.append(
            {
                'cpf': funcionario.cpf,
                'nome': funcionario.nome,
                'cargo': funcionario.cargo,
            }
        )

        cls.save(funcionarios)

    @classmethod
    def read(cls) -> list:
        """Retorna os funcionarios salvos no arquivo JSON

        Returns:
            list: Lista de Objetos Funcionario
        """
        os.makedirs('../json', exist_ok=True)

        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []

    @classmethod
    def update(cls, funcionario: Funcionario) -> None:
        """Altera um Funcipnario com base no CPF

        Args:
            funcionario (Funcionario): Objeto Funcionario com os dados atualizados
        """
        funcionarios: list = cls.read()

        for fun in funcionarios:
            if fun['cpf'] == funcionario.cpf:
                fun['nome'] = funcionario.nome
                fun['cargo'] = funcionario.cargo
                break

        cls.save(funcionarios)

    @classmethod
    def delete(cls, funcionario: Funcionario) -> None:
        """Exclui um Funcionario com base no CPF

        Args:
            funcionario (Funcionario): Objeto Funcionario
        """
        funcionarios: list = cls.read()

        funcionarios = [
            fun for fun in funcionarios if fun['cpf'] != funcionario.cpf
        ]
        cls.save(funcionarios)

    @classmethod
    def save(cls, funcionario: list) -> None:
        """Faz a persistência do Funcionario em arquivo JSON

        Args:
            funcionario (list): Lista de Objetos Funcionario
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(funcionario, arquivo, indent=4)
