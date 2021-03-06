/* Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.*/

class DuplicateRemove{
    static int removeDuplicate(int[] arr){
        int count = arr.length;

        for(int i = 0; i<arr.length-1; i++){
            for(int j = i; j<arr.length; j++){
                if(arr[j]>arr[i]){
                    arr[i+1] = arr[j];
                    break;
                }
            }
        }
        for(int i=0; i<arr.length-1; i++){
            if(arr[i]<=arr[i+1]){
                count = i;
            }
        }
        return count;
    }
}

public class Solution{
    public static void main(String[] args){
        int[] arr = {0, 1, 1, 2, 3, 3, 4};
        int noEle = DuplicateRemove.removeDuplicate(arr);
        for(int i=0; i<noEle; i++){
            System.out.print(arr[i]+ " ");
        }
    }
}