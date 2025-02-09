from model.Produto import Produto
import json
import os

class ProdutoRepository:

    JSON_FILE = '../json/produto.json'

    @classmethod
    def create(cls, produto : Produto) -> None:
        """Cria um Novo Produto

        Args:
            produto (Produto): Objeto Produto
        """
        
        produtos : list = cls.read()
            
        produtos.append({
            "nome": produto.get_nome(),
            "preco": produto.get_preco(),
            "categoria": produto.get_categoria()
        })
        
        cls.save(produtos)

    @classmethod
    def read(cls) -> list:
        """Retorna os produtos salvos no arquivo JSON

        Returns:
            list: Lista de objetos Produto
        """
        os.makedirs('../json', exist_ok=True)
        
        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []
    
    @classmethod
    def update(cls, produto : Produto) -> None:
        """Altera um Produto com base no nome

        Args:
            produto (Produto): Objeto Produto com os dados atualizados
        """
        produtos : list = cls.read()
        
        for pro in produtos:
            if pro["nome"] == produto.get_nome():
                pro["preco"] = produto.get_preco()
                pro["categoria"] = produto.get_categoria()
                break
        
        cls.save(produtos)
    
    @classmethod
    def delete(cls, produto : Produto) -> None:
        """Exclui um Produto com base no nome

        Args:
            produto (Produto): Objeto Produto
        """
        produtos : list = cls.read()

        produtos = [pro for pro in produtos if pro["nome"] != produto.get_nome()]
        cls.save(produtos)

    @classmethod
    def save(cls, produto : list) -> None:
        """Faz a persistência do Produto em arquivo JSON

        Args:
            produto (list): Lista de objetos Produto
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(produto, arquivo, indent=4)
