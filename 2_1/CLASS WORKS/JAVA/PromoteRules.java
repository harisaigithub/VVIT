class PromoteRrules{
public static void main(String args[]){
byte b = 54;
char c = 'a';
short s = 2551;
int i = 246353;
float f = 2.44f;
double d = .4645;

double result = (f * b) + (i / c) - (d * s);
System.out.println((f * b) + " + " + (i/ c) + " - " + (d * s));
System.out.println("result = " + result);
}
}