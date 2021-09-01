package lab.ssafy.corona.app;

import lab.ssafy.corona.virus.Corona;
import lab.ssafy.corona.virus.Virus;

public class CoronaTest {
    public static void main(String[] args) {
        Virus virus = new Virus();
        virus.setName("MERS");
        virus.setLevel(5);

        Corona corona = new Corona("Corona", 8, 200);
//        corona.setName("Corona");
//        corona.setLevel(8);
//        corona.setSpreadSpeed(200);

        corona.showInfo();

        Virus newVirus = new Virus("UNKNOWN", 5);
        // toString 정의하지 않고 실행하게 되는경우,
        // 주소값이 출력됨
        System.out.println(newVirus);

        System.out.println(corona);

    }
}
