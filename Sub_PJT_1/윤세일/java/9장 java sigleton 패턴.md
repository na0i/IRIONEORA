# 9장 Singleton 패턴

###  singleton 패턴

- 하나의 객체만 존재해야할 때, 어떻게 그걸 유지할것인가

```java
private static company instance = new company
```

private로 외부에서 함부로 수정불가능하게 하고, static으로 유일한 변수로 만들어준다.

이후, 사용은 함수를 이용해서 사용한다.



