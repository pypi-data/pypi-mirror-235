import io,os,shutil

class Archivo:
    def __init__(self, nombre_archivo):  # Constructor
        self.nombre_archivo = nombre_archivo

    def leer(self, nombre_archivo):
        try: 
            with open(self.nombre_archivo, "r") as archivo:
                texto=archivo.read() # almacenar la primera linea del archivo
                return texto #retorno de la funcion (esta devuelve una variales en este caso la variable  )
        except  IOError as e:
            print("error al leer al archivo:" ,str(e) )

    def escribir(self, texto):
        try:
            with open(self.nombre_archivo, "w") as archivo:
                archivo.write(texto)
        except IOError as e:
            print("Error al escribir en el archivo:", str(e)) 
            
    #función de crear archivo 
    def crearArchivo(self, nombre_archivo):
        try:
            with open(self.nombre_archivo, "x") as archivo: 
                #imprimimos el aviso que se creo el archivo correctamente :)  
                print("Archivo creado exitosamente en la ruta ", str(self.nombre_archivo)  )
        except IOError as e: 
            print("error al crear el archivo:", str(e))
    
    def eliminarArchivo(self,nombre_archivo):
        if os.path.exists(self.nombre_archivo):
            os.remove(self.nombre_archivo)
            print("el archivo se a eliminado ", str(self.nombre_archivo))
        else:
            print("el archivo no existe")
           
    def copiarArchivo(self,nombre_archivo,destino):
        if os.path.exists(self.nombre_archivo):
            shutil.copy(self.nombre_archivo,destino)
            print("el archivo se copiado")
        else: 
            print("el archivo no existe") 
                
    def moverArchivo(self,nombre_archivo,destino):
            if os.path.exists(self.nombre_archivo):
                shutil.move(self.nombre_archivo,destino)
                print("el archivo se a movido exitosamente")
            else: 
                print("el archivo no existe")         
