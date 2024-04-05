import pywhatkit

# Lista de números de teléfono
phone_numbers = "+59165132164"

# Fecha y hora a las que se enviará el mensaje
date = "2023-08-01"
hour = 12
minute = 00

# Mensaje a enviar
message = "¡Saludos, miembros de SPE UMSA Chapter! Es ese momento del año para renovar tu compromiso con la excelencia y el desarrollo profesional. ¡No te pierdas los beneficios y oportunidades que te ofrece tu membresía SPE! Renueva hoy y sigue siendo parte de nuestra comunidad apasionada y en crecimiento. ¡Te esperamos!"

# Enviar el mensaje a todos los contactos
# pywhatkit.sendwhatmsg(phone_numbers, message)


# Enviar mensaje instantaneo
pywhatkit.sendwhatmsg_instantly(phone_numbers, message, 10)