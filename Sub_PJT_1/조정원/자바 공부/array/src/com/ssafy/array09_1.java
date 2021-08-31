package com.ssafy;

public class array09_1 {
    public static void main(String[] args) {

        int [] cntArray = new int[10];

        int[] intArray = {3, 7, 2, 5, 7, 7, 9, 2, 8, 1, 1, 5, 3};

        for (int x : intArray) {
            cntArray[x] += 1;
        }

        for (int x : cntArray) {
            System.out.println(x);
        }
    }
}
