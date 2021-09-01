package com.ssafy;

public class StringTest {
    public static void main(String[] args) {

        int i1 = 10;
        int i2 = 10;

        String s1 = "Hello";
        String s2 = "Hello";
        String s3 = new String("Hello");
        String s4 = new String("Hello");

        if (i1 == i2) {System.out.println(true);}
        if (s1 == s2) {System.out.println(true);}
        if (s3 == s4) {System.out.println(true);}
        System.out.println("----------");
        if (s3.equals(s4)) {System.out.println(true);}

    }

}
