package com.ssafy;

import java.util.Scanner;

public class array14 {
    public static void main(String[] args) {

        // 사용자 입력 받기
        Scanner sc = new Scanner(System.in);

        char[][] grid = new char[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j=0; j<4; j++ ) {
                grid[i][j] = sc.next().charAt(0);
            }
        }


        for (int i = 0; i < 4; i++) {
            for (int j=0; j<4; j++ ) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }
        sc.close();
    }
}

