package com.ssafy;

public class AbstractClassTest {
    
}

interface ManyIf {
    void m1();
    void m2();
    void m3();
    void m4();
    void m5();
}

// 클래스 직접 구현하는 경우
// 아래처럼 모든 메서드에 대해서 직접 구현이 필요.
// 하나도 빼면 안된다.
//class MyClass implements ManyIf {
//    @Override
//    public void m1() {
//
//    }
//
//    @Override
//    public void m2() {
//
//    }
//
//    @Override
//    public void m3() {
//
//    }
//
//    @Override
//    public void m4() {
//
//    }
//
//    @Override
//    public void m5() {
//
//    }
//}

// 위처럼 전부 구현하지 않고,
// 내가 필요한 일부만 구현해서 사용하기 위해서
// 중간에 abstract class 사용
// m2/ m5 의 경우 구체적인 내용을 구현하지 않을 수 있음.
abstract class ManyIfAdapter implements ManyIf {
    @Override
    public void m1() {}

    public abstract void m2();

    @Override
    public void m3() {

    }

    @Override
    public void m4() {

    }

    public abstract void m5();
}

// 여기서 어댑터를 extend 해와서 m2/ m5의 내용만 정의할 수 있음...
class Myclass extends ManyIfAdapter {
    @Override
    public void m2() {
    }

    @Override
    public void m5() {

    }
}


