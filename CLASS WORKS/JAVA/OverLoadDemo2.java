//automatic type conversions apply to overloading.
class OverLoadDemo {
void test () {
System.out.println("No parameters");
}
void test (int a) {
System.out.println("a: " + a);
}
void test(int a, int b) {
System.out.println("a and b: " + a + " " + b);
}
double test (double a) {
System.out.println("Inside test (double) a: " + a);
return a*a;
}
}
class overload {
public static void main (String args[]) {
OverLoadDemo ob = new OverLoadDemo();
int i = 88;

ob.test();
ob.test(10);

ob.test(i);
ob.test(123.2);
}
}