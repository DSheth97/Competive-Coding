import java.util.*;
public class Solution
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        //System.out.println("Enter n,k,s");
        int n=in.nextInt();
        int k=in.nextInt();
        String s=in.next();
        s="1"+s;
        int arr[]=new int[k];
        for(int i=0;i<k;i++)
        {
           // System.out.print("Array");
            arr[i]=in.nextInt();
        }
        
        for(int j=0;j<k;j++)
        {
            char ch=s.charAt(arr[j]);
            if(ch=='0')
            {
                System.out.println("YES");
                break;
            }
            else if(ch=='1' && j==k-1)
            {
                System.out.println("NO");
                break;
            }
        }
    }
}