import java.util.*;
class Chef
{
    void main()
    {
       Scanner in=new Scanner(System.in);
       System.out.println();
       int T=in.nextInt();
        if(T<1 || T>50)
        main();
        else
        {
            
        for(int i=1;i<=T;i++)
        {
            long D=in.nextLong();
            if(Check(D)==true)
            System.out.println("Yes");
            else if(Check(D)==false)
            System.out.println("No");
        }
    }
    }
    
    boolean Check(long x)
    {
        long len=x;
        int ones=0;int zeroes=0;
        int r;
        while(x!=0)
        {
            r=(int)x%10;
            x=x/10;
            if(r==1)
            ones++;
            else if(r==0)
            zeroes++;
        }
        if(ones==1 || zeroes==1)
        return true;
        else 
        return false;
    }
}
