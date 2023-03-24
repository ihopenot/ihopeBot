# General Chat Bot

## Install

`pip install -r requuirements.txt`

## Usage

Create a config.yaml first.

Example:
```
TTS:
  type: azure
  subscription: YOUR_AZURE_KEY
  region: YOUR_AZURE_REGION
Sr:
  type: azure
  subscription: YOUR_AZURE_KEY
  region: YOUR_AZURE_REGION
Chat:
  type: tcp
  ip: YOUR_CHAT_BOT_IP
  port: YOUR_CHAT_BOT_PORT
```

Run this bot with command:
`python main.py`

## SubModuels

### TTS
Now supports:
- [x] Azure Text to Speech


### Sr
Now supports:
- [x] Azure Speech Recognize

### Chat
Now supports:
- [x] Raw Tcp ChatBot