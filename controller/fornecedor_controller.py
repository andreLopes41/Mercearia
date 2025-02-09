from model.Fornecedor import Fornecedor
from model.Categoria import Categoria
from repository.fornecedor_repository import FornecedorRepository
import re

class FornecedorController:
    def __init__(self) -> None:
        """Inicializa o controlador de Fornecedor
        Cria uma instância do Repository de fornecedor
        """
        self.repository = FornecedorRepository()
    
    def criar_fornecedor(self, cnpj : str, nome : str, categoria : Categoria) -> None:
        """Adiciona um novo fornecedor ao sistema

        Args:
            cnpj (str): CNPJ do fornecedor no formato XX.XXX.XXX/XXXX-XX
            nome (str): Nome do fornecedor
            categoria (Categoria): Categoria do fornecedor

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o CNPJ for inválido
            ValueError: Se já existir um fornecedor com o CNPJ informado
        """
        if not cnpj or not nome or not categoria:
            raise ValueError("CNPJ, nome e categoria são obrigatórios")
        
        if not self.is_cnpj_valido(cnpj):
            raise ValueError("CNPJ inválido")
            
        fornecedores : list = self.listar_fornecedores()
        if any(frn["cnpj"] == cnpj for frn in fornecedores):
            raise ValueError("Já existe um fornecedor com este CNPJ")
            
        novo_fornecedor : Fornecedor = Fornecedor(cnpj, nome, categoria)
        self.repository.create(novo_fornecedor)
    
    def listar_fornecedores(self) -> list:
        """Retorna a lista de todos os fornecedores cadastrados

        Returns:
            list: Lista de dicionários contendo os dados dos fornecedores
        """
        return self.repository.read()
    
    def buscar_fornecedor(self, cnpj : str) -> dict:
        """Busca um fornecedor pelo CNPJ

        Args:
            cnpj (str): CNPJ do fornecedor no formato XX.XXX.XXX/XXXX-XX

        Returns:
            dict: Dicionário com os dados do fornecedor

        Raises:
            ValueError: Se o CNPJ for inválido
            ValueError: Se o fornecedor não for encontrado
        """
        if not self.is_cnpj_valido(cnpj):
            raise ValueError("CNPJ inválido")
            
        fornecedores : list = self.repository.read()
        for fornecedor in fornecedores:
            if fornecedor["cnpj"] == cnpj:
                return fornecedor
        raise ValueError("Fornecedor não encontrado")
    
    def buscar_fornecedores_por_categoria(self, categoria : Categoria) -> list:
        """Busca todos os fornecedores de uma determinada categoria

        Args:
            categoria (Categoria): Categoria para filtrar os fornecedores

        Returns:
            list: Lista de dicionários contendo os fornecedores da categoria

        Raises:
            ValueError: Se a categoria não for informada
            ValueError: Se não houver Fornecedores vinculados a categoria
        """
        if not categoria:
            raise ValueError("Categoria é obrigatória")
            
        fornecedores : list = self.repository.read()
        if not fornecedores:
            raise ValueError('Não há Fornecedores vinculados a categoria do produto.')
        return [frn for frn in fornecedores if frn["categoria"] == categoria]
    
    def atualizar_fornecedor(self, cnpj : str, nome : str, categoria : Categoria) -> None:
        """Atualiza os dados de um fornecedor existente

        Args:
            cnpj (str): CNPJ do fornecedor no formato XX.XXX.XXX/XXXX-XX
            nome (str): Novo nome do fornecedor
            categoria (Categoria): Nova categoria do fornecedor

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o CNPJ for inválido
            ValueError: Se o fornecedor não for encontrado
        """
        if not cnpj or not nome or not categoria:
            raise ValueError("CNPJ, nome e categoria são obrigatórios")
            
        if not self.is_cnpj_valido(cnpj):
            raise ValueError("CNPJ inválido")
            
        self.buscar_fornecedor(cnpj)
        
        fornecedor_atualizado : Fornecedor = Fornecedor(cnpj, nome, categoria)
        self.repository.update(fornecedor_atualizado)
    
    def excluir_fornecedor(self, cnpj : str) -> None:
        """Remove um fornecedor do sistema

        Args:
            cnpj (str): CNPJ do fornecedor no formato XX.XXX.XXX/XXXX-XX

        Raises:
            ValueError: Se o CNPJ não for informado
            ValueError: Se o CNPJ for inválido
            ValueError: Se o fornecedor não for encontrado
        """
        if not cnpj:
            raise ValueError("CNPJ é obrigatório")
            
        if not self.is_cnpj_valido(cnpj):
            raise ValueError("CNPJ inválido")
            
        self.buscar_fornecedor(cnpj)
        
        fornecedor : Fornecedor = Fornecedor(cnpj, "", None)
        self.repository.delete(fornecedor)
    
    def fornece_categoria(self, fornecedor : dict, categoria : dict) -> bool:
        """Verifica se um fornecedor trabalha com uma determinada categoria

        Args:
            fornecedor (dict): Dicionário com os dados do fornecedor
            categoria (dict): Dicionário com os dados da categoria

        Returns:
            bool: True se o fornecedor trabalha com a categoria, False caso contrário
        """
        """Verifica se um fornecedor trabalha com uma determinada categoria"""
        return fornecedor["categoria"]["nome"] == categoria["nome"]

    def is_cnpj_valido(self, cnpj : str) -> bool:
        """Verifica se um CNPJ está em formato válido

        Args:
            cnpj (str): CNPJ a ser validado no formato XX.XXX.XXX/XXXX-XX

        Returns:
            bool: True se o CNPJ estiver em formato válido, False caso contrário
        """
        padrao = re.compile(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$')
        return bool(padrao.match(cnpj))

        
