import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture(0)
pose = mp.solutions.pose
#os parametros dentro de pose.Pose serve para melhorar a detecção de acordo com o ambiente
Pose = pose.Pose(min_tracking_confidence=0.5,min_detection_confidence=0.5)

draw = mp.solutions.drawing_utils

contador = 0
check = True

while True:
    sucess, img = video.read()
    videoRGB = cv2.cvtColor(img ,cv2.COLOR_BGR2RGB)
    result = Pose.process(videoRGB)
    points = result.pose_landmarks
    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)
    h,w,_ = img.shape



    if points:
        peDY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        peDX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)
        
        peEY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        peEX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)

        moDY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        moDX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)

        moEY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        moEX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)


        distMO = math.hypot(moDX - moEX, moDY - moEY)
        distPE = math.hypot(peDX - peEX, peDY - peEY)

        print(f'maos {distMO} pes {distPE}')

        if check == True and distMO <= 300 and distPE >= 100:
            contador += 1
            check = False
        if distMO > 300 and distPE < 100:
            check = True
        texto = f'QTD: {contador}'
        cv2.putText(img,texto,(40,200),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),5)

    cv2.imshow('webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("camera desligada")
        print(f'voce fez {contador} polichinelos, parabens campeão')
        break
    