import pyaudio
import numpy as np
import pyautogui

# 閾値（音が検出されるしきい値）を設定
THRESHOLD = 0.01

# マイクの設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 4800
CHUNK = 2048

cnt = 0

# マイクのストリームを開始
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

while True:
    # マイクから音声データを読み取り
    data = stream.read(CHUNK)
     # ndarrayに変換
    x = np.frombuffer(data, dtype="int16") / 32768.0

    # 音声データの振幅がしきい値を超えた場合、左クリックを模倣
    if x.max() > THRESHOLD:
        pyautogui.click()
        cnt += 1
        print(cnt)

    if cnt == 10000:
        break

   

# ストリームを停止し、マイクを閉じる
stream.stop_stream()
stream.close()
audio.terminate()
