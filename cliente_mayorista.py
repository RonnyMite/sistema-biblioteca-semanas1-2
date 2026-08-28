from cliente import Cliente


class ClienteMayorista(Cliente):

    def calcular_descuento(self, monto):
        return monto * 0.15
