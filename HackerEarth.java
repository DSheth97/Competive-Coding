import java.util.*;
public class HackerEarth
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("enter length"); 
        long n=in.nextLong();
        String s=in.next();
        System.out.println(Calc(s));
    }
    int Calc(String str)
    {
        int i,j,h=0,a=0,c=0,k=0,e=0,r=0,t=0,n=0;
        for(i=0;i<str.length();i++)
        {
            char ch=str.charAt(i);
            if(ch=='h')
            h++;
            else if(ch=='a')
            a++;
            else if(ch=='c')
            c++;
            else if(ch=='k')
            k++;
            else if(ch=='e')
            e++;
            else if(ch=='r')
            r++;
            else if(ch=='t')
            t++;
        }
        while(h>=2 && a>=2 && e>=2 && r>=2 && c>=1 && k>=1 && t>=1)
        {
            n++;
            h-=2;
            a-=2;
            e-=2;
            r-=2;
            c-=1;
            k-=1;
            t-=1;
        }
        return n;
    }
}
            