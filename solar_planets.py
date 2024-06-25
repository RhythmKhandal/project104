import cv2

img = cv2.imread("solar-system.jpg")


cv2.waitKey(0)

cv2.putText(img,
            "Sun",
            (50,100),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.putText(img,
            "Mercury",
            (110,240),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Venus",
            (190,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Earth",
            (290,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Mars",
            (380,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Jupiter",
            (480,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Saturn",
            (720,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Uranus",
            (900,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.putText(img,
            "Neptune",
            (1100,100),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,0,255)
            )

cv2.imshow("Display Image",img)
cv2.waitKey(0)