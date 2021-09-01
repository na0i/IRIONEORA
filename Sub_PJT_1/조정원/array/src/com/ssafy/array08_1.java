package com.ssafy;

public class array08_1 {
    public static void main(String[] args) {

        int [] intArray = {3, 27, 13, 8, 235, 7, 22, 9, 435, 31, 54};

        int min = 999;
        int max = 0;

        for (int i =0; i < intArray.length; i++) {
            if (intArray[i] < min) {
                min = intArray[i];
            }

            if (intArray[i] > max) {
                max = intArray[i];
            }
        }

        System.out.println(min);
        System.out.println(max);
    }
}
