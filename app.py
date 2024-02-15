#como pegar e "arrastar"algo para outro lugar
import pyautogui

for i in range(5):
    # mover até um coord 
    pyautogui.moveTo(259,234,duration=0.5)
    #clicar  e arrastar até um ponto e soltar.
    pyautogui.dragTo(629,298,button= 'left', duration=0.5)
    # repetir o necessario.
