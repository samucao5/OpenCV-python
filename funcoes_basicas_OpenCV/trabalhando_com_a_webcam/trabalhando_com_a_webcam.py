import cv2

camera = cv2.VideoCapture(0)
camera.set(3,640)   # 3 - largura
camera.set(4, 428)  # 4 - altura
camera.set(10, 200) #10 - brilho/ luminosidade
while True:
    check,img = camera.read()
    cameraredimensionada = cv2.resize(img, (480,240))
    cameraredin = cv2.cvtColor(cameraredimensionada, cv2.COLOR_RGB2GRAY)
    cv2.imshow('WebCam', cameraredin)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("camera desligada")
        break
        
# Serve para liberar a câmera do computador.
camera.release()

# Fecha todas as janelas abertas pelo OpenCV.
cv2.destroyAllWindows()
