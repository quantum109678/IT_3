import java.util.Scanner;
public class Employee {
    
     
    private String firstName; 
    private String lastName; 
    private double monthlySalary;
 
    public Employee(String name, String name2, double salary) {
        firstName = name;
        lastName = name2;
        monthlySalary = salary;
    }
 
    public void displayYearlySalary() {
        System.out.printf("%s %s's Yearly Salary is Rs%.2f\n", firstName, lastName,
           monthlySalary*12);
    }
 
    
    public static void main(String[] args){
        Scanner inp=new Scanner(System.in);
        int n;
        double s;
        String a,b;
        System.out.println("Enter number of employees");
        n=inp.nextInt();
        for(int i=0;i<n;i++){
        System.out.println("Enter first name");
        a=inp.next();
        System.out.println("Enter last name");
        b=inp.next();
        System.out.println("Enter monthly salary");
        s=inp.nextDouble();
        Employee e=new Employee(a,b,s);
        e.displayYearlySalary();
    }




    }
 
}
 