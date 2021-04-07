package pl.proj.lab_4;

public class JPMessage {
    private long id;
    private String content;

    public long getId() {
        return id;
    }

    public String getContent() {
        return content;
    }

    public JPMessage(long id, String content) {
        this.id = id;
        this.content = content;
    }
}
