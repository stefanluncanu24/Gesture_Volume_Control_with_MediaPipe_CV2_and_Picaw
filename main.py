import cv2
import time
import HTM as htm  
from VolumeHandControl import VolumeHandControl  

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  
    cap.set(4, 480) 
    pTime = 0
    detector = htm.handDetector(detectionCon=0.90)
    volume_control = VolumeHandControl()

    while True:
        success, img = cap.read()
        if not success:
            continue

        img = detector.findHands(img)
        lmList1 = detector.findPosition(img, handNo=0, draw=False)
        lmList2 = detector.findPosition(img, handNo=1, draw=False)
        img = volume_control.process_frame(img, lmList1, lmList2)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Img", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
