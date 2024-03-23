//adding a method

class Box {
double width;
double height;
double depth;
void volume () {
System.out.println ("Volume is ");
System.out.println (width * height * depth);
}
}
class BoxDemo3 {
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

mybox1.volume();
mybox2.volume();
}
}