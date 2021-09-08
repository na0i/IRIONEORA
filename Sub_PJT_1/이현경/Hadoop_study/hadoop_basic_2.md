# 분산처리



## 1. TB 단위 이상의 기존 데이터와 시간당 GB단위의 신생 로그가 들어오는 서비스에서 모든 가입자에게 개별적으로 계산된 실시간 서비스(웹)를 제공하기 위한 시스템 구조를 구상해봅시다



ref.

김성숙, 김경태, 박기진, 2015, 스트리밍 빅데이터 처리 시스템 설계, 한국정보처리학회

https://www.researchgate.net/profile/Alessio-Botta/publication/315095908/figure/fig1/AS:472376992374784@1489634859581/Hadoop-vs-Spark-Example-of-Big-Data-Analytics-platforms-for-batch-and-streaming.png



### 다양한 센서 기기에서 쏟아지는 대용량의 정형/비정형의 스트림 데이터의 처리

- 기존
  - 대용량 데이터에 대한 처리는 Hadoop 기반의 기존 빅데이터 시스템의 클러스터 분산 병렬 처리로 Map과 Reduce 함수의 간단한 조합만으로 정형/비정형 대용량 처리
  - 하지만 디스크 기반의 일괄 처리 시 발생하는 병목현상으로 실시간 분석 처리를 하기에는 한계가 있음
    - 

- Spark 사용
  - 클러스터의 디스크가 아니라 메모리들을 사용하여 대용량 데이터 처리를 하게 됨
  - Spark -> DP 같은건가?
    - 내용은 완전 다른 것이지만 느낌이나 컨셉추얼한건 맞다고 함
    - map-reduce한 결과물을 무조건 하둡은 디스크에 쓰지만, Spark은 메모리에 둔다
      - 결과적으로 비슷한 것을 다시 돌리는 과정이 매우 빠르게 처리된다
  - 클러스터의 메모리를 이용하여 고속의 스트리밍 배치 처리를 할 수 있다 
  - 하나의 플랫폼 안에서 스트림 데이터 처리와 반복적인 머신러닝 작업, 그래프 처리 등을 동시에 인터렉티브하게 처리할 수 있다. 



![Hadoop vs Spark. Example of Big Data Analytics platforms for batch and streaming computing.  ](https://www.researchgate.net/profile/Alessio-Botta/publication/315095908/figure/fig1/AS:472376992374784@1489634859581/Hadoop-vs-Spark-Example-of-Big-Data-Analytics-platforms-for-batch-and-streaming.png)