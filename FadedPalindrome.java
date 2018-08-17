import java.util.*;
import java.io.*;
public class FadedPalindrome
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter no. of inputs");
        int n=in.nextInt();
        if(n<1 || n>50)
        main();
        for(int i=0;i<n;i++)
        {
            String s=in.next();
            solve(s);
        }
    }
    
    void solve(String s)
    {
        String str=" ";
        int l=s.length();
        if(l>12345 || l<1)
        main();
        for(int i=0;i<l;i++)
        {
            char ch=s.charAt(i);
            if(ch<65 || ch>90 || (ch!='.'))
            main();
        }
        int c=s.indexOf(".");
            if((l%2!=0) && (c==(l/2)))
            {
               str=(s.replace(s.charAt(l/2),'a'));
            }
            else
            {
              str=s.replace(s.charAt(c),s.charAt(l-c-1));
            }
        if(CheckPal(str)==true)
        System.out.println(str);
        else
        System.out.println("-1");
    }
    
    
    boolean CheckPal(String s)
    {
        StringBuffer st=new StringBuffer(s);
        st.reverse();
        String str=st.toString();
        if(str.equals(s))
        return true;
        else
        return false;
    }
}