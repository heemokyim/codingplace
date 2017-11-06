import os
print(os.getcwd())

# list of directory in this path
print(os.listdir())

# glob() 함수는 경로에 대응되는 모든 파일 및 디렉터리의 리스트를 반환
# pip install glob2
# import glob2
# glob2.glob(path)
# ['file.txt','directory']
# ex) glob2.glob("*")
