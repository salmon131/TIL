### BETTER WAY7. map과 filter 대신 리스트 컴프리헨션을 사용하자

- list comprehension: 리스트 함축 표현식
- 한 리스트에서 다른 리스트를 만들어내는 간결한 문법
- map을 쓰려면 lambda 함수를 생성해야 해서 깔끔해 보이지 않는다.

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = [x**2 for x in a if x % 2 == 0]
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))

assert even_squares == alt
```

- 딕셔너리와 세트에도 리스트 컴프리헨션 표현식을 지원한다.

```python
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}

print(rank_dict)
print(chile_len_set)

>>>
{1: 'ghost', 2: 'habanero', 3: 'cayenne'}
{8, 5, 7}
```