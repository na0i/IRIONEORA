package com.ssafy;

public class array13 {
    public static void main(String[] args) {

        int[][] array = {{2, 3, 1, 4, 7}, {8, 13, 3, 33, 1}, {7, 4, 5, 80, 12}, {17, 9, 11, 5, 4}, {4, 5, 91, 27, 7}};

        int cnt = 0;
        int total = 0;

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j ++) {
                if (array[i][j] % 3 == 0) {
                    cnt++;
                    total += array[i][j];
                }
            }
        }

        System.out.println(cnt);
        System.out.println(total);

    }
}
