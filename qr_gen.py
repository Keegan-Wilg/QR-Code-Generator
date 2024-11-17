# ---- Imports ----
import qrcode
import qrcode.constants

# Generates the QR Code and formats error correction input
def generate(input:str, error_correction_amount:str):
  # Error correction code formatting
  if error_correction_amount == "Low - 7%":
    revised_error_correction = qrcode.constants.ERROR_CORRECT_L
  elif error_correction_amount == "Medium - 15%":
    revised_error_correction = qrcode.constants.ERROR_CORRECT_M
  elif error_correction_amount == "Quartile - 25%":
    revised_error_correction = qrcode.constants.ERROR_CORRECT_Q
  elif error_correction_amount == "High - 30%":
    revised_error_correction = qrcode.constants.ERROR_CORRECT_H
  
  # QR Code settings
  qr = qrcode.QRCode(version=1,
                     error_correction=revised_error_correction,
                     box_size=20,
                     border=4)
  # Adding string data
  qr.add_data(input)
  # Creating QR Code
  img = qr.make_image(fill_color="white", back_color="#242424")

  return img