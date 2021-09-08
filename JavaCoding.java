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
  
  /* Robot Bounded In Circle */
  public boolean isRobotBounded(String instructions) {
        // coordinates
        int x = 0;
        int y = 0;
        int tempCoord = 1; // North = 1, West = 2, South = 3, East = 4 
        int i = 0;
        while (i < 4) {
            for (int j = 0; j < instructions.length(); j++) {
                if (instructions.charAt(j) == 'G') {
                    if (tempCoord == 1) {
                        y += 1; // go North
                    }
                    else if (tempCoord == 2) {
                        x -= 1; // go West
                    }
                    else if (tempCoord == 3) {
                        y -= 1; // go South
                    }
                    else {
                        x += 1; // go East
                    }
                }
                else if (instructions.charAt(j) == 'L') {
                    if (tempCoord == 1) {
                        tempCoord = 2; // from North to West
                    }
                    else if (tempCoord == 2) {
                        tempCoord = 3; // from West to South
                    }
                    else if (tempCoord == 3) {
                        tempCoord = 4; // from South ot East
                    }
                    else {
                        tempCoord = 1; // from East to North
                    }
                 }
                else { // turn right
                    if (tempCoord == 1) {
                        tempCoord = 4; // from North to East
                    }
                    else if (tempCoord == 2) {
                        tempCoord = 1; // from West to North
                    }
                    else if (tempCoord == 3) {
                        tempCoord = 2; // from South to West
                    }
                    else {
                        tempCoord = 3; // from East to South
                    }
                }
            }
            if (x != 0 || y != 0) {
                // if either of the x or y is not in the correct position
                i += 1;
            } else {
                i = 4;
            }
        }
        return x == 0 && y == 0;
    }
}
 
/* Illustrate how LRU Cache runs - Medium */
class LRUCache {
    private int capacity;
    private int size;
    private int leastRank;
    private int currMaxRank;
    private Cache[] contents; 
    private int tempIdx;
   
    
    protected class Cache {
        int rank;
        int key;
        int value;
        
        public Cache(int rank, int key, int value) {
            this.rank = rank;
            this.key = key;
            this.value = value;
        }
        
        public int getKey() {
            return this.key;
        }
        
        public int getVal() {
            return this.value;
        }
        
        public int getRank() {
            return this.rank;
        }
        
        public void updateRank(int newRank) {
            this.rank = newRank;
        }
        
        public void update(int newRank, int newKey, int newVal) {
            this.rank = newRank; // change rank
            this.key = newKey; // change key
            this.value = newVal; // change val
        }
    }
    
    // Use circular array idea; lecture 26, cse 12
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.leastRank = 0;
        this.currMaxRank = -1;
        this.tempIdx = 0;
        this.contents = new Cache[capacity];
    }
    
    public int get(int key) {
        int i = 0;
        while (i < this.capacity) {
            if (this.contents[i] != null) {
                if (this.contents[i].getKey() == key) {
                    this.tempIdx = i;
                    this.contents[i].updateRank(this.currMaxRank + 1);
                    this.currMaxRank += 1;
                    return this.contents[i].getVal();
                }
            }        
            i++;
        }
        return -1;
    }
    
    private void updateLeastRank(int key, int value) {
        // Remove least rank, add new (key-value)
        int i = 0;
        while (i < this.capacity) { 
            if (this.contents[i] != null) {
                if (this.contents[i].getRank() == this.leastRank) {
                    this.contents[i].update(this.currMaxRank + 1, key, value);
                    this.currMaxRank += 1; // update current Max rank
                    break;
                }
            }
            i++;
        }
    }
    
    public void put(int key, int value) {
        if (this.find(key) != -1) { // key exists
            this.contents[this.tempIdx].update(this.currMaxRank + 1, key, value); // update value
            this.currMaxRank += 1;
        } else { // key DNE
            if (this.size == this.capacity) {
                this.updateLeastRank(key, value);
            } else {
                // add new
                this.contents[this.size] = new Cache(this.currMaxRank+1, key, value);
                this.size += 1; // update size          
                this.currMaxRank += 1; // update curr max rank
            }
        }
    } 
    
    
    private int find(int key) {
        int i = 0;
        int returnVal = -1;
        this.leastRank = this.currMaxRank;
        while (i < this.capacity) {
            if (contents[i] != null) {
                if (this.contents[i].getKey() == key) {
                    this.tempIdx = i;
                    returnVal = this.contents[i].getVal();
                }
                
                if (this.contents[i].getRank() < this.leastRank) {
                    this.leastRank  = this.contents[i].getRank();
                }
            }    
            i++;
        }
        //this.leastRank = tempMin;
        return returnVal;
    }
  }
}

/* Reverse Linked list */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        // 0 node, 1 node
        if(head == null || head.next == null) {
            return head;
        } 
        // 2 nodes
        if (head.next.next == null) {
            ListNode pre = head;
            ListNode curr = head.next;
            head = curr;
            curr.next = pre;
            pre.next = null;
            return head;
        }
        
        // more than 2 nodes
        ListNode pre = head, curr = head.next, after = head.next.next, temp = null;
        pre.next = null;
        while (after != null) {
            // update curr links
            curr.next = pre;
            temp = after.next;
            after.next = curr;
            
            if (temp == null) {
                head = after;
            }
            
            // update for next iteration
            pre = curr;
            curr = after;
            after = temp;
        }
        return head;
    }
}
