class BreakErr {
public static void main(String args[]) {
one: for(int i=0; i<3; i++) {
System.out.println("Pass " + i + ". ");
}
for(int j=0; j<100; j++) {
if(j == 50) 
//break one; //wrong
System.out.println(j + " ");
}
}
}