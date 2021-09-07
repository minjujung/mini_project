# 프로젝트명 : 오늘도 돼지런!!
>
##### <span style="color:royalblue"> - 행복했던 식사를 잊지 않도록 기록하는 '추억 저장 플랫폼'<br> - 너무나 부지런하게 챙겨먹는다는 의미인 "돼지런하다"에서 네이밍 채용 <br> - 4일동안 함께 진행했던 좌충우돌 생존 스파르타 미니 프로젝트!<br>- 비전공자 4명이 부트캠프 첫 시작 후 만든 미니프로젝트 </span>

<깃헙주소>
https://github.com/goplanit/team35_project

<도메인주소>
http://manju.shop/

---
### 프로젝트 화면
<Home 페이지>
![](https://images.velog.io/images/goplanit/post/01b71a82-090c-4204-8443-730d79f82993/image.png)
![](https://images.velog.io/images/goplanit/post/75227c2a-43fc-47ed-998e-7033c5062443/image.png)

--- 
<회원가입 페이지>
![](https://images.velog.io/images/goplanit/post/99f331d8-9d19-4e9e-9d8c-71effa662b0b/image.png)

---
<로그인 페이지>
![](https://images.velog.io/images/goplanit/post/08f6b9aa-5f28-4323-a228-ee3824c0fee5/image.png)

---
<일기작성 페이지>
![](https://images.velog.io/images/goplanit/post/d221cd9c-4979-4442-a16f-e4662985c972/image.png)

---
## 프로젝트 개요 

### 개발기간

- 21.06.07(월) ~ 06.11(목)
- 4일간(기획 1일, 개발 3일)

### 전체일정 프로세스
- 1일차 
: 프로젝트 기획(API설계, 와이어프레임작성, 워크플로우 작성 등), 기능 선정, 역할분담, 튜터피드백
- 2일차 
: 개발 흐름 및 일정 결정, 로그인, 회원가입, 일기장 저장, 메인페이지 구현  
- 3일차 
: Git과 Github 사용, 좋아요 기능, 사진첨부 기능, 화면 CSS   
- 4일차 
: Git 병합, AWS 연동, 삭제기능, 화면 CSS, 에러 해결, 도메인 연결, 서비스 테스트, 영상 제작 

---
 
### 서비스 기능
** 1. 로그인 페이지**
- 회원가입시 암호화되어 저장된 비밀번호와 로그인 시 받은 비밀번호를 해시함수를 통해 인코딩하여 비교
- DB에 ID와 비밀번호가 일치하는 유저가 있으면 JWT토큰을 받아오는 인증방식으로 구성
- 로그인은 24시간동안 유지되도록 설정
- 입력값이 없으면 경고 텍스트 활성

** 2. 회원가입 페이지**
- ajax의 POST 방식으로 사용자가 회원가입을 위해 입력한 정보를 DB에 저장
- DB에 저장된 아이디와 새롭게 입력된 아이디를 비교 및 중복확인 기능 추가
- 비밀번호와 아이디는 조건에 만족하는 경우만 최종적으로 회원가입 가능 및 정규표현식 사용
- 로그인 이후 사용자의 닉네임을 이용하기 위해 닉네임도 필수입력값으로 구성

** 3. 메인페이지**
- 회원들이 일기를 작성할 경우 Home페이지에서 노출
- 모든 가입자의 포스팅이 공유되도록 하며, 각각의 포스팅마다 좋아요 기능 활성
- Jinja로 html 관리하여 공통적으로 적용되는 태그들의 반복 사용을 줄임
- 포스팅 삭제 기능 활성

** 4. 글쓰기 페이지**
- 부트스트랩에서 제공하는 폼을 기반으로 제목, 장소, 사진파일, 상세정보를 담을 수 있는 페이지를 제작
- 글 작성 후 ajax를 활용, 파일 전송 유무에 따라 다른 url로 포스트하는 방식을 택함
- 플라스크로 API를 관리, 작성 폼에서 파일 존재하는 경우와 파일이 존재하지 않는 경우를 따로 설정


### 구현기능

- 로그인 기능
- 회원가입 기능
- 일기장 저장 / 삭제 
- 사진 첨부 기능
- Feed 모아보기(메인화면)
- 좋아요 기능


### 사용도구
- HTML, CSS
- JavaScript - Ajax
- Python - pymongo, flask, jwt, datetime, bs4, requests
- AWS EC2


---

### 팀빌딩 및 역할
>
- 부트캠프 <향해99> 참가자로 구성
- 비전공자 4인의 첫 미니프로젝트 in Bootcamp

#### 개발자 (가나다순)🙋🏻‍♂️ 🙋🏻‍♀️
고원구[@goplanit](https://github.com/goplanit) / 팀장
- [x] 메인 페이지 담당(Feed)
- [x] 삭제기능 구현
- [x] 개발블로그 & Readme 작성
- [x] AWS 배포 담당

이현주[@leehyeonj](https://github.com/leehyeonj)
- [x] 로그인 페이지 담당
- [x] 노션 회의록 정리
- [x] 유튜브 영상제작
- [x] 파비콘 & logo 이미지 제작
 
전승운[@FrancisJeon](https://github.com/FrancisJeon)
- [x] 작성 페이지 담당
- [x] 사진 첨부기능 구현
- [x] GIT 사용 및 에러해결
- [x] DB, Routing 관리

정민주[@minjujung](https://github.com/minjujung) 
- [x] 회원가입 페이지 담당
- [x] 전체화면 디자인 관리 
- [x] 도메인 연결 담당
- [x] 서비스 테스트 관리
- [x] 좋아요 기능 구현

---
  
### 오늘도 돼지런 API 설계하기
![](https://images.velog.io/images/goplanit/post/8a8f4f91-42ff-43ac-9ec0-d04111704d54/image.png)

  
### 와이어프레임
<워크플로우 차트>
![](https://images.velog.io/images/goplanit/post/a96299f8-457a-4d77-9213-9ab7942021e9/image.png)

<전체 와이어프레임>
![](https://images.velog.io/images/goplanit/post/595ed14b-a56d-4278-9c77-d3ba8baaf1c2/image.png)

<Home 페이지><br>
![](https://images.velog.io/images/goplanit/post/dd8ca341-3727-4728-a27a-8a228b1e1c5a/image.png)

<회원가입 페이지><br>
![](https://images.velog.io/images/goplanit/post/2b0bc175-02fd-4cda-818f-ba62d8d5b309/image.png)

<로그인 페이지><br>
![](https://images.velog.io/images/goplanit/post/821e9503-0d22-4bdb-afac-96c8710945fe/image.png)

<일기 작성 페이지><br>
![](https://images.velog.io/images/goplanit/post/c60ecc79-679c-40ac-adde-6c827d0c4060/image.png)
