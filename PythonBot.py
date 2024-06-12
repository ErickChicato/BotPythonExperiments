from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import PyPDF2
from twilio.rest import Client




app = Flask(__name__)

MenuTest = 'C://Users//robo1//OneDrive//Documentos//PythonTestApril//MenuTest.pdf'


def enviar_pdf_whatsapp(sender_number):
    # Envía el mensaje con el archivo PDF adjunto
    message = client.messages.create(
        from_='whatsapp:+',
        body='Aquí tienes el archivo PDF que solicitaste.',
        to='whatsapp:' + sender_number,
        media_url=[MenuTest]  # Especifica la URL del archivo PDF
    )

    print("Mensaje enviado correctamente!")
    print("SID del mensaje:", message.sid)


@app.route("/wa")
def wa_hello():
    return "Hello, World!"


@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    # Fetch the message
    resp = MessagingResponse()
    msg = request.form.get('Body').lower()
    reply = resp.message()
    print("msg-->", msg)

    # Create reply
    if msg == "hola":
        reply.body("Hola soy tu mesero virtual 😊 Elije las siguientes opciones : \n  1) Mostrar el menu 📕 \n 2)Seleccionar el platillo 🥗 \n 3)Total de la cuenta 💸\n")
    elif msg == "1":
        reply.body("Este es el menu  😎")
        # Send the PDF file
        enviar_pdf_whatsapp(request.form.get('From')) #from amazon
        return str(resp)
    elif msg == "2":
        reply.body("Ahora vamos a seleccionar el platillo 😉")
        # Send the PDF file
        with open(MenuTest, 'rb') as file: #should be in the computer
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
                print(text)
        reply.body("Seleciona una letra de todo ")
    elif msg == "3":
        # function to calculate the total
        reply.body("Ahora calculemos el total de la cuenta 💸")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
