import os
import sys
from datetime import datetime
from simple_term_menu import TerminalMenu

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.categoria_controller import CategoriaController
from controller.produto_controller import ProdutoController
from controller.fornecedor_controller import FornecedorController
from controller.cliente_controller import ClienteController
from controller.funcionario_controller import FuncionarioController
from controller.caixa_controller import CaixaController
from controller.venda_controller import VendaController
from controller.estoque_controller import EstoqueController

def limpar_tela():
    """Limpa a tela do console
    """

    os.system('clear')

def pressionar_enter():
    """Aguarda a tecla ENTER ser pressionada para liberar a interface
    """

    print('\n')
    input('Pressione ENTER para continuar...')

def exibir_logo():
    """Exibe a logo do sistema
    """

    print('███╗   ███╗███████╗██████╗  ██████╗███████╗ █████╗ ██████╗ ██╗ █████╗ ') 
    print('████╗ ████║██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██║██╔══██╗')
    print('██╔████╔██║█████╗  ██████╔╝██║     █████╗  ███████║██████╔╝██║███████║')
    print('██║╚██╔╝██║██╔══╝  ██╔══██╗██║     ██╔══╝  ██╔══██║██╔══██╗██║██╔══██║')
    print('██║ ╚═╝ ██║███████╗██║  ██║╚██████╗███████╗██║  ██║██║  ██║██║██║  ██║')
    print('╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝')
    print('\n                    Sistema de Gerenciamento                      \n')

def menu_principal():
    """Exbibe o menu principal com as funcionalidades do sistema
    """
    while True:
        limpar_tela()
        exibir_logo()

        print('╔════════════════════════════════════╗')
        print('║        MENU PRINCIPAL              ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] 🖥️  Gestão do Sistema           ║')
        print('║ [2] 🔧 Operações e Relatórios      ║')
        print('║ [3] 📖 Guia do Sistema             ║')
        print('║ [0] 🚪 Sair                        ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            menu_gestao_sistema()
        elif user_input == '2':
             menu_operacao_relatorio()
        elif user_input == '3':
             menu_guia_sistema()
        elif user_input == '0':
             break
        else:
             print('\n')
             print('Opção inválida!')
             pressionar_enter()

def menu_gestao_sistema():
    """Fornece o menu de gestão do sistema
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║      🖥️  GESTÃO DO SISTEMA          ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] 🗂️  Categorias                  ║')
        print('║ [2] 📦 Produtos                    ║')
        print('║ [3] 🚚 Fornecedores                ║')
        print('║ [4] 🧑🏻 Clientes                    ║')
        print('║ [5] 💼 Funcionários                ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            menu_categoria()
        elif user_input == '2':
            menu_produto()
        elif user_input == '3':
            menu_fornecedor()
        elif user_input == '4':
            menu_cliente()
        elif user_input == '5':
                menu_funcionario()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()    

def menu_operacao_relatorio():
    """Fornece o menu de operações e relatórios
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║     🔧 OPERAÇÕES E RELATÓRIOS      ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] 💵 Caixa                       ║')
        print('║ [2] 🏬 Estoque                     ║')
        print('║ [3] 🛒 Vendas                      ║')
        print('║ [4] 📊 Relatórios                  ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            menu_caixa()
        elif user_input == '2':
            menu_estoque()
        elif user_input == '3':
            menu_venda()
        elif user_input == '4':
            menu_relatorio()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()    

def menu_categoria():
    """Fornece o menu de gestão de Categorias
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║       🗂️  GESTÃO DE CATEGORIAS      ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Incluir Categoria           ║')
        print('║ [2] 📝 Alterar Categoria           ║')
        print('║ [3] 🗑️  Excluir Categoria           ║')
        print('║ [4] 👁️  Visualizar Categoria        ║')
        print('║ [5] 📜 Listar Categorias           ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            incluir_categoria()
        elif user_input == '2':
            alterar_categoria()
        elif user_input == '3':
            excluir_categoria()
        elif user_input == '4':
            visualizar_categoria()
        elif user_input == '5':
            listar_categorias()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()
        

def menu_produto():
    """Fornece o menu de gestão de Produtos
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║        📦 GESTÃO DE PRODUTOS       ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Incluir Produto             ║')
        print('║ [2] 📝 Alterar Produto             ║')
        print('║ [3] 🗑️  Excluir Produto             ║')
        print('║ [4] 👁️  Visualizar Produto          ║')
        print('║ [5] 📜 Listar Produtos             ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            incluir_produto()
        elif user_input == '2':
            alterar_produto()
        elif user_input == '3':
            excluir_produto()
        elif user_input == '4':
            visualizar_produto()
        elif user_input == '5':
            listar_produtos()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_fornecedor():
    """Fornece o menu de gestão de Fornecedores
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║     🚚 GESTÃO DE FORNECEDORES      ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Incluir Fornecedor          ║')
        print('║ [2] 📝 Alterar Fornecedor          ║')
        print('║ [3] 🗑️  Excluir Fornecedor          ║')
        print('║ [4] 👁️  Visualizar Fornecedor       ║')
        print('║ [5] 📜 Listar Fornecedores         ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            incluir_fornecedor()
        elif user_input == '2':
            alterar_fornecedor()
        elif user_input == '3':
            excluir_fornecedor()
        elif user_input == '4':
            visualizar_fornecedor()
        elif user_input == '5':
            listar_fornecedores()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_cliente():
    """Fornece o menu de gestão de Clientes
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║       🧑🏻 GESTÃO DE CLIENTES        ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Incluir Cliente             ║')
        print('║ [2] 📝 Alterar Cliente             ║')
        print('║ [3] 🗑️  Excluir Cliente             ║')
        print('║ [4] 👁️  Visualizar Cliente          ║')
        print('║ [5] 📜 Listar Clientes             ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            incluir_cliente()
        elif user_input == '2':
            alterar_cliente()
        elif user_input == '3':
            excluir_cliente()
        elif user_input == '4':
            visualizar_cliente()
        elif user_input == '5':
            listar_clientes()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_funcionario():
    """Fornece o menu de gestão de Funcionários
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║     💼 GESTÃO DE FUNCIONÁRIOS      ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Incluir Funcionário         ║')
        print('║ [2] 📝 Alterar Funcionário         ║')
        print('║ [3] 🗑️  Excluir Funcionário         ║')
        print('║ [4] 👁️  Visualizar Funcionário      ║')
        print('║ [5] 📜 Listar Funcionários         ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            incluir_funcionario()
        elif user_input == '2':
            alterar_funcionario()
        elif user_input == '3':
            excluir_funcionario()
        elif user_input == '4':
            visualizar_funcionario()
        elif user_input == '5':
            listar_funcionarios()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_caixa():
    """Fornece o menu de OPerações de Caixa
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║        💵 OPERAÇÕES DE CAIXA       ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] 🔎 Consultar Saldo             ║')
        print('║ [2] 💲 Realizar Depósito           ║')
        print('║ [3] 💸 Realizar Saque              ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            consultar_saldo()
        elif user_input == '2':
            realizar_deposito()
        elif user_input == '3':
            realizar_saque()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_estoque():
    """Fornece o menu de gestão de Estoque
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║        🏬 GESTÃO DE ESTOQUE        ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] ➕ Adicionar Estoque           ║')
        print('║ [2] 👁️  Visualizar Estoque          ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            adicionar_estoque()
        elif user_input == '2':
            visualizar_estoque()
            print()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_venda():
    """Fornece o menu de gestão de Vendas
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════╗')
        print('║        🛒 GESTÃO DE VENDAS         ║')
        print('╠════════════════════════════════════╣')
        print('║ [1] 💲 Realizar Venda              ║')
        print('║ [2] 📜 Listar Vendas               ║')
        print('║ [0] 🔙 Voltar                      ║')
        print('╚════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            realizar_venda()
        elif user_input == '2':
            listar_vendas()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def menu_relatorio():
    """Fornece o menu de geração de Relatórios
    """

    while True:
        limpar_tela()

        print('╔════════════════════════════════════════╗')
        print('║           📊 MENU RELATÓRIOS           ║')
        print('╠════════════════════════════════════════╣')
        print('║ [1] 📜 Relatório Geral                 ║')
        print('║ [2] 📅 Vendas por Período              ║')
        print('║ [3] 📈 Produtos Mais Vendidos          ║')
        print('║ [4] 👥 Clientes Que Mais Compraram     ║')
        print('║ [5] 📋 Relatório Diário                ║')
        print('║ [0] 🔙 Voltar                          ║')
        print('╚════════════════════════════════════════╝')

        user_input : str = str(input('>> '))

        if user_input == '1':
            relatorio_geral()
        elif user_input == '2':
            relatorio_por_periodo()
        elif user_input == '3':
            relatorio_produtos_mais_vendidos()
        elif user_input == '4':
            relatorio_clientes()
        elif user_input == '5':
            relatorio_diario()
        elif user_input == '0':
            break
        else:
            print('\n')
            print('⚠️ Opção inválida!')
            pressionar_enter()

def consultar_saldo():
    """Exibe em tela o saldo disponível no caixa
    """

    caixa_controller = CaixaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        🔎 CONSULTAR SALDO          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        saldo = caixa_controller.get_saldo()
        print('╔════════════════════════════════════╗')
        print(f'  Saldo Atual: R$ {saldo:.2f}')
        print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def realizar_deposito():
    """Faz o depósito em caixa do valor informado pelo usuário
    """

    caixa_controller = CaixaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        💲 REALIZAR DEPÓSITO        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        valor : float = float(input('Valor do depósito: R$ '))
        caixa_controller.depositar(valor)
        print('\n')
        print('✅ Depósito realizado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def realizar_saque():
    """Faz o saque em caixa do valor informado pelo usuário
    """

    caixa_controller = CaixaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        💸 REALIZAR SAQUE           ║')
    print('╚════════════════════════════════════╝\n')

    try:
        valor : float = float(input('Valor do saque: R$ '))
        caixa_controller.sacar(valor)
        print('\n')
        print('✅ Saque realizado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def incluir_categoria():
    """Faz a inclusão de uma nova Categoria no sistema
    """
    categoria_controller = CategoriaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       ➕ INCLUIR CATEGORIA         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        nome : str = input('Nome: ')
        descricao : str = input('Descrição: ')

        categoria_controller.criar_categoria(nome, descricao)
        print('\n')
        print('✅ Categoria cadastrada com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def alterar_categoria():
    """Altera uma Categoria existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    categoria_controller = CategoriaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       📝 ALTERAR CATEGORIA         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        categorias : list = categoria_controller.listar_categorias()
        
        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Selecione a categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        descricao : str = input('Nova descrição: ')

        categoria_controller.atualizar_categoria(categoria["nome"], descricao)
        print('\n')
        print('✅ Categoria alterada com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def excluir_categoria():
    """Exclui uma Categoria existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    categoria_controller = CategoriaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       🗑️  EXCLUIR CATEGORIA         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        categorias = categoria_controller.listar_categorias()
        
        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Selecione a categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        categoria_controller.excluir_categoria(categoria["nome"])
        print('\n')
        print('✅ Categoria excluída com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def visualizar_categoria():
    """Exibe as informações de uma Categoria existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    categoria_controller = CategoriaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      👁️  VISUALIZAR CATEGORIA       ║')
    print('╚════════════════════════════════════╝\n')

    try:
        categorias = categoria_controller.listar_categorias()
        
        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Selecione a categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        print('╔════════════════════════════════════╗')
        print(f'  Nome: {categoria["nome"]}')
        print(f'  Descrição: {categoria["descricao"]}')
        print('╚════════════════════════════════════╝')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_categorias():
    """Lista todas as Categorias cadastradas no sistema
    """

    categoria_controller = CategoriaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       📜 LISTAR CATEGORIAS         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        categorias : list = categoria_controller.listar_categorias()

        for categoria in categorias:
            print('╔════════════════════════════════════╗')
            print(f'  Nome: {categoria["nome"]}')
            print(f'  Descrição: {categoria["descricao"]}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def incluir_produto():
    """Faz a inclusão de um novo Produto no sistema
    """

    categoria_controller = CategoriaController()
    produto_controller = ProdutoController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        ➕ INCLUIR PRODUTO          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        nome : str = str(input('Nome: '))
        preco : float = float(input('Preço: '))
        
        categorias = categoria_controller.listar_categorias()

        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        produto_controller.criar_produto(nome, preco, categoria)
        print(f'Categoria: {categoria["nome"]}')
        print('\n')
        print('✅ Produto cadastrado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def alterar_produto():
    """Altera um Produto existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    categoria_controller = CategoriaController()
    produto_controller = ProdutoController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        📝 ALTERAR PRODUTO          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos = produto_controller.listar_produtos()
        
        menu_produtos = []
        for produto in produtos:
            item = f'{produto["nome"]}'
            menu_produtos.append(item)

        menu = create_terminal_menu(menu_produtos, 'Selecione o produto')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        produto = produtos[index]
        
        preco : float = float(input('Novo preço: '))
        
        categorias = categoria_controller.listar_categorias()

        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Nova Categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        produto_controller.atualizar_produto(produto["nome"], preco, categoria)
        print(f'Nova Categoria: {categoria["nome"]}')
        print('\n')
        print('✅ Produto alterado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def excluir_produto():
    """Exclui um Produto existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    produto_controller = ProdutoController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        🗑️  EXCLUIR PRODUTO          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos = produto_controller.listar_produtos()
        
        menu_produtos = []
        for produto in produtos:
            item = f'{produto["nome"]}'
            menu_produtos.append(item)

        menu = create_terminal_menu(menu_produtos, 'Selecione o produto')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        produto = produtos[index]
        
        produto_controller.excluir_produto(produto["nome"])
        print('\n')
        print('✅ Produto excluído com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def visualizar_produto():
    """Exibe as informações de um Produto existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    produto_controller = ProdutoController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       👁️  VISUALIZAR PRODUTO        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos = produto_controller.listar_produtos()
        
        menu_produtos = []
        for produto in produtos:
            item = f'{produto["nome"]}'
            menu_produtos.append(item)

        menu = create_terminal_menu(menu_produtos, 'Selecione o produto')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        produto = produtos[index]
        
        print('╔════════════════════════════════════╗')
        print(f'  Nome: {produto["nome"]}')
        print(f'  Preço: R$ {produto["preco"]:.2f}')
        print(f'  Categoria: {produto["categoria"]["nome"]}')
        print('╚════════════════════════════════════╝')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_produtos():
    """Lista todos os Produtos cadastrados no sistema
    """

    produto_controller = ProdutoController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        📜 LISTAR PRODUTOS          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos : list = produto_controller.listar_produtos()

        for produto in produtos:
            print('╔════════════════════════════════════╗')
            print(f'  Nome: {produto["nome"]}')
            print(f'  Preço: R$ {produto["preco"]:.2f}')
            print(f'  Categoria: {produto["categoria"]["nome"]}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def incluir_fornecedor():
    """Faz a inclusão de um novo Fornecedor no sistema
    """

    categoria_controller = CategoriaController()
    fornecedor_controller = FornecedorController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      ➕ INCLUIR FORNECEDOR         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        cnpj : str = str(input('CNPJ: '))
        nome : str = str(input('Nome: '))
        
        categorias = categoria_controller.listar_categorias()

        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        fornecedor_controller.criar_fornecedor(cnpj, nome, categoria)
        print(f'Categoria: {categoria["nome"]}')
        print('\n')
        print('✅ Fornecedor cadastrado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def alterar_fornecedor():
    """Altera um Fornecedor existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    categoria_controller = CategoriaController()
    fornecedor_controller = FornecedorController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📝 ALTERAR FORNECEDOR         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        fornecedores = fornecedor_controller.listar_fornecedores()
        
        menu_fornecedores = []
        for fornecedor in fornecedores:
            item = f'{fornecedor["nome"]} (CNPJ: {fornecedor["cnpj"]})'
            menu_fornecedores.append(item)

        menu = create_terminal_menu(menu_fornecedores, 'Selecione o fornecedor')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        fornecedor = fornecedores[index]
        
        nome : str = str(input('Novo nome: '))
        
        categorias = categoria_controller.listar_categorias()

        menu_categorias = []
        for categoria in categorias:
            item = f'{categoria["nome"]}'
            menu_categorias.append(item)

        menu = create_terminal_menu(menu_categorias, 'Nova Categoria')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        categoria = categorias[index]
        
        fornecedor_controller.atualizar_fornecedor(fornecedor["cnpj"], nome, categoria)
        print(f'Nova Categoria: {categoria["nome"]}')
        print('\n')
        print('✅ Fornecedor alterado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def excluir_fornecedor():
    """Exclui um Fornecedor existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    fornecedor_controller = FornecedorController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      🗑️  EXCLUIR FORNECEDOR         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        fornecedores = fornecedor_controller.listar_fornecedores()
        
        menu_fornecedores = []
        for fornecedor in fornecedores:
            item = f'{fornecedor["nome"]} (CNPJ: {fornecedor["cnpj"]})'
            menu_fornecedores.append(item)

        menu = create_terminal_menu(menu_fornecedores, 'Selecione o fornecedor')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        fornecedor = fornecedores[index]
        
        fornecedor_controller.excluir_fornecedor(fornecedor["cnpj"])
        print('\n')
        print('✅ Fornecedor excluído com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def visualizar_fornecedor():
    """Exibe as informações de um Fornecedor existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    fornecedor_controller = FornecedorController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║     👁️  VISUALIZAR FORNECEDOR       ║')
    print('╚════════════════════════════════════╝\n')

    try:
        fornecedores = fornecedor_controller.listar_fornecedores()
        
        menu_fornecedores = []
        for fornecedor in fornecedores:
            item = f'{fornecedor["nome"]} (CNPJ: {fornecedor["cnpj"]})'
            menu_fornecedores.append(item)

        menu = create_terminal_menu(menu_fornecedores, 'Selecione o fornecedor')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        fornecedor = fornecedores[index]
        
        print('╔════════════════════════════════════╗')
        print(f'  CNPJ: {fornecedor["cnpj"]}')
        print(f'  Nome: {fornecedor["nome"]}')
        print(f'  Categoria: {fornecedor["categoria"]["nome"]}')
        print('╚════════════════════════════════════╝')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_fornecedores():
    """Lista todos os Fornecedores cadastrados no sistema
    """

    fornecedor_controller = FornecedorController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📜 LISTAR FORNECEDORES        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        fornecedores : list = fornecedor_controller.listar_fornecedores()

        for fornecedor in fornecedores:
            print('╔════════════════════════════════════╗')
            print(f'  CNPJ: {fornecedor["cnpj"]}')
            print(f'  Nome: {fornecedor["nome"]}')
            print(f'  Categoria: {fornecedor["categoria"]["nome"]}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def incluir_cliente():
    """Faz a inclusão de um novo Cliente no sistema
    """

    cliente_controller = ClienteController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        ➕ INCLUIR CLIENTE          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        cpf : str = str(input('CPF: '))
        nome : str = str(input('Nome: '))
        
        cliente_controller.criar_cliente(cpf, nome)
        print('\n')
        print('✅ Cliente cadastrado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def alterar_cliente():
    """Altera um Cliente existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    cliente_controller = ClienteController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        📝 ALTERAR CLIENTE          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        clientes = cliente_controller.listar_clientes()
        
        menu_clientes = []
        for cliente in clientes:
            item = f'{cliente["nome"]} (CPF: {cliente["cpf"]})'
            menu_clientes.append(item)

        menu = create_terminal_menu(menu_clientes, 'Selecione o cliente')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        cliente = clientes[index]
        
        nome : str = str(input('Novo nome: '))
        valor_gasto = cliente["valor_gasto"]

        cliente_controller.atualizar_cliente(cliente["cpf"], nome, valor_gasto)
        print('\n')
        print('✅ Cliente alterado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def excluir_cliente():
    """Exclui um Cliente existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    cliente_controller = ClienteController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        🗑️  EXCLUIR CLIENTE          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        clientes = cliente_controller.listar_clientes()
        
        menu_clientes = []
        for cliente in clientes:
            item = f'{cliente["nome"]} (CPF: {cliente["cpf"]})'
            menu_clientes.append(item)

        menu = create_terminal_menu(menu_clientes, 'Selecione o cliente')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        cliente = clientes[index]
        
        cliente_controller.excluir_cliente(cliente["cpf"])
        print('\n')
        print('✅ Cliente excluído com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def visualizar_cliente():
    """Exibe as informações de um Cliente existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    cliente_controller = ClienteController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       👁️  VISUALIZAR CLIENTE        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        clientes = cliente_controller.listar_clientes()
        
        menu_clientes = []
        for cliente in clientes:
            item = f'{cliente["nome"]} (CPF: {cliente["cpf"]})'
            menu_clientes.append(item)

        menu = create_terminal_menu(menu_clientes, 'Selecione o cliente')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        cliente = clientes[index]
        
        print('╔════════════════════════════════════╗')
        print(f'  CPF: {cliente["cpf"]}')
        print(f'  Nome: {cliente["nome"]}')
        print(f'  Valor Gasto: R$ {cliente["valor_gasto"]:.2f}')
        print('╚════════════════════════════════════╝')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_clientes():
    """Lista todos os Clientes cadastrados no sistema
    """

    cliente_controller = ClienteController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        📜 LISTAR CLIENTES          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        clientes : list = cliente_controller.listar_clientes()

        for cliente in clientes:
            print('╔════════════════════════════════════╗')
            print(f'  CPF: {cliente["cpf"]}')
            print(f'  Nome: {cliente["nome"]}')
            print(f'  Valor Gasto: R$ {cliente["valor_gasto"]:.2f}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def incluir_funcionario():
    """Faz a inclusão de um novo Funcionário no sistema
    """

    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      ➕ INCLUIR FUNCIONÁRIO        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        cpf : str = str(input('CPF: '))
        nome : str = str(input('Nome: '))
        
        cargos = funcionario_controller.cargos_disponiveis()

        menu = create_terminal_menu(cargos, 'Cargo')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        cargo = cargos[index]
        
        funcionario_controller.criar_funcionario(cpf, nome, cargo)
        print(f'Cargo: {cargo}')
        print('\n')
        print('✅ Funcionário cadastrado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def alterar_funcionario():
    """Altera um Funcionário existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📝 ALTERAR FUNCIONÁRIO        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        funcionarios = funcionario_controller.listar_funcionarios()
        
        menu_funcionarios = []
        for funcionario in funcionarios:
            item = f'{funcionario["nome"]} (CPF: {funcionario["cpf"]})'
            menu_funcionarios.append(item)

        menu = create_terminal_menu(menu_funcionarios, 'Selecione o funcionário')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        funcionario = funcionarios[index]
        
        nome : str = str(input('Novo nome: '))
        
        cargos = funcionario_controller.cargos_disponiveis()

        menu = create_terminal_menu(cargos, 'Novo Cargo')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        cargo = cargos[index]
        
        funcionario_controller.atualizar_funcionario(funcionario["cpf"], nome, cargo)
        print(f'Novo Cargo: {cargo}')
        print('\n')
        print('✅ Funcionário alterado com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def excluir_funcionario():
    """Exclui um Funcionário existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      🗑️  EXCLUIR FUNCIONÁRIO        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        funcionarios = funcionario_controller.listar_funcionarios()
        
        menu_funcionarios = []
        for funcionario in funcionarios:
            item = f'{funcionario["nome"]} (CPF: {funcionario["cpf"]})'
            menu_funcionarios.append(item)

        menu = create_terminal_menu(menu_funcionarios, 'Selecione o funcionário')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        funcionario = funcionarios[index]
        
        funcionario_controller.excluir_funcionario(funcionario["cpf"])
        print('\n')
        print('✅ Funcionário excluído com sucesso.')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')

    pressionar_enter()

def visualizar_funcionario():
    """Exibe as informações de um Funcionário existente no sistema 

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
    """

    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║     👁️  VISUALIZAR FUNCIONÁRIO      ║')
    print('╚════════════════════════════════════╝\n')

    try:
        funcionarios = funcionario_controller.listar_funcionarios()
        
        menu_funcionarios = []
        for funcionario in funcionarios:
            item = f'{funcionario["nome"]} (CPF: {funcionario["cpf"]})'
            menu_funcionarios.append(item)

        menu = create_terminal_menu(menu_funcionarios, 'Selecione o funcionário')

        index = menu.show() 

        if index is None:  
            raise ValueError("Operação cancelada pelo usuário")
            
        funcionario = funcionarios[index]
        
        print('╔════════════════════════════════════╗')
        print(f'  CPF: {funcionario["cpf"]}')
        print(f'  Nome: {funcionario["nome"]}')
        print(f'  Cargo: {funcionario["cargo"]}')
        print('╚════════════════════════════════════╝')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_funcionarios():
    """Lista todos os Funcionários cadastrados no sistema
    """

    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📜 LISTAR FUNCIONÁRIOS        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        funcionarios : list = funcionario_controller.listar_funcionarios()

        for funcionario in funcionarios:
            print('╔════════════════════════════════════╗')
            print(f'  CPF: {funcionario["cpf"]}')
            print(f'  Nome: {funcionario["nome"]}')
            print(f'  Cargo: {funcionario["cargo"]}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def adicionar_estoque():
    """Adiciona um Produto ao Estoque

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
        ValueError: Quantidade deve ser maior que zero
    """

    estoque_controller = EstoqueController()
    produto_controller = ProdutoController()
    fornecedor_controller = FornecedorController()
    caixa_controller = CaixaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      ➕ ADICIONAR ESTOQUE          ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos = produto_controller.listar_produtos()
        
        menu_produtos = []
        for produto in produtos:
            item = f'{produto["nome"]} (R$ {produto["preco"]:.2f})'
            menu_produtos.append(item)

        menu = create_terminal_menu(menu_produtos, 'Selecione o produto')
        index = menu.show()

        if index is None:
            raise ValueError("Operação cancelada pelo usuário")

        produto = produtos[index]
        
        fornecedores = fornecedor_controller.buscar_fornecedores_por_categoria(produto['categoria'])
        menu_fornecedores = []
        for fornecedor in fornecedores:
            item = f'{fornecedor["nome"]} (CNPJ: {fornecedor["cnpj"]})'
            menu_fornecedores.append(item)

        menu = create_terminal_menu(menu_fornecedores, 'Selecione o fornecedor')
        index = menu.show()

        if index is None:
            raise ValueError("Operação cancelada pelo usuário")

        fornecedor = fornecedores[index]

        quantidade : int = int(input('Quantidade: '))
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que zero")

        valor_total = produto['preco'] * quantidade

        if not caixa_controller.verificar_saldo(valor_total):
            raise ValueError("Saldo insuficiente no caixa")

        caixa_controller.sacar(valor_total)
        estoque_controller.adicionar_produto_estoque(produto, quantidade)

        print('✅ Compra realizada com sucesso')
        print()
        print(f'Valor Total: R$ {valor_total:.2f}')
        print(f'Novo Saldo: R$ {caixa_controller.get_saldo():.2f}')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def visualizar_estoque():
    """Exibe todos os Produtos armazenados no estqoue
    """

    estoque_controller = EstoqueController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║       👁️  VISUALIZAR ESTOQUE        ║')
    print('╚════════════════════════════════════╝\n')

    try:
        estoque = estoque_controller.listar_estoque()
        
        for item in estoque:
            print('╔════════════════════════════════════╗')
            print(f'  Produto: {item["produto"]["nome"]}')
            print(f'  Preço: R$ {item["produto"]["preco"]:.2f}')
            print(f'  Quantidade: {item["quantidade"]}')
            print(f'  Categoria: {item["produto"]["categoria"]["nome"]}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def realizar_venda():
    """Realiza um venda no sistema com base em: Produto, quantidade do produto, Cliente e Funcionário

    Raises:
        ValueError: Caso o usuário cancele a operação do Terminal Menu
        ValueError: Não há funcionários de cargo vendedor cadastrado no sistema
    """

    venda_controller = VendaController()
    produto_controller = ProdutoController()
    cliente_controller = ClienteController()
    funcionario_controller = FuncionarioController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        💰 REALIZAR VENDA           ║')
    print('╚════════════════════════════════════╝\n')

    try:
        produtos = produto_controller.listar_produtos()
        menu_produtos = []
        for produto in produtos:
            item = f'{produto["nome"]} (R$ {produto["preco"]:.2f})'
            menu_produtos.append(item)

        menu = create_terminal_menu(menu_produtos, 'Selecione o produto')
        index = menu.show()

        if index is None:
            raise ValueError("Operação cancelada pelo usuário")

        produto = produtos[index]
        
        quantidade : int = int(input('Quantidade: '))
        
        clientes = cliente_controller.listar_clientes()
        menu_clientes = []
        for cliente in clientes:
            item = f'{cliente["nome"]} (CPF: {cliente["cpf"]})'
            menu_clientes.append(item)

        menu = create_terminal_menu(menu_clientes, 'Selecione o cliente')
        index = menu.show()

        if index is None:
            raise ValueError("Operação cancelada pelo usuário")

        cliente = clientes[index]

        funcionarios = funcionario_controller.listar_funcionarios()
        menu_funcionarios = []
        for funcionario in funcionarios:
            if funcionario["cargo"].lower() == "vendedor":
                item = f'{funcionario["nome"]} (CPF: {funcionario["cpf"]})'
                menu_funcionarios.append(item)

        if not menu_funcionarios:
            raise ValueError("Não há funcionários de cargo vendedor cadastrado no sistema")

        menu = create_terminal_menu(menu_funcionarios, 'Selecione o vendedor')
        index = menu.show()

        if index is None:
            raise ValueError("Operação cancelada pelo usuário")

        vendedor = funcionarios[index]

        venda_controller.realizar_venda(produto, quantidade, cliente, vendedor)
        print('✅ Venda realizada com sucesso')
        print()
        print(f'Produto: {produto["nome"]}')
        print(f'Quantidade: {quantidade}')
        print(f'Valor Total: R$ {produto["preco"] * quantidade:.2f}')
        print(f'Cliente: {cliente["nome"]}')
        print(f'Vendedor: {vendedor["nome"]}')

    except ValueError as e:
        print('\n')
        print(f'❌ {e}.')
    
    pressionar_enter()

def listar_vendas():
    """Exibe todas as vendas realizadas no sistema
    """

    venda_controller = VendaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║         📜 LISTAR VENDAS           ║')
    print('╚════════════════════════════════════╝\n')

    try:
        vendas = venda_controller.listar_vendas()

        total_vendas = len(vendas)
        valor_total = sum(venda["valor"] for venda in vendas)
        
        print('╔════════════════════════════════════╗')
        print(f'  Total de Vendas: {total_vendas}')
        print(f'  Valor Total: R$ {valor_total:.2f}')
        print('╚════════════════════════════════════╝\n')

        for venda in vendas:
            print('╔════════════════════════════════════╗')
            print(f'  Produto: {venda["produto"]["nome"]}')
            print(f'  Quantidade: {venda["quantidade"]}')
            print(f'  Valor: R$ {venda["valor"]:.2f}')
            print(f'  Cliente: {venda["comprador"]["nome"]}')
            print(f'  Vendedor: {venda["vendedor"]["nome"]}')
            print(f'  Data: {venda["data"].strftime("%d/%m/%Y %H:%M")}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')

    pressionar_enter()

def relatorio_geral():
    """Exibe o histórico de vendas registradas no sistema

    Raises:
        ValueError: Não há vendas registradas
    """

    venda_controller = VendaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📜 RELATÓRIO GERAL            ║')
    print('╚════════════════════════════════════╝\n')

    try:
        vendas = venda_controller.listar_vendas()
        if not vendas:
            raise ValueError("Não há vendas registradas")

        total_vendas = len(vendas)
        valor_total = sum(venda["valor"] for venda in vendas)
        
        print('╔════════════════════════════════════╗')
        print(f'  Total de Vendas: {total_vendas}')
        print(f'  Valor Total: R$ {valor_total:.2f}')
        print('╚════════════════════════════════════╝\n')

        for venda in vendas:
            print('╔════════════════════════════════════╗')
            print(f'  Produto: {venda["produto"]["nome"]}')
            print(f'  Quantidade: {venda["quantidade"]}')
            print(f'  Valor: R$ {venda["valor"]:.2f}')
            print(f'  Cliente: {venda["comprador"]["nome"]}')
            print(f'  Vendedor: {venda["vendedor"]["nome"]}')
            print(f'  Data: {venda["data"].strftime("%d/%m/%Y %H:%M")}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')
    
    pressionar_enter()

def relatorio_por_periodo():
    """Exibe o histórico de vendas por período registradas no sistema

    Raises:
        ValueError: Nenhuma venda encontrada no período especificado
    """
    venda_controller = VendaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║      📅 VENDAS POR PERÍODO         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        data_inicio = datetime.strptime(input('Data Inicial (dd/mm/aaaa): '), '%d/%m/%Y')
        data_fim = datetime.strptime(input('Data Final (dd/mm/aaaa): '), '%d/%m/%Y')
        
        vendas = venda_controller.buscar_vendas_por_periodo(data_inicio, data_fim)
        if not vendas:
            raise ValueError("Nenhuma venda encontrada no período especificado")
            

        total_vendas = len(vendas)
        valor_total = sum(venda["valor"] for venda in vendas)
        
        print('╔════════════════════════════════════╗')
        print(f'  Período: {data_inicio.strftime("%d/%m/%Y")} a {data_fim.strftime("%d/%m/%Y")}')
        print(f'  Total de Vendas: {total_vendas}')
        print(f'  Valor Total: R$ {valor_total:.2f}')
        print('╚════════════════════════════════════╝\n')

        for venda in vendas:
            print('╔════════════════════════════════════╗')
            print(f'  Produto: {venda["produto"]["nome"]}')
            print(f'  Quantidade: {venda["quantidade"]}')
            print(f'  Valor: R$ {venda["valor"]:.2f}')
            print(f'  Data: {venda["data"].strftime("%d/%m/%Y %H:%M")}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')
    
    pressionar_enter()

def relatorio_produtos_mais_vendidos():
    """Exibe as informações dos Produtos mais vendios em ordem decrescente

    Raises:
        ValueError: Não há vendas registradas
    """

    venda_controller = VendaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║     📈 PRODUTOS MAIS VENDIDOS      ║')
    print('╚════════════════════════════════════╝\n')

    try:
        vendas = venda_controller.listar_vendas()
        if not vendas:
            raise ValueError("Não há vendas registradas")

        produtos_vendidos = {}
        for venda in vendas:
            nome_produto = venda['produto']['nome']
            if nome_produto in produtos_vendidos:
                produtos_vendidos[nome_produto]['quantidade'] += venda['quantidade']
                produtos_vendidos[nome_produto]['valor'] += venda['valor']
            else:
                produtos_vendidos[nome_produto] = {
                    'quantidade': venda['quantidade'],
                    'valor': venda['valor']
                }
        
        produtos_ordenados = sorted(
            produtos_vendidos.items(),
            key=lambda x: x[1]['quantidade'],
            reverse=True
        )
        
        for produto, dados in produtos_ordenados:
            print('╔════════════════════════════════════╗')
            print(f'  Produto: {produto}')
            print(f'  Quantidade Vendida: {dados["quantidade"]}')
            print(f'  Valor Total: R$ {dados["valor"]:.2f}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')
    
    pressionar_enter()

def relatorio_clientes():
    """Exibe as informações dos Clientes que mais compraram em ordem decrescente

    Raises:
        ValueError: Não há vendas registradas
    """

    venda_controller = VendaController()
    limpar_tela()

    print('╔═══════════════════════════════════════════╗')
    print('║       👥 CLIENTES QUE MAIS COMPRARAM      ║')
    print('╚═══════════════════════════════════════════╝\n')

    try:
        vendas = venda_controller.listar_vendas()
        if not vendas:
            raise ValueError("Não há vendas registradas")

        clientes_compras = {}
        for venda in vendas:
            cpf_cliente = venda['comprador']['cpf']
            nome_cliente = venda['comprador']['nome']
            valor_compra = venda['produto']['preco'] * venda['quantidade']
            
            if cpf_cliente in clientes_compras:
                clientes_compras[cpf_cliente]['total'] += valor_compra
                clientes_compras[cpf_cliente]['compras'] += 1
            else:
                clientes_compras[cpf_cliente] = {
                    'nome': nome_cliente,
                    'total': valor_compra,
                    'compras': 1
                }
        
        clientes_ordenados = sorted(
            clientes_compras.items(),
            key=lambda x: x[1]['total'],
            reverse=True
        )
        
        for cpf, dados in clientes_ordenados:
            print('╔════════════════════════════════════╗')
            print(f'  Cliente: {dados["nome"]}')
            print(f'  CPF: {cpf}')
            print(f'  Total de Compras: {dados["compras"]}')
            print(f'  Valor Total: R$ {dados["total"]:.2f}')
            print('╚════════════════════════════════════╝')
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')
    
    pressionar_enter()

def relatorio_diario():
    """Exibe todas as vendas realizadas no dia atual

    Raises:
        ValueError: Não há vendas no dia de hoje
    """
    venda_controller = VendaController()
    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║        📋 RELATÓRIO DIÁRIO         ║')
    print('╚════════════════════════════════════╝\n')

    try:
        data = datetime.now()
        relatorio = venda_controller.gerar_relatorio_vendas_diario(data)
        
        print('╔════════════════════════════════════╗')
        print(f'  Data: {relatorio["data"]}')
        print(f'  Total de Vendas: {relatorio["total_vendas"]}')
        print(f'  Valor Total: R$ {relatorio["valor_total"]:.2f}')
        print('╚════════════════════════════════════╝')
        
        if relatorio['produtos_vendidos']:
            print('\nProdutos Vendidos:')
            for produto, dados in relatorio['produtos_vendidos'].items():
                print('╔════════════════════════════════════╗')
                print(f'  Produto: {produto}')
                print(f'  Quantidade: {dados["quantidade"]}')
                print(f'  Valor Total: R$ {dados["valor_total"]:.2f}')
                print('╚════════════════════════════════════╝')
        else:
            raise ValueError("Não há vendas no dia de hoje")
    except ValueError as e:
        print('\n')
        print(f'❌ {e}')
    
    pressionar_enter()

def menu_guia_sistema():
    """Exibe o menu com um guia e dicas de utilização do sistema
    """

    limpar_tela()

    print('╔════════════════════════════════════╗')
    print('║         📖 GUIA DO SISTEMA         ║')
    print('╚════════════════════════════════════╝\n')

    print('📌 VISÃO GERAL')
    print('O sistema de gerenciamento de Mercearía possui três menus principais:')
    print('• Gestão do Sistema: Gerenciamento e manutenção de cadastros')
    print('• Operações e Relatórios: Manutenção do estoque, controle de vendas e geração de relatórios')
    print('• Guia do Sistema: Manual de referência para navegação e uso eficiente do sistema.\n')

    print('🖥️  GESTÃO DO SISTEMA')
    print('Neste menu você pode gerenciar:')
    print('• Categorias: Manutenção')
    print('• Produtos: Itens disponíveis para venda')
    print('• Fornecedores: Empresas que fornecem produtos')
    print('• Clientes: Cadastro dos compradores')
    print('• Funcionários: Equipe de trabalho\n')

    print('🔧 OPERAÇÕES E RELATÓRIOS')
    print('Aqui você encontra:')
    print('• Caixa: Controle financeiro (consultas, depósitos e saques)')
    print('• Estoque: Gestão de produtos (entrada e consulta)')
    print('• Vendas: Registro de vendas e histórico')
    print('• Relatórios: Análises (geral, período, produtos, clientes & diária)\n')

    print('💡 DICAS DE NAVEGAÇÃO')
    print('• Use as teclas numéricas para selecionar as opções dos menus')
    print('• Em listas de seleção, use ↑↓ para navegar')
    print('• Pressione Enter para confirmar uma seleção')
    print('• Pressione ESC para cancelar uma operação')
    print('• Digite 0 para voltar ao menu anterior\n')

    print('⚠️  OBSERVAÇÕES IMPORTANTES')
    print('• Antes de cadastrar produtos, certifique-se de registrar suas categorias')
    print('• Fornecedores devem estar vinculados às categorias correspondentes')
    print('• O saldo do caixa deve estar positivo para permitir a entrada de novos produtos no estoque')
    print('• Apenas funcionários com o cargo "vendedor" podem registrar vendas no sistema')
    print('• Sempre verifique o estoque antes de confirmar uma venda, evitando indisponibilidades\n')

    print('╔══════════════════════════════════════════╗')
    print('║    Desenvolvido por: André Davi Lopes    ║')
    print('║                                          ║')
    print('║  © Copyright 2025 - All Rights Reserved  ║')
    print('╚══════════════════════════════════════════╝\n')

    pressionar_enter()

def create_terminal_menu(itens : list, titulo : str) -> TerminalMenu:
    """Cria um Terninal Menu onde é possível selecionar um item com base em uma navegação intuitiva com o teclado

    Args:
        itens (list): Contexto dos itens a serem exibidos no menu
        titulo (str): Título do menu

    Returns:
        TerminalMenu: Retorna o menu com as opções para serem selecionadas pelo usuário
    """

    return TerminalMenu(
            menu_entries=itens,
            title=f'{titulo}: ',
            menu_cursor=">> ",
            menu_cursor_style=("fg_green", "bold"),
            menu_highlight_style=("bg_green", "fg_black"),
            show_search_hint=True,
            status_bar="↑↓: Navegar | Enter: Selecionar | ESC: Cancelar",
            status_bar_style=("fg_yellow", "bold"),
        )

try:
    menu_principal()
except Exception as e:
        print(f'❌ {e}')