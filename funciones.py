import csv


def crea_menu(tipo:str,usuario:str)-> dict:
    ''' Creamos un diccionario para cada usuario dependiendo el tipo (ej. admin) nos regresa el menu con sus respectivos direccionamientos
    '''
    # Creamos el diccionario del cliente
    dusuario = {'Mascotas':f'/mascotas/{usuario}',
                'Clientes':f'/clientes/{usuario}'
            }
    # Creamos el diccionario usuario haciendo una copia del diccionario cliente con 2 valores extra
  #  dusuario = dcliente.copy()
   # dusuario['Receta'] = f'/recetas/{usuario}'
    #dusuario['Procedimiento'] = f'/procedimiento/{usuario}'


    # Creamos el diccionario admin haciendo una copia del diccionario usuario con 2 valores extra
    dadmin = dusuario.copy()
    dadmin['Agregar Usuarios'] = f'/add_user/{usuario}'
    dadmin['Informes'] = f'/informes/{usuario}'

    # Ruteamos cada uno  de los diccionarios
    dmenus = {'usuario':dusuario,
              'admin':dadmin}
              
    # Definimos el diccionario correspondiente
    menu = dmenus[tipo]

    return menu


def lee_diccionario_csv(archivo:str)->list:
    '''Lee un archivo CSV y regresa un diccionario de diccionarios
    '''
    diccionario = {}
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                llave = renglon['nombre_usuario']
                diccionario[llave]=renglon
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return diccionario

def crea_lista_mascotas(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista
    '''
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista

def crea_lista_usuarios(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista
    '''
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista

def crea_lista_clientes(archivo:str)->list:
    '''Lee un archivo CSV y regresa una lista
    '''
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista

def eliminaMascota(propietario:str,nombre:str):
    '''re escribe el csv sin la fila que se elimino'''
    archivo = "mascotas.csv"
    """primero se identifican las filas que se van a quedar"""
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                if(renglon['propietario'] == propietario):
                    if(renglon['nombre'] != nombre):
                        lista.append(renglon)
                else:
                    lista.append(renglon)
           # print(lista)
    except IOError:
        print(f"No se pudo leer el arch]ivo {archivo}")
        """re escribe el archivo"""
    try:
        with open(archivo,'w',encoding='utf-8', newline="") as fl:
            writer = csv.writer(fl)
            writer.writerow(["propietario","nombre","raza","sexo"])
            for renglon in lista:
                mascota =[renglon['propietario'],renglon['nombre'],renglon['raza'],renglon['sexo']]
                writer.writerow(mascota)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")

def Funcion_AgregaMascota(propietario,nombre,raza,sexo):
    archivo = "mascotas.csv"
    lista = []
    #obtiene todas las mascotas que estan en el archivo
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    
    except IOError:
        print(f"No se pudo leer el arch]ivo {archivo}")
        #vuelve a agregar todas las mascotas al archivo y al final la nueva mascota
    try:
        with open(archivo,'w',encoding='utf-8', newline="") as fl:
            writer = csv.writer(fl)
            writer.writerow(["propietario","nombre","raza","sexo"])
            for renglon in lista:
                mascota =[renglon['propietario'],renglon['nombre'],renglon['raza'],renglon['sexo']]
                writer.writerow(mascota)
            writer.writerow([propietario,nombre,raza,sexo])
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")

def agregar_usuario(nombre_usuario, nombre, appat, apmat, correo, tipo_usuario, contraseña):
    archivo = "usuarios.csv"
    lista = []
    #obtiene todas los usuarios que estan en el archivo
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el arch]ivo {archivo}")
        #vuelve a agregar todas los usuarios al archivo y al final el usuario nuevo
    try:
        with open(archivo,'w',encoding='utf-8', newline="") as fl:
            writer = csv.writer(fl)
            writer.writerow(["nombre_usuario", "nombre", "appat", "apmat", "correo", "tipo_usuario", "contraseña"])
            for renglon in lista:
                mascota =[renglon['nombre_usuario'],renglon['nombre'],renglon['appat'],renglon['apmat'],renglon['correo'],renglon['tipo_usuario'],renglon['contraseña']]
                writer.writerow(mascota)
            writer.writerow([nombre_usuario, nombre, appat, apmat, correo, tipo_usuario, contraseña])
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")

def agregar_cliente(nombre, appat, apmat, correo):
    archivo = "clientes.csv"
    lista = []
    #obtiene todas los usuarios que estan en el archivo
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el arch]ivo {archivo}")
        #vuelve a agregar todas los usuarios al archivo y al final el usuario nuevo
    try:
        with open(archivo,'w',encoding='utf-8', newline="") as fl:
            writer = csv.writer(fl)
            writer.writerow(["nombre", "appat", "apmat", "correo"])
            for renglon in lista:
                mascota =[renglon['nombre'],renglon['appat'],renglon['apmat'],renglon['correo']]
                writer.writerow(mascota)
            writer.writerow([nombre, appat, apmat, correo])
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")

def read_file(file:str)->list:
    list= []
    try:
        with open(file,'r',encoding='UTF-8') as fh:
            csv_reader = csv.reader(fh)
            for row in csv_reader:
                list.append(row)
    except IOError:
        print(f"No se pudo leer el archivo {file}")
   
    return list
   
def verify_password_user(password:str,user:str)->bool:
    list = read_file("users.csv")
    flag = False
    for row in list:
        if  password == row[3] and user == row[2]:
            flag = True 
    return flag
#eliminaMascota("elpatoninja","rufus")
