package lab.ssafy.corona.app;

import lab.ssafy.corona.virus.Corona;
import lab.ssafy.corona.virus.Virus;

import java.util.*;

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




        Corona c1 = new Corona("Corona1", 8, 1);
        Corona c2 = new Corona("Corona2", 8, 2);
        Corona c3 = new Corona("Corona3", 8, 3);
        Corona c4 = new Corona("Corona4", 8, 4);
        Corona c5 = new Corona("Corona5", 8, 5);
        Corona c6 = new Corona("Corona6", 8, 6);
        Corona c7 = new Corona("Corona7", 8, 7);

        // 우선순위 큐
        PriorityQueue<Corona> pq = new PriorityQueue<>();
        pq.add(c1);
        pq.add(c2);
        pq.add(c3);
        pq.add(c4);
        pq.add(c5);
        pq.add(c6);
        pq.add(c7);

        while(!pq.isEmpty()) System.out.println(pq.poll());
        // poll == pop
        // pick == 꺼내지는 않고 보기만 하는 애


        Virus fv1 = new Virus("fv1", 5);
        Virus fv2 = new Virus("fv2", 9);
        Virus fv3 = new Virus("fv3", 1);
        Virus fv4 = new Virus("fv4", 7);
        Virus fv5 = new Virus("fv5", 3);

        List<Virus> list = new ArrayList<>();
        list.add(fv1);
        list.add(fv2);
        list.add(fv3);
        list.add(fv4);
        list.add(fv5);

        // anonymous class
//        Collections.sort(list, new Comparator<Virus>() {
            // 객체를 만드는 시점에 필요한 부분을 정의
//            @Override
//            public int compare(Virus o1, Virus o2) {
//                return o1.getLevel() - o2.getLevel();
//            }
//        });

        // lambda
        Collections.sort(list, (o1, o2) -> {
            return o1.getLevel() - o2.getLevel();
        });

        for (Virus fv : list) System.out.println(fv);

    }
}
