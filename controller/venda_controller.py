from model.Venda import Venda
from model.Produto import Produto
from model.Cliente import Cliente
from model.Funcionario import Funcionario
from repository.venda_repository import VendaRepository
from controller.estoque_controller import EstoqueController
from controller.cliente_controller import ClienteController
from controller.caixa_controller import CaixaController
import datetime

class VendaController:
    def __init__(self) -> None:
        """Inicializa o controlador de Venda
        Cria uma instância do Repository de venda e dos controllers necessários
        """
        self.repository = VendaRepository()
        self.estoque_controller = EstoqueController()
        self.cliente_controller = ClienteController()
        self.caixa_controller = CaixaController()
    
    def realizar_venda(self, produto : Produto, quantidade : int, comprador : Cliente, vendedor : Funcionario) -> None:
        """Registra uma nova venda no sistema

        Args:
            produto (Produto): Produto vendido
            quantidade (int): Quantidade vendida
            comprador (Cliente): Cliente que realizou a compra
            vendedor (Funcionario): Funcionário que realizou a venda

        Raises:
            ValueError: Se algum dos campos obrigatórios estiver vazio
            ValueError: Se a quantidade for menor ou igual a zero
            ValueError: Se não houver quantidade suficiente em estoque
        """
        if not produto or not comprador or not vendedor:
            raise ValueError("Produto, Comprador e Vendedor são obrigatórios")
            
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
            
        if not self.estoque_controller.verificar_disponibilidade(produto, quantidade):
            raise ValueError("Quantidade insuficiente em estoque")
            
        valor_total : float = produto["preco"] * quantidade
        
        nova_venda : Venda = Venda(
            produto,
            quantidade,
            comprador,
            vendedor,
            datetime.datetime.now()
        )

        self.caixa_controller.depositar(valor_total)
        
        self.estoque_controller.baixar_estoque(produto, quantidade)
        
        self.cliente_controller.atualizar_valor_gasto(
            comprador["cpf"],
            valor_total
        )
        
        self.repository.create(nova_venda)
    
    def listar_vendas(self) -> list:
        """Retorna a lista de todas as vendas realizadas

        Returns:
            list: Lista de dicionários contendo os dados das vendas
        """
        return self.repository.read()
    
    def buscar_vendas_por_periodo(self, data_inicio : datetime, data_fim : datetime) -> list:
        """Busca vendas realizadas em um período específico

        Args:
            data_inicio (datetime): Data inicial do período
            data_fim (datetime): Data final do período

        Returns:
            list: Lista de dicionários contendo as vendas do período

        Raises:
            ValueError: Se a data inicial for posterior à data final
        """
        if data_inicio > data_fim:
            raise ValueError("Data inicial não pode ser posterior à data final")
            
        vendas : list = self.repository.read()
        return [vnd for vnd in vendas if data_inicio <= vnd["data"] <= data_fim]
    
    def buscar_vendas_por_cliente(self, cpf_cliente : str) -> list:
        """Busca vendas realizadas para um cliente específico

        Args:
            cpf_cliente (str): CPF do cliente no formato XXX.XXX.XXX-XX

        Returns:
            list: Lista de dicionários contendo as vendas do cliente

        Raises:
            ValueError: Se o CPF não for informado
        """
        if not cpf_cliente:
            raise ValueError("CPF do cliente é obrigatório")
            
        vendas : list = self.repository.read()
        return [vnd for vnd in vendas if vnd["comprador"]["cpf"] == cpf_cliente]
    
    def buscar_vendas_por_vendedor(self, cpf_vendedor : str) -> list:
        """Busca vendas realizadas por um vendedor específico

        Args:
            cpf_vendedor (str): CPF do vendedor no formato XXX.XXX.XXX-XX

        Returns:
            list: Lista de dicionários contendo as vendas do vendedor

        Raises:
            ValueError: Se o CPF não for informado
        """
        if not cpf_vendedor:
            raise ValueError("CPF do vendedor é obrigatório")
            
        vendas : list = self.repository.read()
        return [vnd for vnd in vendas if vnd["vendedor"]["cpf"] == cpf_vendedor]
    
    def buscar_vendas_por_produto(self, nome_produto : str) -> list:
        """Busca vendas de um produto específico

        Args:
            nome_produto (str): Nome do produto

        Returns:
            list: Lista de dicionários contendo as vendas do produto

        Raises:
            ValueError: Se o nome do produto não for informado
        """
        if not nome_produto:
            raise ValueError("Nome do produto é obrigatório")
            
        vendas : list = self.repository.read()
        return [vnd for vnd in vendas if vnd["produto"]["nome"].lower() == nome_produto.lower()]
    
    def calcular_total_vendas_periodo(self, data_inicio : datetime, data_fim : datetime) -> float:
        """Calcula o valor total das vendas em um período

        Args:
            data_inicio (datetime): Data inicial do período
            data_fim (datetime): Data final do período

        Returns:
            float: Valor total das vendas no período
        """
        vendas_periodo : list = self.buscar_vendas_por_periodo(data_inicio, data_fim)
        return sum(venda["valor"] for venda in vendas_periodo)
    
    def calcular_total_vendas_vendedor(self, cpf_vendedor : str) -> float:
        """Calcula o valor total das vendas de um vendedor

        Args:
            cpf_vendedor (str): CPF do vendedor no formato XXX.XXX.XXX-XX

        Returns:
            float: Valor total das vendas do vendedor
        """
        vendas_vendedor : list = self.buscar_vendas_por_vendedor(cpf_vendedor)
        return sum(venda["valor"] for venda in vendas_vendedor)
    
    def gerar_relatorio_vendas_diario(self, data : datetime = None) -> dict:
        """Gera um relatório das vendas de um dia específico

        Args:
            data (datetime, optional): Data para o relatório. Defaults to None (data atual).

        Returns:
            dict: Dicionário contendo:
                - data: Data do relatório (str)
                - total_vendas: Quantidade de vendas realizadas (int)
                - valor_total: Valor total das vendas (float)
                - produtos_vendidos: Dicionário com produtos e suas quantidades/valores
        """
        if not data:
            data = datetime.datetime.now()
            
        inicio_dia : datetime = datetime.datetime(data.year, data.month, data.day)
        fim_dia : datetime = inicio_dia + datetime.timedelta(days=1)
        
        vendas_dia : list = self.buscar_vendas_por_periodo(inicio_dia, fim_dia)
        
        return {
            "data": data.strftime("%d/%m/%Y"),
            "total_vendas": len(vendas_dia),
            "valor_total": sum(venda["valor"] for venda in vendas_dia),
            "produtos_vendidos": self._agrupar_produtos_vendidos(vendas_dia)
        }
    
    def _agrupar_produtos_vendidos(self, vendas : list) -> dict:
        """Agrupa os produtos vendidos por nome, somando quantidades e valores

        Args:
            vendas (list): Lista de vendas a serem agrupadas

        Returns:
            dict: Dicionário com produtos agrupados contendo:
                - quantidade: Quantidade total vendida
                - valor_total: Valor total das vendas
        """
        produtos : dict = {}
        for venda in vendas:
            nome_produto = venda["produto"]["nome"]
            if nome_produto in produtos:
                produtos[nome_produto]["quantidade"] += venda["quantidade"]
                produtos[nome_produto]["valor_total"] += venda["valor"]
            else:
                produtos[nome_produto] = {
                    "quantidade": venda["quantidade"],
                    "valor_total": venda["valor"]
                }
        return produtos