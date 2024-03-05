import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
       Scanner sc = new Scanner(System.in);
       int n1 = sc.nextInt();
       int n2 = sc.nextInt();
       int n3 = sc.nextInt();
       int a[] = new int[n1];
       int b[] = new int[n2];
       int c[] = new int[n3];
        for(int i=0;i<n1;i++){
            a[i] = sc.nextInt();
        }
        for(int i=0;i<n2;i++){
            b[i] = sc.nextInt();
        }
        for(int i=0;i<n3;i++){
            c[i] = sc.nextInt();
        }
        int p=0;
        int q=0;
	    LinkedHashMap<Integer,Integer> hmap = new LinkedHashMap<>();
	    for(int i :a)hmap.put(i,hmap.getOrDefault(i,0)+1);
	    for(int i :c)hmap.put(i,hmap.getOrDefault(i,0)+1);
	    for(int i :b)hmap.put(i,hmap.getOrDefault(i,0)+1);
	    for(int i :hmap.keySet())if(hmap.get(i)>1)q++;
	    int d[] = new int[q];
	    for(int i : hmap.keySet())if(hmap.get(i)>1)d[p++]=i;
	    Arrays.sort(d);
	    System.out.println(q);
	    for(int i:d)System.out.println(i);
	}
	
}
