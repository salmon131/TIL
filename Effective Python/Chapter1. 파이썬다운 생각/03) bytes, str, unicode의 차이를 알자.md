### BETTER WAY3. bytes, str, unicode의 차이점을 알자

파이썬 3이 문자 시퀀스를 나타내는 두 가지 타입 : bytes , str

- bytes: 로(raw) 8비트 값을 저장
- str: unicode 문자를 저장

UTF-8

: 유니코드 문자를 바이너리 데이터로 표현하는 가장 일반적인 인코딩

- 파이썬 3의 open 함수의 encoding 파라미터의 기본값은 ‘utf-8’ 이다.
- 즉 파일 핸들을 사용하는 read나 write연산은 bytes인스턴스가 아니라 유니코드 문자를 담은 str인스턴스를 기대한다.
- 바이너리 데이터를 파일에서 읽거나 쓸때는 파일을 바이너리 모드(’rb’ 또는 ‘wb’) 로 오픈한다.

```python
with open('/tmp/random.bin', 'b') as f:
    f.write(os.urandom(10))
>>>
TypeError: must be str, not bytes

with open('/tmp/random.bin', 'wb') as f:
		f.write(os.urandom(10))
```