import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

smtp_server = "smtp.gmail.com"
smtp_port = 465 # SSL
email_origem = os.getenv("EMAIL_ORIGEM")
email_destino = os.getenv("EMAIL_DESTINO")
senha = os.getenv("EMAIL_SENHA")


# Criar a mensagem
msg = MIMEMultipart()
msg["From"] = email_origem
msg["To"] = email_destino
msg["Subject"] = " Relatório Automático - Python"

# Corpo em HTML
corpo_html = """
<html>
  <body>
    <h2 style="color:blue;">Relatório Automático</h2>
    <p>Olá,</p>
    <p>Segue em anexo o relatório solicitado.</p>
    <p><b>Enviado automaticamente com Python </b></p>
  </body>
</html>
"""
msg.attach(MIMEText(corpo_html, "html"))

# Anexo
caminho_arquivo = "relatorio.pdf"

if os.path.exists(caminho_arquivo):
    with open(caminho_arquivo, "rb") as anexo:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(caminho_arquivo)}"
        )
        msg.attach(parte)
else:
    print(" Aviso: Arquivo de anexo não encontrado, enviando sem anexo.")

# Enviar e-mail via SSL
try:
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as servidor:
        servidor.login(email_origem, senha)
        servidor.sendmail(email_origem, email_destino, msg.as_string())
    print("E-mail enviado com sucesso via SSL!")
except smtplib.SMTPAuthenticationError:
    print("Falha de autenticação. Verifique se está usando a senha de app correta.")
except Exception as e:
    print("Erro ao enviar e-mail:", e)
