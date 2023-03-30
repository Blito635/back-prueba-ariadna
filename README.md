# servicios

## Prueba Ariadna
```
# Servicios creados con flask
Pablo A. Galvis. S 
```

## Primeros comandos

```powershell
# Crear entorno
$ virtualenv .venv
# O
$ python -m venv .venv

# Activar entorno
$ .\.venv\Scripts\activate

# Instalar dependencias en el entorno
$ pip install -r .\requirements.txt
```

## Ejecutar aplicacion

```powershell
$ python .\application.py
```

## Tablas base de datos

-- Create tables
CREATE TABLE IF NOT EXISTS Productos
(
    id SERIAL NOT NULL,
    fecha_creacion DATE,
    nombre VARCHAR(20),
    categoria BIGINT,
    precio BIGINT,
    valor BIGINT,
    stock INTEGER,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS Categoria
(
    id BIGINT NOT NULL,
    nombre VARCHAR(20),
    descripcion VARCHAR(50),
    PRIMARY KEY(id)
);


-- Create FKs
ALTER TABLE Productos
    ADD    FOREIGN KEY (categoria)
    REFERENCES Categoria(id)
    MATCH SIMPLE
;
    