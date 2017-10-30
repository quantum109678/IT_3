import java.util.Scanner;
public class p2{
	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int[] arr=new int[100];
		int n,c=0;
		System.out.println("Enetr size of the array");
		n=inp.nextInt();
		System.out.println("Enter the elements of the array");
		for(int i=0;i<n;i++)
			arr[i]=inp.nextInt();

		for(int i=0;i<n;i++)
	{if(arr[i]==10)
		c++;}

		if(c==3)
			System.out.println("True");
		else
			System.out.println("False");




	}
}