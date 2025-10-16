#ISP principio de segregacion Hugo Alonso

from abc import ABC, abstractmethod

class imprime_color(ABC):
    @abstractmethod
    def imprimir_color(self, documento):
        pass

class imprime_bn(ABC):
    @abstractmethod
    def imprimir_bn(self, documento):
        pass

class escanear(ABC):
    @abstractmethod
    def escanear(self):
        pass

class fax(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass

class multifuncion(imprime_bn, imprime_color, fax, escanear):

    def imprimir_bn(self, documento):
        print(f"Imprimiendo en blanco y negro: {documento}")

    def imprimir_color(self, documento):
        print(f"Imprimiendo a color: {documento}")

    def escanear(self):
        print("Escaneando documento...")

    def enviar_fax(self, documento):
        print(f"Enviando fax con el documento: {documento}")


class impresora_color(imprime_color):
    def imprimir_color(self, documento):
            print(f"Imprimiendo a color exclusivamente: {documento}")

class impresora_bn(imprime_bn):
    def imprimir_bn(self, documento):
        print(f"Imprimiendo en blanco y negro exclusivamente: {documento}")



def probar_multifuncion():
    impresora = multifuncion()
    impresora.imprimir_bn("Contrato.pdf")
    impresora.imprimir_color("Cartel.png")
    impresora.escanear()
    impresora.enviar_fax("Factura.docx")


def probar_color():
    impresora = impresora_color()
    impresora.imprimir_color("hola.pdf")

def probar_bn():
    impresora = impresora_bn()
    impresora.imprimir_bn("adios.pdf")




probar_multifuncion()
probar_bn()
probar_color()


    