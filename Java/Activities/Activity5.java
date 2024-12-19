package hello;

abstract class Book {
	 String title;
	
	abstract void setTitle(String s);
	
	public String getTitle() {
		return this.title;
	}

}

 class MyBook extends Book {

	@Override
	public void setTitle(String s) {
		title= s;
		
	}}
	
public class Activity5{
	
	public static void main(String[] args) {
		MyBook newNovel = new MyBook();
		newNovel.setTitle("Rich Dad Poor Dad");
		
		System.out.println("The title of the book is:" + newNovel.getTitle());
		
	}
}

	

