import java.util.*;
public class Gear
{
    void main()
    {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        for(int i=1;i<=n;i++)
        {
            int t=in.nextInt();
            if(t%2==0 && t!=2)
            System.out.println("Yes");
            else
            System.out.println("No");
        }
    }
}