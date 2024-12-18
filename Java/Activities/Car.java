package hello;

public class Car {
	
	private int make;
	private String colour ;
	private String transmissionType ;
	
	//constructor
	public Car(int make, String colour, String transmissionType) {
		this.make = make;
		this.colour = colour;
		this.transmissionType = transmissionType;
	}
	
	public void printData() {
		System.out.println("The details of Audi is: ");
		System.out.println(make + " " + colour + " " + transmissionType  );
	}

	public void accelerate() {
		 System.out.println("The speed is increased");
	
	}
	
	public void brake() {
		System.out.println("The speed has reduced to 0");
		
	}
}
