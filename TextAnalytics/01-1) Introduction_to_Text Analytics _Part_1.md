# 01 Text Analytics: Overview

강의 링크: [https://www.youtube.com/watch?v=UInnl60pzkA&list=PLetSlH8YjIfVzHuSXtG4jAC2zbEAErXWm](https://www.youtube.com/watch?v=UInnl60pzkA&list=PLetSlH8YjIfVzHuSXtG4jAC2zbEAErXWm)

## Background

80% 이상의 새로 생기는 데이터들은 비정형 데이터이고, 그중에서도 text data가 큰 비중을 차지한다.

검색어에 맞는 문서를 반환(retrieval) 해주는 것 만으로는 충분하지 않다. 

⇒ 새로운 지식을 찾아내는 것이 요구됨!

## Definition

> Text Data를 다양한 방법론으로 분석하여 의미있는 지식을 추출
> 

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F84e6de30-7f51-44f1-894b-40b592d68975%2FUntitled.png?table=block&id=1342e040-a1b1-431a-9654-0eb7ed1c5f72&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1530&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

## Applications

1. 한국은행을 포함한 전 세계 중앙 은행 총재들의 주기적인 연설문 또는 공고문을 영어로 번역한 웹사이트

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F4c73e844-b7d4-4574-bfef-9c043f7ebc78%2FUntitled.png?table=block&id=3fe8db8b-f084-4a17-bb46-f9c9597ca8f0&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1530&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

연설문 속 단어를 통해 각국의 통화정책에 대한 방향성, 즉 비슷한 국가들에 대해 파악해 보자는 목적

문서를 특정 길이의 벡터로 표현하여 유사성을 계산하고 고차원의 피처를 차원 축소하여 나타냄

1. 추천 (Recommendation)

![Untitled](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fefbbeabc-e0ba-4239-b155-3a31f54398cc%2FUntitled.png?table=block&id=0ba5a235-7017-41c8-ad09-27b27969592d&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1530&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

가볼만한 곳으로 뜨는 여행지들은 사용자의 블로그에 대한 텍스트 본문을 분석하여 가장 긍정적인 뉘앙스가 많았던 여행지 순으로 보여주는 것

![맛집 랭킹을 보여주는 다이닝 코드 앱](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F601b1e68-bf5d-4fa5-ad9c-4f5e9e701da1%2FUntitled.png?table=block&id=75e12514-5d1a-4904-95f9-4ca5fd6c0a71&spaceId=3aa9293f-6175-4ef8-ab1f-5ac6c7c6e16d&width=1530&userId=5559e7d5-3152-49d5-b79d-7aabc7a64dce&cache=v2)

맛집 랭킹을 보여주는 다이닝 코드 앱

광고성 블로그는 필터링하고 인플루언서들의 영향력을 크게 반영한 서비스

1. 질의응답 (Question Answering)

구글에서는 위키 데이터를 통해 질문이 주어지면 답이 어디에 있는지 찾아가는 방식으로 QA 데이터를 생성

📃 papers with code

[Papers with Code - The latest in Machine Learning](https://paperswithcode.com/)

특정 task에 대해 sota에 가까운 성능을 나타내는 논문들, 혹은 해당하는 github 코드를 공유하는 site

1. 챗봇 (Dialogue system)

QA의 궁극적 목적은 대화형 시스템을 만드는 것

지금까지는 사용자가 제시하는 키워드에 대해 rule base로 적합한 답변을 만들어 주었지만, 최종 목적은 사람과 구별이 불가할 정도의 챗봇을 만드는 것

## Challenges

1. 차원의 수가 굉장히 크다 (word, phrases, etc.)
    
    - 한국어는 위키기준 110만개의 단어, 영어는 17만개의 단어가 존재
    
2. 단어의 개념 자체가 모호하다
    1. 장명준은 즐겁게 오버워치를 하다가 지도교수에게 들켰다.
    2. 강필성 교수는 우연히 들른 신공학과 220호에서 게임을 하는 한 학생을 목격했다.
    
    - 사람의 경우는 문장 a, b가 같은 의미라는 것을 본능적으로 파악할 수 있지만 컴퓨터는 단어 빈도 기반이기 때문에 두 문장을 전혀 관계없는 문서로 파악할 확률이 높음
    

## Text Structures

> 얼마나 "비구조화" 되어있느냐?
> 

1. Weakly structured
- 어느 정도의 포맷이 존재
- research papers, legal memoranda, news stories, etc.

1. Semi-structured
- weakly structured 보다는 좀더 포맷이 확장
- E-mail, HTML/XML web pages, pdf files, etc.