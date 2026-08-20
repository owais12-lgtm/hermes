import time
import board
import digitalio
import busio
import adafruit_ssd1306

i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)
oled.text("LED Matrix", 0, 0, 1)
oled.text("bring-up test", 0, 12, 1)
oled.show()

ROW_PINS = [board.D9, board.D8, board.D7, board.D6]
COL_PINS = [board.D0, board.D1, board.D2, board.D3]

rows = []
for p in ROW_PINS:
    pin = digitalio.DigitalInOut(p)
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = False
    rows.append(pin)

cols = []
for p in COL_PINS:
    pin = digitalio.DigitalInOut(p)
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = True
    cols.append(pin)

LED_NAMES = [
    ["D1", "D2", "D3", "D4"],
    ["D5", "D6", "D7", "D8"],
    ["D9", "D10", "D11", "D12"],
    ["D13", "D14", "D15", "D16"],
]


def all_off():
    for r in rows:
        r.value = False
    for c in cols:
        c.value = True


def light(row_idx, col_idx):
    all_off()
    rows[row_idx].value = True
    cols[col_idx].value = False


def update_oled(name):
    oled.fill(0)
    oled.text("LED Matrix", 0, 0, 1)
    oled.text("Testing:", 0, 20, 1)
    oled.text(name, 0, 32, 1)
    oled.show()


while True:
    for r in range(4):
        for c in range(4):
            name = LED_NAMES[r][c]
            update_oled(name)
            light(r, c)
            time.sleep(0.15)
    all_off()
    time.sleep(0.3)
