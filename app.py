from fastapi import FastAPI
from gtts import gTTS
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return "Enter any text in the URL"

@app.get("/{text}")
def generate_audio(text: str):
    output_file = "output.mp3"
    tts = gTTS(text=text, slow=True)
    tts.save(output_file)
    return FileResponse(output_file, media_type="audio/mpeg", filename=output_file, headers={"Content-Disposition": "inline"})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)