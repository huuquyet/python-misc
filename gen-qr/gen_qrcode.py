import qrcode

# Data to be encoded
data = "test"

# Create a QR Code instance
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

# Add data to the QR code
qr.add_data(data)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
