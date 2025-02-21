from model.Estoque import Estoque
import json
import os


class EstoqueRepository:

    JSON_FILE = '../json/estoque.json'

    @classmethod
    def create(cls, item: Estoque) -> None:
        """Cria o Estqoue de um Produto

        Args:
            item (Estoque): Objeto Estoque
        """

        estoque: list = cls.read()

        estoque.append(
            {
                'produto': item.produto,
                'quantidade': item.quantidade,
            }
        )

        cls.save(estoque)

    @classmethod
    def read(cls) -> list:
        """Retorna os estoques de cada produto salvo no arquivo JSON

        Returns:
            list: Lista de Estqoues dos Produtos
        """
        os.makedirs('../json', exist_ok=True)

        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []

    @classmethod
    def update(cls, item: Estoque) -> None:
        """Altera um Estoque com base no Produto

        Args:
            item (Estoque): Objeeto Estoque com os dados atualizados
        """
        estoque: list = cls.read()

        for itm in estoque:
            if itm['produto'] == item.produto:
                itm['quantidade'] = item.quantidade
                break

        cls.save(estoque)

    @classmethod
    def delete(cls, item: Estoque) -> None:
        """Exclui um Estoque com base no Produto

        Args:
            item (Estoque): Objeto Estoque
        """
        estoque: list = cls.read()

        estoque = [
            itm for itm in estoque if itm['produto'] != item.produto
        ]
        cls.save(estoque)

    @classmethod
    def save(cls, estoque: list) -> None:
        """Faz a persistência do Estoque em arquivo JSON

        Args:
            estoque (list): Lista de Objetos Estoque
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(estoque, arquivo, indent=4)
