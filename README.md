# J.A.R.V.I.S. Chatbot

A conversational AI assistant inspired by Tony Stark's J.A.R.V.I.S., built using the Llama model and Streamlit. This chatbot maintains a professional yet witty personality while addressing users as "Mr. Stark" and supports both English and Portuguese languages.

## Features

- 🤖 Jarvis-like personality with British humor
- 💬 Natural conversation flow in English or Portuguese
- 🎭 Consistent character role-playing
- 🔄 Context-aware responses
- 🖥️ Modern web interface
- 🌐 Bilingual support
- 📱 Responsive design

## Prerequisites

- Python 3.x
- Llama model file
- Environment variable `MODEL_PATH` set to your Llama model file location

## Setup

1. Clone this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the environment variable for your model path:
   ```bash
   # On Windows
   set MODEL_PATH=path\to\your\llama\model

   # On Linux/Mac
   export MODEL_PATH=path/to/your/llama/model
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. The application will open in your default web browser

3. Features:
   - Select your preferred language (English/Português)
   - Chat with Jarvis using the input field
   - View conversation history
   - Clear conversation using the "Clear Conversation" button

## Example Conversations

### English
```
Jarvis: Good day, Mr. Stark. How may I assist you today?
Mr. Stark: What's the weather like?
Jarvis: I'm afraid I don't have direct access to weather data, Mr. Stark. However, I can suggest checking your Stark Industries weather monitoring system or the local meteorological service. Would you like me to help you with that?
```

### Português
```
Jarvis: Bom dia, Sr. Stark. Como posso ajudá-lo hoje?
Sr. Stark: Como está o tempo hoje?
Jarvis: Infelizmente não tenho acesso direto aos dados meteorológicos, Sr. Stark. No entanto, posso sugerir verificar o sistema de monitoramento climático da Stark Industries ou o serviço meteorológico local. Gostaria que eu o ajudasse com isso?
```

## Customization

You can modify the system prompts and messages in `config.py` to adjust Jarvis's personality traits, tone, or response style in either language.

## License

This project is open source and available under the MIT License. 