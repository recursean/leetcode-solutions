import java.util.Hashtable;
import java.util.Map.Entry;
import java.util.ArrayList;
import java.util.Collections;

class Pr1481 {
    class Holder implements Comparable<Holder> {
        int val;
        int num;

        public Holder(int v, int n) {
            val = v;
            num = n;
        }

        @Override
        public int compareTo(Holder h) {
            return Integer.compare(num, h.num);
        }
    }
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        Hashtable<Integer,Integer> ht = new Hashtable<Integer,Integer>();

        // build hashtable
        for(int ele: arr) {
            Integer elei = new Integer(ele);

            int count = ht.containsKey(elei) ? ht.get(elei) : 0;
            ht.put(elei, count + 1);
        }

        // build sorted array
        ArrayList<Holder> al = new ArrayList<Holder>(ht.size());
        for(Entry<Integer, Integer> e: ht.entrySet()) {
            al.add(new Holder(e.getKey(), e.getValue()));
        }

        Collections.sort(al);

        // remove k entries
        for(int i = 0; i < k; i++) {
            Holder h = al.get(0);
            if(h.num == 1) {
                al.remove(0);
            }
            else {
                h.num--;
            }
        }

        return al.size();
    }

    public static void main(String[] args) {
        Pr1481 pr = new Pr1481();
        int[] arr = {4,3,1,1,3,3,2};
        int k = 3;

        System.out.println(pr.findLeastNumOfUniqueInts(arr, k));
    }
}