### 가상환경 (venv)

```shell
# 가상환경 생성
$ python3 -m venv .venv

# 가상환경 활성화 (환경별로 상이)
$ source .venv/bin/activate #bash/zsh	
$ source .venv/bin/activate.csh #csh/tcsh
$ .venv/bin/Activate.ps1 #PowerShell Core	
PS C:\> .venv\Scripts\Activate.ps1 #PowerShell
C:\> .venv\Scripts\activate.bat #cmd.exe	

# pip install (pip설치되어 있다면 생략, pip or pip3를 타이핑시 실행 안될 경우)
https://foreverhappiness.tistory.com/67

# requirement 설치
pip install -r requirements.txt

#pip freeze > requirements.txt #다른 패키지 설치후 requirements 갱신
```


# 데이터베이스 (DataBase)
### create database and table 
```shell
$ sudo systemctl start postgresql.service
$ sudo -u postgres createuser --interactive
$ sudo -u postgres createdb team6
$ sudo adduser team6
$ sudo -u team6 psql
$ CREATE table history ( id INT, ts varchar(16), topic VARCHAR(30), prob NUMERIC(4,3))
```
### DB Class
- insertDB(table, data)
    - table : table명
    - data : [id,timestamp,topic,probability] list form
- readDB(table, topic)
    - table : table명
    - topic : 입력한 topic
    - return [timestamp, probability] list form
- db = psycopg2.connect(host='localhost', dbname='team6',user='team6',password='team6',port=5432)

### Table
- HISTORY ( id INT, ts varchar(16), topic VARCHAR(30), prob NUMERIC(4,3) )
    - has history of topics
    - id : assign in input order
    - topic : input topic
    - prob : positive probability of topic ( negative probability = 1 - prob)

# 크롤링 (Crawling)
### 크롬 및 크롬드라이버 설치
# For Mac
맥용 패키지 관리자 brew가 설치되어 있지 않은 경우 아래 링크를 통해 설치합니다.

https://brew.sh/index_koi

```shell
# brew install --cask google-chrome chromedriver --force # 크롬이 이미 설치된 경우 강제 재설치
```
# For Windows & Linux
GUI 상으로 구글 크롬이 설치 되어있지 않은 경우 아래 링크를 통해 설치합니다.

https://www.google.com/intl/ko_kr/chrome/

크롬 버전을  아래 링크를 참고하여 확인합니다.

https://support.google.com/chrome/answer/95414?hl=ko&co=GENIE.Platform%3DDesktop#zippy=%2C업데이트-및-현재-브라우저-버전-확인

크롬 버전과 동일한 버전의 chromedriver를 아래 사이트를 통해 다운로드 한 후 TwitterCrawler.py가 존재하는 폴더에 넣어줍니다. (Team6_Final_Project/api/)

https://sites.google.com/chromium.org/driver/downloads

리눅스의 경우 아래 명령어로도 구글 크롬 설치가 가능합니다.
```shell
$ sudo apt install google-chrome
```
