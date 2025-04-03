from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Crear documento PDF
pdf = SimpleDocTemplate("ejemplo.pdf", pagesize=A4)

# Definir estilos de texto
styles = getSampleStyleSheet()
parrafo = Paragraph("Este es un reporte con una tabla:", styles["Normal"])

# Crear datos de la tabla
data = [["Nombre", "Edad"], ["Alice", 25], ["Bob", 30]]

# Crear tabla
tabla = Table(data)

# Aplicar estilo a la tabla
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
tabla.setStyle(style)

# Agregar elementos al PDF
pdf.build([parrafo, tabla])

print("PDF generado exitosamente 🎉")