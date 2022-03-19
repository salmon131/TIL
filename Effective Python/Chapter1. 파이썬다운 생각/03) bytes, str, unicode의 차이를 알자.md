### BETTER WAY3. bytes, str, unicode의 차이점을 알자

파이썬 3이 문자 시퀀스를 나타내는 두 가지 타입 : bytes , str

- bytes: 로(raw) 8비트 값을 저장
- str: unicode 문자를 저장

문자열은 일련의 문자, 즉 유니코드이고 이들은 추상적 개념이며 디스크에 직접 저장할 수 없다. 디스크에 기록되기 위해서는 디스크에 저장할 수 있는 바이트 시퀀스인 바이트 문자열로 인코딩이 수행되어야 한다.

(아스키코드, 유니코드, utf-8 에 대한 설명은 [링크](https://halfmoon9.tistory.com/61) 참조)

**UTF-8**

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

**ASCII**

: 파이썬에서 문자열(str)의 기본 인코딩은 UTF-8인데, `b'hello'`와 같이 문자열을 바이트 객체로 만들면 각 문자를 ASCII 코드로 저장한다. 보통 문자열을 UTF-8이 아닌 ASCII 코드로 처리하고 싶을 때 바이트 객체를 사용한다.

```python
'I am a string'.encode ('ascii')
>>> 
b'I am a string'
```

ascii로 인코딩 된것은 인간이 읽을수 있는것처럼 보이지만 사실은 그렇게 보여줄 뿐이다. (print 할 때 파이썬이 디코딩해서 보여주는 것이기 때문이다.)

영어가 아닌 다른 언어로 아스키 인코딩을 해보면 왜 바이트 문자열이 인간이 읽을 수 없는 것인지 이해가 된다.

```python
'τoρνoς'.encode('utf-8')
>>>
b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
```