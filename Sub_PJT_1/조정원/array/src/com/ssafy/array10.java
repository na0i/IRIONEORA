package com.ssafy;

public class array10 {
    public static void main(String[] args) {

        int[] cntArray = new int [20];

        int[] intArray = {1, 3, 4, 7, 8, 10, 12, 15, 16, 17, 18};

        for (int x: intArray) {
            cntArray[x-1]++;
        }

        for (int i = 0; i < cntArray.length; i++) {
            if (cntArray[i] == 0) {
                System.out.println(i+1);
            }
        }


    }
}
