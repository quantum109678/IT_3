import java.util.Scanner;
public class p1{
	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int n;
		System.out.println("Enter a number between 1 & 7");
		n=inp.nextInt();
		if(n<1 || n>7)
			System.out.println("Invalid Input");
		else
		{
			if(n==1)
				System.out.println("Monday");
			if(n==2)
				System.out.println("Tuesday");
			if(n==3)
				System.out.println("Wednesday");
			if(n==4)
				System.out.println("Thursday");
			if(n==5)
				System.out.println("Friday");
			if(n==6)
				System.out.println("Saturday");
			if(n==7)
				System.out.println("Sunday");
		}
	}
	
}