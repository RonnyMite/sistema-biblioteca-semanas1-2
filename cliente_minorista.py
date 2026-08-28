from cliente import Cliente


class ClienteMinorista(Cliente):

    def calcular_descuento(self, monto):
        return monto * 0.05
