### hadoop 명령어 정리



##### localhost 연결이 안되어있다고 한다면?

```
start-dfs.sh
```



##### 컴파일

맵리듀스 코드 컴파일

src 디렉토리에 있는것들 다 모아서 컴파일 → ssafy.jar 생성

/hadoop/Project/

```
ant
```



##### 테스트 데이터 hdfs에 넣기

/hadoop/Project/

```
hdfs dfs -mkdir wordcount_test

hdfs dfs -put data/wordcount-data.txt wordcount_test
```



##### hdfs dfs 파일 확인

```
hdfs dfs -ls(만든거 확인)
```

![image-20210907093217388](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210907093217388.png)



##### 맵리듀스 알고리즘 코드 실행

```
hadoop jar [jar file] [program name] <input args>
```

wordcount를 써서 Wordcount 맵 리듀스 코드를 수행
wordcount_test 디렉토리의 파일을 입력으로 사용하겠다

/hadoop/Project/

```
hadooop jar ssafy.jar wordcount wordcount_test wordcount_test_out
```

코드 실행 후 결과

![image-20210907093825803](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210907093825803.png)





##### 결과 확인

0번 reducer가 출력할 파일

```
reducer를 2개 이용했을 때

hdfs dfs -cat wordcount_test_out/part-r-00000|more
hdfs dfs -cat wordcount_test_out/part-r-00001|more
```



`|more`

: 화면에 찰 수 있는 양까지만 보여준 후 그 다음부터는 more로 보여준다

 ![image-20210909082603628](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210909082603628.png)





##### 맵리듀스 코드 컴파일 순서

1. (ubuntu 재부팅 or localhost 꺼져있는 경우) 서버시작 

   ```
   start-dfs.sh
   ```

2. 소스코드 파일 Project/src/ 디렉토리에 넣기

3. Driver.java 수정

   ```
   pgd.addClass("program name", class name, "description")
   ```

4. 맵리듀스 코드 컴파일

   ```
   ant
   ```

5. HDFS 디렉토리 생성(입력 데이터용)

   ```
   hdfs dfs -mkdir wordcount_test
   ```

6. linux data 디렉토리의 txt 파일을 하둡의 HDFS 디렉토리로 전송

   ```
   hdfs dfs -put data/wordcount-data.txt wordcount_test
   ```

7. 맵리듀스 프로그램의 결과를 저장할 디렉토리 삭제

   ```
   hdfs dfs -rm -r wordcount_test_out
   ```

8. 맵리듀스 알고리즘 코드 실행

   ```
   hadoop jar ssafy.jar wordcount wordcount_test wordcount_test_out
   ```

9. 결과 확인

   ```
   hdfs dfs -cat wordcount_test_out/part-r-00000|more
   ```

   

   

