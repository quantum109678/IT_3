import java.util.Scanner;

public class P3{
	public static void main(String[] args){
		int a,b,c,m,n,k;
		double f1,f2,y,x;
		Scanner inp=new Scanner(System.in);
		System.out.println("For the equation a*x +b*y +c=0, enter the values of a,b,c respectively");
		a=inp.nextInt();
		b=inp.nextInt();
		c=inp.nextInt();
		System.out.println("For the equation m*x +n*y +k=0, enter the values of m,n,k respectively");
		m=inp.nextInt();
		n=inp.nextInt();
		k=inp.nextInt();
        
        b=b*m;
        c=c*m;
        n=n*a;
        k=k*a;

		if((a>0&&m>0)||(a<0&&m<0))
			{f1=b-n;
			f2=c-k;}

		else
			{f1=b+n;
			f2=c+k;}
			
			b=b/m;

			y=(-f2/f1);
		
			x=(-c/m-b*y)/a;

		System.out.println("x="+x+" y="+y);

	}
}