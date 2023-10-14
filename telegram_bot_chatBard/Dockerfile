#DOCKERFILE bot_telegram_chat_IA


FROM python:latest

WORKDIR /usr/src/app

# Necesario al tener que poner en marcha un programa con configuración horaria
ENV TZ=Europe/Madrid

COPY \
    bard_api.py \
    bot_telegram_chat_IA.py \
    database.py \
    manipulate.py \
    models.py \
    requirements.txt \
    respuesta_no_autorizados.txt ./

LABEL \ 
    name="bot_telegram_chat_IA" \ 
    version="1.0"

RUN apt-get update && apt-get install -y sqlite3
RUN apt-get update && apt-get install -y tzdata
RUN pip install -r requirements.txt

CMD ["python", "bot_telegram_chat_IA.py"]

