agenda = {}
while True:
    apodo = input("DIGITE APODO: ")
    if apodo == "":
        break    
    nombre=input("DIGITE NOMBRE: ")
    apellido=input("DIGITE APELLIDO: ")
    telefono=input("DIGITE TELEFONO: ")
    direccion=input("DIGITE DIRECCION: ")
    whatsapp=input("DIGITE CORREO WHATSAPP: ")
    hotmail=input("DIGITE CORREO HOTMAIL: ") 
    gmail=input("DIGITE CORREO GMAIL: ")

    agenda[apodo]={
    "NOMBRE":nombre,
    "APELLIDO":apellido,
    "TELEFONO":telefono,
    "DIRECCION":direccion,
    "WHATSAPP":whatsapp,
    "HOTMAIL":hotmail,
    "GMAIL":gmail
    }

for clave in agenda: #clave is for key, but it can be anything. It will always take the key in this case is apodo
    print(clave)
for valor in agenda.values(): #valor is for value idem up ^. The value in this case is valor
    print(valor)
for clave, valor in agenda.items():
    print(clave,valor) # prints a dictionary for every key
print(agenda)# prints the whole dictionary