class area{
	private double len;
	private double wid;
	private double ht;


	public area(double len){
		this.len=len;
		this.wid=len;
		this.ht=1;
	}

	public area(double len,double wid,double ht){
		this.len=len;
		this.wid=wid;
		this.ht=ht;

	}

	public area(double len,double wid){
		this.len=len;
		this.wid=wid;
		this.ht=1;
	
	}

	public double calc_area(){
		return (this.len*this.wid*this.ht);
	}
	 public double cubear(){
	 	return (6*this.len*this.len);
	 }

	
 
	public static void main(String[] args){
		area obj=new area(5);
		System.out.println("Area of square="+obj.calc_area());
		area rec=new area(5,6);
		System.out.println("Area of rectangle="+rec.calc_area());
		area cube=new area(3,3,3);
		System.out.println("Area of cube="+cube.cubear());
		area sph=new area(4);
		System.out.println("Area of sphere="+(4*Math.PI*4*4));
		area cylin=new area(3,5);
		System.out.println("Area of cylinder="+(2*Math.PI*3*8));
	}


}
