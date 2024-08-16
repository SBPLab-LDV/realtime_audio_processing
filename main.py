import pyaudio
import wave
import numpy as np
import torch
import time
from collections import deque
from models.simple_network import SimpleNetwork

RATE = 44100
CHANNELS = 1
FORMAT = pyaudio.paInt16
FRAME_DURATION_MS = 20
CHUNK = int(RATE * FRAME_DURATION_MS / 1000)
BUFFER_MAX_SIZE = 10  # 保持較小的緩衝區

buffer = deque(maxlen=BUFFER_MAX_SIZE)
audio_file = None  # 全局變量來存儲音頻文件對象

model = SimpleNetwork()
model.load_state_dict(torch.load('models/simple_network.pth'))
model.eval()

def process_frame(frame):
    start_time = time.time()
    audio_array = np.frombuffer(frame, dtype=np.int16).copy()
    audio_float = audio_array.astype(np.float32) / 32767.0
    tensor = torch.from_numpy(audio_float).unsqueeze(0)
    with torch.no_grad():
        processed_tensor = model(tensor)
    processed_array = (processed_tensor.squeeze(0).numpy() * 32767.0).astype(np.int16)
    end_time = time.time()
    print(f"Frame processing time: {(end_time - start_time)*1000:.2f} ms")
    return processed_array.tobytes()

def callback(in_data, frame_count, time_info, status):
    if len(buffer) == 0:
        # 當緩衝區為空時，嘗試讀取更多數據
        data = audio_file.readframes(CHUNK)
        if data:
            buffer.append(data)
        else:
            # 文件結束
            return (None, pyaudio.paComplete)
    
    if buffer:
        data = buffer.popleft()
        processed_data = process_frame(data)
        print(f"Processed frame size: {len(processed_data)} bytes")
        return (processed_data, pyaudio.paContinue)
    else:
        print("Buffer empty, stopping stream")
        return (None, pyaudio.paComplete)

def main():
    global audio_file
    try:
        audio_file = wave.open("data/sin_wave.wav", 'rb')
        print(f"Opened WAV file: channels={audio_file.getnchannels()}, width={audio_file.getsampwidth()}, rate={audio_file.getframerate()}")
        
        p = pyaudio.PyAudio()
        try:
            stream = p.open(format=pyaudio.paInt16,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True,
                            frames_per_buffer=CHUNK,
                            stream_callback=callback)

            print("Starting audio stream")
            stream.start_stream()

            # 等待直到流停止
            while stream.is_active():
                time.sleep(0.1)
            print("Stream is no longer active")

        finally:
            if 'stream' in locals():
                stream.stop_stream()
                stream.close()
            p.terminate()
            audio_file.close()
            print("Audio stream closed and PyAudio terminated")

    except IOError as e:
        print(f"錯誤：無法打開音頻文件。{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")

    print("程序執行完成")

if __name__ == "__main__":
    main()