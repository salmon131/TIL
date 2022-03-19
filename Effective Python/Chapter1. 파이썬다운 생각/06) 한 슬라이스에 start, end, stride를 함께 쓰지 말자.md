### BETTER WAY6. 한 슬라이스에 start, end, stride를 함께 쓰지 말자

- 기본 슬라이싱 형태 somelist[start:end] 의 확장형으로 슬라이스의 간격을 설정하는 문법 somelist[start:end:stride]도 있다.
- 해당 문법을 사용하면 시퀀스를 슬라이스할 때 매 n번째 아이템을 가져올 수 있다.

Ex) stride를 사용하여 홀수와 짝수 인덱스를 그룹으로 묶기

```python
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2] #인덱스0부터 끝까지 슬라이스 후 2간격씩 아이템 가져오기
evens = a[1::2] #인덱스1부터 끝까지 슬라이스 후 2간격씩 아이템 가져오기
print(odds)
print(evens)
>>>
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
```

> 문제는 stride 문법이 종종 예상치 못한 동작으로 버그를 만들어 낸다는 점이다.
> 

Ex) 문자열을 역순으로 만들기 위해 stride -1로 문자열을 슬라이스 할 경우

```python
# 바이트 문자열의 경우
x = b'mongoose'
y = x[::-1]
print(y)
>>>
b'esoognom'

# UTF-8 바이트 문자열로 인코드 된 유니코드 문자의 경우
w = '謝謝'
x = w.encode('utf-8')  # b'\xe8\xac\x9d\xe8\xac\x9d'
y = x[::-1] # b'\x9d\xac\xe8\x9d\xac\xe8'
z = y.decode('utf-8')
>>>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x9d in 
position 0: invalid start byte
```

음수값의 stride를 사용할 경우 바이트 문자열이나 아스키 문자에는 잘 동작하지만, UTF-8 바이트 문자열로 인코드된 유니코드 문자를 다시 디코드할때는 동작하지 않는다.

- 따라서 stride를 사용해야한다면 양수 값을 사용하는 것이 좋다.
- 또한 한 슬라이스에 start, end, stride를 지정하면 매우 혼란스러울 수 있으니 피하는 것이 좋다.
- stride를 꼭 start나 end 인덱스와 함께 사용해야 한다면 stride를 적용한 결과를 변수에 할당하고, 이 변수를 슬라이스한 결과를 다른 변수에 할당해서 사용하자.

```python
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

b = a[::2]   # ['a', 'c', 'e', 'g']
c = b[1:-1]  # ['c', 'e']
```