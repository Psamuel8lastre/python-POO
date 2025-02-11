class Dispositivos:
    # Método constructor
    def __init__(self, marca, modelo, año):
        # Defino los atributos de instancia de la clase
        self.marca = marca 
        self.modelo = modelo
        self.año = año 
        
        self.capacidadbateria = int(input("Ingrese capacidad de la batería: "))
        
    # Método para mostrar la información del objeto
    def registro(self):
        print("---------------------------->")
        print("Dispositivos registrados")
        print("---------------------------->")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Capacidad de la batería: {self.capacidadbateria} mAh")

        
class Smartphone(Dispositivos):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        
        # Definir el sistema operativo y conectividad
        self.sistemaop = input("Ingrese el sistema operativo: ")
        self.tipoconexion = input("Ingrese el tipo de conectividad: ")
        
    def encender(self):
        self.energia = int(input("Digite el valor de la carga: "))
        
        if self.energia > 0:
            print(f"El celular {self.marca} se puede encender")
            print(f"|||||||||| {self.energia} % de carga")
            print("------------------------->")
        else:
            print(f"El celular {self.marca} no se puede encender")
            
    def apagar(self):
        self.off = input("Desea apagar el celular: (y/n): ")
        
        if self.off.lower() == "y":
            print(f"El celular {self.marca} se apagó correctamente")
        else:
            print("...")

            
# Crear el objeto de la clase Smartphone
objeto_smartphone = Smartphone("Samsung", "S23 Ultra", "2023")
objeto_smartphone.registro()
objeto_smartphone.encender()
objeto_smartphone.apagar()
