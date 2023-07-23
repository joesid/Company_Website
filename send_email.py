import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = 'joesidious@gmail.com'

    with open('sec.txt', 'r') as file:
        password = file.readline()

    receiver = user_name
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
