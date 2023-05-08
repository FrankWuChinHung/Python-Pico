# 匯入控制版模組
import board
import time

# 匯入數位輸出輸入模組
from digitalio import DigitalInOut, Direction, Pull

# 建立GP15腳位的DigitalInOut物件，命名led
led = DigitalInOut(board.GP15)
led2 = DigitalInOut(board.GP16)

# 設定led爲輸出位
led.direction = Direction.OUTPUT
led2.direction = Direction.OUTPUT

# 建立GP17腳位的DigitalInOut物件，命名button
button = DigitalInOut(board.GP17)
# 設定button爲輸入位
button.direction = Direction.INPUT
# 設定button爲上拉電阻
button.pull = Pull.UP

# 創建一個名為 led_enabled 的變量，初始值為 0。這表示 LED 是否應該閃爍。
led_enabled = 0

while True:
    if not button.value:
        # 在每次按下按鈕時，切換 led_enabled 的值。如果它原本為 True，則變為 False，反之亦然。這樣可以在按下按鈕時啟動或停止 LED 閃爍。
        led_enabled = not led_enabled
        time.sleep(1)

    while led_enabled:
        led.value = True
        time.sleep(0.2)
        led.value = False
        time.sleep(0.2)
        led2.value = True
        time.sleep(0.2)
        led2.value = False
        time.sleep(0.2)

        if not button.value:
            led_enabled = not led_enabled
            time.sleep(1)
