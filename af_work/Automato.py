__author__ = 'Bernardo & Victor'

import re

class Automato:

    estados = None
    alphabeto = None
    transicoes = dict()
    iniciais = None
    finais = None

    instruction = 0;

    def __verifySintax__(self, line):

        if re.search('^E:', line) or self.instruction == 1:

            if not re.search('[.]', line):
                self.instruction = 1
            else:
                self.instruction = 0

            estados = re.findall('^E:([^;.]*)', line)

            if(len(estados) > 0):
                estados[0] = "".join(estados[0].split())
                self.estados = estados[0].split(',')
                #print(self.estados)


        elif re.search('^A:', line) or self.instruction == 2:

            if not re.search('[.]', line):
                self.instruction = 2
            else:
                self.instruction = 0

            alphabeto = re.findall('^A:([^;.]*)', line)

            if(len(alphabeto) > 0):
                alphabeto[0] = "".join(alphabeto[0].split())
                self.alphabeto = alphabeto[0].split(',')
                #print(self.alphabeto)

        elif re.search('^T:', line) or self.instruction == 3:

            if not re.search('[.]', line):
                self.instruction = 3
            else:
                self.instruction = 0

            line = line.strip('\t')
            transicao = re.findall('.:=.([^}]*)', line)
            estado = re.findall('(.*):=', line)

            if(len(transicao) > 0):
                for i in range(len(transicao)):
                    transicao[i] = transicao[i].replace('{', '')
                    transicao[i] = "".join(transicao[0].split())
                    temp = transicao[i].split(',')
                    if(len(estado) == 0):
                        self.transicoes[line[0]+line[1]+line[2]+line[3]] = temp
                    else:
                        self.transicoes[estado[i]] = temp
                    #print(self.transicoes)

        elif re.search('^I:', line) or self.instruction == 4:

            if not re.search('[.]', line):
                self.instruction = 4
            else:
                self.instruction = 0

            iniciais = re.findall('^I:([^;.]*)', line)

            if(len(iniciais) > 0):
                iniciais[0] = "".join(iniciais[0].split())
                self.iniciais = iniciais[0].split(',')
                #print(self.iniciais)

        elif re.search('^F:', line) or self.instruction == 5:

            if not re.search('[.]', line):
                self.instruction = 5
            else:
                self.instruction = 0

            finais = re.findall('^F:([^;.]*)', line)

            if(len(finais) > 0):
                finais[0] = "".join(finais[0].split())
                self.finais = finais[0].split(',')
                #print(self.finais)