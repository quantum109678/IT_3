import java.util.Scanner;

public class P2{
	public static void main(String[] args){
		int num,i=0;
		int arr[]=new int[4];
		Scanner inp=new Scanner(System.in);
		System.out.println("Enter the decimal number");
	    
	   num=inp.nextInt();
	   int numc=num;

	    if(num<0)
	    	num=num*-1;
	    for(int j=0;j<4;j++)
	    	arr[j]=0;

	    for( ;num>1;num/=2)
	    {arr[i]=num%2;
	    	i++;}
	    	arr[i]=1;

	    	if(numc<0)
	    		{for(int j=3;j>=0;j--)
	    			{if(arr[j]==0)
	    				arr[j]=1;
	    			else
	    				arr[j]=0;
	    			}
	    			for(int j=0;j<=3;j++)
	    				{if(arr[j]==0)
	    					{arr[j]=1;
	    						break;}

	    					else
	    						arr[j]=0;}
	    				}

	    for(int j=3;j>=0;j--)
	    	System.out.print(arr[j]);

	}
}