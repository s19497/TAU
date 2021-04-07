package pl.proj.lab_4;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class JPMessageTest {

    Listener listener = new Listener();

    @Test
    void listenerShouldReturnHello() {
        JPMessage message = mock(JPMessage.class);
        when(message.getContent()).thenReturn("say hello, please");
        String returnString = listener.onMessage(message);
        assertEquals("Hello", returnString);
    }

    @Test
    void listenerShouldReturnNull() {
        JPMessage message = mock(JPMessage.class);
        when(message.getContent()).thenReturn("say !play, please");
        String returnString = listener.onMessage(message);
        assertNull(returnString);
    }

    @Test
    void listenerShouldDeclareConfigFileValid() {
        JPConfigFile configFile = mock(JPConfigFile.class);
        when(configFile.getImportantToken()).thenReturn("123456789");
        boolean isValid = listener.validateConfig(configFile);
        assertTrue(isValid);
    }

    @Test
    void listenerShouldDeclareConfigFileInValid() {
        JPConfigFile configFile = mock(JPConfigFile.class);
        when(configFile.getImportantToken()).thenReturn("1234");
        boolean isValid = listener.validateConfig(configFile);
        assertFalse(isValid);
    }
}
