import java.util.Scanner;
class prod{
	public String name;
	public double price;
	public static double tot=0;
	public int qty;

	prod(String name,double price){
		this.name=name;
		this.price=price;
		this.qty=0;

	} 

	public void set(int q){
		this.qty=q;
	}

	void display(){
		System.out.print("Name:"+this.name+"\t");
		System.out.print("Price:"+this.price);
		System.out.println();
	}

	void display1(){
		System.out.print("Name:"+this.name+"\t");
		System.out.print("Quantity selected:"+this.qty);
		System.out.println();
	}

	public static void totall(double a,double b){
		tot=tot+a*b;
		
	}
}
public class prob{
	public static void main(String args[]){
		Scanner inp=new Scanner(System.in);
		System.out.println("Enter number of objects");
		int n=inp.nextInt();
		prod arr[]=new prod[n];
		String na;
		double p;
		double total=0;
		for(int i=0;i<n;i++){
			System.out.println("Product name:");
			na=inp.next();
			System.out.println("Price:");
			p=inp.nextDouble();
			arr[i]=new prod(na,p);

		}
		int q;
		for(int i=0;i<n;i++){
			arr[i].display();

		}
		for(int i=0;i<n;i++)
{
	System.out.println("Enter quantity for "+arr[i].name);
	q=inp.nextInt();
	arr[i].set(q);

}
for(int i=0;i<n;i++){
			arr[i].display1();}



for(int i=0;i<n;i++){
	prod.totall(arr[i].price,arr[i].qty);
}

System.out.println("Total="+prod.tot);




	}
}