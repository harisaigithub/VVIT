class ScopeErr{
public static void main(String args[]){
int bar = 1;
{
int bar = 2; //this cause an error coz bar is alredy defined
}
}
}