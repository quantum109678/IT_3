import java.util.Scanner;
 public class P1{
 	public static void main(String[] args){
 		Scanner inp=new Scanner(System.in);
 		double num1,num2,sig;
 		System.out.println("Enter the first number");
 		num1=inp.nextDouble();
 		System.out.println("Enter 1 for addition\n2 for subtraction\n3 for multiplication\n4 for division");
 		sig=inp.nextInt();;
 		System.out.println("Enter the second number");
 		num2=inp.nextDouble();

 		if(sig==1)
 			System.out.println(num1+num2);
 		if(sig==2)
 			System.out.println(num1-num2);
 		if(sig==3)
 			System.out.println(num1*num2);
 		if(sig==4)
 			System.out.println(num1/num2);
 	}
 }