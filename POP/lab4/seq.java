import java.util.Scanner;
public class seq{
	public static void main(String[] args){
		int[] arr=new int[100];
		Scanner inp=new Scanner(System.in);
		int n,temp;
		System.out.println("Enter the array size");
		n=inp.nextInt();
		System.out.println("Enter the array elements");
		for(int i=0;i<n;i++)
			arr[i]=inp.nextInt();

		for(int i=0;i<n;i++){
			for(int j=0;j<n-i-1;j++){
				if(arr[j]>arr[j+1])
				{
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
				}
			}
		}
		
		int in=0;
		int[] count=new int[20];
		for(int i=0;i<n;i++)
			count[i]=0;

		for(int i=0;i<n;i++)
			{if(arr[i+1]-arr[i]==1)
				count[in]++;

			else
				in++;
			}

			int max=count[0];
			for(int i=1;i<in+1;i++)
			{if(max<count[i])
				max=count[i];
				else 
					continue;}
				System.out.println("Length of longest sequence="+(max+1));
	}

}