package lab.ssafy.corona.app;

import lab.ssafy.corona.virus.Corona;
import lab.ssafy.corona.virus.Virus;

public class Polymorphism {
    public static void main(String[] args) {

        Virus virus = new Corona("Corona", 8, 200);
        System.out.println(virus);
        // 객체가 Virus 객체지만, Corona의 method 가 실행되었숩니다..
        // overriding 된 method 가 호출됨

        // virus.speadSpeed;
        // virus.showInfo();
        // 얘네한테는 또 접근이 안됨..
        // 즉, 왼쪽에 정의되어 있는 method 의 경우에만 호출이 가능하고,
        // 이 때 자식에서 overriding 되어 있는 경우, 자식의 method 가 호출된다.
        // 자식이 가지고 있더라도, 객체에 없는 method나 멤버변수에는 접근이 불가능하다.

    }
}
