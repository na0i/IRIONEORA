# 10장 ArrayList

### 배열선언

```java
// 빈배열 선언
자료형[] 배열이름 = new 자료형[개수];
int[] arr = new int[10];

자료형 배열이름[] = new 자료형[개수];
int arr[] = new int[10];

// 배열값 넣기
arr[0] = 8

//초기화 하는법
int[] numbers = new int[] {0,1,2};
```



### 객체배열

```
Book[] library = new Book[5];
```

- book은 미리 만들어둔 객체를 의미
- 해당코드는 book 개체(인스턴스) 다섯 개를 만드는게 아닌 book을 가리키는 주소 담을 수 있는 공간을 5개 만듬
- 이후 따로, 객체값을 대입해야함



### 배열 얕은 복사

- 배열이 꽉 차거나 같은 배열을 생성해야할 때 사용

- ```
  System.arraycopy(src, srcPos, dest, destPos, length)
  ```

  - src: 복사할 배열의 이름
  - srcPos: 복사할 배열의 첫 위치
  - dest: 복사해서 붙여 넣을 대상 배열 이름
  - destPos: 복사해서 넣을 첫위치
  - length: 복사할 요소 개수



### 깊은 복사

- 따로 배열을 새롭게 만든 후 반복문과 함수를 이용하여 각 배열에 배치



### 향상된 for문

```
for (변수: 배열) {
	반복문
}
```

- 배열의 모든 요소를 확인할때 매우 편리하다



### 다차원배열

```
int[][] arr = new int[2][3]
```



### arraylist

- 자바에서 제공하는 객체 배열을 관리하기 좋은 클래스

```
ArrayList<type> listName = new ArrayList<type>();

ArrayList<String> list = new ArrayList<String>();
```

 - add, size, get, remove 
