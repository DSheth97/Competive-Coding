import java.util.*;
public class Lighthouse
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter n grid = ");
        int n=in.nextInt();
        if(n>50)
        main();
        String arr[][]=new String[n][n];
        int i,j;
        System.out.println("Enter * or . ");
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                System.out.println();
                arr[i][j]=in.next();
            }
        }
        int c=0,max=0,row=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(arr[i][j].equals("."))
                c++;
            }
            if(c>max)
            {
                max=c;
                row=i;
            }
        }
        int k,t=0;
        if(max%2==0)
        System.out.println("0");
        
        else
        {
            for(k=0;k<n;k++)
            {
                if(arr[k][row].equals("."))
                t++;
            }
        }
        if(t==max)
        System.out.println(t/2);
    }
}
            