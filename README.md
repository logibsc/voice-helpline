# voice-helpline

    A voice powered intelligent assistant that allows users to ask questions via speech and get natural responses using gemini-1.5-pro. The assistant speaks the answer
back, making it feel like a real conversation.

## Features

- Speech to Text - using `speech_recognition`
- Gemini Model - for AI generated responses
- Text to Speech - using `pyttsx3`
- Modular and scalable code structure
- Designed for local use in VS Code

## Future Enhancements

- Document Based RAG - using `langchain` and `FAISS`
- Personalized memory
- Real time voice assistant (call interface)

## Tech Stack

- Python 3.10+ (recommended)
- [Google Generative AI (Gemini)] (https://ai.google.dev/)
- `speech_recognition`
- `pyttsx3`
- `pyaudio`
- `dotenv` for environment management

## Project Structure

voice-helpline
    app
       api
        gemini_api.py 
       __init__.py
       config.py
       document_handler.py
       stt.py
       tts.py
    uploads
    venv
    venv310
    .env
    .gitignore
    client.py(for test purpose only. no need)
    LICENSE
    main.py
    README.md
    requirements.txt


## Environment Setup

- Create a `.env` file in the roor with:

GEMINI_API_KEY = your actual api key

## Install dependencies:

```bash
pip install -r requirements.txt

## License

MIT License


** Let me know your thoughts ** 