class Coversion{
public static void main (String args[]){
byte b;
int i = 123;
double d = 2735254.5836;

System.out.println("\nConversion of int to byte: ");
b = (byte) i;
System.out.println("i and b " + i + " " + b);

System.out.println("\nConversion of double to int: ");
i = (int) d;
System.out.println("d and i " + d + " " + i);

System.out.println("\nConversion of double to byte: ");
b = (byte) d;
System.out.println("d and b " + d + " " + b);
}
}