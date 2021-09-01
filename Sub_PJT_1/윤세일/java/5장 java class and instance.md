# 5장: java class and instance

### 인스턴스

- 클래스 == static코드 == 개(강아지)
- 인스턴스 == 클래스가 생성된 것 == 몽실이, 다다 등



### 클래스  생성하기

```
class 변수이름 = new 생성자;

Student studentA = new Student();
```

- 인스턴스 생성위치: heap 메모리(동적메모리: 필요한만큼 생성)
- studentA는 이 heap메모리의 주소를 가리키는 역활



### 생성자

- 생성자는 따로 정의하지 않으면 자바컴퍼일러가 디폴트 생성자를 생성
- 생성자는 클래스와 이름이 같음
- 커스텀생성자

```
public Student (int id, String name) {
	studentID = id;
	studentName = name;
}
```

 - 이 경우 매개변수를 통해서 필요한 정보를 받아야만 생성할 수 있음

	- 이 경우 디폴트 생성자를 따로 정의하기 전에는 사용할 수 없음 
