from flask import Flask, jsonify, request
from apscheduler.schedulers.background import BackgroundScheduler
import requests
import json
import time

from WriteMecro import WriteMecro

# 3분마다 방송 상태 확인
def scheduler():

    check_Broadcasting()

# 스케줄러 설정
schedule = BackgroundScheduler(daemon=True, timezone='Asia/Seoul')
schedule.add_job(scheduler, 'interval', seconds=30)
schedule.start()


app = Flask(__name__)

# 전역 변수로 방송 상태를 저장
streaming = False

# 방송 상태 변경 메소드
def streaming_task(value):
    global streaming
    streaming = value

# 테스트용 ========
@app.route('/dc')
def write_dc():
    dc = WriteMecro()
    dc.dc_mecro()
    return "Hello, World!"


@app.route('/ruri')
def write_ruri():
    ruri = WriteMecro()
    ruri.ruri_mecro()
    return "Hello, World!"

# ========

@app.route('/')
def start():
    check_Broadcasting()

# 핵심 비지니스 로직
def check_Broadcasting():

    # api를 통한 방송 정보 획득
    res = requests.get('https://bjapi.afreecatv.com/api/vllagekanin/station',
                       headers={'User-Agent': 'Mozilla/5.0'}).json()

    data = json.dumps(res)
    data = json.loads(data)

    # broad == 방송 정보(user_id, broad_no, broad_title, current_sum_viwer, broad_grade, is_passward
    # 방송 없으면 null 값
    board_values = data.get("broad")

    print("방송 상태 체크")

    # 방송을 하고 있고, 방송 정보가 false라면 글 작성 메크로 작동
    if board_values != None:

        if streaming == False:
            # 방송 상태 변수값 변경
            streaming_task(True)
            print("방송중!!")

            print(board_values)
            title = board_values.get("broad_title")
            print(title)

            dc = WriteMecro()
            dc.dc_mecro(title)

    # 방송 없을 경우
    else:
        if streaming == True:
            # 방송 상태 변수값 변경
            streaming_task(False)

        print("No Broadcasting")

    return board_values


if __name__ == '__main__':
    app.run()
