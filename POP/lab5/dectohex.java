import java.util.Scanner;
public class dectohex{
	
	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int n,rem,c=0,i;
		System.out.println("Enter a decimal number");
		n=inp.nextInt();
		int[] arr=new int[20];
		while(n>15){
			rem=n%16;
			arr[c]=rem;
			c++;
			n=n/16;
		}
		arr[c]=n;
		

		System.out.print("Given number in Hexadecimal=0x");
		for( i=c;i>-1;i--){
			if(arr[i]<10)
				System.out.print(arr[i]);
			else if(arr[i]==10)
				System.out.print("A");
			else if(arr[i]==11)
			System.out.print("B");
			else if(arr[i]==12)
			System.out.print("C");
			else if(arr[i]==13)
			System.out.print("D");
			else if(arr[i]==14)
			System.out.print("E");
			else if(arr[i]==15)
			System.out.print("F");

		}


	}
}