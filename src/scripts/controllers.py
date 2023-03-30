from ast import If
from turtle import update
from unicodedata import name
from .query import Query
from flask import request, jsonify, json
from psycopg2.errors import Error as PGError


query_helper = Query()



def datosProducto():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=request.args.copy()
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query = query_helper.buscarProducto(args)
        
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "Consulta exitosa"
    res["status"] = True
    res["codigo"] = 200
    res["obj"]=json.loads(json.dumps(query))

    return res

def crearProducto():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query=query_helper.insertar("productos",Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La prenda ha sido creado exitosamente"
    res["status"] = True
    res["codigo"] = 200
    res["obj"] = json.loads(json.dumps(query))

    return res

def modificarProducto():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query_helper.update("productos",args ,Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "La Prenda ha sido modificado exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res

def eliminarProducto():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=list(request.args.items())
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query_helper.delete("productos",args)

    except PGError as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La Prenda ha sido eliminada exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res


def crudProducto():
    if request.method == "POST":
        return crearProducto()
    elif request.method == "GET":
        return datosProducto()
    elif request.method == "PUT":
        return modificarProducto()
    elif request.method == "DELETE":
        return eliminarProducto()



def datosCategoria():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=list(request.args.items())
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query = query_helper.buscarCategoria("categoria",args)
        
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "Consulta exitosa"
    res["status"] = True
    res["codigo"] = 200
    res["obj"]=json.loads(json.dumps(query))

    return res

def crearCategoria():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query=query_helper.insertar("categoria",Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La categoria ha sido creado exitosamente"
    res["status"] = True
    res["codigo"] = 200
    res["obj"] = json.loads(json.dumps(query))

    return res

def modificarCategoria():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        if not request.json:
            raise Exception("Request con body vacio")
        args=list(request.args.items())
        Data = request.json
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    try:
        query_helper.update("categoria",args ,Data)
        
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    res["msg"] = "La categoria ha sido modificado exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res

def eliminarCategoria():
    res = {"status": False, "codigo": 0, "msg": "", "obj": {}}
    try:
        args=list(request.args.items())
    except Exception as e :
        res["status"]= False
        res["msg"] = f" error {e}"
        return res

    try:
        query_helper.delete("categoria",args)

    except PGError as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    except Exception as e:
        res["status"]= False
        res["msg"] = f" error {e}"
        return res
    
    res["msg"] = "La categoria ha sido eliminada exitosamente"
    res["status"] = True
    res["codigo"] = 200

    return res


def crudCategoria():
    if request.method == "POST":
        return crearCategoria()
    elif request.method == "GET":
        return datosCategoria()
    elif request.method == "PUT":
        return modificarCategoria()
    elif request.method == "DELETE":
        return eliminarCategoria()
