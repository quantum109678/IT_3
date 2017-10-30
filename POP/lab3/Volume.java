import java.util.Scanner;

public class Volume{
	double x,y,z;
	public double computeVolume(double side){
		return side*side*side;
	}
	public double computeVolume(double len, double wid, double heit){
		return len*wid*heit;
	}

	public double computeVolume(double rad,double heit){
		return Math.PI*rad*rad*heit;
	}
	public double computeVolume(double rad, double heit, int k){
		return (1.0/3)*Math.PI*rad*rad*heit;
	}
	public static void main(String[] args) {
		Volume v=new Volume();
		//Scanner sc=new Scanner(System.in);
		System.out.println("Volume of the cube ="+ v.computeVolume(10));
		System.out.println("Volume of the cuboid ="+ v.computeVolume(10,12,5));
		System.out.println("Volume of the Cylinder ="+ v.computeVolume(2.5,6.2));
System.out.println("Volume of the cone ="+ v.computeVolume(2.0,3.0,1));


	}
}
