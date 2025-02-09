from model.Funcionario import Funcionario
from repository.funcionario_repository import FuncionarioRepository
import re

class FuncionarioController:
    def __init__(self) -> None:
        """Inicializa o controlador de Funcionário
        Cria uma instância do Repository de funcionário e define os cargos válidos
        """
        self.repository = FuncionarioRepository()
        self.cargos_validos = [
            'Açougueiro',
            'Atendente de Hortifruti',
            'Auxiliar de Estoque',
            'Auxiliar de Limpeza',
            'Caixa',
            'Confeiteiro',
            'Gerente',
            'Padeiro',
            'Repositor',
            'Supervisor',
            'Vendedor'
        ]
    
    def criar_funcionario(self, cpf : str, nome : str, cargo : str) -> None:
        """Adiciona um novo funcionário ao sistema

        Args:
            cpf (str): CPF do funcionário no formato XXX.XXX.XXX-XX
            nome (str): Nome do funcionário
            cargo (str): Cargo do funcionário

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o CPF for inválido
            ValueError: Se o cargo não for válido
            ValueError: Se já existir um funcionário com este CPF
        """
        if not cpf or not nome or not cargo:
            raise ValueError("CPF, nome e cargo são obrigatórios")
        
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        if not self.is_cargo_valido(cargo):
            raise ValueError(f"Cargo inválido. Cargos permitidos: {', '.join(self.cargos_validos)}")
            
        funcionarios : list = self.listar_funcionarios()
        if any(fun["cpf"] == cpf for fun in funcionarios):
            raise ValueError("Já existe um funcionário com este CPF")
            
        novo_funcionario : Funcionario = Funcionario(cpf, nome, cargo)
        self.repository.create(novo_funcionario)
    
    def listar_funcionarios(self) -> list:
        """Retorna a lista de todos os funcionários cadastrados

        Returns:
            list: Lista de dicionários contendo os dados dos funcionários
        """
        return self.repository.read()
    
    def buscar_funcionario(self, cpf : str) -> dict:
        """Busca um funcionário pelo CPF

        Args:
            cpf (str): CPF do funcionário no formato XXX.XXX.XXX-XX

        Returns:
            dict: Dicionário com os dados do funcionário

        Raises:
            ValueError: Se o CPF for inválido
            ValueError: Se o funcionário não for encontrado
        """
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        funcionarios : list = self.repository.read()
        for funcionario in funcionarios:
            if funcionario["cpf"] == cpf:
                return funcionario
        raise ValueError("Funcionário não encontrado")
    
    def buscar_funcionarios_por_cargo(self, cargo : str) -> list:
        """Busca todos os funcionários de um determinado cargo

        Args:
            cargo (str): Cargo para filtrar os funcionários

        Returns:
            list: Lista de dicionários contendo os funcionários do cargo

        Raises:
            ValueError: Se o cargo não for válido
        """
        if not self.is_cargo_valido(cargo):
            raise ValueError(f"Cargo inválido. Cargos permitidos: {', '.join(self.cargos_validos)}")
            
        funcionarios = self.repository.read()
        return [fun for fun in funcionarios if fun["cargo"].lower() == cargo.lower()]
    
    def atualizar_funcionario(self, cpf : str, nome : str, cargo : str) -> None:
        """Atualiza os dados de um funcionário existente

        Args:
            cpf (str): CPF do funcionário no formato XXX.XXX.XXX-XX
            nome (str): Novo nome do funcionário
            cargo (str): Novo cargo do funcionário

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se o CPF for inválido
            ValueError: Se o cargo não for válido
            ValueError: Se o funcionário não for encontrado
        """
        if not cpf or not nome or not cargo:
            raise ValueError("CPF, nome e cargo são obrigatórios")
            
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        if not self.is_cargo_valido(cargo):
            raise ValueError(f"Cargo inválido. Cargos permitidos: {', '.join(self.cargos_validos)}")
            
        self.buscar_funcionario(cpf)
        
        funcionario_atualizado : Funcionario = Funcionario(cpf, nome, cargo)
        self.repository.update(funcionario_atualizado)
    
    def excluir_funcionario(self, cpf : str) -> None:
        """Remove um funcionário do sistema

        Args:
            cpf (str): CPF do funcionário no formato XXX.XXX.XXX-XX

        Raises:
            ValueError: Se o CPF não for informado
            ValueError: Se o CPF for inválido
            ValueError: Se o funcionário não for encontrado
        """
        if not cpf:
            raise ValueError("CPF é obrigatório")
            
        if not self.is_cpf_valido(cpf):
            raise ValueError("CPF inválido")
            
        self.buscar_funcionario(cpf)
        
        funcionario : Funcionario = Funcionario(cpf, "", "")
        self.repository.delete(funcionario)
    
    def is_cargo_valido(self, cargo : str) -> bool:
        """Verifica se um cargo é válido no sistema

        Args:
            cargo (str): Cargo a ser verificado

        Returns:
            bool: True se o cargo for válido, False caso contrário
        """
        return cargo in self.cargos_validos

    def cargos_disponiveis(self) -> list:
        """Retorna a lista de cargos válidos no sistema

        Returns:
            list: Lista contendo todos os cargos válidos
        """
        return self.cargos_validos
    
    def is_cpf_valido(self, cpf : str) -> bool:
        """Verifica se um CPF está em formato válido

        Args:
            cpf (str): CPF a ser validado no formato XXX.XXX.XXX-XX

        Returns:
            bool: True se o CPF estiver em formato válido, False caso contrário
        """
        padrao = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        return bool(padrao.match(cpf))