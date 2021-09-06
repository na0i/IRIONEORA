# matrix Multiplication

### 입력

- 행렬이름 행번호 열번호 원소값

  ex) A 0 0 3 , B 1 2 -10



### 출력

- 행번호 열번호 원소값

  ex) 0 0 5 , 1 4 -10



### 1-phase Matrix key, value

a_ip

- key: (i,1), (i,2) ... (i,m)
- value: (p,a_ip)



b_pj

- (1,j), (2,j) ... (n,j)
- value (p,b_pj)



### multiple

- 같은 key를 가진 인원을 모두 모은다 

  ex) (1,1) < (1,3), (2,-5), (1,-2), (2,1) >

- value에 앞부분이 같은 값들을 곱한다

  ex). 3x2 = 6 , -5x1 = -5

- 모두 합한다

  ex). 6-5 = 1

- 해당 자리에 배치한다

  ex). key= (1,1)이므로 행렬의 (1,1)의 값은 1이다



### 2-phase Matrix key, value

a_ip

- key: (i,1,P), (i,2,P) ... (i,m,P)
- value: (a_ip)



b_pj

- (1,j,P), (2,j,P) ... (n,j,P)
- value (b_pj)



### multiple

- 같은 key를 가진 인원을 모두 모은다 

  ex) (1,1,1) < 3,2 > ,(1,1,2) <-1,5>

- value에 앞부분이 같은 값들을 곱한다

  ex). 3x2 = 6 , -1X5 = -5

- 키에서 앞에 두가지만 뽑아낸다 

  ex). (1,1),6) ()(1,2),-5)

- 두 값을 모아서 합친 후 배치한다

  ex). key= (1,1)이므로 행렬의 (1,1)의 값은 6-5 = 1이다



### code

```java
package ssafy;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class MatrixMulti {
	// Map
	public static class MMMapper extends Mapper<Object, Text, Text, Text>{
		private Text keypair = new Text();
		private Text valpair =new Text();
                private String Matrix1name;
                private String Matrix2name;

		private int n;	// number of rows in matrix A
		private int l;	// number of columns in matrix A
		private int m;	// number of columns matrix B
		protected void setup(Context context) throws IOException, InterruptedException {
			Configuration config = context.getConfiguration();
                        // TODO
                        Matrix1name = config.get("Matrix1name","A");
                        Matrix2name = config.get("Matrix2name","B");
                        
                        n = config.getInt("n",10);
                        l = config.getInt("l",10);
                        m = config.getInt("m",10);
		}
		public void map(Object key, Text value, Context context
				) throws IOException, InterruptedException {
			StringTokenizer token = new StringTokenizer(value.toString());
                        // TODO
                        String mat = token.nextToken();
                        int row = Integer.parseInt(token.nextToken());
                        int col = Integer.parseInt(token.nextToken());
                        int v = Integer.parseInt(token.nextToken());
                        
                        if (mat.equals(Matrix1name)) {
                        	valpair.set(""+col+""+v);
                        	for (int j=0; j<m; j++) {
                        		String p = ""+row+","+j;
                        		keypair.set(p);
                        		context.write(keypair,valpair);
                        	}
                        }
                        else if (mat.equals(Matrix2name)) {
                        	valpair.set(""+row+""+v);
                        	for (int i=0; i<m; i++) {
                        		String p = ""+i+","+col;
                        		keypair.set(p);
                        		context.write(keypair,valpair);
                        	}
                        }
		}
	}
	// Reduce
	public static class MMReducer extends Reducer<Text, Text, Text, Text> {
		private IntWritable val = new IntWritable();	// emitÇÒ value·Î »ç¿ëÇÒ º¯Œö

		public void reduce(Text key, Iterable<Text> values, Context context) 
			throws IOException, InterruptedException {
                        // TODO
                        for (Text tx:values) {
                        context.write(key,tx);
			}
		}
	}
	// Main
	public static void main(String[] args) throws Exception {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
		if (otherArgs.length != 7) {
			System.err.println("Usage: <Matrix 1 name> <Matrix 2 name> <Number of row in Matrix 1><Number of columns in Matrix 1 (i.e., Number of rows in Matrix 2)> <Number of columns in Matrix 2> <in> <out>");
			System.exit(2);
		}

                FileSystem hdfs = FileSystem.get(conf);
                Path output = new Path(otherArgs[6]);
                if (hdfs.exists(output))
                        hdfs.delete(output, true);

		Job job = new Job(conf, "matrix multiplication prepare");
		Configuration config = job.getConfiguration();
                config.set("Matrix1name", otherArgs[0]);
                config.set("Matrix2name", otherArgs[1]);
		config.setInt("n",Integer.parseInt(otherArgs[2]));
		config.setInt("l",Integer.parseInt(otherArgs[3]));
		config.setInt("m",Integer.parseInt(otherArgs[4]));


		job.setJarByClass(MatrixMulti.class);
		job.setMapperClass(MMMapper.class);
		job.setReducerClass(MMReducer.class);
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		job.setNumReduceTasks(2);

		FileInputFormat.addInputPath(job, new Path(otherArgs[5]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[6]));
		FileSystem.get(config).delete(new Path(otherArgs[1]),true);
		System.exit(job.waitForCompletion(true) ? 0 : 1);
	}
}
```



### 문제

- 코드가 무언가 잘못되어서 다시 볼 예정이다.