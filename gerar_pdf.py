from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Criar PDF de exemplo
nome_arquivo = "relatorio.pdf"

c = canvas.Canvas(nome_arquivo, pagesize=A4)
c.drawString(100, 800, "Relatório Automático Python")
c.drawString(100, 760, "Arquivo está sendo usado como teste desconsidere esse arquivo e use o seu prório")
c.drawString(100, 700, "Enviado com Python ")
c.save()

print(f" Arquivo {nome_arquivo} criado com sucesso!")
