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
}
