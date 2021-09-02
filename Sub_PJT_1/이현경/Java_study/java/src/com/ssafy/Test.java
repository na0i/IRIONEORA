package com.ssafy;

/*
public class Test {
    public static void main(String[] args) {
        int i;
        // java: variable i might not have been initialized 오류 뜸

        System.out.println(i);
    }
}
*/


//public class Test {
//    public static void main(String[] args) {
//        {
//            int i = 10;
//            System.out.println(i);
//        }
////        System.out.println(i);
//        /*
//        java: cannot find symbol
//        symbol:   variable i
//        location: class com.ssafy.Test
//        */
//    }
//}


/*
public class Test {
    public static void main(String[] args) {

        final int i = 10;
        System.out.println(i);

        i = 20;
        // java: cannot assign a value to final variable i
        System.out.println(i);
    }
}
*/

// 영시적 형변환
public class Test {
    public static void main(String[] args) {
        // A
        // error: java: incompatible types: possible lossy conversion from int to byte
        /*
        {
            int i = 10;
            byte b = i;
        }
         */
        {
            int i = 10;
            byte b = (byte) i;
            System.out.println(b);
        }

        // B
        {
            byte b = 10;
            int i = b;
            System.out.println(i);
        }
    }
}