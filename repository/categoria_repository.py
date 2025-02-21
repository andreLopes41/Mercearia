from model.Categoria import Categoria
import json
import os


class CategoriaRepository:

    JSON_FILE = '../json/categoria.json'

    @classmethod
    def create(cls, categoria: Categoria) -> None:
        """Cria uma nova categoria

        Args:
            categoria (Categoria): Objeto Categoria
        """

        categorias: list = cls.read()

        categorias.append(
            {
                'nome': categoria.nome,
                'descricao': categoria.descricao,
            }
        )

        cls.save(categorias)

    @classmethod
    def read(cls) -> list:
        """Retorna as categorias salvas no arquivo JSON

        Returns:
            list: Lista de Objetos Categoria
        """
        os.makedirs('../json', exist_ok=True)

        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []

    @classmethod
    def update(cls, categoria: Categoria) -> None:
        """Altera uma Categoria com base no nome

        Args:
            categoria (Categoria): Objeto Categoria com os dados atualizados
        """
        categorias: list = cls.read()

        for cat in categorias:
            if cat['nome'] == categoria.nome:
                cat['descricao'] = categoria.descricao
                break

        cls.save(categorias)

    @classmethod
    def delete(cls, categoria: Categoria) -> None:
        """Exclui uma Categoria com base no nome

        Args:
            categoria (Categoria): Objeto Categoria
        """
        categorias: list = cls.read()

        categorias = [
            cat for cat in categorias if cat['nome'] != categoria.nome
        ]
        cls.save(categorias)

    @classmethod
    def save(cls, categorias: list) -> None:
        """Faz a persistência da Categoria em arquivo JSON

        Args:
            categorias (list): Lista de Objetos Categoria
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(categorias, arquivo, indent=4)
