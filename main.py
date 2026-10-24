from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(title="CareTalk")
PAGE = Path(__file__).resolve().parent / "public" / "index.html"


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1, max_length=5000)
    source: str = Field(min_length=2, max_length=10)
    target: str = Field(min_length=2, max_length=10)


@app.get("/")
async def home():
    return FileResponse(PAGE)


@app.post("/api/translate")
async def translate(payload: TranslationRequest):
    if payload.source == payload.target:
        return {"translation": payload.text}
    try:
        async with httpx.AsyncClient(timeout=12) as client:
            response = await client.get(
                "https://api.mymemory.translated.net/get",
                params={"q": payload.text, "langpair": f"{payload.source}|{payload.target}"},
            )
            response.raise_for_status()
            data = response.json()
        if data.get("responseStatus") != 200:
            raise HTTPException(status_code=502, detail="Translation service could not translate this text.")
        return {"translation": data["responseData"]["translatedText"]}
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=502, detail="Translation service is temporarily unavailable.") from exc
