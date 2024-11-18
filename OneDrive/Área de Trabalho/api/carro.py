# Classe para representar um carro
class Carro:
    def __init__(self, modelo, placa):
        """
        Inicializa um carro com modelo e placa.
        """
        self.modelo = modelo
        self.placa = placa

    def __str__(self):
        """
        Retorna a representação textual do carro.
        """
        return f"Modelo: {self.modelo}, Placa: {self.placa}"


# Classe para representar a fila de carros
class AutoLavagem:
    def __init__(self):
        """
        Inicializa uma fila vazia para os carros.
        """
        self.fila = []

    def registrar_entrada(self, modelo, placa):
        """
        Adiciona um carro à fila.
        """
        carro = Carro(modelo, placa)
        self.fila.append(carro)
        print(f"Carro {modelo} com placa {placa} foi registrado na fila.")

    def lavar_carro(self):
        """
        Remove o primeiro carro da fila e o considera lavado.
        """
        if self.fila:
            carro_lavado = self.fila.pop(0)
            print(f"Carro lavado: {carro_lavado}")
        else:
            print("Não há carros na fila para lavar.")

    def imprimir_fila(self):
        """
        Imprime todos os carros atualmente na fila.
        """
        if self.fila:
            print("Fila de carros:")
            for idx, carro in enumerate(self.fila, start=1):
                print(f"{idx}. {carro}")
        else:
            print("A fila está vazia.")


# Funçao principal para gerenciar o menu
def main():
    auto_lavagem = AutoLavagem()

    while True:
        print("\n--- Menu Auto Lavagem ---")
        print("1. Registrar entrada de carro")
        print("2. Lavar próximo carro")
        print("3. Imprimir fila")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            modelo = input("Digite o modelo do carro: ")
            placa = input("Digite a placa do carro: ")
            auto_lavagem.registrar_entrada(modelo, placa)
        elif opcao == "2":
            auto_lavagem.lavar_carro()
        elif opcao == "3":
            auto_lavagem.imprimir_fila()
        elif opcao == "4":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
