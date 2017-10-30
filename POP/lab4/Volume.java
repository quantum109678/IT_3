import java.util.Scanner;

public class Volume{
	double x,y,z;
	public double computeVolume(double side){
		return 3*Math.PI*side*side;
	}
	public double computeVolume(double len, double wid, double heit){
		return len*wid+len*Math.sqrt(wid*wid/4+heit*heit)+wid*Math.sqrt(len*len/4+heit*heit);
	}

	public double computeVolume(double rad,double heit){
		return Math.PI*2*rad*(rad+heit);
	}
	public double computeVolume(double rad, double heit, int k){
		return Math.PI*rad*(rad+Math.sqrt(rad*rad+heit*heit));
	}
	public double computeVolume(double l, double w, double h,int k){
		return 2*(w*l+l*h+h*w);
	}
	public static void main(String[] args) {
		Volume v=new Volume();
		//Scanner sc=new Scanner(System.in);
		System.out.println("Area of the hemisphere  ="+ v.computeVolume(10.0));
		System.out.println("Area of the pyramid="+ v.computeVolume(10.0,12.0,5.0));
		System.out.println("Area of the Cylinder ="+ v.computeVolume(2.5,6.2));
System.out.println("Area of the cone ="+ v.computeVolume(2.0,3.0,1));
System.out.println("Area of the prism ="+ v.computeVolume(2.0,3.0,1.0,1));



	}
}
