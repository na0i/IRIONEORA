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

    }
}
