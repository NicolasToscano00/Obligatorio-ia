from typing import List

def row_to_doc(row) -> str:
    cantidad = row.get("Cantidad", 0)
    precio = row.get("Precio", 0)
    total = cantidad * precio

    return (
        f"Venta ID {row.get('IdVenta')}. "
        f"Fecha: {row.get('FechaVenta')}. "
        f"Cliente: {row.get('NombreCliente')} de la ciudad de {row.get('Ciudad')}. "
        f"Producto: {row.get('NombreProducto')} (Categoría: {row.get('Categoria')}). "
        f"Cantidad comprada: {cantidad}. "
        f"Precio unitario: {precio}. "
        f"Total calculado: {total}."
    )

def build_documents(df) -> List[str]:
    return [row_to_doc(r.to_dict()) for _, r in df.iterrows()]
