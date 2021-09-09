##### partitioner class

- Map 함수의 출력인 (key, value) 쌍이

- **key에 의해**

- 어느 reducer(머신)으로 보내질지 정해지는데 결정을 정의하는 class

- ex) key가 1~30 이면 reducer1로 그 외에는 reducer2로 보낸다

- 하둡 기본 타입은 hash 함수가 디폴트로 제공되어 key에 대한 해시값에 따라 어느 reducer로 보낼지 결정

  ```
  hash 함수
  
  임의의 길이를 갖는 임의의 데이터에 대해 고정된 길이의 데이터로 매핑하는 함수
  ```

  



