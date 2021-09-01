package com.ssafy;

public class array08_2 {
    public static void main(String[] args) {

        int [] intArray = {3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54};

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;

        for (int i = 0; i < intArray.length; i++) {
            min = Math.min(min, intArray[i]);
            max = Math.max(max, intArray[i]);
        }
    }
}
