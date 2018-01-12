from auto_11st import get_11st
from openpyxl import Workbook
from subprocess import run
# subprocess = 외부파일을 실행할 수 있게 해줌 (ex. 카카오톡 실행)
import pyautogui as py
import time

def get_target(filename):
    ret = 3
    point = None

    for idx in range(ret):
        point = py.locateCenterOnScreen(filename)
        if point:
            break
        time.sleep(0.1)

    return point

# result_list = get_11st('자전거')
#
# wb = Workbook()
# ws = wb.active
# ws.append(['상품명','가격','판매자명'])
# for product in result_list:
#     ws.append(product)

# Linux folder path
# base_dir = '/home/ej/codingplace/fc_autopython/7_application/data'

# Windows folder path
base_dir = 'D:\\codingplace\\fc_autopython\\7_application\\data'
# print(base_dir+'/result.xlsx')

# wb.save(base_dir + '/result.xlsx')

# Mac에서 실행
# run(['open','-a','kakaotalk'])

# Windows에서 실행
run(['D:\\카카오톡\\KakaoTalk\\KakaoTalk.exe'])

# time.sleep(0.1)

# py.PAUSE = 1

width,height = py.size()
print(width,height)

# Mac 사용 시 단축키를 눌러 친구 목록으로 이동
# py.hotkey('command','1')

#  Windows 사용 시 헤더를 클릭하여 친구 목록을 선택해야 함
point = get_target('kakao.png')
if not point:
    print('카톡을 찾을 수 없습니다')
    quit()

print(point)

# 친구 목록 선택
# py.click(point[0]-30, point[1]-40)

# Windows 사용 시 나에게 보내기 클릭하기
py.click(point[0], point[1])
# py.press('down')
# time.sleep(0.1)
py.press('enter')

# time.sleep(0.1)
py.click(point[0],point[1])
# time.sleep(0.1)
py.click(point[0],point[1] + 100)
py.hotkey('alt', 'tab')

# MAc에서 폴더 열기
# run(['open','base_dir'])

# Windows에서 폴더 열기
run(['cmd','/c','start',base_dir])

# 두 번째 시행 시 인식이 안되는 문제해결
# time.sleep(0.2)
py.keyDown('alt')
py.keyDown('f4')
py.keyUp('f4')
py.keyUp('alt')
# time.sleep(0.2)
run(['cmd','/c','start',base_dir])
# time.sleep(0.1)

point = get_target('header.png')
if not point:
    print('탐색기를 찾을 수 없습니다.')
    quit()

print(point)
# 해당 파일 화면상 위치
# py.moveTo(point[0], point[1])
py.click(point[0], point[1])

send_point = get_target('send_btn.png')
if not send_point:
    print('보내기 버튼을 찾을 수 없습니다.')
    quit()
print(send_point)

py.dragTo(send_point[0]+180, send_point[1]-38, button='left')
