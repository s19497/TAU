package pl.proj.lab_4;

import com.sun.security.auth.login.ConfigFile;

public class Listener {
    String onMessage(JPMessage message) {
        if (message.getContent().startsWith("!play")) {
            return playMusic();
        } else if (message.getContent().contains("hello")) {
            return sayHello();
        }
        return null;
    }

    String playMusic() {
        return "Playing music";
    }

    String sayHello() {
        return "Hello";
    }

    boolean validateConfig(JPConfigFile configFile) {
        return configFile.getImportantToken().length() > 5;
    }
}
