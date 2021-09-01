package com.ssafy;

public class AnonymousFolder {
    private Folder folder;

    // setFolder 할 때는 interface implements
    public void setFolder(Folder folder) {
        this.folder = folder;
    }

    public Folder getFolder() {
        return this.folder;
    }
}
