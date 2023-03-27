import PySimpleGUI as sg
import qrcode

# Set the theme for the GUI
sg.theme("LightGreen")

# Define the layout of the GUI
layout = [
    [sg.InputText(key="text_input", size=(30,1), font=("Helvetica", 14))],
    [sg.Button("Create QR code", font=("Helvetica", 14))],
    [sg.Image(key="qr_image", size=(300,300))]
]

# Create the GUI window
window = sg.Window("QR Code Creator", layout)

# Handle events in the GUI
while True:
    event, values = window.read()

    if event == "Create QR code":
        text_input = values["text_input"]
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(text_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save("qrcode.png")
        window["qr_image"].update("qrcode.png")
        sg.Popup("QR code created successfully!", title="Success")
        break
    elif event == "WIN_CLOSED":
        break

# Close the GUI window
window.close()
