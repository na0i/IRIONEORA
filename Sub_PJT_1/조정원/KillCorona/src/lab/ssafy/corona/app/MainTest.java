package lab.ssafy.corona.app;

import lab.ssafy.corona.medical.CDC;
import lab.ssafy.corona.medical.Hospital;
import lab.ssafy.corona.person.Patient;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class MainTest {
    public static void main(String[] args) {

        // 병원
        Hospital univHospital = new Hospital("대학병원", 15, "001", 50, 10);
        Hospital localHospital = new Hospital("동네병원", 3, "901", 10, 2);

        // 환자
        Patient p1 = new Patient("환자1", 42, "010-1111-2222", "호흡곤란", "001", true);
        Patient p2 = new Patient("환자2", 30, "010-3333-4444", "과음", "901", true);

        // 병원 collection
        // Hospital 로 이루어진 새로운 array List 를 만들겠다는 말인 것 같다..
        List<Hospital> hospitalList = new ArrayList<Hospital>();
        hospitalList.add(univHospital);
        hospitalList.add(localHospital);

        // 환자 collection
        Set<Patient> patientList = new HashSet<Patient>();
        patientList.add(p1);
        patientList.add(p2);

        CDC cdc = new CDC("질병관리본부", 200, hospitalList, patientList);
        cdc.about();
//        cdc.printPatientList();

        univHospital.setCdc(cdc);
        localHospital.setCdc(cdc);

        // 새로운 환자 등록
        Patient p3 = new Patient("환자3", 33, "010-3333-4444", "고열", "001", false);
        // 이거 그냥 실행하면 Null Point Exception 발생하는데,
        // cdc 를 위에서 만들었지만, hospital이 가지고 있는 cdc와 연결되지 않아서 hospital 의 cdc 가 null이라서 발생
        // 위에 setCdc 통해서 연결해주게 되면 에러 안 발생
        univHospital.addPatient(p3);

        // 같은 사람으로 인식하도록 equals() method overriding
        Patient p4 = new Patient("환자3", 33, "010-3333-4444", "고열", "001", false);
        univHospital.addPatient(p4);

        cdc.printPatientList();

    }
}
