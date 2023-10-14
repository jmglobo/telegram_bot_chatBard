# BOT BARD API

from bardapi import BardCookies
from manipulate import fecha,hora
from models import Registro_Errores,Cookies
from database import session




# Cookie donde se almacena la clave necesaria para hacer funcionar el bot
# Se puede obtener haciendo click derecho sobre la pagina web, en:
# Inspeccionar > Aplicacion > Cookies > __Secure-1PSID

def chat_Bard_API(_prompt=str(),_id_usuario=int()):
    id_usuario = _id_usuario
    __Secure_1PSID = session.query(Cookies.valor).filter(Cookies.nombre=="__Secure-1PSID").all()
    __Secure_1PSIDTS = session.query(Cookies.valor).filter(Cookies.nombre=="__Secure-1PSIDTS").all()
    try:
        cookie_dict = {
        "__Secure-1PSID": [result[0] for result in __Secure_1PSID][0],
        "__Secure-1PSIDTS":[result[0] for result in __Secure_1PSIDTS][0],
        # Cualquier otra cookie que se necesite
        }
        bard = BardCookies(cookie_dict=cookie_dict)
        result = bard.get_answer(_prompt)
        resultado = result["content"]
        return resultado
    
    except Exception as e:
        # Registro del error en la base de datos
        id_usuario_error = id_usuario
        error_modulo = "Bard.API"
        mensaje_error = str(e)
        guardar_error = Registro_Errores(id_usuario_error,
                                         error_modulo,
                                         mensaje_error,
                                         fecha(),
                                         hora())
        session.add(guardar_error)
        session.commit

        # Información al usuario
        respuesta_usuario = """
Has agotado el limite de interacciones que Google da para Bard. Debes esperar para volver a escribir."""
        return respuesta_usuario
