import java.io.*;
import java.util.*;

public class pangram {

    void main()
    {
      Scanner in=new Scanner(System.in);
        
       System.out.println("Enter a string");
        String s=in.nextLine();
        s=s.toUpperCase();
        int i,j;
        int flag=0,c=0;
        System.out.println(s);
        
                for(i=65;i<=90;i++)
                    {    
        for(j=0;j<s.length();j++)
            {
                        char ch=s.charAt(j);
                        if(i==(int)ch)
                        {
                            c++;
                        }
                    }
                    if(c==0)
                    {
                            flag=1;
                            break;
                    }
                    else
                    c=0;
                }
      
            if(flag==1)
            System.out.println("not pangram");
            else
            System.out.println("pangram");
            }
        }                  