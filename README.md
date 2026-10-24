# Healthcare Hackathon — CareTalk

A small, two-way clinician and patient conversation board. Each side can type or use browser speech recognition; messages appear in both windows. Optional machine translation can be enabled separately for each direction.

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000. Microphone dictation works in browsers that support the Web Speech API (typically Chrome and Edge) and requires microphone permission. Speech recognition is provided by the browser and may send audio to its speech service.

## Deploy to Vercel

Push this folder to a GitHub repository and import it into Vercel. Vercel detects the FastAPI app in `main.py`; no build command, custom routing, or environment variables are required.

Translation uses the MyMemory translation service through `/api/translate`. The text being translated is sent to that third-party service. Do not enter identifiable or sensitive health information unless your organization has reviewed and approved the services and privacy terms involved. Machine translations can be inaccurate; confirm important information with the patient. Conversation content remains in the open browser page and is not saved to a database.

Patient profiles (name, age, address, and preferred language) are saved in the current browser's local storage so they remain available after refresh. They are not encrypted, synced, or stored on the server. Use test data only; remove profiles from the patient selector when finished.

## Privacy and intended use

CareTalk is a prototype communication aid, not a medical record or a certified clinical translation service. It has no accounts, encryption layer, audit log, or compliance certification. Review your organization's security, privacy, and accessibility requirements before using it with patient information.
