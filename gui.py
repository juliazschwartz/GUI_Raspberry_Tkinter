from pathlib import Path 
import serial  #adicionamos esse import para permitir a comunicação com o leitor RFID via USB serial

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Downloads\figmas\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_escape(event=None):

    print("escaped")

    window.destroy()

window = Tk()

window.geometry("716x490")
window.configure(bg = "#FFFFFF")

window.bind("<Escape>", on_escape)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 490,
    width = 716,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    272.0,
    0.0,
    716.0,
    490.0,
    fill="#F5F5F5",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    272.0,
    490.0,
    fill="#000000",
    outline="")

canvas.create_text(
    298.0,
    29.0,
    anchor="nw",
    text="Access Control  Application",
    fill="#515156",
    font=("Inter Bold", 25 * -1)
)

canvas.create_text(
    300.0,
    62.0,
    anchor="nw",
    text="Quarta, 01 Maio, 2024, 13:09 ",
    fill="#A2A2A2",
    font=("Inter", 14 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    67.0,
    285.0,
    image=image_image_1
)

canvas.create_text(
    91.0,
    347.0,
    anchor="nw",
    text="Settings",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    112.0,
    226.0,
    image=image_image_2
)

canvas.create_text(
    89.0,
    273.0,
    anchor="nw",
    text="Past Records",
    fill="#FFFFFF",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    55.0,
    325.0,
    232.0,
    326.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    129.0,
    61.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    122.9100341796875,
    166.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    68.0,
    360.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    485.0,
    239.0,
    image=image_image_6
)

number =canvas.create_text(
    358.0,
    156.0,
    anchor="nw",
    text="90020034530",
    fill="#646474",
    font=("Inter Medium", 18 * -1)
)
print(number)

name = canvas.create_text(
    356.0,
    199.0,
    anchor="nw",
    text="Júlia Z. Schwartz",
    fill="#01150C",
    font=("Inter Bold", 23 * -1)
)

print(name)

canvas.create_text(
    360.0,
    299.0,
    anchor="nw",
    text="Last time checked: ",
    fill="#515156",
    font=("Inter ExtraLight", 14 * -1)
)

canvas.create_text(
    569.0,
    159.0,
    anchor="nw",
    text="Employee",
    fill="#646474",
    font=("Inter", 9 * -1)
)

last = canvas.create_text(
    569.0,
    300.0,
    anchor="nw",
    text="Today",
    fill="#006710",
    font=("Inter Light", 14 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    408.0,
    258.0,
    image=image_image_7
)

position =canvas.create_text(
    369.0,
    246.0,
    anchor="nw",
    text="Dev Backend",
    fill="#212123",
    font=("Inter Light", 13 * -1)
)

print(position);

free = PhotoImage(
    file=relative_to_assets("free.png"))
banner = canvas.create_image(
    514.0,
    383.0,
    image=free
)

window.resizable(True, True),
# window.attributes("-fullscreen", True)


Employees = {
  '0013087914': {
    "name" : "Júlia Z. Schwartz",
    "position" : "Dev Backend",
     "last": "Today"
  },
  '0003866073': {
    "name" : "Maria da Silva",
    "position" : "Data Engineer",
     "last": "Today"
  },
  '0002710499': {
    "name" : "João Da Silva",
    "position" : "DevOps",
    "last": "Yesterday"
  }
}

for tent in range(10):

        try:
            ser = serial.Serial('/dev/ttyUSB'+tent, 9600, timeout=1)

            ser.reset_input_buffer()
           
            print("porta"+tent+"encontrada")

        except:
            print('porta não encontrada')
 if ser.in_waiting > 0:
     line = ser.readline().decode('utf-8').rstrip();
     
try:     #se o funcionário estiver cadastrado ( estiver no dicionário), preenche os dados do card e apresenta o banner de "Bem Vindo"
    line = Employees[ser]
    canvas.itemconfig(number, text=ser)
    canvas.itemconfig(name, text=line['name'])
    canvas.itemconfig(position, text=line['position'])
    canvas.itemconfig(last, text=line['last'])
    block = PhotoImage(file=relative_to_assets("free.png"))
    canvas.itemconfig(banner, image=block)

except:   #se o funcionário estiver cadastrado (não estiver no dicionário), preenche os dados do card com uma string vazia e apresenta o banner de "Bloqueado"
    canvas.itemconfig(number, text=ser)
    canvas.itemconfig(name, text='Não Cadastrado')
    canvas.itemconfig(position, text='')
    canvas.itemconfig(last, text='')
    block = PhotoImage(
        file=relative_to_assets("blocked.png"))
    canvas.itemconfig(banner, image=block)


window.mainloop()


