import java.util.*;
public class Plates
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter Details");
        String s=in.next();
        int l=s.length();
        int n=s.charAt(0);
        int k=s.charAt(l-1);
        int arr[][]=new int[n][2];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<2;j++)
            {
                System.out.println("Enter in array");
                arr[i][j]=in.nextInt();
            }
        }
        int max=0;
        int inc[]=new int[n];
        int ded[]=new int[n];
        for(int t=0;t<n;t++)
        {
            for(int p=0;p<2;p++)
            {
                if(p==0)
                {
                inc[t]=arr[t][p];
            }
            else if(p==1)
            {
                ded[t]=arr[t][p];
            }
        }
    }
    int a,b;
    int sum=0,loss=0;
    for(a=0;a<n;a++)
    {
        for(b=1;b<=k;b++)
        {
            sum=sum+inc[a+1];
            loss=loss-ded[a+1];
        }
        if((sum-loss)>max)
        max=sum-loss;
    }
    System.out.println(max);
}
}
            