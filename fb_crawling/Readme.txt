Crawling shared, non-public posts on my page from FaceBook Chrome Browser
(using Selenium)

1. Crawling -> Text file in designated path
(it needs 'index' file inside of same path)
(Note that no ':' in file path in Windows)

1-1. 다른 사람한테서 공유한 게시물 중 가능한 종류
  a. 게시물
  b. 사진
  c. 동영상
  d. 링크

1-2. 아직 구현 못한 것
  a. 문구
  b. 제품

  # What to put in file?
  # 1. 게시물 url
  # 1. 링크가 있다면 링크 url
  # 2. 이미지가 있다면 이미지 url
  # 1. 동영상이 있다면 동영상 url
  # 3. 텍스트
  # 4. 게시물에 달린 댓글 (텍스트, 이미지 url)

  # 예외처리해서 없으면 넘어가도 되게 처리

2. Password is read from local file system

3. It only crawls non-public, shared posts of my page
(skipping public posts)

4. Crawling list
each post of my page
  -> listrize shared posts of my page
    -> go to each source and crawl post and crawl replies
      -> store as text file of relavant text, link, comments etc

5. Exception logging == 'TODOL/exception.txt'
  a. 발생시간
  b. 링크
  c. 에러 메시지

--------------------------------------------------------------

1. 셀레니움 크롬 드라이버 다운로드 후 driver 폴더에 비치

2. 저장할 폴더 경로

3. 아이디, 비밀번호 설정

4. python app.py
--------------------------------------------------------------

element is not clickable error 뜨면 action chain으로 대체
1. vanila selenium을 가급적 쓴다.
2. clickable error가 나면 action chain으로 대체

--------------------------------------------------------------

페북 친구가 나한테 쓴 게시물은 태그가 달라서 그냥 스킵

-------------------------------------------------------------

TODOLIST
  1. 다른 사람이 내 탐라에 작성한 게시물은 태그가 다름

  2. 가끔 tag element가 deprecated된 동영상이 있다.
    이런 동영상 발견하면 태그 다시 분석해서 수정

  3. 내가 작성한 비공개 게시물에 더보기 있으면 누르고 가져오기

  4. 맨 위에서부터 긁어올 땐 문제가 안되지만
  아래 있는 게시물을 긁어올 땐 스크롤을 내려야만 가능함
  오래된 게시물일수록 시간이 오래걸림
    a. 브라우저를 두 개 만듦
    하나는 내 타임라인에서 링크 파악하고 숨기는 브라우저
    다른 하나는 파악된 링크 주소로 가서 크롤링하는 브라우저

  5. GUI 입히기
    a. 파일저장경로
    b. 페이스북 아이디, 비밀번호
    c. 전체 타임라인 검색
    d. 가장 최근 타임라인만 검색
