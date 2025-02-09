from model.Venda import Venda
import json
import os
from datetime import datetime

class VendaRepository:

    JSON_FILE = '../json/venda.json'

    @classmethod
    def create(cls, venda : Venda) -> None:
        """Cria uma nova Venda

        Args:
            venda (Venda): Objeto Venda
        """
        
        vendas : list = cls.read()
            
        vendas.append({
            "produto": venda.get_produto(),
            "quantidade": venda.get_quantidade(),
            "comprador": venda.get_comprador(),
            "vendedor": venda.get_vendedor(),
            "data": venda.get_data().strftime("%d/%m/%Y %H:%M:%S"),
            "valor": venda.get_valor()
        })
        
        cls.save(vendas)

    @classmethod
    def read(cls) -> list:
        """Retorna as vendas salvas no arquivo JSON

        Returns:
            list: Lista de Objetos Venda
        """
        os.makedirs('../json', exist_ok=True)
        
        try:
            with open(cls.JSON_FILE, 'r') as arquivo:
                vendas = json.load(arquivo)
                for venda in vendas:
                    venda['data'] = datetime.strptime(venda['data'], "%d/%m/%Y %H:%M:%S")
                return vendas
        except FileNotFoundError:
            cls.save([])
            return []

    @classmethod
    def save(cls, vendas : list) -> None:
        """Faz a persistência da Venda em arquivo JSON

        Args:
            vendas (list): Lista de Objetos Venda
        """
        dados_json : list = []

        for vnd in vendas:
            venda : dict = vnd.copy()
            if isinstance(venda['data'], datetime):
                venda['data'] = venda['data'].strftime("%d/%m/%Y %H:%M:%S")
            dados_json.append(venda)
            
        with open(cls.JSON_FILE, 'w') as arquivo:
            json.dump(dados_json, arquivo, indent=4)
