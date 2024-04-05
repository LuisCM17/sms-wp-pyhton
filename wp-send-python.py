import pywhatkit

# Número de teléfono
phone_number = "+59165132164"

# Lista de números de teléfono (añadir)
contacts = []

# Fecha y hora a las que se enviará el mensaje
date = "2024-04-04"
hour = 18
minute = 00

# Mensaje a enviar
message = "¡Saludos, miembros de SPE UMSA Chapter! Es ese momento del año para renovar tu compromiso con la excelencia y el desarrollo profesional. ¡No te pierdas los beneficios y oportunidades que te ofrece tu membresía SPE! Renueva hoy y sigue siendo parte de nuestra comunidad apasionada y en crecimiento. ¡Te esperamos!"
img_to_send = "D://renew_members.jpg"

# Enviar el mensaje 
# pywhatkit.sendwhatmsg(phone_number, message, 15)
pywhatkit.sendwhats_image(phone_number, "../sms-wp-pyhton/renew_benefits.jpg", message, 10, True, 5)


# Enviar mensaje instantaneo
# pywhatkit.sendwhatmsg_instantly(phone_number, message, img_to_send, 10)

# Enviar mensajes masivos

# for contact in contacts:
    # pywhatkit.sendwhatmsg_instantly(contacts, message, 10)