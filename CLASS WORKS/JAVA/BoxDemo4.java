class Box {
double width;
double height;
double depth;

double volume () {
return width * height * depth;
}
}
class BoxDemo4 {
public static void main (String args[]) {
Box mybox1 = new Box();
Box mybox2 = new Box();
double vol;

mybox1.width = 10;
mybox1.height = 20;
mybox1.depth = 30;

mybox2.width = 9;
mybox2.height = 2;
mybox2.depth = 3;

vol = mybox1.width * mybox1.height * mybox1.depth;
System.out.println("volume of box 1 is: " + vol);

vol = mybox2.width * mybox2.height * mybox2.depth;
System.out.println("volume of box 2 is: " + vol);
}
}