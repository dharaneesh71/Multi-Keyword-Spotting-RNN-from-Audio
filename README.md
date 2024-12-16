# Multi Keyword Spotting (Multi-KWS) Using RNN

## Overview
This project focuses on developing a Multi-Keyword Spotting (Multi-KWS) system using Recurrent Neural Networks (RNNs). The system is designed to detect multiple keywords in continuous audio data accurately and efficiently, addressing challenges such as varying acoustic conditions and linguistic diversity.

## Features
- **Keyword Detection**: Simultaneous recognition of multiple keywords in audio streams.
- **Deep Learning Models**: Includes RNN architectures like LSTM, GRU, BiRNN, and CRNN.
- **Performance Evaluation**: Measures accuracy, latency, true acceptance (TA), false acceptance (FA), and model footprint.
- **Dataset Augmentation**: Uses audio augmentations for robust training.

## Applications
- Voice Assistants
- Transcription Services
- Security Systems
- Customer Support Automation

## Dataset
- **Audio Samples**: 500+ audio files with 50 distinct keywords.
- **Preprocessing**: Spectrograms and Mel-Frequency Cepstral Coefficients (MFCCs) for feature extraction.

## Model Architectures
The project implements and evaluates eight RNN models:
- **LSTM**: Two architectures with varying hidden units and layers.
- **GRU**: Two architectures optimized for efficiency.
- **BiRNN**: Combines GRU and LSTM for improved sequential understanding.
- **CRNN**: Merges convolutional layers with RNNs for feature-rich embeddings.

## Performance Metrics
- **True Acceptance (TA) Rate**
- **False Acceptance (FA) Rate**
- **Latency**: Time to process audio inputs.
- **Footprint**: Memory usage and model size.

| Model       | Hidden Units | Layers | Size (MB)  |
|-------------|--------------|--------|------------|
| LSTM 1      | 64           | 2      | 14.97      |
| LSTM 2      | 128          | 2      | 34.13      |
| GRU 1       | 64           | 2      | 11.42      |
| GRU 2       | 64           | 3      | 12.56      |
| BiRNN 1     | 128 (GRU)    | 2      | 23.65      |
| BiRNN 2     | 128 (LSTM)   | 2      | 31.13      |
| CRNN 1      | 64 (GRU)     | 4      | 7.41       |
| CRNN 2      | 128 (LSTM)   | 4      | 36.72      |

## Experimental Results
- The CRNN model with GRU layers achieved the smallest footprint and high accuracy, making it suitable for resource-constrained devices.
- Data augmentation improved robustness against varying acoustic conditions.

## Technologies Used
- **Framework**: TensorFlow
- **Languages**: Python
- **Audio Preprocessing**: Spectrograms, MFCCs

## Usage
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Dataset Preparation**:
   - Organize audio files into folders for training, validation, and testing.
   - Apply augmentations for dataset enhancement.

3. **Model Training**:
   - Train each model using the `train_model.py` script.
   ```bash
   python train_model.py --model_type <model_name>
   ```

4. **Evaluation**:
   - Evaluate models using `evaluate_model.py`.
   ```bash
   python evaluate_model.py --model_path <path_to_model>
   ```

5. **Deployment**:
   - Deploy optimized models on edge devices with minimal latency.

## Future Work
- Integrating more robust architectures like Transformers for Multi-KWS.
- Expanding datasets to include multilingual audio samples.
- Optimizing latency for real-time applications.

## References
- [Natural Language Processing - IBM](https://www.ibm.com/topics/natural-language-processing)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [Audio Classification with CNNs](https://www.atmosera.com/blog/audio-classification-with-cnns)
