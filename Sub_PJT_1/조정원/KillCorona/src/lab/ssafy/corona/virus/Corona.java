package lab.ssafy.corona.virus;

public class Corona extends Virus implements Comparable<Corona>{
    private String name = "코로나";
    public int spreadSpeed;

    public int getSpreadSpeed() {
        return spreadSpeed;
    }

    public void setSpreadSpeed(int spreadSpeed) {
        this.spreadSpeed = spreadSpeed;
    }

    public void showInfo() {
        // 부모 클래스에서 바로 가져와서 사용할 수 없음 this.name/ this.level => 오류 발생 => protected
        String info = super.getName() + " " + this.getLevel() + " " + this.spreadSpeed;
        System.out.println(info);
    }

    public Corona() {
        // 사실 이게 아무것도 없는 거 같지만, 자동으로
        //super();
        // 이거 호출해주는 것인데, 없으면 오류가 발생
    }

    // setter를 이용하지 않고 생성자로 곧바로 만들 수 있다.
    public Corona(String name, int level, int spreadSpeed) {
        // protected 의 경우
//        super.name = name;
//        super.level = level;
        // private 인 경우
//        super.setName(name);
//        super.setLevel(level);
        // 부모가 생성자로 만들어질 수 있을 때,
        super(name, level);
        this.spreadSpeed = spreadSpeed;
    }

    @Override
    public String toString() {
        // 부모 객체에 정의되어 있는 toString 에 추가적으로 spreadSpeed도 추가하겠다!
        return super.toString() + " " + this.spreadSpeed;
    }

    // priority queue
    // implements Comporable
    @Override
    public int compareTo(Corona c) {
        return this.spreadSpeed - c.spreadSpeed;
    }
}
