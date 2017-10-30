import java.util.*;
public class Test{
double n1,n2,n3;
private Test(double a, double b, double c){
	this.n1=a;
	this.n2=b;
	this.n3=c;
}
private String check(double a, double b, double c){
	if(n1>n2 && n2>n3)
		return "Decreasing";
	else if(n1<n2 && n2<n3)
		return "Increasing";
	else
		return "Neither Increasing or Decreasing";
}

public static void main(String[] args) {
	double n1,n2,n3;
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter three numbers: ");
	n1=sc.nextDouble();
	n2=sc.nextDouble();
	n3=sc.nextDouble();
	Test test=new Test(n1,n2,n3);
	String res=test.check(n1,n2,n3);
	System.out.println(res);
}

}