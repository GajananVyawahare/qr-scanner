import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("gajananvyawahare610@gmail.com")
myqr1 = qrcode.make("https://github.com/GajananVyawahare/qr-scanner.git")


myqr.save("myqr.png",scale = 8)
myqr1.save("myqr1.png",scale = 7)

b = decode(Image.open("myqr.png"))
print (b[0].data.decode("ascii"))






