from datetime import datetime, timedelta

class Administrador:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def autenticar(self):
        return self.login == 'admin' and self.senha == 'admin'

class Condominio:
    def __init__(self):
        self.moradores = []
        self.visitantes = []
        self.veiculos = []

    def cadastrar_morador(self, nome, apartamento, telefone, documento):
        morador = {
            'nome': nome,
            'apartamento': apartamento,
            'telefone': telefone,
            'documento': documento
        }
        self.moradores.append(morador)
        self.salvar_dados("moradores.txt", self.moradores)

    def cadastrar_visitante(self, nome, apartamento, telefone, data_entrada, data_saida, documento):
        visitante = {
            'nome': nome,
            'apartamento': apartamento,
            'telefone': telefone,
            'data_entrada': data_entrada,
            'data_saida': data_saida,
            'documento': documento
        }
        self.visitantes.append(visitante)
        self.salvar_dados("visitantes.txt", self.visitantes)

    def cadastrar_veiculo(self, placa, apartamento, marca, modelo, documento):
        veiculo = {
            'placa': placa,
            'apartamento': apartamento,
            'marca': marca,
            'modelo': modelo,
            'documento': documento
        }
        self.veiculos.append(veiculo)
        self.salvar_dados("veiculos.txt", self.veiculos)

    def exibir_dados(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                data = file.read()
                if data:
                    print(data)
                else:
                    print("Nenhum dado disponível.")
        except FileNotFoundError:
            print("Nenhum dado disponível.")

    def salvar_dados(self, arquivo, dados):
        with open(arquivo, 'a') as file:
            for item in dados:
                file.write(str(item) + '\n')

    def verificar_prazo_visitante(self):
        now = datetime.now()
        for visitante in self.visitantes:
            data_saida = datetime.strptime(visitante['data_saida'], "%Y-%m-%d")
            if now > data_saida:
                print(f"Visitante {visitante['nome']} com acesso expirado.")
                self.visitantes.remove(visitante)
                self.salvar_dados("visitantes.txt", self.visitantes)

def main():
    condominio = Condominio()

    tentativas = 3
    while tentativas > 0:
        administrador = Administrador(input('Login: '), input('Senha: '))
        if administrador.autenticar():
            print('Autenticado com sucesso!')
            break
        else:
            tentativas -= 1
            print(f'Autenticação falhou! Tentativas restantes: {tentativas}')

    if tentativas == 0:
        print('Número máximo de tentativas atingido. Saindo...')
        return

    while True:
        print('Selecione uma opção:')
        print('1 - Cadastrar morador')
        print('2 - Cadastrar visitante')
        print('3 - Cadastrar veículo')
        print('4 - Exibir moradores')
        print('5 - Exibir visitantes')
        print('6 - Exibir veículos')
        print('7 - Sair')

        opcao = input('Digite o número da opção desejada: ')

        condominio.verificar_prazo_visitante()

        if opcao == '1':
            nome = input('Nome: ')
            apartamento = input('Apartamento: ')
            telefone = input('Telefone: ')
            documento = input('Documento de Identificação: ')
            condominio.cadastrar_morador(nome, apartamento, telefone, documento)
        elif opcao == '2':
            nome = input('Nome: ')
            apartamento = input('Apartamento: ')
            telefone = input('Telefone: ')
            data_entrada = input('Data de entrada: ')
            data_saida = input('Data de saída: ')
            documento = input('Documento de Identificação: ')
            condominio.cadastrar_visitante(nome, apartamento, telefone, data_entrada, data_saida, documento)
        elif opcao == '3':
            placa = input('Placa: ')
            apartamento = input('Apartamento: ')
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            documento = input('Documento de Identificação: ')
            condominio.cadastrar_veiculo(placa, apartamento, marca, modelo, documento)
        elif opcao == '4':
            print('Moradores cadastrados:')
            condominio.exibir_dados("moradores.txt")
        elif opcao == '5':
            print('Visitantes cadastrados:')
            condominio.exibir_dados("visitantes.txt")
        elif opcao == '6':
            print('Veículos cadastrados:')
            condominio.exibir_dados("veiculos.txt")
        elif opcao == '7':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    main()
