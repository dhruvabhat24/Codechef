import java.util.*;
import java.lang.*;
import java.io.*;

class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes hert
		Scanner sc= new Scanner(System.in);
		int n=sc.nextInt();
		int maxlead=-1;
		int winner=-1;
		int a=0;
		int b=0;
		while(n-->0){
		    int sa=sc.nextInt();
		    int sb=sc.nextInt();
		    a+=sa;
		    b+=sb;
		    int lead=0;
		    if(a<b){
		        lead=b-a;
		        if(lead>maxlead){
		            maxlead=lead;
		            winner=2;
		        }
		    }
		    else {
		        lead=a-b;
		        if(lead>maxlead){
		            maxlead=lead;
		            winner=1;
		        }
		    }
		    
		}
		System.out.println(winner+" "+maxlead);
	}
}