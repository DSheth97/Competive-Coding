import java.util.*;
public class ChefAndCalculation
{
    int UniqDig(String arr[])
    {
        int l=arr.length;
        for(int i=1;i<l;i++)
        {
            char ch=arr[i].charAt(0);
            if(ch!=32)
            for(int j=i+1;j<l;j++)
            {
                if(arr[i].equals(arr[j]))
                arr[j]=" ";
            }
        }
        
        char ch1;int c=0;
        for(int k=1;k<l;k++)
        {
            ch1=arr[k].charAt(0);
            if(ch1!=32)
            c++;
        }
        
        return c;
    }
    
    void main()
    {
        Scanner in=new Scanner(System.in);
        System.out.println("Enter no of players");
        int n=in.nextInt();
        int maxcookies=0;
        int player=1;
        int flag=0,equalcookies=0;
        for(int i=1;i<=n;i++)
        {
            System.out.println("Enter cookies");
            String s=in.next();
            StringTokenizer st=new StringTokenizer(s);
            int l=st.countTokens();
            int c=0;
            String arr[]=new String[l];
            for(int j=0;j<l;j++)
            {
                String a=st.nextToken();
                arr[c]=a;
                c++;
            }
            int p=UniqDig(arr);
            System.out.println("unique digits = "+p);
            if(p==4)
            p++;
            else if(p==5)
            p+=2;
            else if(p==6)
            p+=3;
            int totalcookies=Integer.parseInt(arr[0])+p;
            System.out.println("Total cookies = "+totalcookies);
            if(totalcookies>maxcookies)
            {
                maxcookies=totalcookies;
                player=i;
                flag=1;
            }
            else if(totalcookies==maxcookies)
            {
                equalcookies++;
            }
        }
        System.out.println("Equal cookies = "+equalcookies);
        System.out.println("Flag = "+flag);
        System.out.println("Player = "+player);
        if(equalcookies==n)
        System.out.println("Tie");
        else if(flag==1 && player==1)
        System.out.println("Chef");
        else if(flag==1 && player!=1)
        System.out.println(player);
        else
        System.out.println("Error");
    }
}
        