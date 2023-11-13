#Ejercicio 3.3.1¶
#Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes,
#la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
#[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"),
#("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
#("Jorge Russo", 15, 958, "Mirasol 218")]
#Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne 
# los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede
# haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada
# domicilio una sola vez.

def obtenerDirecciones(datos_clientes: list):
    """Obtiene una lista con los datos de los clientes y devuelve sus direcciones sin duplicados

    Args:
        datos_clientes (list): los datos del cliente con el siguiente formato:
        [(cliente, día del mes, monto, domicilio del cliente),
        (cliente2, día del mes2, monto2, domicilio del cliente2)]

    Returns:
        set:las direcciones de los clientes
    """
    direcciones = set()
    for dato_cliente in datos_clientes:
        direcciones.add(dato_cliente[3])
    return direcciones

if __name__ == '__main__': 
    print(obtenerDirecciones([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"),
                       ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
                       ("Jorge Russo", 15, 958, "Mirasol 218")]))