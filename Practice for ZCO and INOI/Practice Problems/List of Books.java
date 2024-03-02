import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc=new Scanner(System.in);
		int m=sc.nextInt();
		ArrayList <Integer> a=new ArrayList<>(m);
		for(int i=0;i<m;i++){
		 int b=sc.nextInt();
		 a.add(b);
		}
		int n=sc.nextInt();
		 while(n!=0){
            int r = sc.nextInt();
            System.out.println(a.get(r-1));
            a.remove(r-1);
            n--;
        }
	}
}
