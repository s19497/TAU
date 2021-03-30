package pl.proj;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

class ComplexNumberTest {

    ComplexNumber a, b, x, y;

    @BeforeEach
    void setUp() {
        a = new ComplexNumber(5, 2);
        b = new ComplexNumber(3, -7);

        x = new ComplexNumber(10, -100);
        y = new ComplexNumber(10, -100);
    }

    @Test
    void testStringEncoding() {
        ComplexNumber number = new ComplexNumber(10, 2);
        assertEquals("(10 + 2i)", number.toString());
    }

    @Test
    void add() {
        assertEquals("(8 - 5i)", a.add(b).toString());
    }

    @Test
    void subtract() {
        assertEquals("(2 + 9i)", a.subtract(b).toString());
    }

    @Test
    void multiply() {
        assertEquals("(29 - 29i)", a.multiply(b).toString());
    }

    @Test
    void divide() {
        assertEquals("(1.952380952380952 - 0.04761904761904756i)", a.divide(b).toString());
    }

    @AfterEach
    void tearDown() {
    }

    @Test
    void equalComplexNumbersShouldBeEqual() {
        assertTrue(x.equals(y));
    }

    @Test
    void notEqualComplexNumbersShouldNotBeEqual() {
        assertFalse(x.equals(a));
    }

    @Test
    void complexNumberShouldNotBeEqualToObjectOfDifferentClass() {
        assertFalse(x.equals(Math.PI));
    }

    @Test
    void complexNumberAndStringEncodedComplexNumberShouldBeEqual() {
        assertTrue(a.equals("(5 + 2i)"));
    }

    @Test
    void complexNumberAndStringEncodedComplexNumberShouldNotBeEqual() {
        assertFalse(a.equals("(3 - 2i)"));
    }

    @Test
    void shouldThrowWhenDividingByZero() {
        Assertions.assertThrows(ArithmeticException.class, () -> {
            a.divide(new ComplexNumber(10, 0));
        });
    }
}