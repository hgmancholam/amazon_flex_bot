from google.cloud import firestore


FIREBASE_DATABASE_URL = "https://easyflex-402204-default-rtdb.firebaseio.com"
# declarar la ruta a mi archivo firebase_config.json
FIREBASE_CREDENTIALS = "./lib/credentials/firebase_config.json"


class FirebaseManager:
    def __init__(self):
        cred_path = FIREBASE_CREDENTIALS
        database_url = FIREBASE_DATABASE_URL
        self.db = firestore.Client.from_service_account_json(cred_path)

    def getUsers(self):
        usuarios = []
        # Obtener documentos de la colección "usuarios"
        usuarios_ref = self.db.collection("usuarios").get()

        for usuario in usuarios_ref:
            usuario_data = usuario.to_dict()
            usuario_id = usuario.id
            usuario_data['id'] = usuario_id

            # Obtener documentos de la subcolección "suscripciones"
            suscripciones_ref = self.db.collection(
                f"usuarios/{usuario_id}/suscripciones").get()
            suscripciones = []

            for suscripcion in suscripciones_ref:
                suscripcion_data = suscripcion.to_dict()
                suscripcion_data['id'] = suscripcion.id
                if suscripcion_data.get("robot") == "flex" and suscripcion_data.get("activo") == True:
                    suscripcion_id = suscripcion.id
                    pagos = []
                    # Obtener documentos de la subcolección "pagos"
                    pagos_ref = self.db.collection(
                        f"usuarios/{usuario_id}/suscripciones/{suscripcion_id}/pagos").get()
                    for p in pagos_ref:
                        pago_data = p.to_dict()
                        pago_data['id'] = p.id
                        pagos.append(pago_data)

                    # Obtener documentos de la subcolección "descuentos"
                    descuentos = []
                    descuentos_ref = self.db.collection(
                        f"usuarios/{usuario_id}/suscripciones/{suscripcion_id}/descuentos").get()
                    for d in descuentos_ref:
                        descuento_data = d.to_dict()
                        descuento_data['id'] = d.id
                        descuentos.append(descuento_data)

                    suscripcion_data["pagos"] = pagos
                    suscripcion_data["descuentos"] = descuentos
                    suscripciones.append(suscripcion_data)

            usuario_data["suscripciones"] = suscripciones
            usuarios.append(usuario_data)
        return usuarios

    def suscripcionActiva(self, idUsuario, idSuscripcion):
        botEncendido = False
        suscripcionActiva = False
        # print("datos ", idUsuario, idSuscripcion)

        try:
            usuario_doc = self.db.collection(
                "usuarios").document(idUsuario).get()

            if usuario_doc.exists:
                usuario = usuario_doc.to_dict()
                # Hacer algo con el usuario
            else:
                return False

            suscripcion_doc = self.db.collection(
                f"usuarios/{idUsuario}/suscripciones").document(idSuscripcion).get()
            if suscripcion_doc.exists:
                suscripcion = suscripcion_doc.to_dict()
            else:
                return False

            suscripcionActiva = suscripcion["activo"]
            botEncendido = suscripcion["settings"]["botstate"]

            return suscripcionActiva and botEncendido
        except Exception as e:
            return False

    def registraSolicitud(self, idUsuario, idSuscripcion):
        try:
            # Obtener la referencia del documento
            suscripcion_ref = self.db.collection(
                f"usuarios/{idUsuario}/suscripciones").document(idSuscripcion)

            # Obtener la fecha y hora actual del servidor de Firebase
            timestamp = firestore.SERVER_TIMESTAMP

            # Actualizar el campo ultima_consulta con el timestamp
            suscripcion_ref.update({
                "ultima_consulta": timestamp
            })
            return True
        except Exception as e:
            return False
