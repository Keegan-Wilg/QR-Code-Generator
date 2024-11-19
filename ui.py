# ---- Imports ----
import qr_gen
import customtkinter as ctk
from PIL import Image
from io import BytesIO

# ---- Functions ----
def generate_qr_menu(menu_value):
  input_value = input_box.get()
  print(f"Error Correction ({menu_value})\nInput ({input_value})")
  
  img = qr_gen.generate(input_value, menu_value)
  
  buffer = BytesIO()
  img.save(buffer, format="PNG")
  buffer.seek(0)
  img = Image.open(buffer)
  
  qr_image = ctk.CTkImage(light_image=img,
                           dark_image=img,
                           size=(450, 450))
  
  qr_image_label.configure(image=qr_image)
  qr_image_label.image = qr_image

def generate_qr_input(*args):
  input_value = input_box.get()
  menu_value = error_correct_input.get()
  print(f"Error Correction ({menu_value})\nInput ({input_value})")
  
  img = qr_gen.generate(input_value, menu_value)
  
  buffer = BytesIO()
  img.save(buffer, format="PNG")
  buffer.seek(0)
  img = Image.open(buffer)
  
  qr_image = ctk.CTkImage(light_image=img,
                           dark_image=img,
                           size=(450, 450))
  
  qr_image_label.configure(image=qr_image)
  qr_image_label.image = qr_image

# ---- Set Up ----
window = ctk.CTk()
window.title("QR Code Generator")
window.geometry("500x550")
window._set_appearance_mode("dark")
window.resizable(width=False,
                 height=False)

# ---- Variables ----
input_var = ctk.StringVar()
input_var.trace_add("write", generate_qr_input)

# Input and error correction container
input_error_frame = ctk.CTkFrame(master=window,
                                 fg_color="#242424",
                                 height=50)
input_error_frame.pack(side="top",
                       fill="x",
                       pady=20,
                       padx=10)

# Error correction input
error_correct_input = ctk.CTkOptionMenu(master=input_error_frame,
                                        values=["Low - 7%",
                                                "Medium - 15%",
                                                "Quartile - 25%",
                                                "High - 30%"],
                                        width=130,
                                        command=generate_qr_menu)
error_correct_input.pack(side="right",
                         padx=10)

# Input
input_box = ctk.CTkEntry(master=input_error_frame,
                         textvariable=input_var,
                         placeholder_text="Input")
input_box.pack(side="right",
               fill="x",
               expand="True",
               padx=10)

qr_image_label = ctk.CTkLabel(master=window,
                              text="")
qr_image_label.pack(side="top",
                    fill="both",
                    padx=20)

# ---- Run ----
window.mainloop()
