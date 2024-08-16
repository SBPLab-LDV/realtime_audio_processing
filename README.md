# Real-time Audio Processing Project

This project demonstrates real-time audio processing and playback using a PyTorch neural network.

## Features

- Generate a sine wave audio file
- Process audio in real-time using a simple PyTorch neural network
- Stream processed audio to the speaker

## Prerequisites

- Python 3.7+
- PyTorch
- NumPy
- PyAudio

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/realtime-audio-processing.git
   cd realtime-audio-processing
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Generate the test audio file:
   ```
   python scripts/generate_sin_wave.py
   ```

2. Create and save the simple neural network model:
   ```
   python scripts/train_simple_network.py
   ```

3. Run the main program for real-time audio processing and playback:
   ```
   python main.py
   ```

## Project Structure

- `data/`: Directory for storing audio files
- `models/`: Contains neural network model definitions
- `utils/`: Contains utility functions and tools
- `scripts/`: Contains standalone scripts
- `main.py`: Main program for audio processing and playback
- `requirements.txt`: Project dependencies
- `README.md`: This file

## Notes

- Ensure your system's audio devices are properly configured.
- Adjusting `BUFFER_MAX_SIZE` and `FRAME_DURATION_MS` in `main.py` may affect latency and audio quality.
- This project is designed for educational purposes and may not be suitable for production environments without further optimization.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
