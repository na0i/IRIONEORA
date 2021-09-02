package com.ssafy;

// 코드 작성할 때 타입을 여러개를 적을 수 있다..
public class GenericContainer <T>{
    private T obj;

    public GenericContainer() {}

    public T getObj() {
        return obj;
    }

    public void setObj(T obj) {
        this.obj = obj;
    }
}
