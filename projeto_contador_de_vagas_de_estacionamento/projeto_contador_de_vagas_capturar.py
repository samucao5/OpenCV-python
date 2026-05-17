import cv2
import pickle
img = cv2.imread(r'projeto_contador_de_vagas_de_estacionamento\conteudos\estacionamento.png')

vagas = []

for x in range(69):
    vaga = cv2.selectROI('vagas', img,False)
    cv2.destroyAllWindows()
    vagas.append((vaga))

    for x,y,w,h in vagas:
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)


with open('vagas.pkl','wb') as arquivo:
    pickle.dump(vagas,arquivo)


#cv2.imshow("estacionamento",img)

#cv2.waitKey(0)