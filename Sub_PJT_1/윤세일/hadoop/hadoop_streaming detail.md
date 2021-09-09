# hadoop_streaming

### hadoop_streaming

- 하둡을 파이썬이나 기타 다른 언어로 돌리는 방법
- 아래 참조문서들을 참고하면 좀더 쉽다



### 폴더구조

- 이 문서에서 대부분의 코드는 Project 폴더에서 실행

- pythonProject 내부에 pmapper.py와 preducer.py가 존재
- hdfs 폴더구조는 따로 표시하지 않음

![image-20210909234305003](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909234305003.png)



### python code

- 가장 상단에 `#!/usr/bin/env python`을 표시하여 우분투 파이썬 경로를 불러오는 것이 중요!

- excode:  pmapper.py

```python
#!/usr/bin/env python

import sys
for line in sys.stdin:
	line = line.strip()
	words = line.split()
	
	for word in words:
		print ('%s\t%s' % (word,1))

```

- excode: preucer.py

```python
#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t',1)
	try:
		count = int(count)
	except ValueError:
		continue
		
	if current_word == word:
		current_count +=count
	else:
		if current_word:
			print ('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word
		
if current_word == word:
	print ('%s\t%s' % (current_word, current_count))
```



### find

- 아래 코드는 `hadoop-streaming*.jar`를 찾기위한 코드로 위치를 알면 생략해도 된다

```java
 find / -name 'hadoop-streaming*.jar'
```

- 실행코드

![image-20210909230235614](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909230235614.png)

- 실행결과

  ![image-20210909230422387](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909230422387.png)



### mapreduce 실행하기

- 사전 준비(실제 예시)

  - hdfs dfs -mkdir p_wordcount : hdfs에 데이터 저장폴더 생성하기
  - hdfs dfs -put data/wordcount-data.txt p_wordcount : input data 가져오기
  - hdfs dfs -rm -r p_wordcount_out : output파일 삭제하기 (이름은 본인이 만드는 것)

  

- maprduce 코드 양식

```java
hadoop jar /hadoop-streaming-3.2.2.jar \
-input input \
-output output \
-mapper 'python3 mapper.py' \
-reducer 'python3 reducer.py'
```



- maprduce 실제 실행 코드

```java
hadoop jar ../../../usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.2.jar -input p_wordcount -output p_wordcount_out -mapper 'python3 ../pythonProject/pmapper.py' -reducer 'python3 ../pythonProject/preducer.py'
```

	1. hadoop jar ..... : 하둡을 이용하여 jar파일을 실행시키겠다는 뜻, 이 코드에서는hadoop-streaming-3.2.2.jar를 실행시켰다 
 	2. -input: p_wordcount : `p_wordcount`를 input파일로 사용한다
 	3. -output `p_wordcount_out`로 output파일을 저장한다. 이 때 이름은 자유롭게 지정가능하며 만약 같은 파일이 있다면 에러가 발생한다
 	4. -mapper 'python3 ...' : mapper로 다음 파일을 사용한다. 여기서 ''가 없거나 ''안에 python3를 명시해주지 않으면 default가 java기 때문에 에러가 발생한다.  
 	5. -reudce 'python3 ...' : reducer로 다음 파일을 사용한다. 여기서 ''가 없거나 ''안에 python3를 명시해주지 않으면 default가 java기 때문에 에러가 발생한다.  



### 결과

- 결과값은 wordcount_out 이라는 `dictionary`로 존재하여 기존 명령어인`hdfs dfs -cat p_wordcount_out/part-r-00000 |more`으로 할 경우 정확한 값을 알 수 없다

![image-20210909233439881](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909233439881.png)

- `hdfs dfs -cat p_wordcount_out/part-00000 |more`로 정확하게 지정해줘야한다.

![image-20210909233716391](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909233716391.png)



### 문제점

- main 함수 적용이 안되어서 더 알아봐야한다



### 참고문헌

- https://hadoop.apache.org/docs/r1.2.1/streaming.html

- https://www.youtube.com/watch?v=QNB1SZm2jS4&t=738s
- https://www.youtube.com/watch?v=rsMQ1Z3KZLM&t=47s
- https://www.youtube.com/watch?v=TcBkvCKE1rw&t=1831s
