from .connection import Connection
from flask import json
from psycopg2.errors import UniqueViolation


class Query(Connection):

    # --------------- CONSUMO A QUERY DE BASE DE DATOS --------------------

    def buscarProducto(self, datosBuscar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            condition=[]
            for key, value in datosBuscar.items():
                
                if str(value).isnumeric() is True:
                    condition.append(f"productos.{key} = '{value}'")
                else:
                    condition.append(f"productos.{key} like '%{value}%'")
                    
            # query= f"""SELECT * FROM {tabla} {f" WHERE {datosBuscar[0][0]} = '{str(datosBuscar[0][1])} '" if datosBuscar else "" } """
            query= f"""SELECT *, productos.id AS id_producto ,productos.nombre AS nombre_producto FROM productos INNER JOIN categoria ON categoria.id = productos.categoria
                    {f" WHERE {' and '.join(condition)}" if len(condition)>0 else "" }"""
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:

            return "error prueba"

    def buscarCategoria(self, tabla,datosBuscar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""SELECT * FROM {tabla} {f" WHERE {datosBuscar[0][0]} = '{str(datosBuscar[0][1])} '" if datosBuscar else "" } """
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:

            return "error prueba"
    
    def insertar(self, tabla ,datosInsertar):
        cnx = self.connect()
        cursor = cnx.cursor()
        var=list(datosInsertar)
        datos=[]
        for k in datosInsertar:
            datos.append(str(datosInsertar[str(k)]))

        var_text=", ".join(var)
        datos_text="','".join(datos)
 
        try:
            query= f""" INSERT INTO {tabla} ({var_text}) VALUES ('{datos_text}') RETURNING * ;"""
        
            cursor.execute(query)
            cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
           
            return f"error {e}"

    def update(self, tabla,datosBuscar, datoModificar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            for k in datoModificar:
                query= f""" UPDATE {tabla} SET  {  f"{k} = '{str(datoModificar[str(k)])}'"}   WHERE {datosBuscar[0][0]} = {datosBuscar[0][1]} RETURNING * ;"""
            
                cursor.execute(query)
                cnx.commit()
            lista = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
            self.closeConnection(cnx)
            return lista
        except Exception as e:
           
            return f"error {e}"
        
    def delete(self, tabla, datosEliminar):
        cnx = self.connect()
        cursor = cnx.cursor()
        try:
            query= f"""DELETE FROM {tabla} WHERE {datosEliminar[0][0]} = {str(datosEliminar[0][1])} """
        
            cursor.execute(query)
            cnx.commit()
            self.closeConnection(cnx)
            return "Data Eliminada"
        except Exception as e:  
           
            return "error prueba"
    