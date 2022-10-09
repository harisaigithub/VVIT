class Box {
double width;
double height;
double depth;
Box() {
System.out.println("Constructing Box");
width = 10;
height = 20;
depth = 30;
} 
double volume() {
return width * height * depth;
}
}

class BoxDemo6 {
public static void main (String args[]) {
Box mybox1 = new Box();
Box mybox2 = new Box();
double vol;

vol = mybox1.volume();
System.out.println("volume of box 1 is: " + vol);

vol = mybox2.volume();
System.out.println("volume of box 2 is: " + vol);
}
}