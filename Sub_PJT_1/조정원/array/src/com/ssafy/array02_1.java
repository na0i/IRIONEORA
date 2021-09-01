package com.ssafy;

public class array02_1 {
    public static void main(String[] args) {

        String ssafy = "SSAFY";

        char [] ssafyArray = new char[ssafy.length()];

        for (int i = 0; i < ssafy.length(); i++) {
            ssafyArray[i] = ssafy.charAt(i);
        }

//        for (int i = 0; i < ssafyArray.length; i++) {
//            System.out.println(ssafyArray[i]);
//        }

        // for-each 구문
        // 원본 변경은 불가함. readonly
        for (char c : ssafyArray) {
            System.out.print(c);
//            System.out.println(c);
            // 이게 println 얘는 newline 아니면 줄바꿈 없음
        }

//        Arrays.toString()
//        배열 알아서 출력 가능한 methods
        System.out.println("__________");
        ssafyArray.toString();


    }
}
