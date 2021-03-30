package pl.proj;

import javax.naming.PartialResultException;

public class ComplexNumber {
    public final double real;
    public final double imaginary;

    ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    ComplexNumber add(ComplexNumber z) {
        return new ComplexNumber(real + z.real, imaginary + z.imaginary);
    }

    ComplexNumber subtract(ComplexNumber z) {
        return new ComplexNumber(real - z.real, imaginary - z.imaginary);
    }

    ComplexNumber multiply(ComplexNumber z) {
        return new ComplexNumber(
                real * z.real - imaginary * z.imaginary,
                imaginary * z.real + z.imaginary * real
        );
    }

    ComplexNumber divide(ComplexNumber z) {
        if (z.real * z.imaginary == 0) {
            throw new ArithmeticException("You can't divide by zero");
        }
        ComplexNumber result = new ComplexNumber(1 / z.real, 1 / z.imaginary);
        return multiply(result);
    }

    public static String formatDouble(double d) {
        if (d == (long) d)
            return String.format("%d", (long) d);
        else
            return String.format("%s", d);
    }

    @Override
    public String toString() {
        char sign = imaginary >= 0 ? '+' : '-';
        return String.format("(%s %s %si)", formatDouble(real), sign, formatDouble(Math.abs(imaginary)));
    }

    public boolean equals(Object obj) {
        if (obj instanceof String) {
            return obj.equals(toString());
        }
        if (obj instanceof ComplexNumber) {
            ComplexNumber z = ((ComplexNumber) obj);
            return z.real == real && z.imaginary == imaginary;
        }

        return false;
    }
}
