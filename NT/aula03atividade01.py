# DESAFIO 2: GERENCIADOR DE FROTA
# Objetivo: Uso de classes, composição e interação entre objetos.

class Equipamento:
    def __init__(self, id_equip, nome, preco_diaria):
        self.id_equipamento = id_equip
        self.nome = nome
        self.preco_diaria = preco_diaria
        self.status = "Disponível"

    def alugar(self):
        self.status = "Alugado"

    def devolver(self):
        self.status = "Disponível"

class Locadora:
    def __init__(self):
        # Lista armazena objetos da classe Equipamento
        self.inventario = []
        # Dicionário vincula cliente ao total gasto
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for eq in self.inventario:
            if eq.id_equipamento == id_equipamento and eq.status == "Disponível":
                eq.alugar()
                custo = eq.preco_diaria * dias
                # Atualiza faturamento do cliente no dicionário
                self.faturamento_por_cliente[nome_cliente] = self.faturamento_por_cliente.get(nome_cliente, 0) + custo
                return f"Locação de {eq.nome} para {nome_cliente} concluída."
        return "Equipamento indisponível ou não encontrado."

    def equipamentos_disponiveis(self):
        # Retorna lista apenas com nomes de itens prontos para uso
        return [eq.nome for eq in self.inventario if eq.status == "Disponível"]

# Execução e Teste
locadora = Locadora()
e1 = Equipamento(1, "Notebook Dell", 50.0)
e2 = Equipamento(2, "Projetor Epson", 80.0)

locadora.cadastrar_equipamento(e1)
locadora.cadastrar_equipamento(e2)

print(locadora.realizar_locacao("Adrielle", 1, 3))
print(f"Disponíveis: {locadora.equipamentos_disponiveis()}")
print(f"Faturamento: {locadora.faturamento_por_cliente}")
