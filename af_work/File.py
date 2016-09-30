__author__ = 'Bernardo & Victor'

from Automato import *

class File:

    automato = Automato()
    nomeAFD = '\"AFN\"'

    def __openFile__(self, nameFile):

        try:
            fHand = open(nameFile, 'r')
        except:
            print("Erro: Arquivo nao pode ser aberto")
            quit()

        return fHand


    def __readFile__(self, fHand):

        for line in fHand:
            line = line.strip()

            if(re.search('\.', line)):
                lines = line.split('.')
                for linha in lines:
                    linha = linha + '.'
                    self.automato.__verifySintax__(linha.strip())
            else:
                self.automato.__verifySintax__(line.strip())

        fHand.close()

    def __createDOT__(self, nameFile, automato):

            try:
                fHand = open(nameFile, 'w')
            except:
                print('Erro: Arquivo nao pode ser criado.')
                quit()

            try:
                fHand.write('digraph ' + self.nomeAFD + ' {\n')

                for i in range(int(len(automato.iniciais))):
                    fHand.write('\t_nil' + str(i + 1) + ' [style=\"invis\"];\n')
                    fHand.write('\t_nil' + str(i + 1) + ' -> ' + automato.iniciais[i] + ' [label=\"\"];\n')

                for i in range(int(len(automato.finais))):
                    fHand.write('\t' + automato.finais[i] + ' [peripheries=2];\n')

                for key, value in automato.transicoes.items():
                    for i in range(len(value)):
                        fHand.write('\t' + ''.join(re.findall('[a-zA-Z]+', str(key))) + ' -> ' + value[i] + ' [label=' + ''.join(re.findall('[0-9]+', str(key))) + '];\n')

                fHand.write("}\n")
                fHand.close()
            except:
                print('Error: nao foi possivel escrever no arquivo')
                quit()

    def __createFile__(self, nameFile, automato):

        try:
            fHand = open(nameFile, 'w')
        except:
            print('Erro: Arquivo nao pode ser criado.')
            quit()

        fHand.write('E:')

        for i in range(len(automato.estados)):
            if i == (len(automato.estados) - 1):
                fHand.write(' ' + automato.estados[i])
            else:
                fHand.write(' ' + automato.estados[i] + ',')

        fHand.write('.\n')

        fHand.write('A:')

        for i in range(len(automato.alphabeto)):
            if i == (len(automato.estados) - 1):
                fHand.write(' ' + automato.alphabeto[i])
            else:
                fHand.write(' ' + automato.alphabeto[i] + ',')

        fHand.write('.\n')
        fHand.write('T:\n')

        for key, value in automato.transicoes.items():
            fHand.write('\t' + str(key) + ' := {' + str(value).replace('[', '').replace(']', '').replace('\'', '') + '},\n')

        fHand.write('\tError[0] := {Error},\n\tError[1] := {Error}.\n')

        fHand.write('I:')

        for i in range(len(automato.iniciais)):
            if i == (len(automato.iniciais) - 1):
                fHand.write(' ' + automato.iniciais[i])
            else:
                fHand.write(' ' + automato.iniciais[i] + ',')

        fHand.write('.\n')
        fHand.write('F:')

        for i in range(len(automato.finais)):
            if i == (len(automato.finais) - 1):
                fHand.write(' ' + automato.finais[i])
            else:
                fHand.write(' ' + automato.finais[i] + ',')

        fHand.write('.\n')
