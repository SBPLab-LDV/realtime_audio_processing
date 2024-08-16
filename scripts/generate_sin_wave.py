from utils.audio_utils import generate_sin_wave, save_wave_file

if __name__ == "__main__":
    sample_rate = 44100
    frequency = 440
    duration = 5
    sin_wave = generate_sin_wave(frequency, duration, sample_rate)
    save_wave_file('data/sin_wave.wav', sin_wave, sample_rate)
    print("Sin wave 已生成並保存為 'data/sin_wave.wav'")