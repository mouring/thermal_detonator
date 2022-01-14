import board
from digitalio import DigitalInOut, Direction
from audioio import AudioOut
from audiocore import WaveFile

# audio file / Audio Stream Init
f = open("thermo.wav", "rb")
decode = WaveFile(f)
audio = AudioOut(board.A0)

# LEDs
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

    yellow1.value = pattern[x][0]
    yellow2.value = pattern[x][1]
    yellow3.value = pattern[x][2]
    x = (x + 1) % pattern_len
    print(pattern[x])

    while audio.playing:
        pass
