### BETTER WAY12. for와 while 루프 뒤에는 else 블록을 쓰지 말자

- 파이썬에는 다른 언어에는 없는 추가 기능이 있는데, 바로 루프에서 반복되는 내부 블록 바로 다음에 else 블록을 둘 수 있는 기능이다.
- 그러나 이때 else는 if/else에서의 else와는 다르게 루프가 종료되자마자 실행되게 된다.
- 이렇게 동작하는 이유는 루프 다음의 else는 루프로 뭔가를 검색할 떄 유용하기 때문이다.

Ex) 두 수가 서로소인지 판별하고자 할때 

두 수가 서로소가 아니면 루프 도중 break하게 되고 else문을 건너뛴다. 두 수가 서로소일때 루프가 끝나고 else블록이 실행된다.

```python
a = 4
b = 9
for i in range(2, min(a,b)+1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')
>>>
Testing 2
Testing 3
Testing 4
Coprime
```


> 하지만 이런 방식으로 코드를 작성하면 안된다. loop뒤에 else 블록을 사용하면 직관적이지 않고 혼동하기 쉽다. 루프처럼 간단한 구조는 파이썬에서 따로 설명할 필요가 없어야 한다.
> 

따라서 loop-else 대신 헬퍼 함수를 작성하는 게 좋다.

1. 찾으려는 조건을 찾았을 때 바로 반환한다.
2. 루프에서 찾으려는 대상을 찾았는지 알려주는 결과 변수를 사용한다.

```python
def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def coprime2(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = True
            break
    return is_coprime
```