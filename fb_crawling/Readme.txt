Crawling shared posts on my page from FaceBook Chrome Browser
(using Selenium)

1. Crawling -> Text file in designated path
(it needs 'index' file inside of same path)

2. Password is read from local file system

3. It only crawls non-public, shared posts of my page
(skipping public posts)

4. Crawling list
each post of my page
  -> listrize shared posts of my page
    -> go to each source post and crawling
      -> store as text file of relavant text, link, comments etc

--------------------------------------------------------------
To-do-list
1. read constant from separate file

2. 게시물의 댓글도 가져오는 기능
  a. 더보기 누름
  b. 댓글의 댓글보기 누름
  c. 댓글과 댓글의 댓글도 가져옴
