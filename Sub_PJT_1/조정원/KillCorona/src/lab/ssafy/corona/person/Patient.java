package lab.ssafy.corona.person;

public class Patient extends Person{
    private String diseaseName;
    private String hospitalId;
    private boolean isCorona;

    public Patient() {};

    public Patient(String name, int age, String phone, String diseaseName, String hospitalId, boolean isCorona) {
        super(name, age, phone);
        this.diseaseName = diseaseName;
        this.hospitalId = hospitalId;
        this.isCorona = isCorona;
    }

    public String getDiseaseName() {
        return diseaseName;
    }

    public void setDiseaseName(String diseaseName) {
        this.diseaseName = diseaseName;
    }

    public String getHospitalId() {
        return hospitalId;
    }

    public void setHospitalId(String hospitalId) {
        this.hospitalId = hospitalId;
    }

    public boolean isCorona() {
        return isCorona;
    }

    public void setCorona(boolean corona) {
        isCorona = corona;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(super.getName() + " ");
        sb.append(super.getPhone() + " ");
        if (isCorona) sb.append("코로나환자입니다");
        return sb.toString();
    }

    // 이름하고 전화번호가 같은 경우, 같은 사람이라고 인식될 수 있도록 equals() 추가
    @Override
    // equals 는 object 가 가지고 있어서 equals(Object 이렇게 적어준다.
    public boolean equals(Object o) {
        Patient p = (Patient) o;
        if (this.getName().equals(p.getName()) && this.getPhone().equals(p.getPhone())) {
            return true;
        }
        return false;
    }

    // set 에서 중복 확인 위해서
    // 다른 객체가 내용이 같은 경우 같은 객체라고 인식되기 위해서
    @Override
    public int hashCode() {
        int hash = 7;
        hash = 31 * hash + this.getName().hashCode();
        hash = 31 * hash + this.getPhone().hashCode();
        return hash;
    }
}
