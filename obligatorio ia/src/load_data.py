import pandas as pd
import os
from pathlib import Path

EXCEL_PATH = Path("./data/TrabajoFinalPowerBI_v2 (1).xlsx")

def load_dataset():
    ventas = pd.read_excel(EXCEL_PATH, sheet_name="Ventas")
    productos = pd.read_excel(EXCEL_PATH, sheet_name="Productos")
    clientes = pd.read_excel(EXCEL_PATH, sheet_name="Clientes")

    # Unir Productos. Agrega: NombreProducto, Categoria, Precio
    df = ventas.merge(productos, on="IdProducto", how="left")

    # Unir Clientes. Agrega: NombreCliente, Ciudad
    df = df.merge(clientes, on="IdCliente", how="left")

    return df
