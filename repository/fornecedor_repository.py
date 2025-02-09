from model.Fornecedor import Fornecedor
import json
import os

class FornecedorRepository:

    JSON_FILE = '../json/fornecedor.json'

    @classmethod
    def create(cls, fornecedor : Fornecedor) -> None:
        """Cria um novo Fornecedor

        Args:
            fornecedor (Fornecedor): Objeto Fornecedor
        """
        fornecedores : list = cls.read()
            
        fornecedores.append({
            "cnpj": fornecedor.get_cnpj(), 
            "nome": fornecedor.get_nome(),
            "categoria": fornecedor.get_categoria()
        })
        
        cls.save(fornecedores)

    @classmethod
    def read(cls) -> list:
        """Retorna os fornecedores salvos no arquivo JSON

        Returns:
            list: Lista de objetos Fornecedor
        """
        os.makedirs('../json', exist_ok=True)
        
        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []
    
    @classmethod
    def update(cls, fornecedor : Fornecedor) -> None:
        """Altera um Fornecedor com base no CNPJ

        Args:
            fornecedor (Fornecedor): Objeto Fornecedor com os dados atualizados
        """
        fornecedores : list = cls.read()
        
        for frn in fornecedores:
            if frn["cnpj"] == fornecedor.get_cnpj():
                frn["nome"] = fornecedor.get_nome()
                frn["categoria"] = fornecedor.get_categoria()
                break
        
        cls.save(fornecedores)
    
    @classmethod
    def delete(cls, fornecedor : Fornecedor) -> None:
        """Exclui um Fornecedor com base no CNPJ

        Args:
            fornecedor (Fornecedor): Objeto Fornecedor
        """
        fornecedores : list = cls.read()

        fornecedores = [frn for frn in fornecedores if frn["cnpj"] != fornecedor.get_cnpj()]
        cls.save(fornecedores)

    @classmethod
    def save(cls, fornecedor : list) -> None:
        """Faz a persistência do Fornecedor em arquivo JSON

        Args:
            fornecedor (list): Lista de Objetos Fornecedor
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(fornecedor, arquivo, indent=4)