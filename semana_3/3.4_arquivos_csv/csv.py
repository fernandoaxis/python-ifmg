import csv
from os.path import isfile

def linha():
    print('-' * 50)

class Contato:
    campos = ['Nome', 'Telefone', 'Aniversário']

    def __init__(self, valores):
        self._dic = {}
        for cont, campo in enumerate(self.campos):
            self._dic[campo] = valores[cont]

    def alterar(self):
        linha()
        print('Alteração de contato')
        linha()

        for campo, valor in self._dic.items():
            print(campo + ' (' + valor + ')', sep='')
            novo_valor = input('Novo valor: ').strip()
            if novo_valor != '':
                self._dic[campo] = novo_valor

    def __str__(self):
        lista_cv = [campo + ': ' + self._dic[campo]
                    for campo in self._dic]
        return '\n'.join(lista_cv)

    def __lt__(self, other):
        return tuple(self.valores) < tuple(other.valores)

    @classmethod
    def novo(cls):
        linha()
        print('Novo contato')
        linha()
        lista_valores = []
        for campo in cls.campos:
            valor = input(campo + ': ').strip()
            lista_valores.append(valor)
        if len(lista_valores[0]) == 0:
            print('Contato inválido, o nome é obrigatório!')
            return None
        else:
            return Contato(lista_valores)

    @property
    def valores(self):
        lista_valores = []
        for campo in self.campos:
            lista_valores.append(self._dic[campo])
        return lista_valores

class Arquivo:
    def __init__(self, nome_arquivo):
        self._nome_arquivo = nome_arquivo
        self._lista_contatos = []
        if isfile(self._nome_arquivo):
            with open(self._nome_arquivo) as arq:
                leitor = csv.reader(arq)
                next(leitor)
                for linha in leitor:
                    contato = Contato(linha)
                    self._lista_contatos.append(contato)

    def listar(self):
        if len(self._lista_contatos) == 0:
            print('Nenhum contato cadastrado!')
            linha()
        else:
            self._lista_contatos.sort()
            for cont, contato in enumerate(self._lista_contatos):
                print('Código:', cont)
                print(str(contato))
                linha()

    def buscar(self, codigo):
        if 0 <= codigo < len(self._lista_contatos):
            return self._lista_contatos[codigo]
        return None

    def incluir(self):
        contato = Contato.novo()
        if contato is not None:
            self._lista_contatos.append(contato)

    def excluir(self, codigo):
        if 0 <= codigo < len(self._lista_contatos):
            self._lista_contatos.pop(codigo)

    def salvar(self):
        with open(self._nome_arquivo, 'w') as arq:
            escritor = csv.writer(arq)
            escritor.writerow(Contato.campos)
            for contato in self._lista_contatos:
                escritor.writerow(contato.valores)

class Agenda:
    def __init__(self, nome_arquivo):
        self._arq = Arquivo(nome_arquivo)

    def menu(self):
        linha()
        print('Agenda de contatos')
        linha()
        self._arq.listar()
        print('(I)ncluir | (E)xcluir | (A)lterar | (S)alvar | Sai(r)')
        return input('Informe a opção desejada: ').strip().lower()

    def executar(self):
        while True:
            resp = self.menu()
            if resp == 'i':
                self._arq.incluir()
            elif resp == 'e':
                codigo = int(input('Código do contato: '))
                self._arq.excluir(codigo)
            elif resp == 'a':
                codigo = int(input('Código do contato: '))
                contato = self._arq.buscar(codigo)
                if contato is not None:
                    contato.alterar()
            elif resp == 's':
                self._arq.salvar()
            elif resp == 'r':
                break

if __name__ == '__main__':
    agenda = Agenda('contatos.csv')
    agenda.executar()