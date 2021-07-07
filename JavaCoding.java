import java.util.*;
class JavaCoding {
  /**
  Problem 1:
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    Each number is used exactly once.

  Solution: Thinking of a hash table to store and find the complement of an element;
            The sum of the complement and that element is equal to target.
  */
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer, ArrayList<Integer>> table = new Hashtable<>();
        // Use hash table to keep track of the values presented
        int idx = 0;
        for (int key : nums) {
            if (table.containsKey(key)) {
                ArrayList<Integer> lst = table.get(key);
                lst.add(idx);
                table.replace(key, lst);
            } else {
                ArrayList<Integer> lst = new ArrayList<>();
                lst.add(idx);
                table.put(key, lst); // first appearance
            }
            idx++;
        }
        
        int[] ids = new int[2];
        // Loop to check sum equals to target
        for (int i = 0; i < nums.length; i++) {   
            int remaining = target - nums[i];
            if (table.containsKey(remaining)) {
                if (remaining != nums[i]) {
                    ids[0] = i;
                    ids[1] = table.get(remaining).get(0);
                    return ids;
                } else {
                    int value = table.get(remaining).size();
                    if (remaining == nums[i] && value > 1) {
                        ids[0] = table.get(remaining).get(0); // repeated elements
                        ids[1] = table.get(remaining).get(1);
                        return ids;
                    }
                }
            }
        }      
        return ids;      
    }
  
  /** Problem 1909.
  Given a 0-indexed integer array nums, return true if it can be made strictly increasing
  after removing exactly one element, or false otherwise. If the array is already strictly
  increasing, return true. The array nums is strictly increasing if nums[i - 1] < nums[i] 
  for each index (1 <= i < nums.length).
 */
  public boolean canBeIncreasing(int[] nums) {
        
        boolean outOrder1 = false, outOrder2 = false;
        ArrayList<Integer> arrList = new ArrayList<>();
        for (int num : nums) {
            arrList.add(num);
        }
        for (int i = 0; i < arrList.size() - 1; i++) {
            
            if (arrList.get(i) >= arrList.get(i+1)) {
                if (!outOrder1) {
                    outOrder1 = true;
                    if (i - 1 >= 0 && nums[i+1] <= nums[i-1]) {
                        arrList.remove(i+1);
                        i--;
                    } else if (i + 2 < arrList.size() && arrList.get(i) >= arrList.get(i+2)) {
                        arrList.remove(i);
                        i--;
                    }
                } else {
                    outOrder2 = true;
                    break;
                }
            }
        }
        return !outOrder2;
       
    }
}
