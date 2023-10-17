import pyautogui as pag, time
time.sleep(5)
screen = pag.screenshot(region=(0,0,250,1250))
screen.save('pic1.png')
print('Finished')