# ---- Imports ----
import qr_gen
import customtkinter as ctk
from PIL import Image
from io import BytesIO

# ---- Functions ----
def gen_button():
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
  qr_image_label = ctk.CTkLabel(master=window,
                              image=qr_image,
                              text="")
  qr_image_label.pack(side="top",
                      fill="both",
                      padx=20)
  qr_image_label.configure(image=qr_image)
  qr_image_label.image = qr_image

# ---- Set Up ----
window = ctk.CTk()
window.title("QR Code Generator")
window.geometry("500x700")
window._set_appearance_mode("dark")
window.resizable(width=False,
                 height=False)

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
                                        width=130)
error_correct_input.pack(side="right",
                         padx=10)

# Input
input_box = ctk.CTkEntry(master=input_error_frame,
                     placeholder_text="Input")
input_box.pack(side="right",
           fill="x",
           expand="True",
           padx=10)

# Slider and value container
slider_container = ctk.CTkFrame(master=window,
                                fg_color="#242424",
                                height=50)
slider_container.pack(side="top",
                      fill="x",
                      padx=10)

# Generate Button
gen_button = ctk.CTkButton(master=window,
                           text="Generate",
                           width=100,
                           command=gen_button)
gen_button.pack(side="bottom",
                pady=20)

# ---- Run ----
window.mainloop()
