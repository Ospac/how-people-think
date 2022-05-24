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
pip install requirements.txt

#pip freeze > requirements.txt #다른 패키지 설치후 requirements 갱신
```
