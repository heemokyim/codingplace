Crawling shared posts on my page from FaceBook Chrome Browser
(using Selenium)

1. Crawling -> Text file in designated path
(it needs 'index' file inside of same path)
(Note that no ':' in file path in Windows)

  # What to put in file?
  # 1. 게시물 url
  # 1. 링크가 있다면 링크 url
  # 2. 이미지가 있다면 이미지 url
  # 1. 동영상이 있다면 동영상 url
  # 3. 텍스트
  # 4. 게시물에 달린 댓글

  # 예외처리해서 없으면 넘어가도 되게 처리

2. Password is read from local file system

3. It only crawls non-public, shared posts of my page
(skipping public posts)

4. Crawling list
each post of my page
  -> listrize shared posts of my page
    -> go to each source and crawl post and crawl replies
      -> store as text file of relavant text, link, comments etc

--------------------------------------------------------------
1. 셀레니움 크롬 드라이버 다운로드 후 driver 폴더에 비치

2. 저장할 폴더 경로

3. 아이디, 비밀번호 설정

4. python app.py
--------------------------------------------------------------
element is not clickable error 뜨면 action chain으로 대체
1. vanila selenium을 가급적 쓴다.
2. clickable error가 나면 action chain으로 대체
