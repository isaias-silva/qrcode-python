import qrcode
def qrc(a):
    img = qrcode.make(a)
    print(img)
    img.save("qrcode.png")
    return 0