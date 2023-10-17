import pyautogui as pag
import time
#Tìm tọa độ
time.sleep(5)
pos = pag.position()
print(pos)
#Auto click
for _ in range(3):
    pag.click(pos)
    time.sleep(3)
#Tìm theo đối tượng
# time.sleep(5)
# image = 'image.png'
# loc = pag.locateOnScreen(image)
# pag.click()
