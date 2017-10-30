import java.util.Scanner;
public class comp{
	public static void main(String[] args){
 Scanner inp=new Scanner(System.in);
 double p,r,a;
 int t;
 System.out.println("Enter principal amount");
 p=inp.nextDouble();
 System.out.println("Enter rate of interest");
 r=inp.nextDouble();
 System.out.println("Enter time in years");
 t=inp.nextInt();
System.out.println("Year   Value");
 for(int i=0;i<t;i++)
 {a=p*Math.pow((1+r/1200),12);
 	System.out.println((i+1)+"  "+a);
 	p=a;}
	}
}