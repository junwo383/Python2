# 오늘의파이썬  나만의 기초코딩 ~  2문제  

# 나는 길을 가다가 자동차 번호판 봤는데 우연차있게 123가 1234 번호판을 조회해보고싶은데 마침 내가 파이썬을 배우고있다.! 파이썬을 이용해서
# 번호판을 조회를 해보자! 

#조건1 : 앞번호 123가 조회하고  다음번호 1234 조회하시오 다하고 마지막에 번호판 모두를 조회하세요!

# 함수 조건 : 인덱싱(슬라이딩) , 변수, print문 이거만쓸것!

print("번호판을 조회를 해보자!")

car_number = "123가 1234" # 변수입니다

print("앞번호 조회하시오") # print문입니다

print(car_number[0:4]) # 인덱싱 슬라이딩 문입니다

print("뒷번호 조회하시오")

print(car_number[5:]) # 슬라이딩문 이렇게 5: 123가 에서 1234만 출력이가능합니다.

print(str(car_number)+"조회가완료되었습니다.") # 변수에서 문자를 출력할때+ 해줘야 출력이됩니다. str 해줘야합니다.


#이상으로 마치겠습니다 . 다음파이썬기초문법 코딩시간때뵈용!