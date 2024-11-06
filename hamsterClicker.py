import pyautogui, sys 
from time import sleep 
from random import uniform, randint

first_hamster_w = 333
first_hamster_h = 720
second_hamster_w = 978
second_hamster_h = 755
third_hamster_w = 1597
third_hamster_h = 769

tab_h = 120
first_close_w = 90
first_open_w = 230
second_close_w = 760
second_open_w = 917
third_close_w = 1379
third_open_w = 1530

first_collect_w = 328
first_collect_h = 898
second_collect_w = 957
second_collect_h = 855
third_collect_w = 1600
third_collect_h = 856
first_collect_w = 328

play_h = 965
first_play_w = 85
first_play_h = play_h
second_play_w = 745
second_play_h = play_h
third_play_w = 1375
third_play_h = play_h

first_clicks = 555
second_clicks = 555
third_clicks = 555

energy_recovery = 3100

 
def main(): 
  while(True):

    #first clicks
    for i in range(first_clicks): 
      pyautogui.click(randint(first_hamster_w - 50, first_hamster_w + 50), randint(first_hamster_h - 50, first_hamster_h + 50)) 
      sleep(uniform(0.005, 0.02))
    # close the tab 
    pyautogui.click(first_close_w, tab_h)
    
    #second clicks
    for i in range(second_clicks): 
      pyautogui.click(randint(second_hamster_w - 50, second_hamster_w + 50), randint(second_hamster_h - 50, second_hamster_h + 50)) 
      sleep(uniform(0.005, 0.02))
    # close the tab 
    pyautogui.click(second_close_w, tab_h)
    
    #third clicks
    for i in range(third_clicks): 
      pyautogui.click(randint(third_hamster_w - 50, third_hamster_w + 50), randint(third_hamster_h - 50, third_hamster_h + 50)) 
      sleep(uniform(0.005, 0.02))
    # close the tab 
    pyautogui.click(third_close_w, tab_h)

    # wait
    sleep(randint(energy_recovery - 200, energy_recovery + 50))

    #first

    #open tab
    pyautogui.click(first_open_w, tab_h)
    sleep(10)
    #press play
    pyautogui.click(first_play_w, first_play_h)
    sleep(15)
    #press collect
    pyautogui.doubleClick(randint(first_collect_w - 20, first_collect_w + 20), randint(first_collect_h - 20, first_collect_h + 20))
    #second

    #open tab
    pyautogui.click(second_open_w, tab_h)
    sleep(10)
    #press play
    pyautogui.click(second_play_w, second_play_h)
    sleep(10)
    #press collect
    pyautogui.click(randint(second_collect_w - 20, second_collect_w + 20), randint(second_collect_h - 20, second_collect_h + 20))    
    
    #third

    #open tab
    pyautogui.click(third_open_w, tab_h)
    sleep(10)
    #press play
    pyautogui.click(third_play_w, third_play_h)
    sleep(10)
    #press collect
    pyautogui.click(randint(third_collect_w - 20, third_collect_w + 20), randint(third_collect_h - 20, third_collect_h + 20))

if __name__ == "__main__":
  main() 