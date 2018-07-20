# Linky 외주

## 1. 개발 프로그램
* 웹페이지 기반의 영상 자막 송출 시스템

## 2. 개발 스택
* django==1.11.10
* django channels==2.1.1 <br>
체킹 방법:
```python
python3 -c 'import channels; print(channels.__version__)'
```
* psql - DB
* asgi - middleware

## 3. 배포
* daphne, redis server로 진행.

### 3.1 가상환경 키기
```bash
export PATH="$HOME/anaconda3/bin:$PATH"
source acitivate linkey
```

### 3.2 tmux 내에 채팅 서버 열기 by redis
```bash
tmux
export PATH="$HOME/anaconda3/bin:$PATH"
source acitivate linkey
redis-server
```
tmux 나오려면 `Ctrl + b` 그 다음 `Ctrl + d` 를 누르면 됩니다.

### 3.3 tmux에 daphne로 배포
```bash
cd ex_linkey # ex_linkey 폴더로 들어가시면 됩니다 어떻게든!
tmux
export PATH="$HOME/anaconda3/bin:$PATH"
source acitivate linkey
daphne -b 0.0.0.0 -p 8001 django_project.asgi:application
```
tmux 나오려면 `Ctrl + b` 그 다음 `Ctrl + d` 를 누르면 됩니다.


## 참고자료
* [django channels example](https://github.com/jacobian/channels-example)
* [django channels 공홈](https://github.com/django/channels)
* [channels 공홈 튜토리얼](https://channels.readthedocs.io/en/latest/tutorial/part_1.html)
* [daphne](https://github.com/django/daphne)
