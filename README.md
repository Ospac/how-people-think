![Uploading image.jpg...](/presentation/presentation%20(1).jpg)
![Uploading image.jpg...](/presentation/presentation%20(2).jpg)
![Uploading image.jpg...](/presentation/presentation%20(3).jpg)
![Uploading image.jpg...](/presentation/presentation%20(4).jpg)
![Uploading image.jpg...](/presentation/presentation%20(5).jpg)
![Uploading image.jpg...](/presentation/presentation%20(6).jpg)
![Uploading image.jpg...](/presentation/presentation%20(7).jpg)
![Uploading image.jpg...](/presentation/presentation%20(8).jpg)
![Uploading image.jpg...](/presentation/presentation%20(9).jpg)

# 빠른 시작(Linux(bash) 환경 기준)
/Team6_Final_Project/init.sh를 실행하여 모든 과정을 빠르게 시작할 수 있습니다.

현재 google-chrome의 stable version은 102입니다.

chromedriver의 버전이 google-chrome 버전 102에 대응되어 있습니다.

추후 stable version이 업데이트 될 경우 하단의 chromedriver 설치 관련 내용을 참고하여 직접 맞는 버전을 다운로드 하셔야합니다.

Linux(bash) 이외의 환경이거나 문제 발생시 아래 내용들을 참고하시기 바랍니다.

# 가상환경 (venv)
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
# CREATE table history ( id INT, ts varchar(16), topic VARCHAR(30), pos_prob NUMERIC(4,3) ,neg_prob NUMERIC(4,3),neu_prob NUMERIC(4,3));
# CREATE table keywords ( id INT,word VARCHAR(30));
```
### DB Class
- get_id(table) : get id for input data

- get_timestamps : get current_timestamp

- insertDB(data, keyword)
    - insert data into history, keywords table
    - data = dictionary{’id’ : id, ‘ts’ : ts, ‘topic’ : topic , ‘prob’ : prob }
    - keyword = list[key_words]
- history_exist(topic)
    - if history of topics within a week is exist, return True
    - else return False


- get_history(topic)
    - get history corresponding with topic
    - return type : dictionary{’ts’ : [timestamp_list], ‘prob’ : [probability_list]}
    
- get_keywords(topic, ts)
    - get keywords corresponding with topic, ts(timestamp)
    - return type : list[key_words]
    - 
- db = psycopg2.connect(host='localhost', dbname='team6',user='team6',password='team6',port=5432)

### Table
- HISTORY ( id INT, ts varchar(16), topic VARCHAR(30), pos_prob NUMERIC(4,3)
                                                    ,neg_prob NUMERIC(4,3),neu_prob NUMERIC(4,3))
    - has history of topics
    - id : assign in input order
    - topic : input topic
    - pos_prob : 검색한 topic 에 대한 sentimental analysis 의 positive probability
    - neg_prob : 검색한 topic 에 대한 sentimental analysis 의 negative probability
    - neu_prob : 검색한 topic 에 대한 sentimental analysis 의 neutral probability

- KEYWORDS ( id INT,word VARCHAR(30))
    - topic 검색 후 추출된 단어를 저장하는 table
    - id : matching for history's id 
    - word : keyword

# 크롤링 (Crawling)
## 크롬 및 크롬드라이버 설치
### For Mac
맥용 패키지 관리자 brew가 설치되어 있지 않은 경우 아래 링크를 통해 설치합니다.

https://brew.sh/index_koi

```shell
# brew install --cask google-chrome chromedriver --force # 크롬이 이미 설치된 경우 강제 재설치
```
### For Linux & WSL
```shell
$ cd /tmp
$ sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ sudo apt install --fix-broken -y
$ sudo dpkg -i google-chrome-stable_current_amd64.deb
$ google-chrome --version
```
크롬 버전과 동일한 버전의 chromedriver를 아래 사이트를 통해 다운로드 한 후 TwitterCrawler.py가 위치하는 경로로 옮겨주세요. (/Team6_Final_Project/controller/)

https://sites.google.com/chromium.org/driver/downloads
## Troubleshooting
### google-chrome 한글 깨짐 현상
아래 링크를 참고하여 해결합니다.

https://www.lesstif.com/lpt/ubuntu-linux-fcitx-129008000.html
