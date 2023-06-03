import board
from digitalio import DigitalInOut, Direction
try:
    from audioio import AudioOut
    audio = AudioOut(board.A0)
except Exception:
    import audiopwmio
    audio = audiopwmio.PWMAudioOut(board.A0)

from audiocore import WaveFile
import adafruit_dotstar
import neopixel

f = open("thermo.wav", "rb")
decode = WaveFile(f)

neop = False
try:
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
except Exception:
    pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
    neop = True

yellow1 = DigitalInOut(board.D10)
yellow1.direction = Direction.OUTPUT
yellow2 = DigitalInOut(board.D9)
yellow2.direction = Direction.OUTPUT
yellow3 = DigitalInOut(board.D7)
yellow3.direction = Direction.OUTPUT
pattern = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 1, 0],
    [0, 1, 1],
]
pattern_len = len(pattern)

x = 0
while True:
    audio.play(decode)

    if neop:
        pixel.fill((pattern[x][0] * 255, pattern[x][1] * 255, pattern[x][2] * 255))
    else:
        led[0] = (pattern[x][0] * 255, pattern[x][1] * 255, pattern[x][2] * 255)

    yellow1.value = pattern[x][0]
    yellow2.value = pattern[x][1]
    yellow3.value = pattern[x][2]
    x = (x + 1) % pattern_len
    print(pattern[x])

    while audio.playing:
        pass
