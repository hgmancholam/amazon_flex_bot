from multiprocessing import Process
from lib.Firebase import FirebaseManager
from lib.FlexManager import FlexManager
import os
import winsound
import json


class ColasBots:

    def __init__(self) -> None:
        print("Instancia del objeto creada")

    def correrProcesos(self):

        # {'idioma': 'en', 'contrasena': '12345', 'apellido': 'Manchola', 'correo': 'hgmancholam@gmail.com', 'nombre': 'Giovanny', 'telefono': 7143814243, 'id': 'hVZQQ787d2SGWBOkx0rx', 'suscripciones': [{'activo': True, 'fecha_activacion': DatetimeWithNanoseconds(2023, 10, 1, 7, 0, 0, 90000, tzinfo=datetime.timezone.utc), 'settings': {'password': '12345', 'desiredwarehouses': [{'value': 'b7d9db9f-e4d2-4bf1-be2d-bd8caa8ab519', 'nombre': 'Fullerton Metro Center (PFCR) - Retail Delivery'}], 'minblockrate': '100', 'botmode': 'pasivo', 'minpayrateperhour': '25', 'desiredweekdays': {'wed': {'end': '17:00', 'start': '08:00', 'state': True}, 'sun': {'end': '', 'start': '', 'state': False}, 'tue': {'end': '17:00', 'start': '08:00', 'state': True}, 'fri': {'end': '17:00', 'start': '08:00', 'state': True}, 'thu': {'end': '17:00', 'start': '08:00', 'state': True}, 'mon': {'end': '17:00', 'start': '08:00', 'state': True}, 'sat': {'end': '', 'start': '', 'state': False}}, 'arrivalbuffer': '30', 'botstate': True, 'username': 'hgmanchola@gmail.com'}, 'robot': 'flex', 'id': 'UZSXF0j8udOaKbnZrdH1'}]}
        print("Inicio la ejecución de los bots.")
        procesos = []

        firebase = FirebaseManager()
        usuarios = firebase.getUsers()

        print("Usuarios activos: ", len(usuarios))
        print("------ Instanciamos los robots ------")
        for usuario in usuarios:
            try:
                suscripcionActiva = firebase.suscripcionActiva(
                    usuario["id"], usuario["suscripciones"][0]["id"])
                if suscripcionActiva:
                    print("El usuario ", usuario["correo"], " ACTIVO")
                    proceso = Process(target=self.ejecutarBot, args=(usuario,))
                    procesos.append(proceso)
                else:
                    print("El usuario ", usuario["correo"], " INACTIVO")
            except Exception as e:
                print("El usuario ", usuario["correo"], " INACTIVO")

        print("Ejectuar los procesos")
        for proceso in procesos:
            proceso.start()

        print("Esperar los procesos")
        for proceso in procesos:
            proceso.join()

        print("Fin de la ejecución de los procesos")

    def ejecutarBot(self, usuario):
        idusuario = usuario["id"]
        idsuscripcion = usuario["suscripciones"][0]["id"]
        correo = usuario["correo"]
        settings = usuario["suscripciones"][0]["settings"]

        print(os.getpid())
        print(os.getpid(), "ID Usuario: ", idusuario)
        print(os.getpid(), "Usuario: ", correo)
        print(os.getpid(), "IdSuscripcion: ", idsuscripcion)
        flex = FlexManager(settings)

        for n in range(10):
            valor = n * n + n
            print(usuario["id"], " ----> ", valor)
            # winsound.Beep(2500, 100)
            # registro una nueva solicitud
        firebase = FirebaseManager()
        firebase.registraSolicitud(idusuario, idsuscripcion)
