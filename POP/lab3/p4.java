import java.util.Scanner;
public class p4{
	
	public static void main(String[] args){
		int[] arr1=new int[100];
		int[] arr2=new int[100];
		Scanner inp=new Scanner(System.in);
		int n1,n2,flag=0;

		System.out.println("Enter size of array1");
		n1=inp.nextInt();
		System.out.println("Enter elements of array1");
		for(int i=0;i<n1;i++)
			arr1[i]=inp.nextInt();

		System.out.println("Enter size of array2");
		n2=inp.nextInt();
		System.out.println("Enter elements of array2");
		for(int i=0;i<n2;i++)
			arr2[i]=inp.nextInt();

		System.out.println("Common elements:");

		for(int i=0;i<n1;i++){
			for(int j=0;j<n2;j++){
				if(arr1[i]==arr2[j])
					{System.out.print(arr1[i]+" ");
				flag=1;}}}

				if(flag==0)
					System.out.print("No common elements");
			
		
		




	}
}