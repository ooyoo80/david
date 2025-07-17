from flask import Flask, render_template, request
import os
from io import BytesIO
from gtts import gTTS
import base64                 
from datetime import datetime     


DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    audio = None
    ALLOWED_LANGS = {"ko", "en", "ja", "es"}

   
    if request.method == "POST" :
        
        text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", DEFAULT_LANG)

        
        if lang not in ALLOWED_LANGS:
            error = "지원하지 않는 언어입니다."
        elif not text:
            error = "텍스트를 입력하세요."

        else :
            try :
                fp = BytesIO()
                tts = gTTS(text, lang=lang)
                tts.write_to_fp(fp)
                fp.seek(0)
               
                audio = base64.b64encode(fp.read()).decode("utf-8")
               
                with open("input_log.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} | {text} | {lang}\n")

            except Exception as e :
                error = "TTS 변환에 실패했습니다."
    
    return render_template("index.html", error=error, audio=audio)


if __name__ == '__main__':
    app.run('0.0.0.0', 8080)