# 2장: java tutorial

### 컴파일

저장 시 자동으로 컴파일이 진행된다.



### 출력문

```
System.out.println("내용");
```



### 자료형

1.  자료형 크기 제한(리터럴)

```
long num = 12345678900
```

이 코드는 에러가 발생한다. 왜냐하면 기본 int형(4byte)으로 숫자가 저장되는데 그 범위를 넘는 자료이기 때문이다.

이 에러를 해결하기 위해서 숫자뒤에 long 자료형으로 저장하라고 'L'을 붙여야한다

마찬가지로 float를 해결하려면 'F'를 붙여야한다.



2. 변수 자료형

   - 문자형: char

   - 숫자형: int, long

   - 실수형: float, double

   - 논리형: bolean

     

3. var

   - 지역변수에서만 가능

   - 알아서 자료형을 알맞게 설정해준다

   - 단, 이후 다른 자료형으로 대입하면 에러가 발생한다

     ```java
     public static void main(String[] args) {
     		var num =10;
         	num = 5; //같은 자료형이라 에러 안남
     		num = 3.14; // 다른 자료형이라 에러남
     		System.out.println(num);
     	}
     ```

     

4. final

   - 상수를 선언

   - 이후 값을 절대 수정이 불가능함

     

5. 형변환

   -  작은 값 -> 큰 값 : 아무문제 없고 자연스럽게 진행됨(묵시적 형변환)
   - 큰 값 -> 작은 값 : 앞에 (byte) 등으로 변환되는 형태를 지정해줘야하며 일부 데이터의 손실이 생길 수 있음( 명시적 형변환)



### 연산자(생략: 파이썬과 동일)



### 조건문

-  if 조건문

```java
if ( 조건문) {
	실행문
} else if  {
 	실행문
} else {
    실행문
}
```



- switch-case 

```java
switch (rank) {
	case 1: medalColor = 'G';
		break  //반드시 필요 없으면 밑에도 실행
	case 2: medalColor = 'S';
		break
	case "GOLD": medalColor = 'B';
		break
	defaut : medalColor = 'A';
}
```



### 반복문

- while(생략)

- dowhile

  ```
  do {
  	수행문1
  } while (조건문1)
  ```

  무조건 1회 수행 후, 조건 체크

- for(생략)
