import pyautogui as pag
import time
time.sleep(5)
for _ in range(3):
    pos = pag.position(554, 691)
    pag.doubleClick(pos)
    time.sleep(3)
    pos2 = pag.position(1132, 754)
    pag.click(pos2)
    time.sleep(3)
    