# DailyStudy

## 목차
> 1. 프로젝트 소개
> 2. 기술 스택
> 3. Daily Study 기능 설명
> 4. deploy
> 5. DailyStudy ERD

## 1. 프로젝트 소개
> - 개요
>   - algorithm 문제 풀이를 위한 플랫폼
> - 동기
>   - google spreadsheet에서 관리하던 기존 알고리즘 스터디을 사이트로 관리하기 위해
> - 주요 기능
>   - `회원가입`, `스터디 그룹 초대 및 탈퇴 기능`, `메시지 기능`, `문제풀이 업로드 기능`
>
> ### 1-1. 환경설정
> - `requirements.txt`있는 디렉토리(root path)에서 명령어 실행
> ```shell
> pip install -r requirements.txt
> ```

## 2. 기술 스택
----
| skill | version | 
| -- | -- |
| python | 3.8.5 |
| django | 3.2.7 |
| mysqlclient | 2.0.3 |

## 3. Daily Study 기능 설명
----
### login page
- django의 login, register를 커스터마이징하여 구현
![image](https://user-images.githubusercontent.com/77317312/134388077-db1d78bd-78a8-4277-9580-528cb4d455d6.png)

### main page
- 사이트의 유저들의 정보를 한번에 확인할 수 있는 메인페이지
- pagination과 search query를 이용하여 회원정보를 관리 및 찾기 쉽게 구성
- 알고리즘 풀이 횟수가 높은 순으로 정렬

![image](https://user-images.githubusercontent.com/77317312/134388136-604a94f6-b06c-4545-a8dc-6103ee3c6c93.png)

### profile page
- 내정보 및 다른 유저들이 나의 정보를 볼 수 있는 페이지
- 해당 유저 본인이 로그인했을 때만 CRUD 작업이 가능하도록 구현
- 알고리즘을 create하면 solved count가 증가하며 해당 title과 link를 자동으로 추가 되도록 구현
- 원하는 문제의 풀이법을 쉽게 찾아보기 위해 search 기능 구현

![image](https://user-images.githubusercontent.com/77317312/134388197-6724c0fd-6ab8-4764-aef1-a4e7845db401.png)

### study group page
- 혼자 보다는 다수가 같이 풀이를 공유하여 약간의 강제성을 위해 패널티를 설정
- 각각의 스터원들의 일단위 문제풀이 횟수를 확인하며 서로에 대한 열의 불태우기
- 그룹에 대한 업데이트와 초대, 탈퇴, 스터디 해체 기능 구현
- github heatmap 구현 예정

![image](https://user-images.githubusercontent.com/77317312/134388236-ba9cf055-aba0-4d33-a355-6f793825c88e.png)

### invite page
- 다수의 그룹원들에게 초대 메세지를 보내기 위해 check box를 활용하여 구현
- 이미 스터디 그룹에 속해있는 user는 검색 결과에서 제외

![image](https://user-images.githubusercontent.com/77317312/134388311-31b1dc8b-8341-4cf4-82ce-790541de2404.png)

### invite message
- 초대 메세지 등 각 user의 profile에 들어가 메시지 기능 구현
- 메시지 box에 읽은 메시지와 안읽은 메시지 구분 구현

![image](https://user-images.githubusercontent.com/77317312/134388337-05fe61ab-d09d-4421-a7e4-6e051b73af33.png)

### invite message detail
- 초대에 대한 메시지에는 그룹 참여 기능을 구현
![image](https://user-images.githubusercontent.com/77317312/134388412-cdec84c7-90c3-42d1-a9d7-ab5f06d38b32.png)


## 4. deploy
--- 
- AWS의 RDS를 활용하여 DataBase 구축(mysql)
- AWS의 S3를 활용하여 Static file등 저장
- Heroku를 활용하여 배포

## 5. DailyStudy ERD
-------
![ERD](Daily_Study_ERD.PNG)
