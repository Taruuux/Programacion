from abc import ABC, abstractmethod


class Notificador(ABC):
    @abstractmethod
    def enviar(self, destino: str, mensaje: str) -> None:
        pass


class EmailNotificador(Notificador):
    def enviar(self, destino, mensaje):
        print(f"[EMAIL] a {destino}: {mensaje}")

class PushNotificador(Notificador):
    def enviar(self, destino, mensaje):
        print(f"[PUSH] a {destino}: {mensaje}")

class SMSNotificador(Notificador):
    def enviar(self, destino, mensaje):
        print(f"[SMS] a {destino}: {mensaje}")


class SistemaNotificaciones:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador

    def notificar(self, destino, mensaje):
        self.notificador.enviar(destino, mensaje)


def probar_dip():
    destinos = [("hugo@correo.com", "Hola por email"),
                ("hugo_device", "Hola por push"),
                ("+34123456789", "Hola por SMS")]

    sistema = SistemaNotificaciones(EmailNotificador())
    sistema.notificar(destinos[0][0], destinos[0][1])

    sistema.notificador = PushNotificador()  
    sistema.notificar(destinos[1][0], destinos[1][1])

    sistema.notificador = SMSNotificador()    
    sistema.notificar(destinos[2][0], destinos[2][1])

    print("✅ DIP OK: el sistema funciona cambiando la implementación sin modificar su código.")


if __name__ == "__main__":
    probar_dip()


