##### MapReduce Framework

- 값싼 컴퓨터들을 모아서 클러스터를 만들고
- 여기에서 빅데이터를 처리하기 위한
- 스케일러블(사용자 수가 급등하거나 데이터가 급증해도 성능이 떨어지는 일이 없다)
- 병렬 소프트웨어의 구현을 쉽게 할 수 있도록 도와주는
- 간단한 프로그래밍 모델
- 구글의 맵리듀스 or 하둡은 맵리듀스 프레임워크의 우수한 구현 형태
- main 함수(드라이버)가 map 함수와 reduce 함수를 호출해 처리





##### MapReduce Programming Model

- 함수형 프로그래밍 언어의 형태
- 유저는 3가지 함수를 구현해 제공해야함
  - Main 함수
  - Map 함수: (key1 - value1) → [(key2 - value2)]
  - Reduce 함수: (key2 - value2) → [(key3 - value3)]
- 입출력이 Key-value를 쌍으로 함
- [] 라고 쓰여있는 이유는 key-value 페어를 다수 출력 가능하기 때문





##### MapReduce Framework

- main 함수를 한개의 master machine에서 수행
- master machine은 **맵 함수 수행 전 전처리** or **리듀스 함수 결과를 후처리**하는데 사용 될 수 있음
- 컴퓨팅은 map reduce 페이즈를 여러번 반복해 수행할 수 있음
- 한번의 맵리듀스 페이지는 맵 → 리듀스 호출 순서이지만 때에 따라서 중간에 combine 함수를 수행할 수 있음
- main 프로그램에서 맵리듀스를 수행시킴





##### MapReduce Phase

- Map 페이즈
  - 제일 먼저 수행
  - 데이터의 여러 파티션에 병렬 분산으로 호출되어 수행
  - 입력 데이터 한 줄마다 맵 함수 호출
  - key value 쌍 형태로 결과를 출력
  - 여러 머신에 나누어 보내며
  - 같은 key를 가진 key-value 쌍은 같은 머신으로 보내진다
- Shuffling 페이즈
  - 모든 머신에서 맵 페이즈가 끝나면 시작된다
  - 맵 페이즈에서 각각의 머신으로 보내진 key value 쌍을 key를 이용해 정렬 후
  - 각각의 key마다 같은 key를 가진 key-value 쌍으로 모아서
  - value-list를 만든 후
  - key, value-list 형태로 key에 따라 여러 머신에 분산해 보낸다
- Reduce 페이즈
  - 모든 머신에서 Shuffling 페이즈가 끝나면 리듀스 페이즈가 시작된다
  - 셔플링 페이즈에서 해당 머신으로 보내진 각각의 key, value-list 쌍마다 리듀스 함수가 호출
  - 하나의 리듀스 함수가 끝나면 다음 key, value-list 쌍에 리듀스 함수 호출
  - 출력이 있다면 key-value 쌍 형태로 출력





##### HDFS

- 하둡 분산 파일 시스템(Hadoop Distributed File System)
- 빅데이터 파일을 여러 대의 컴퓨터에 나누어서 저장
- 각 파일은 여러개의 순차적인 블록으로 저장
- 하나의 파일의 각각의 블록은 fault tolerance(시스템 구성 부품 일부에서 결함 또는 고장이 발생하여도 정상적 혹은 부분적으로 기능을 수행 가능함)를 위해
- 여러개로 복사되어 여러 머신의 여기저기 저장됨





##### Hadoop

- 수행:  mapreduce
- 분산: hdfs
- 한개의 NameNode(master)와 여러대의 DataNode(slave)





##### MapReduce의 Function

- Map Function
  - org.apache.hadoop.mapreduce 라는 패키지에 있는 mapper 클래스를 상속받아
  - map method를 수정
  - 입력 텍스트 파일에서 라인 단위로 호출(입력은 key-value list의 형태)
  - key는 입력 텍스트 파일에서 맨 앞 문자 기준, 해당 라인의 첫번째 문자까지의 오프셋
  - value는 텍스트의 해당 라인 전체
- Reduce Function
  - org.apache.hadoop.mapreduce 라는 패키지에 있는 reducer 클래스를 상속받아
  - reduce method를 수정
  - value-list는 맵 함수의 출력에서 key를 갖는 (key, value) 쌍들의 value 리스트





##### Mapper & Reducer

- 각 머신에서 독립적으로 수행됨
- Mapper에서는 Map 함수를, Reducer는 Reduce 함수를 각각 수행
- Map 페이즈만 수행하고 중단할 수도 있다



##### Linux와 HDFS

- 데이터 생성이나 코딩은 Linux에서
- MapReduce 코드와 입력 데이터는 hdfs에 옮겨서
- MapReduce 알고리즘을 수행