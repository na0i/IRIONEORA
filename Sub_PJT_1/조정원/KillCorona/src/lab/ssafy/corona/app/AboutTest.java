package lab.ssafy.corona.app;

import lab.ssafy.corona.medical.Hospital;
import lab.ssafy.corona.medical.Organization;

public class AboutTest {
    public static void main(String[] args) {

        // overriding 된 hospital 의 about 출력
        Organization org = new Hospital("대학병원", 15, "001", 50, 10);
        org.about();
    }
}
