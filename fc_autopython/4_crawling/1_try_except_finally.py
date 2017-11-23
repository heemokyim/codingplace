try:
    int('asdf')
    print("after error")
except Exception as e:
    print(e)
    print("ERROR!!")
finally:
    print("finally!!")

# --------------------------------
# int('asdf')

# 점선을 기준으로 코드 차이 확인
