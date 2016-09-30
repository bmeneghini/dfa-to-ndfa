__author__ = 'Bernardo & Victor'

from Automato import *
import re

class Transformacao:

    automato = Automato()
    automatoNovo = Automato()
    grupos = dict()
    minimizados = []

    def __init__(self, automato):
        self.automato = automato
        self.automatoNovo.finais = []
        self.automatoNovo.estados = []
        self.automatoNovo.transicoes = dict()
        self.automatoNovo.iniciais = []
        self.automatoNovo.alphabeto = []

    def transformacaoAutomato(self):

        inicial = ''

        for i in range(int(len(self.automato.iniciais))):
            inicial = inicial + self.automato.iniciais[i]

        self.automatoNovo.iniciais.append(inicial)
        self.automatoNovo.estados.append(inicial)
        self.transicao(inicial)
        self.automatoNovo.alphabeto = self.automato.alphabeto

        for i in range(len(self.automatoNovo.estados)):
            for j in range(len(self.automato.finais)):
                if re.search(self.automato.finais[j], self.automatoNovo.estados[i]):
                    if not self.automatoNovo.estados[i] is 'Error':
                        if not str(self.automatoNovo.estados[i]) in self.automatoNovo.finais:
                            self.automatoNovo.finais.append(self.automatoNovo.estados[i])

        return self.automatoNovo


    def transicao(self, inicial):

        estado = ''
        transicao  = ''

        alfabeto = -1

        for key, value in self.automato.transicoes.items():
            for i in range(len(value)):
                for j in range(len(inicial)):
                    if str(inicial)[j] in str(key)[0]:
                        if int(str(key)[2]) == 0:
                            if not str(inicial)[j] in estado:
                                estado = estado + str(inicial)[j]
                            alfabeto = 0
                            temp = value[i].split(',')

                            for k in range(len(temp)):
                                transicao = transicao + temp[k]

        if alfabeto != -1:
            estado = ''.join(sorted(estado))
            inicial = ''.join(sorted(inicial))
            transicao = ''.join(sorted(transicao))
            list = []
            list.append(transicao)
            self.automatoNovo.transicoes[inicial + '[' + str(alfabeto) + ']'] = list
            if not str(transicao) in self.automatoNovo.estados:
                self.automatoNovo.estados.append(transicao)
            if not str(transicao + '[' + str(alfabeto) + ']') in self.automatoNovo.transicoes:
                self.transicao(transicao)
        else:
            alfabeto = 0
            list = []
            list.append('Error')
            self.automatoNovo.transicoes[inicial + '[' + str(alfabeto) + ']'] = list
            if not any('Error' in s for s in self.automatoNovo.estados):
                self.automatoNovo.estados.append('Error')

        estado = ''
        transicao  = ''

        alfabeto = -1

        for key, value in self.automato.transicoes.items():
            for i in range(len(value)):
                for j in range(len(inicial)):
                    if str(inicial)[j] in str(key)[0]:
                        if int(str(key)[2]) == 1:
                            if not str(inicial)[j] in estado:
                                estado = estado + str(inicial)[j]
                            alfabeto = 1
                            temp = value[i].split(',')

                            for k in range(len(temp)):
                                transicao = transicao + temp[k]

        if alfabeto != -1:
            estado = ''.join(sorted(estado))
            inicial = ''.join(sorted(inicial))
            transicao = ''.join(sorted(transicao))
            list = []
            list.append(transicao)
            self.automatoNovo.transicoes[inicial + '[' + str(alfabeto) + ']'] = list
            if not str(transicao) in self.automatoNovo.estados:
                self.automatoNovo.estados.append(transicao)
            if not str(transicao + '[' + str(alfabeto) + ']') in self.automatoNovo.transicoes:
                self.transicao(transicao)
        else:
            alfabeto = 1
            list = []
            list.append('Error')
            self.automatoNovo.transicoes[inicial + '[' + str(alfabeto) + ']'] = list
            if not any('Error' in s for s in self.automatoNovo.estados):
                self.automatoNovo.estados.append('Error')