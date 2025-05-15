"""
터미널 설치 명령어:
[gTTS]
python -m venv myenv
.\myenv\Scripts\activate
pip install gTTS
pip install playsound==1.2.2

[STT]
pip install SpeechRecognition
Pip install PyAudio
"""

import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def listen(recognizer, audio):  #음성인식
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print("[사용자] "+ text)
        answer(text)
    except sr.UnknownValueError:
        print("인식실패")
    except sr.RecognitionError as e:
        print("요청 실패 : {0}".format(e))

def answer(input_text):     #대답
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요. 저는 인공지능스피커 입니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '개교 기념일' in input_text:
        answer_text = '천안고에 개교기념일은 7월 3일 입니다.'
    elif '설립' in input_text:
        answer_text = '천안고에 설립 날짜는 1954년 2월 19일 입니다.'
    elif '학생 수' in input_text:
        answer_text = '천안고에 학생 수는 1013명 입니다.'
    elif '길' in input_text:
        answer_text = '택시, 도보 대중교통을 이용할수 있고 대중교통은 3번, 7번, 2번, 12번, 20번, 910번이 있습니다.'
    elif '본관' in input_text:
        answer_text = '현재 본관은 공사중에 있습니다. 2024년 개학 전까지 완공될 예정입니다.'
    elif '열정관' in input_text:
        answer_text = '열정관은 1층부터 4층까지 있으며 1,2학년들 교실이 있습니다.'
    elif '우강관' in input_text:
        answer_text = '우강관은 3학년이 쓰는 곳입니다'
    elif '정심관' in input_text:
        answer_text = '정심관에는 도서관, 음악실, 공자학당, 미술실 등이 위치해 있습니다.'
    elif '웅비관' in input_text:
        answer_text = '웅비관은 기숙사 입니다.'
    elif '청마홀' in input_text:
        answer_text = '청마홀은 우강관 1층에 위치해 있습니다.'
    elif '과학관' in input_text:
        answer_text = '과학관은 우강관 매화관 사이에 있으며 모든 과학실이 있습니다.'
    elif '매화관' in input_text:
        answer_text = '급식실 입니다.'
    elif '보건실' in input_text:
        answer_text = '정심관 1층에 위치해 있습니다.'
    elif '행정실' in input_text:
        answer_text = '우강관 1층에 위치해 있습니다.'
    elif '급식실' in input_text:
        answer_text = '매화관에 위치해 있으며 과학관 옆에 있습니다.'
    elif '정보공학' in input_text:
        answer_text = '과학관 2층에 위치해 있습니다.'
    elif '루이스' in input_text:
        answer_text = '과학관 1층에 있습니다.'
    elif '플레밍' in input_text:
        answer_text = '과학관 1층에 있습니다.'
    elif '베게너' in input_text:
        answer_text = '과학관 1층에 있습니다.'
    elif '뉴턴' in input_text:
        answer_text = '과학관 1층에 있습니다.'
    elif '1학년' in input_text:
        answer_text = '1학년 교실은 열정관 3,4층에 위치해 있습니다.'
    elif '2학년' in input_text:
        answer_text = '2학년 교실은 열정관 1,2층에 위치해 있습니다.'
    elif '3학년' in input_text:
        answer_text = '3학년 교실은 우강관 3,4층에 위치해 있습니다.'
    elif '진로 마루' in input_text:
        answer_text = '진로마루는 열정관 3층에 위치해 있습니다'
    elif '진로활동' in input_text:
        answer_text = '진로활동실은 열정관 3층에 위치해 있습니다'
    elif '홈 베이스' in input_text:
        answer_text = '홈베이스는 열정관 1,2층에 있습니다.'
    elif '음악실' in input_text:
        answer_text = '음악실은 정심관 1층에 위치해 있습니다'
    elif '미술실' in input_text:
        answer_text = '미술실은 정심관 1층에 위치해 있습니다'
    elif '공자학당' in input_text:
        answer_text = '공자학당은 정심관 1층에 위치해 있습니다'
    elif '체육실' in input_text:
        answer_text = '체육실은 정심관 1층에 위치해 있습니다'
    elif '도서관' in input_text:
        answer_text = '도서관은 정심관 2층에 위치해 있습니다'
    elif '본부 교무실' in input_text:
        answer_text = '본부교무실은 정심관 2층에 위치해 있습니다'
    elif '박주병' in input_text:
        answer_text = '박주병선생님은 진로과목을 맡고 계십니다'
    elif '박종연' in input_text:
        answer_text = '박종연선생님은 1학년 한국사, 3학년 세계사를 맡고 계시는 선생님 입니다.'
    elif '박정호' in input_text:
        answer_text = '박정호선생님은 사회과목을 맡고 계십니다'
    elif '김길용' in input_text:
        answer_text = '김길용선생님은 중국어과목을 맡고 계십니다'
    elif '김주윤' in input_text:
        answer_text = '김주윤선생님은 국어과목을 맡고 계십니다'
    elif '김영진' in input_text:
        answer_text = '김영진선생님은 수학과목을 맡고 계십니다'
    elif '이태호' in input_text:
        answer_text = '이태호선생님은 과학과목을 맡고 계십니다'
    elif '이효영' in input_text:
        answer_text = '이효영선생님은 국어과목을 맡고 계십니다'
    elif '김세명' in input_text:
        answer_text = '김세명선생님은 음악과목을 맡고 계십니다'
    elif '문경호' in input_text:
        answer_text = '문경호선생님은 영어과목을 맡고 계십니다'
    elif '박선정' in input_text:
        answer_text = '박선정선생님은 한국사과목을 맡고 계십니다'
    elif '정지용' in input_text:
        answer_text = '정지용선생님은 체육과목을 맡고 계십니다'
    elif '김민하' in input_text:
        answer_text = '김민하선생님은 과탐과목을 맡고 계십니다'
    elif '유민아' in input_text:
        answer_text = '유민아선생님은 사회과목을 맡고 계십니다'
    elif '방강훈' in input_text:
        answer_text = '방강훈선생님은 체육과목을 맡고 계십니다'
    elif '이태호' in input_text:
        answer_text = '이태호선생님은 수학과목을 맡고 계십니다'
    elif '김지형' in input_text:
        answer_text = '김지형선생님은 정보과목을 맡고 계십니다'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '무슨 말씀인지 이해하지 못했어요.'
    speak(answer_text)

def speak(text):    #소리내어 읽어 줌
    print("[인공지능] "+text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak("무엇을 도와드릴까요?")
stop_listening = r.listen_in_background(m, listen)
#stop_listening(wait_for_stop=False)

while True:
    time.sleep(0.1)