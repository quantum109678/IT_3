import java.util.Scanner;
public class student{
	public String name;
	public int[] sub=new int[5];
	

	public student(String name,int[] marks){
		this.name=name;
		for(int i=0;i<5;i++)
			this.sub[i]=marks[i];
	}

	public int total(){
		int tot=0;
		for(int i=0;i<5;i++)
			tot=tot+this.sub[i];
		return tot;
	}



	public static void main(String[] args){
		Scanner inp=new Scanner(System.in);
	
		int[] tota=new int[5];
		student[] stu=new student[5];

		
		String n;
		int[] marks=new int[5];
		for(int j=0;j<5;j++)
		{System.out.println("Enter name of student"+(j+1));
		n=inp.next();
		System.out.println("Enter marks in 5 subjects");
		for(int i=0;i<5;i++)
			marks[i]=inp.nextInt();
			stu[j]=new student(n,marks);}

		for(int i=0;i<5;i++){
			tota[i]=stu[i].total();
			System.out.println("Total marks of "+stu[i].name+"= "+tota[i]);
		}


		


	}
}