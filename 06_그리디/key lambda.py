"""
    l. lambda란 바로 정의하여 사용할 수 있는 함수로,
        sum = (lambda x : x+10)(1) = 11 과 같이 사용한다.

    2. 리스트를 정렬할 때 key로 사용되는데,
        c = sorted(a, key=lambda x : x[0]) 과 같이 사용한다.
        x[0]인자를 기준으로 오름차순, -x[0]은 내림차순

    3. map으로도 사용되는데,
        list(map(lambda x : x+10, [1,2,3])) = [11,12,13] 과 같이 사용한다.

    4. filter()로도 사용되는데,
        list(filter(lambda x : x>7 and x<15, a)) 로 a값이 true인 요소만 반환한다.

    5. 값을 누적시키는 reduce()로도 사용되는데,
        reduce(lambda x, y : x+y, t) 와 같이 사용한다.

    참조: https://gorokke.tistory.com/38
"""
