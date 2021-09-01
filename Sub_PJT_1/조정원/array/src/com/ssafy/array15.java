package com.ssafy;

import java.util.Scanner;


public class array15 {
    public static void main(String[] args) {
        char[][] grid = new char[4][4];

        Scanner sc = new Scanner(System.in);

        for (int i=0; i<4; i++) {
            for (int j=0; j<4; j++) {
                grid[i][j] = sc.next().charAt(0);
            }
        }

        int total = 0;

        for (int i=0; i<4; i++) {
            for (int j=1; j<3; j++) {
                {                if (grid[i][j] == 'x') {
                    int num1 = grid[i][j-1] - '0';
                    int num2 = grid[i][j+1] - '0';
                    if ( 0 <= num1 && num1 <= 9 ) {
                        total += num1;
                    }
                    if ( 0 <= num2 && num2 <= 9 ) {
                        total += num2;
                    }
                }
            }
        }

        System.out.println(total);

        }
    }
}
