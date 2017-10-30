import java.util.Scanner;
class swap{
	int i;
	int j;

	swap(int i,int j){
		this.i=i;
		this.j=j;
	}

	static void value(int k,int l){
		int tmp=k;
		k=l;
		l=tmp;
		System.out.println(k+" "+l);
	}

 void ref(){
		int tmp;
		tmp=this.i;
		this.i=this.j;
		this.j=tmp;
		System.out.println(this.i+" "+this.j);
	}


	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
		int n1,n2;
		System.out.println("Enter 2 numbers to be swapped");
		n1=inp.nextInt();
		n2=inp.nextInt();
		swap obj=new swap(n1,n2);
		System.out.println("Swap by call by value");
		value(n1,n2);
		System.out.println("Swap by call by reference");
		obj.ref();


	}
}