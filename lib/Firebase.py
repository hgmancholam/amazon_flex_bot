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

            # Obtener documentos de la subcolección "suscripciones"
            suscripciones_ref = self.db.collection(
                f"usuarios/{usuario_id}/suscripciones").get()
            suscripciones = []

            for suscripcion in suscripciones_ref:
                suscripcion_data = suscripcion.to_dict()
                if suscripcion_data.get("robot") == "flex" and suscripcion_data.get("activo") == True:
                    suscripcion_id = suscripcion.id

                    # Obtener documentos de la subcolección "pagos"
                    pagos_ref = self.db.collection(
                        f"usuarios/{usuario_id}/suscripciones/{suscripcion_id}/pagos").get()
                    pagos = [p.to_dict() for p in pagos_ref]

                    # Obtener documentos de la subcolección "descuentos"
                    descuentos_ref = self.db.collection(
                        f"usuarios/{usuario_id}/suscripciones/{suscripcion_id}/descuentos").get()
                    descuentos = [d.to_dict() for d in descuentos_ref]

                    suscripcion_data["pagos"] = pagos
                    suscripcion_data["descuentos"] = descuentos
                    suscripciones.append(suscripcion_data)

            usuario_data["suscripciones"] = suscripciones
            usuarios.append(usuario_data)

        for usuario in usuarios:
            # if usuario.suscripciones[0].get("activo") == True and usuario.suscripciones[0].get("settings").get("state") == True:
            print(usuario)
