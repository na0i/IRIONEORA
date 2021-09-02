package com.ssafy;

import java.io.File;
import java.io.IOException;

public class FileTest {
    public static void main(String[] args) throws IOException {

        // 이거 경로 정해야 하는데
        // 어떻게 하는 지 모르겠네여
        String dirName = "Users"+ File.separator+ "cho.jardin"+ File.separator+"mydir";

        // 파일 객체 생성
        File file1 = new File(dirName);

        // 있다면,
        if (file1.exists()) {
            System.out.println("Folder Exists!");
        }
        // 파일이 이미 존재하지 않다면,
        else {
            boolean success = file1.mkdir();
            if (success) {
                System.out.println("Folder Created!");
            }
        }

        File file2 = new File(dirName, "test2.txt");

        file2.createNewFile();
    }
}
