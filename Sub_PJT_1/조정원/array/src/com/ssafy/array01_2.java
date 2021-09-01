package com.ssafy;

import java.sql.Array;

public class array01_2 {
    public static void main(String[] args) {

        int N = 6;

        int [] resultArray = new int[5];

        resultArray[0] = (int) (Math.random()*N) + 1;
        resultArray[1] = (int) (Math.random()*N) + 1;
        resultArray[2] = (int) (Math.random()*N) + 1;
        resultArray[3] = (int) (Math.random()*N) + 1;
        resultArray[4] = (int) (Math.random()*N) + 1;

        System.out.println(resultArray[0]);
        System.out.println(resultArray[1]);
        System.out.println(resultArray[2]);
        System.out.println(resultArray[3]);
        System.out.println(resultArray[4]);


        System.out.println("----------");

//        반복문 활용
        int [] changeArray = new int[5];

        System.out.println(changeArray);
//        이거 왜 [I@1b0375b3 이렇게 나오져.. 주소값 나오는 건가유?

        for (int i = 0; i < changeArray.length; i++) {
            changeArray[i] = (int)(Math.random()*N) +1;
        }

        for (int i = 0; i < 5; i++) {
            System.out.println(changeArray[i]);
        }

    }
}
