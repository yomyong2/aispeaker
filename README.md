# 천안고 인공지능 음성 비서 👂🧠🗣

> 천안고등학교의 다양한 정보를 음성으로 알려주는 AI 스피커 프로젝트입니다.  
> 사용자의 질문을 음성으로 인식하고, 텍스트 분석을 통해 음성으로 대답해줍니다.

---

## 🛠 기능 소개

- 🎤 **STT (Speech to Text)**: 사용자의 음성을 실시간으로 인식
- 🧠 **키워드 분석**: 천안고 관련 질문을 판별해 적절한 응답 생성
- 🔊 **TTS (Text to Speech)**: 대답을 자연스러운 음성으로 출력
- 🏫 **학교 정보 내장**: 교사 정보, 건물 위치, 학년별 교실 등 수십 가지 응답 가능


---

## ✅ 실행 방법

### 1. 가상환경 생성 및 실행 (Windows 기준)

```bash
python -m venv myenv
.\myenv\Scripts\activate
```

### 2. 필요 라이브러리 설치

```bash
pip install -r requirements.txt
```

`requirements.txt` 파일이 없다면 아래를 수동으로 입력:

```bash
pip install gTTS
pip install playsound==1.2.2
pip install SpeechRecognition
pip install PyAudio
```

### 3. 프로그램 실행

```bash
python ai_speaker.py
```

---

## 🧪 예시 질문

다음과 같은 질문을 할 수 있습니다:

- "천안고 개교기념일이 언제야?"
- "본관 어디에 있어?"
- "김길용 선생님은 어떤 과목 가르쳐?"
- "3학년 교실은 어디야?"
- "도서관 어디에 있어?"
- "종료" → 프로그램 종료

---

## 💡 사용 기술

- Python 3.x
- [gTTS](https://pypi.org/project/gTTS/) - Google Text-to-Speech
- [playsound](https://pypi.org/project/playsound/) - 오디오 재생
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - 음성 인식
- [PyAudio](https://pypi.org/project/PyAudio/) - 마이크 입력

---

## 🙋🏻‍♂️ 기여 및 라이선스

이 프로젝트는 천안고등학교 학생들을 위해 제작되었습니다.  
더 많은 기능을 추가하고 싶으시다면 자유롭게 포크하고 Pull Request를 보내주세요!

---

## 📞 문의

개발자 이메일 또는 GitHub Issues를 통해 문의해주세요.
