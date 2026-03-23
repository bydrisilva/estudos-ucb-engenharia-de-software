# DESAFIO 2: GERENCIADOR DE FROTA
# Objetivo: Composição de classes e interação entre objetos.

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
        # Lista armazena instâncias da classe Equipamento
        self.inventario = []
        # Dicionário vincula cliente ao valor total gasto
        self.faturamento_por_cliente = {}

    def cadastrar_equipamento(self, equipamento):
        self.inventario.append(equipamento)

    def realizar_locacao(self, nome_cliente, id_equipamento, dias):
        for eq in self.inventario:
            if eq.id_equipamento == id_equipamento and eq.status == "Disponível":
                eq.alugar()
                custo = eq.preco_diaria * dias
                # Incrementa faturamento no dicionário usando .get para evitar KeyError
                self.faturamento_por_cliente[nome_cliente] = self.faturamento_por_cliente.get(nome_cliente, 0) + custo
                return f"Locação concluída: {eq.nome} para {nome_cliente}."
        return "Erro: Equipamento indisponível ou inexistente."

    def equipamentos_disponiveis(self):
        # List comprehension para filtrar nomes por status
        return [eq.nome for eq in self.inventario if eq.status == "Disponível"]

# Teste do sistema
locadora = Locadora()
locadora.cadastrar_equipamento(Equipamento(1, "Notebook", 50.0))
locadora.cadastrar_equipamento(Equipamento(2, "Projetor", 100.0))

print(locadora.realizar_locacao("Adrielle", 1, 5))
print(f"Disponíveis: {locadora.equipamentos_disponiveis()}")
print(f"Faturamento: {locadora.faturamento_por_cliente}")
