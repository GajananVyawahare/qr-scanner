import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

myqr = qrcode.make("https://www.instagram.com/pritam_official_1137?igsh=aGhueTBubXlyb3N1&utm_source=qr")
myqr1 = qrcode.make("https://www.instagram.com/s/aGlnaGxpZ2h0OjE3OTI1NjkzMzQyMTE2NDUw?story_media_id=3718701748895382397&igsh=MWNzaDB1dzl5aHFyMw==")


myqr.save("myqr.png",scale = 8)
myqr1.save("myqr1.png",scale = 7)

b = decode(Image.open("myqr.png"))
print (b[0].data.decode("ascii"))






