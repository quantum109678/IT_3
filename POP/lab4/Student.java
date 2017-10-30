import java.util.Scanner;

public class Student{
	int roll;
	String name;
	long ph;
	public Student(int r,String name,long phone){
		roll=r;
		this.name=name;
		ph=phone;
	}

	public int getRoll(){ return roll; }

	public String getName(){ return name;}

	public long getPhone(){ return ph; }

	public static void main(String[] args) {
			Scanner sc=new Scanner(System.in);

			System.out.println("Enter the details of Student1: ");
			System.out.print("Enter the roll: ");
			int roll=sc.nextInt();
			System.out.print("Enter the name: ");
			String name=sc.next();
			System.out.print("Enter the phone: ");
			long phone=sc.nextLong();
			Student s1=new Student(roll,name,phone);
			System.out.println("");

			System.out.println("Enter the details of Student2: ");
			System.out.print("Enter the roll: ");
			roll=sc.nextInt();
			System.out.print("Enter the name: ");
			name=sc.next();
			System.out.print("Enter the phone: ");
			phone=sc.nextLong();
			Student s2=new Student(roll,name,phone);
			System.out.println("");

			System.out.println("Enter the details of Student3: ");
			System.out.print("Enter the roll: ");
			roll=sc.nextInt();
			System.out.print("Enter the name: ");
			name=sc.next();
			System.out.print("Enter the phone: ");
			phone=sc.nextLong();
			Student s3=new Student(roll,name,phone);
			System.out.println("");

			System.out.println("Roll number of Student1: "+s1.getRoll());
			System.out.println("Name of Student2: "+s2.getName());
			System.out.println("Phone number of Student3: "+s3.getPhone());

		}	
}