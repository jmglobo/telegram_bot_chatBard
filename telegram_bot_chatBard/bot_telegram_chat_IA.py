# BOT TELEGRAM 

import telebot
from bard_api import chat_Bard_API
from manipulate import lector_txt, fecha, hora
import time
from models import Usuario, Nuevo_Usuario, Registro_Errores
from database import session


# Código BOT
codigo_token = "INTRODUCE AQUÍ EL TOKEN DE TU BOT"

# Mensajes predefinidos
texto_espera_respuesta = "<b>Espera 30 segundos antes de volver a escribir para evitar el rate limit de Google...</b>"


try:

    # Inicialización del bot
    bot = telebot.TeleBot(codigo_token)

    # Chat ID autorizados (se extrae de base de datos)
    chatID_query = session.query(Usuario.id_usuario).all()
    chatID = [result[0] for result in chatID_query]


    # Respuesta TEXTO al usuario con ChatGPT
    @bot.message_handler(content_types=['text'])
    def mensaje_(message):
            try:
                mensaje = message.text
                usuario_chat_id = message.chat.id
                usuario_chat_nombre = message.chat.first_name


                # Mantener conversación con ID autorizado
                if usuario_chat_id in chatID:
                    # Respuesta IA a la consulta 
                    respuesta_autorizado = chat_Bard_API(mensaje,usuario_chat_id)
                    bot.send_message(chat_id=usuario_chat_id,text=respuesta_autorizado)
                    # Respuesta informando de la espera y borrado del mensaje de espera después
                    mensaje_espera = bot.send_message(chat_id=usuario_chat_id,text=texto_espera_respuesta,parse_mode="HTML")
                    time.sleep(30)
                    bot.delete_message(chat_id=usuario_chat_id,message_id=mensaje_espera.id)
                    

                # Mensaje al usuario con ID no autorizado
                elif usuario_chat_id not in chatID:
                    respuesta_no_autorizado = lector_txt("respuesta_no_autorizados.txt")
                    # Tomar nota del usuario (SQL)
                    nuevo_usuario = Nuevo_Usuario(usuario_chat_id,
                                                usuario_chat_nombre,
                                                fecha(),
                                                hora(),
                                                mensaje)
                    session.add(nuevo_usuario) 
                    session.commit() 
                    # Respuesta al usuario no autorizado
                    bot.send_message(chat_id=usuario_chat_id,text=respuesta_no_autorizado)
                    #Dejar de escuchar al usuario no autorizado
                    bot.stop_polling()

            except Exception as e:
                id_usuario_error = usuario_chat_id
                error_modulo = "Telebot"
                mensaje_error = str(e)
                # Registro del error en la base de datos
                guardar_error = Registro_Errores(id_usuario_error,
                                                    error_modulo,
                                                    mensaje_error,
                                                    fecha(),
                                                    hora())
                session.add(guardar_error)
                session.commit()


    # Bucle de escucha infinito (a diferencia de bot.polling() que acaba al cabo de unas horas)
    bot.infinity_polling()

except Exception as error_general:
    id_usuario_error_general = "root"
    error_modulo_general = "main"
    mensaje_error_general = str(error_general)
    # Registro del error en la base de datos
    guardar_error_general = Registro_Errores(id_usuario_error_general,
                                             error_modulo_general,
                                             mensaje_error_general,
                                             fecha(),
                                             hora())
    session.add(guardar_error_general)
    session.commit()

