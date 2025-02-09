from model.Cliente import Cliente
import json
import os

class ClienteRepository:

    JSON_FILE = '../json/cliente.json'

    @classmethod
    def create(cls, cliente : Cliente) -> None:
        """Cria um novo Cliente

        Args:
            cliente (Cliente): Objeto Cliente
        """
        
        clientes : list = cls.read()
            
        clientes.append({
            "cpf": cliente.get_cpf(),
            "nome": cliente.get_nome(),
            "valor_gasto": cliente.get_valor_gasto()
        })
        
        cls.save(clientes)

    @classmethod
    def read(cls) -> list:
        """Retorna os clientes salvos no arquivo JSON

        Returns:
            list: Lista de objetos Cliente
        """
        os.makedirs('../json', exist_ok=True)
        
        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            cls.save([])
            return []
    
    @classmethod
    def update(cls, cliente : Cliente) -> None:
        """Altera um Cliente com base no CPF

        Args:
            cliente (Cliente): Objeto Cliente com os dados atualizados
        """
        clientes : list = cls.read()
        
        for cli in clientes:
            if cli["cpf"] == cliente.get_cpf():
                cli["nome"] = cliente.get_nome()
                cli["valor_gasto"] = cliente.get_valor_gasto()
                break
        
        cls.save(clientes)
    
    @classmethod
    def delete(cls, cliente : Cliente) -> None:
        """Exclui um Cliente com base no CPF

        Args:
            cliente (Cliente): Objeto Cliente
        """
        clientes : list = cls.read()
        
        clientes = [cli for cli in clientes if cli["cpf"] != cliente.get_cpf()]
        cls.save(clientes)

    @classmethod
    def save(cls, clientes : list) -> None:
        """Faz a persistência do Cliente em arquivo JSON

        Args:
            clientes (list): Lista de Objetos Cliente
        """
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(clientes, arquivo, indent=4)
