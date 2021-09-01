package com.ssafy;


public class PhoneTest {
    public static void main(String[] args) {

        Phone [] phoneArray = new Phone[5];

        for (int i=0; i<phoneArray.length; i++) {
            phoneArray[i] = new Phone();
            phoneArray[i].setPrice(i*2000);
        }

        for (int i=0; i<phoneArray.length; i++) {
            System.out.println(phoneArray[i].getPrice());
        }

        // for each
        for (Phone phone: phoneArray) {
            System.out.println(phone);
            System.out.println(phone.getPrice());
        }

        // outer phone
        OuterPhone op = new OuterPhone("12334");
        System.out.println(op.ic.serialNo);

        // anonymous folder
        AnonymousFolder af = new AnonymousFolder();
        af.setFolder(new Folder() {
            @Override
            public void fold() {
                System.out.println("anonymous-folder");
            }

            @Override
            public void open() {
                System.out.println("anonymous-open");
            }
        });

//        Folder anonymous = new AnonymousFolder();
//        af.setFolder(anonymous);

        // static
        System.out.println(OuterPhoneStatic.InnerChip.serialNo);


    }
}
