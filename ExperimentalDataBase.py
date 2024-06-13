import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')

# Crear un cursor
cursor = conn.cursor()

# Crear la tabla 'usuarios' si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')

# Datos a insertar
usuarios = [
    ('Juan', 30),
    ('Ana', 25),
    ('Luis', 35)
]

# Insertar datos en la tabla
cursor.executemany('''
    INSERT INTO usuarios (nombre, edad) VALUES (?, ?)
''', usuarios)

# Confirmar los cambios
conn.commit()

# Seleccionar y mostrar los datos
conn = sqlite3.connect('mi_base_de_datos.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM usuarios')
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()