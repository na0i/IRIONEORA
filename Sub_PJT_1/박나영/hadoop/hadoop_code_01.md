### 빅데이터 분석 [사전강의 01 - 과제]



#### Driver.java

```java
package ssafy;

import org.apache.hadoop.util.ProgramDriver;

public class Driver {
	public static void main(String[] args) {
		int exitCode = -1;
		ProgramDriver pgd = new ProgramDriver();
		try {
			pgd.addClass("wordcount", Wordcount.class, "A map/reduce program that performs word counting.");
      		pgd.addClass("wordcount1char", Wordcount1char.class, "A map/reduce program that counts the 1st character of words in the input files")
      		pgd.driver(args);
			exitCode = 0;
		}
		catch(Throwable e) {
			e.printStackTrace();
		}

		System.exit(exitCode);
	}
}
```

pgd.addClass는 새로운 코드를 등록할 때 사용한다.

`pgd.addClass("사용할 이름", 클래스 이름, 설명)` 의 형태로 사용

src 디렉토리에 새로운 코드를 만들 때마다 Driver.java 파일에 pgd.addClass를 새로 넣어주어야 한다.

Driver.java 파일이 수정되면 반드시 `ant`를 수행해야한다.(compile)





#### WordCount.java

```java
package ssafy;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class Wordcount1char {
	/* 
	Object, Text : input key-value pair type (always same (to get a line of input file))
	Text, IntWritable : output key-value pair type
	*/
	public static class TokenizerMapper
			extends Mapper<Object,Text,Text,IntWritable> {

		// variable declairations
		private final static IntWritable one = new IntWritable(1);
		private Text word = new Text();

		// map function (Context -> fixed parameter)
		public void map(Object key, Text value, Context context)
				throws IOException, InterruptedException {

			// value.toString() : get a line
			StringTokenizer itr = new StringTokenizer(value.toString());
			while ( itr.hasMoreTokens() ) {
				word.set(itr.nextToken().substring(0,1));

				// emit a key-value pair
				context.write(word,one);
			}
		}
	}

	/*
	Text, IntWritable : input key type and the value type of input value list
	Text, IntWritable : output key-value pair type
	*/
	public static class IntSumReducer
			extends Reducer<Text,IntWritable,Text,IntWritable> {

		// variables
		private IntWritable result = new IntWritable();

		// key : a disticnt word
		// values :  Iterable type (data list)
		public void reduce(Text key, Iterable<IntWritable> values, Context context) 
				throws IOException, InterruptedException {

			int sum = 0;
			for ( IntWritable val : values ) {
				sum += val.get();
			}
			result.set(sum);
			context.write(key,result);
		}
	}


	/* Main function */
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf,args).getRemainingArgs();
		if ( otherArgs.length != 2 ) {
			System.err.println("Usage: <in> <out>");
			System.exit(2);
		}
		Job job = new Job(conf,"word count");
		job.setJarByClass(Wordcount1char.class);

		// let hadoop know my map and reduce classes
		job.setMapperClass(TokenizerMapper.class);
		job.setReducerClass(IntSumReducer.class);

		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(IntWritable.class);

		// set number of reduces
		job.setNumReduceTasks(2);

		// set input and output directories
		FileInputFormat.addInputPath(job,new Path(otherArgs[0]));
		FileOutputFormat.setOutputPath(job,new Path(otherArgs[1]));
		System.exit(job.waitForCompletion(true) ? 0 : 1 );
	}
}

```

`hdfs dfs -put data/wordcount-data.txt wordcount_test` : data 디렉토리의 wordcount-data.txt를 하둡 hdfs의 wordcount_test 디렉토리로 보낸다는 의미이다.

`hdfs dfs -rm -r wordcount_test_out` : 코드 실행전 프로그램 결과를 저장할 디렉토리를 꼭 삭제해야 한다.

`hadoop jar ssafy.jar wordcount wordcount_test wordcount_test_out`

- Driver.java에 명시한대로 wordcount 맵 리듀스 코드를 수행한다는 의미이다.
- wordcount_test 디렉토리의 파일을 맵 함수의 입력 파일로 사용한다는 의미이다.



#### 하둡 실행 방법

`hadoop jar [jar file] [program name] [input arguments]`



#### 결과 확인

`hdfs dfs -cat wordcount_test_out/part-r-00000|more`

0번 reducer가 출력한 파일의 내용을 보여준다.

여기서 `|more`은 화면에 차는 부분까지만 결과를 보여준다는 의미이다.





