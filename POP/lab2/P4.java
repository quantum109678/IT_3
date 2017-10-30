import java.util.Scanner;

public class P4{
	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int x,y,r,s,t;
		System.out.println("Enter the integer");
		x=inp.nextInt();
		System.out.println("Enter the number of bits by which the number has to be shifted");
		y=inp.nextInt();
		r=x>>>y;
		s=x>>y;
		t=x<<y;
		System.out.println("Right unsigned shift="+r+"\nRight signed shift="+s+"\nLeft shift="+t);


	}
}