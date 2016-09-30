from File import *
from Transformacao import *
import argparse

__author__ = 'Bernardo & Victor'

def argsparseSetup():

    global AFN_DOT
    AFN_DOT = None
    global AFD_DOT
    AFD_DOT = None
    global CASO_AFN
    CASO_AFN = None
    global CASO_AFD
    CASO_AFD = None

    parser = argparse.ArgumentParser()
	# Se o usuário desejar o arquivo .DOT do AFN
    parser.add_argument("-n", "--afn",
						help="Parâmetro Opcional. Nome do arquivo AFN.DOT.")
	# Se o usuário desejar o arquivo .DOT do AFD
    parser.add_argument("-d", "--afd",
						help="Parâmetro Opcional. Nome do arquivo AFD.DOT.")
    # Arquivo caso.afn
    parser.add_argument("casoAFN",
						help="Parâmetro Obrigatório. Nome do arquivo CASO.AFN")
    # Arquivo caso.afd
    parser.add_argument("casoAFD",
						help="Parâmetro Obrigatório. Nome do arquivo CASO.AFD")
    args = parser.parse_args()

    if args.afn:
    	AFN_DOT = str(args.afn)
    if args.afd:
    	AFD_DOT = str(args.afd)

    # Recebendo o nome do arquivo caso.afn
    CASO_AFN = str(args.casoAFN)
    # Recebendo o nome do arquivo caso.afn
    CASO_AFD = str(args.casoAFD)

def main():

    argsparseSetup()

    file = File()

    fHand = file.__openFile__(CASO_AFN)
    file.__readFile__(fHand)
    if AFN_DOT:
        file.__createDOT__(AFN_DOT, file.automato)

    transfor = Transformacao(file.automato)
    automato = transfor.transformacaoAutomato()
    file.nomeAFD = 'AFD'

    if AFD_DOT:
        file.__createDOT__(AFD_DOT, automato)
    file.__createFile__(CASO_AFD, automato)

main()
