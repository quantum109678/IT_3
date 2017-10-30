import java.util.Scanner;
class pd{
	private String name;
	private int id;

	pd(String n,int k){
		this.name=n;
		this.id=k;
	}

	void display()
	{
		System.out.println("Name:"+this.name);
		System.out.println("ID:"+this.id);
	}
}

class app extends pd{
	private double apr;

	app(String n,int k,double apr){
		super(n,k);
		this.apr=apr;
	}

	void displayapr(){
		System.out.println("Name:"+this.name);
		System.out.println("ID:"+this.id);
		System.out.println("Appraisal:"+this.apr)
	}

	}

class payroll extends pd{
	private double basic;

	payroll(String n,int k,double b){
		super(n,k);
		this.basic=b;
	}

	void displaypay(){
		display();
		System.out.println("Payroll:"+(this.b*1.5+this.b*1.5*0.08));
	}
}

class pay{
	public static void main(String[] args){
		int n;
		Scanner inp=new Scanner(System.in);
		System.out.println("Enter number of employees");
		n=inp.nextInt();
		
	}
}