
# Método para leer archivo de texto plano
def lector_txt(_ruta_fichero):
    fichero_ruta = _ruta_fichero
    with open(fichero_ruta,"r",encoding="utf-8") as fichero:
        lineas = fichero.readlines()
        fichero_join = "".join(lineas)
        txt = fichero_join
    return txt


# Metodo para dar la fecha actual
def fecha():
    from datetime import datetime 
    dt = datetime.now()
    fecha = str("{:02}/{:02}/{}".format(dt.day,dt.month,dt.year))
    return fecha


# Metodo para dar la hora actual
def hora():
    from datetime import datetime 
    dt = datetime.now()
    hora = str("{:02}:{:02}:{:02}".format(dt.hour,dt.minute,dt.second))
    return hora



   
