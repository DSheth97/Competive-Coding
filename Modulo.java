import java.util.*;
public class Modulo
{
    int Divisors(int d)
    {
        int i,c=0;
        for(i=1;i<=d;i++)
        {
            if(d%i==0)
            c++;
        }
        return c;
    }
    
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter no of inputs");
        int n=in.nextInt();
        int i,j,s=0,p;
        for(i=1;i<=n;i++)
        {
            int a=in.nextInt();
            int b=in.nextInt();
            for(j=1;j<=a;j++)
            {
                p=(int)(Math.pow(j,b));
                System.out.println("j^b = "+p);
                s=s+Divisors(p);
                System.out.println("s = "+s);
            }
            System.out.println("Final sum = "+s);
            s=0;
        }
    }
    }