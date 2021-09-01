# 7장 this

### this

- 자신(인스턴스)의 메모리를 가리킴

- 생성자에서 다른 생성자를 호출

```java
public Person() {
	this("이름없음",1);
}

public Person(String name, int age) {
	this.name = name;
	this.age = age;
}
```
1번 person()이 2번 person을 불러와서, 매개변수로 "이름없음"과 1을 전달


생성자안 this는 생성자만 불러오며, 생성자와 매개변수 개수와 형태가 동일한 걸 자동 매핑함



- 자신의 주소를 반환(잘안씀)

