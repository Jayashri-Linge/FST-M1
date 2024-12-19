package hello;

import java.util.Arrays;

public class Activity4 {
	public static void main(String[] args) {
		int[] arr = {4,3,2,10,12,1,5,6};
		
		for(int i = 1 ; i<arr.length ; i++) {
			int temp = arr[i];
			int j= i-1;
			
			while(j >=0 && arr[j] > temp) {
				//shift the other elements to right
				arr[j+1] = arr[j];
				j--;
			}
			
			arr[j+1] = temp;
		}
		
		System.out.println("Sorted Array by Inserion Sort is: ");
		System.out.println(Arrays.toString(arr));
	}

}
