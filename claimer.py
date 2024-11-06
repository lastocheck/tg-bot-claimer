import pyautogui, sys 
import time
from random import uniform, randint

class Instance:
  def __init__(self, region, imgs, index):
    self.region = region
    self.imgs = imgs
    self.index = index

first_region = (5, 85, 650 - 5, 1025 - 95)
second_region = (655, 95, 1295 - 655, 1025 - 95)
third_region = (1240, 95, 1900 - 1240, 1025 - 95)
fourth_region = (570, 5, 1400 - 570, 1077)

alfa_click_region = (850, 450, 1100 - 850, 700 - 450)

first_imgs = {
  'open_hamster': './img/first/first-hamster.png',
  'open_1win': './img/first/first-1win.png',
  'play_hamster': './img/first/first-hamster-play.png',
  'play_1win': './img/first/first-1win-play.png',
  'claim_hamster': './img/hamster-claim-eng.png',
  'claim_1win': './img/1win-claim-ru.png',
  'close': './img/first/first-close.png',
  'launch': './img/1win-launch.png'
}

second_imgs = {
  'open_hamster': './img/second/second-hamster.png',
  'open_1win': './img/second/second-1win.png',
  'play_hamster': './img/second/second-hamster-play.png',
  'play_1win': './img/second/second-1win-play.png',
  'claim_hamster': './img/hamster-claim-ru.png',
  'claim_1win': './img/1win-claim-ru.png',
  'close': './img/second/second-close.png',
  'launch': './img/1win-launch.png'

}

third_imgs = {
  'open_hamster': './img/third/third-hamster.png',
  'open_1win': './img/third/third-1win.png',
  'play_hamster': './img/third/third-hamster-play.png',
  'play_1win': './img/third/third-1win-play.png',
  'claim_hamster': './img/hamster-claim-ru.png',
  'claim_1win': './img/1win-claim-ru.png',
  'close': './img/third/third-close.png',
  'launch': './img/1win-launch.png'
}

okx_region = (550, 59, 1450 - 550, 1080 - 50)
okx_fuel_capacity = 28
okx_imgs = {
  'open_telegam': './img/okx/open-tele.png',
  'open_telegam_2': './img/okx/open-tele-2.png',
  'open_bot_dialog': './img/okx/okx-bot-open.png',
  'open_bot_dialog_2': './img/okx/okx-bot-open-blue.png',
  'open_bot_app': './img/okx/okx-play.png',
  'collect': './img/okx/okx-collect.png',
  'moon': './img/okx/okx-moon.png',
  'close': './img/okx/okx-close.png',
  'close_telegram': './img/okx/close-tele.png',
}

not_capacity = 20
not_recharge = 480
not_regions = [
  {
    'map': (320, 620),
    'paint': (330, 950)
  },
  {
    'map': (985, 575),
    'paint': (1000, 950)
  },
  {
    'map': (1565, 575),
    'paint': (1580, 950)
  },
  {
    'map': (985, 575),
    'paint': (1000, 950)
  }
]

coub_watch_count = 20

def log(msg):
  hour = time.localtime().tm_hour
  min = time.localtime().tm_min
  sec = time.localtime().tm_sec
  print(f'{hour}:{min}:{sec} ------ RUNNING {msg} ------')

def wait_for(img, _region, _confidence, seconds, click):
  count = 0
  while count < seconds:
    try:
      location = pyautogui.locateCenterOnScreen(img, region=_region, confidence=_confidence)
      if click:
        location.click()
      return True
    except pyautogui.ImageNotFoundException:
      count += 1
      time.sleep(1)
  return False

def click_button(img, _region, _confidence=0.7):
  try:
    location = pyautogui.locateCenterOnScreen(img, region=_region, confidence=_confidence)
    if location:
      pyautogui.click(location)
      print(f'clicked {img}')
    else:
      print(f'no location for {img}')
  except pyautogui.ImageNotFoundException:
      print(f'ImageNotFoundException for {img}')

def click_either(img1, img2, _region, _confidence):
  try:
    location = pyautogui.locateCenterOnScreen(img1, region = _region, confidence = _confidence)
    if location:
      pyautogui.click(location)
      print(f'clicked {img1}')
      return True
  except pyautogui.ImageNotFoundException:
      try:
        location = pyautogui.locateCenterOnScreen(img2, region = _region, confidence = _confidence)
        if location:
          pyautogui.click(location)
          print(f'clicked {img2}')
          return True
      except pyautogui.ImageNotFoundException:
        print(f'could not find either {img1} or {img2}')
        return False

def run_claim(instance, bot):
  log(bot)

  click_button(instance.imgs[f'open_{bot}'], instance.region)
  time.sleep(7)
  click_button(instance.imgs[f'play_{bot}'], instance.region)
  time.sleep(3)

  # check for launch button
  if (bot == '1win'):
    try:
      launch_location = pyautogui.locateCenterOnScreen(instance.imgs['launch'], region=instance.region, confidence=0.75)
      if launch_location:
        print(f'found launch button')
        click_button(instance.imgs['launch'], _region=instance.region, _confidence=0.75)
    except pyautogui.ImageNotFoundException:
      pass
  time.sleep(12)

  # check for referal window
  if (bot == '1win'):
    try:
      gift_location = pyautogui.locateCenterOnScreen('./img/gift.png', region=instance.region, confidence=0.75)
      if gift_location:
        print(f'found gift image')
        click_button('./img/gift-close.png', _region=instance.region, _confidence=0.95)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
      pass

  click_button(instance.imgs[f'claim_{bot}'], instance.region)
  time.sleep(3)
  click_button(instance.imgs['close'], instance.region)

def run_alfa():
  log('alfa')

  click_button('./img/alfa/alfa-open.png', second_region)
  time.sleep(5)
  for i in range(randint(5500, 6000)):
    x, y, width, height = alfa_click_region
    random_x = randint(x, x + width)
    random_y = randint(y, y + height)
    pyautogui.click(random_x, random_y)
  time.sleep(1)
  click_button(second_imgs['close'], second_region)

def run_okx():
  log('okx')

  click_either(okx_imgs['open_telegam'], okx_imgs['open_telegam_2'], okx_region, 0.85)
  time.sleep(1)
  click_either(okx_imgs['open_bot_dialog'], okx_imgs['open_bot_dialog_2'], okx_region, 0.85)
  time.sleep(2)
  click_button(okx_imgs['open_bot_app'], _region=okx_region, _confidence=0.85)
  time.sleep(10)
  click_button(okx_imgs['collect'], _region=okx_region, _confidence=0.85)
  time.sleep(2)
  for i in range(okx_fuel_capacity):
    click_button(okx_imgs['moon'], okx_region, 0.9)
    pyautogui.moveTo(1050, 500)
    time.sleep(9)
  click_button(okx_imgs['close'], _region=okx_region, _confidence=0.85)
  time.sleep(1)
  pyautogui.moveTo(1050, 500)
  time.sleep(1)
  click_button(okx_imgs['close_telegram'], _region=okx_region, _confidence=0.8)
  time.sleep(1)

def run_not():
  log('not pixel')
  for i in range(3):
    match i:
      case 0:
        current = 'first'
        region = first_region
        paint_region = (369, 345, 434 - 369, 417 - 345)
        template_coords = (46, 374)
      case 1:
        current = 'second'
        region = second_region
        paint_region = (1000, 342, 1065 - 1000, 407 - 342)
        template_coords = (743, 371)
      case 2:
        current = 'third'
        region = third_region
        paint_region = (1600, 335, 1665 - 1600, 400 - 335)
        template_coords = (1320, 365)
      case 3:
        current = 'fourth'
        region = fourth_region
        paint_region = (986, 340, 1205 - 986, 490 - 340)
    if (i == 3):
      click_button('./img/fourth/opera_open.png', _region=region, _confidence=0.8)
      time.sleep(2)
    click_button(f'./img/{current}/not/open.png', _region=region, _confidence=0.85)
    time.sleep(9)
    click_button(f'./img/{current}/not/start.png', _region=region, _confidence=0.8)
    time.sleep(15)
    click_button('./img/not-flag-btn.png', region, 0.85)    
    # check for bot to load
    menu_img = f'./img/{current}/not/open-menu.png'
    if not wait_for(menu_img, region, 0.8, 20, False):
      print(f'could not find {menu_img}, closing')
      click_button(f'./img/{current}/{current}-close.png', _region=region, _confidence=0.8)
      if (i == 3):
        time.sleep(1)
        click_button('./img/fourth/opera_close.png', _region=region, _confidence=0.8)
      continue
    time.sleep(1)

    # click template button
    # click_button('./img/not/template-smile.png', region, 0.8)
    pyautogui.click(randint(template_coords[0] - 5, template_coords[0] + 5), randint(template_coords[1] - 5, template_coords[1] + 5))
    time.sleep(1)

    # check for template to load
    # tnt_img = f'./img/not/tnt.png'
    # if not wait_for(tnt_img, region, 0.8, 20, False):
    #   print(f'could not find {tnt_img}, closing')
    #   click_button(f'./img/{current}/{current}-close.png', _region=region, _confidence=0.8)
    #   if (i == 3):
    #     time.sleep(1)
    #     click_button('./img/fourth/opera_close.png', _region=region, _confidence=0.8)
    #   continue
    # time.sleep(1)

    # painting until the capacity is over
    for j in range(not_capacity):
      random_x = randint(paint_region[0], paint_region[0] + paint_region[2])
      random_y = randint(paint_region[1], paint_region[1] + paint_region[3])
      pyautogui.click(random_x, random_y)
      time.sleep(0.5)
      pyautogui.click(not_regions[i]['paint'][0] + randint(-10, 10), not_regions[i]['paint'][1] + randint(-10, 10))
      time.sleep(0.5)
      # check if energy is over
      try:
        pyautogui.locateCenterOnScreen('./img/not-energy-over.png', region=region, confidence=0.8)
        break
      except pyautogui.ImageNotFoundException:
        pass
    
    click_button(f'./img/{current}/not/open-menu.png', _region=region, _confidence=0.8)
    time.sleep(2)
    click_button(f'./img/{current}/not/claim.png', _region=region, _confidence=0.8)
    time.sleep(5)
    click_button(f'./img/{current}/{current}-close.png', _region=region, _confidence=0.8)
    if (i == 3):
      time.sleep(1)
      click_button('./img/fourth/opera_close.png', _region=region, _confidence=0.8)
    
def click_pixels_old():
  # choose random area and paint within click_offset
  area_offset = 150
  click_offset = 5
  click_point = ((not_regions[i]['map'][0] + randint(-area_offset, area_offset), not_regions[i]['map'][1] + randint(-area_offset, area_offset)))
  for j in range(not_capacity):
    pyautogui.click(click_point[0] + randint(-click_offset, click_offset), click_point[1] + randint(-click_offset, click_offset))
    time.sleep(0.5)
    pyautogui.click(not_regions[i]['paint'][0] + randint(-10, 10), not_regions[i]['paint'][1] + randint(-10, 10))
    time.sleep(0.5)
    # check if energy is over
    try:
      pyautogui.locateCenterOnScreen('./img/not-energy-over.png', region=region, confidence=0.8)
      break
    except pyautogui.ImageNotFoundException:
      pass

def run_coub(region, index): 
  if (index == 'fourth'):
      click_button('./img/fourth/opera_open.png', _region=region, _confidence=0.8)
      time.sleep(2)
  click_button(f'./img/{index}/coub/open.png', _region=region, _confidence=0.85)
  time.sleep(9)
  click_button(f'./img/{index}/coub/start.png', _region=region, _confidence=0.8)
  # check for launch button
  try:
    location = pyautogui.locateCenterOnScreen('./img/1win-launch.png', region=region, confidence=0.8)
    pyautogui.click(location)
  except pyautogui.ImageNotFoundException:
    pass
  time.sleep(15)

  
  click_button('./img/coub/claim-daily.png', region, 0.8)
  time.sleep(1)
  click_button('./img/coub/friend-promo-btn.png', region, 0.8)
  time.sleep(1)
  click_button('./img/coub/friend-promo-btn.png', region, 0.8)
  time.sleep(1)

  # check for bot to load
  tasks_img = f'./img/coub/tasks.png'
  if not wait_for(tasks_img, region, 0.8, 20, False):
    print(f'could not find {tasks_img}, closing')
    click_button(f'./img/{index}/{index}-close.png', _region=region, _confidence=0.8)
    if (index == 'fourth'):
      time.sleep(1)
      click_button('./img/fourth/opera_close.png', _region=region, _confidence=0.8)
    return
  time.sleep(1)

  click_button('./img/coub/home.png', region, 0.8)
  time.sleep(4)
  click_button('./img/coub/random.png', region, 0.8)
  time.sleep(0.5)
  pyautogui.moveRel(80, 100)
  time.sleep(4)
  watch_coub_videos(region)
  time.sleep(1)
  click_button('./img/coub/shorts.png', region, 0.8)
  time.sleep(3)
  click_button('./img/coub/home.png', region, 0.8)
  time.sleep(4)
  click_button('./img/coub/trending.png', region, 0.8)
  time.sleep(0.5)
  pyautogui.moveRel(80, 100)
  time.sleep(4)
  watch_coub_videos(region)
  click_button(f'./img/{index}/{index}-close.png', _region=region, _confidence=0.8)
  if (index == 'fourth'):
    time.sleep(1)
    click_button('./img/fourth/opera_close.png', _region=region, _confidence=0.8)

def watch_coub_videos(region):
  scroll_range = -300
  for i in range (coub_watch_count):
    time.sleep(randint(8, 13))
    if randint(1, 10) > 5:
      click_button('./img/coub/like.png', region, 0.8)
      time.sleep(0.5)
      try:
        location = pyautogui.locateCenterOnScreen('./img/coub/like.png', region=region, confidence=0.8)
        pyautogui.moveTo(location.x + 80, location.y)
      except pyautogui.ImageNotFoundException:
        pass
    pyautogui.scroll(randint(scroll_range, scroll_range + 100))
    time.sleep(0.5)
    pyautogui.scroll(randint(scroll_range, scroll_range + 100))

def run_moon():
  log('moonbix')
  region = okx_region

  click_either(okx_imgs['open_telegam'], okx_imgs['open_telegam_2'], region, 0.85)
  time.sleep(1)
  if not click_either('./img/moon/open-bot-white.png', './img/moon/open-bot-blue.png', region, 0.85):
    click_button(okx_imgs['close_telegram'], _region=okx_region, _confidence=0.8)
    time.sleep(1)
    return
  time.sleep(2)
  click_button('./img/moon/start-app.png', region, 0.85)
  time.sleep(10)
  # click_button(okx_imgs['collect'], region, 0.85)
  time.sleep(2)
  click_button('./img/moon/cookie-deny.png', region, 0.85)
  time.sleep(1)

  #check for phone
  try:
    pyautogui.locateCenterOnScreen('./img/moon/play-on-phone.png', region=region, confidence=0.8)
    click_button('./img/moon/tg-three-dots.png', region, 0.85)
    time.sleep(0.5)
    click_button('./img/moon/tg-reload-page.png', region, 0.85)
    time.sleep(13)
  except pyautogui.ImageNotFoundException:
    pass

  click_button('./img/moon/cookie-deny.png', region, 0.85)
  time.sleep(1)
  click_button('./img/moon/start-game.png', region, 0.85)
  for i in range(6):
    time.sleep(3.5)
    look_for_moon()
    time.sleep(2)
    try:
      pyautogui.locateCenterOnScreen('./img/moon/gameover-share.png', region=region, confidence=0.85)
      click_button('./img/moon/close-app.png', _region=okx_region, _confidence=0.85)
      time.sleep(1)
      pyautogui.moveTo(1050, 500)
      time.sleep(1)
      click_button(okx_imgs['close_telegram'], _region=okx_region, _confidence=0.8)
      time.sleep(1)
      return
    except pyautogui.ImageNotFoundException:
      pass
    click_button('./img/moon/play-again.png', region, 0.85)
  click_button('./img/moon/close-app.png', _region=okx_region, _confidence=0.85)
  time.sleep(1)
  pyautogui.moveTo(1050, 500)
  time.sleep(1)
  click_button(okx_imgs['close_telegram'], _region=okx_region, _confidence=0.8)
  time.sleep(1)

def look_for_moon():
  end_time = time.time() + 45
  while time.time() < end_time:
    try:
      location = pyautogui.locateCenterOnScreen('./img/moon/arm-straight.png', region=okx_region, confidence=0.75)
      pyautogui.click(location)
    except pyautogui.ImageNotFoundException:
      pass

def run_kucoin():
  log('kucoin')
  region = okx_region

  click_either(okx_imgs['open_telegam'], okx_imgs['open_telegam_2'], region, 0.85)
  time.sleep(1)
  if not click_either('./img/kucoin/open-bot.png', './img/kucoin/open-bot.png', region, 0.85):
    click_button('./img/moon/close-app.png', _region=region, _confidence=0.85)
    time.sleep(1)
    click_button('./img/tele-close-confirm.png', _region=region, _confidence=0.8)
    time.sleep(1)
    click_button(okx_imgs['close_telegram'], _region=region, _confidence=0.8)
    time.sleep(1)
    return
  time.sleep(2)
  click_button('./img/kucoin/open-app.png', region, 0.85)
  time.sleep(15)
  try:
    center = pyautogui.locateCenterOnScreen('./img/kucoin/frog-center.png', region=region, confidence=0.85)
    offset = 100
    for i in range(randint(2500, 2800)):
      pyautogui.click(randint(center.x - offset, center.x + offset), randint(center.y - offset, center.y + offset))
  except pyautogui.ImageNotFoundException:
    click_button('./img/moon/close-app.png', _region=region, _confidence=0.85)
    time.sleep(1)
    click_button('./img/tele-close-confirm.png', _region=region, _confidence=0.8)
    time.sleep(1)
    click_button(okx_imgs['close_telegram'], _region=region, _confidence=0.8)
    time.sleep(1)
    return
  time.sleep(5)
  click_button('./img/moon/close-app.png', _region=region, _confidence=0.85)
  time.sleep(1)
  click_button('./img/tele-close-confirm.png', _region=region, _confidence=0.8)
  time.sleep(1)
  click_button(okx_imgs['close_telegram'], _region=region, _confidence=0.8)
  time.sleep(1)

def run_seed(region, index):
  if (index == 'fourth'):
    click_button('./img/fourth/opera_open.png', region, 0.8)
    time.sleep(2)
  click_button(f'./img/{index}/seed/open.png', region, 0.85)
  time.sleep(9)
  click_button(f'./img/{index}/seed/start-app.png', region, 0.8)
  # check for launch button
  try:
    location = pyautogui.locateCenterOnScreen('./img/1win-launch.png', region=region, confidence=0.8)
    pyautogui.click(location)
  except pyautogui.ImageNotFoundException:
    pass
  time.sleep(15)

  # collect worm
  click_button('./img/seed/worm-1.png', region, 0.75)
  click_button('./img/seed/worm-2.png', region, 0.75)
  click_button('./img/seed/worm-3.png', region, 0.75)
  click_button('./img/seed/worm-4.png', region, 0.75)
  time.sleep(5)
  click_button('./img/seed/worm-claim.png', region, 0.8)
  time.sleep(3)
  
  click_button('./img/seed/check-news.png', region, 0.75)
  time.sleep(2)
  click_button('./img/seed/claim.png', region, 0.8)
  time.sleep(3)
  click_button(f'./img/{index}/{index}-close.png', region, 0.8)
  if (index == 'fourth'):
    time.sleep(1)
    click_button('./img/fourth/opera_close.png', region, 0.8)


def test_img(img, region):
  try:
    location = pyautogui.locateCenterOnScreen(img, region=region, confidence=0.9)
    if location:
      pyautogui.click(location)
      print(f'clicked {img}')
    else:
      print(f'no location for {img}')
  except pyautogui.ImageNotFoundException:
      print(f'ImageNotFoundException for {img}')

def main():
  while True:
    run_not()
    time.sleep(1)
    run_moon()  
    time.sleep(1)
    if randint(1, 2) == 2:
      log('coub and seed')
      for instance in [Instance(first_region, None, 'first'),
      Instance(second_region, None, 'second'),
      Instance(third_region, None, 'third')]:
        run_seed(instance.region, instance.index)
        time.sleep(1)
        run_coub(instance.region, instance.index)
    time.sleep(1)
    run_okx()
    time.sleep(randint(okx_fuel_capacity * 90, okx_fuel_capacity * 90 + 50))
    run_not()
    time.sleep(1)
    run_okx()
    for instance in [Instance(first_region, first_imgs, None), Instance(second_region, second_imgs, None), Instance(third_region, third_imgs, None)]:
      run_claim(instance, '1win')
    time.sleep(randint(okx_fuel_capacity * 90 - 600, okx_fuel_capacity * 90 - 550))

if __name__ == "__main__":
  main()
