import java.util.Scanner;
public class p3{
	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int n,k,flag=0;
		System.out.println("Enter size of the array");
		n=inp.nextInt();
		int[] arr=new int[n];
		System.out.println("Enter the elements of the array");
		for(int i=0;i<n;i++)
			arr[i]=inp.nextInt();
		System.out.println("Enter the element whose index is to be searched for");
		k=inp.nextInt();

		for(int i=0;i<n;i++)
			{if(k==arr[i])
				{System.out.println("Index :"+i);
				flag=1;
				break;}}

				if(flag==0)
					System.out.println("Element not found");


	}
}