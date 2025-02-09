from model.Cliente import Cliente
from repository.cliente_repository import ClienteRepository
import re

class ClienteController:

    def __init__(self) -> None:
        self.repository = ClienteRepository()
    
    def criar_cliente(self, cpf : str, nome : str, valor_gasto : float = 0.0) -> None:
        """Cria um novo cliente no sistema

        Args:
            cpf (str): CPF do cliente no formato XXX.XXX.XXX-XX
            nome (str): Nome do cliente
            valor_gasto (float, optional): Valor total gasto pelo cliente. Defaults to 0.0.

        Raises:
            ValueError: Se CPF ou nome estiverem vazios
            ValueError: Se o CPF for inválido
            ValueError: Se o valor gasto for negativo
            ValueError: Se já existir um cliente com o CPF informado
        """
        if not cpf or not nome:
            raise ValueError("CPF e nome são obrigatórios")
        
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        if valor_gasto < 0:
            raise ValueError("Valor gasto não pode ser negativo")
            
        clientes : list = self.listar_clientes()
        if any(cli["cpf"] == cpf for cli in clientes):
            raise ValueError("Já existe um cliente com este CPF")
            
        novo_cliente : Cliente = Cliente(cpf, nome, valor_gasto)
        self.repository.create(novo_cliente)
    
    def listar_clientes(self) -> list:
        """Retorna a lista de todos os clientes

        Returns:
            list: Lista de dicionários contendo os dados dos clientes
        """
        return self.repository.read()
    
    def buscar_cliente(self, cpf : str) -> Cliente:
        """Busca um cliente pelo CPF

        Args:
            cpf (str): CPF do cliente a ser buscado

        Returns:
            dict: Dicionário com os dados do cliente

        Raises:
            ValueError: Se o CPF for inválido
            ValueError: Se o cliente não for encontrado
        """
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        clientes : list = self.repository.read()
        for cliente in clientes:
            if cliente["cpf"] == cpf:
                return cliente
        raise ValueError("Cliente não encontrado")
    
    def atualizar_cliente(self, cpf : str, nome : str, valor_gasto : float) -> None:
        """Atualiza os dados de um cliente existente

        Args:
            cpf (str): CPF do cliente
            nome (str): Novo nome do cliente
            valor_gasto (float): Novo valor gasto do cliente

        Raises:
            ValueError: Se o CPF for inválido
            ValueError: Se o valor gasto for negativo
            ValueError: Se o cliente não for encontrado
        """
         
        if not cpf or not nome:
            raise ValueError("CPF e nome são obrigatórios")
            
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        if valor_gasto < 0:
            raise ValueError("Valor gasto não pode ser negativo")
            
        self.buscar_cliente(cpf)
        
        cliente_atualizado : Cliente = Cliente(cpf, nome, valor_gasto)
        self.repository.update(cliente_atualizado)
    
    def excluir_cliente(self, cpf : str) -> None:
        """Exclui um cliente pelo CPF

        Args:
            cpf (str): CPF do cliente a ser excluído

        Raises:
            ValueError: Se o CPF estiver vazio
            ValueError: Se o CPF for inválido
            ValueError: Se o cliente não for encontrado
        """

        if not cpf:
            raise ValueError("CPF é obrigatório")
            
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        self.buscar_cliente(cpf)
        
        cliente : Cliente = Cliente(cpf, "", "", 0.0)
        self.repository.delete(cliente)
    
    def atualizar_valor_gasto(self, cpf : str, valor_adicional : float) -> None:
        """Atualiza o valor gasto por um cliente

        Args:
            cpf (str): CPF do cliente
            valor_adicional (float): Valor a ser adicionado ao total gasto

        Raises:
            ValueError: Se o valor adicional for negativo
            ValueError: Se o cliente não for encontrado
        """

        if valor_adicional < 0:
            raise ValueError("Valor adicional não pode ser negativo")
            
        cliente_atual : Cliente = self.buscar_cliente(cpf)
        novo_valor : float = cliente_atual["valor_gasto"] + valor_adicional
        
        self.atualizar_cliente(
            cpf,
            cliente_atual["nome"],
            novo_valor
        )
    
    def is_cpf_valido(self, cpf : str) -> bool:
        """Verifica se um CPF é válido

        Args:
            cpf (str): CPF a ser validado no formato XXX.XXX.XXX-XX

        Returns:
            bool: True se o CPF for válido, False caso contrário
        """
        padrao = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        return bool(padrao.match(cpf))

         