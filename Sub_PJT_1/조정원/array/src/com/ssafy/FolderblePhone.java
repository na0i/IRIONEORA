package com.ssafy;

public class FolderblePhone extends Phone implements Folder{

    private int width;
    private int height;

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public int getSmallSize() {
        return (this.width/2) * this.height;
    }

    public int getLargeSize() {
        return this.width * this.height;
    }

    // implement methods 추가
    @Override
    public void fold() {
        System.out.println("fold");
    }

    @Override
    public void open() {
        System.out.println("open");
    }


}
