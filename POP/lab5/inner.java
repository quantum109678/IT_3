class myclass{

	static class Nested{
		void static_method(){
			System.out.println("This is the static nested class");
		}
	}
 class free{

 	 void method(){
 	 	System.out.println("This is the inner class");
 	 }
 void display(){
 	free obj=new free();
 	obj.method();
 }}
 

}
public class inner{
 public static void main(String[] args){
 	
 	myclass.Nested obj2=new myclass.Nested();
 	obj2.static_method();
 	System.out.println("This is the inner class");

 }}
