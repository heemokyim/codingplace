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
        time.sleep(0.5)

    return point

result_list = get_11st('자전거')

wb = Workbook()
ws = wb.active
ws.append(['상품명','가격','판매자명'])
for product in result_list:
    ws.append(product)

base_dir = '/home/ej/codingplace/fc_autopython/7_application/data'
print(base_dir+'/result.xlsx')
wb.save(base_dir + '/result.xlsx')

# Mac에서 실행
run(['open','-a','kakaotalk'])

# Windows에서 실행
run(['C:\\KAKAOTALK_PATH'])

time.sleep(1)

py.PAUSE = 1

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
py.click(point[0]-22, point[1]+40)
# Windows 사용 시 나에게 보내기 클릭하기
py.click(point[0]+90, point[1]+190)
py.press('enter')
