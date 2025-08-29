# Flask 웹 프레임워크, HTML 렌더링, 폼 데이터 처리 함수 임포트
from flask import Flask, render_template, request
import os
from io import BytesIO           # 메모리 버퍼(파일처럼 사용) 제공
from gtts import gTTS            # Google Text-to-Speech 라이브러리
import base64                    # 바이너리 데이터를 base64로 인코딩/디코딩
from datetime import datetime     # 현재 시간 기록용

# 환경변수에서 기본 언어를 가져오고, 없으면 'ko'(한국어)로 설정
DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')

app = Flask(__name__)

# 루트 URL('/')에 대해 GET, POST 요청 모두 처리
@app.route("/", methods=["GET", "POST"])
def home():
    error = None   # 에러 메시지 저장 변수
    audio = None   # 변환된 음성(base64 인코딩) 저장 변수
    ALLOWED_LANGS = {"ko", "en", "ja", "es"}  # 허용 언어 목록

    # POST 요청(폼 제출)일 때만 실행
    if request.method == "POST" :
        # 폼에서 입력한 텍스트와 언어를 가져옴
        text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", DEFAULT_LANG)

        # 언어가 허용된 값인지 확인
        if lang not in ALLOWED_LANGS:
            error = "지원하지 않는 언어입니다."

        # 텍스트가 비어있으면 에러 메시지
        elif not text:
            error = "텍스트를 입력하세요."
        else :
            try :
                # gTTS로 텍스트를 음성(mp3)으로 변환
                fp = BytesIO()  # 메모리 버퍼 생성
                tts = gTTS(text, lang=lang)  # TTS 객체 생성
                tts.write_to_fp(fp)          # mp3 데이터를 버퍼에 저장
                fp.seek(0)                   # 버퍼의 처음으로 이동
                # mp3 데이터를 base64로 인코딩(HTML에 직접 삽입하기 위함)
                audio = base64.b64encode(fp.read()).decode("utf-8")
                # 입력 내역을 로그 파일에 저장
                with open("input_log.txt", "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now()} | {text} | {lang}\n")
            except Exception as e :
                # TTS 변환 실패 시 에러 메시지
                error = "TTS 변환에 실패했습니다."
    # GET 요청이든 POST 요청이든 index.html을 렌더링(에러/오디오 데이터 전달)
    return render_template("index.html", error=error, audio=audio)

# 이 파일을 직접 실행할 때만 Flask 서버를 실행
if __name__ == '__main__':
    app.run('0.0.0.0', 8080)  # 0.0.0.0:8080에서 서버 실행(외부 접속 허용)