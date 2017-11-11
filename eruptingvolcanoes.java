import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        boolean[][] checks = new boolean[n][n];
        int[][] volcanoes = new int[n][n];
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
            volcanoes[i][j]=0;
        int max_=0;
        
            for(int a0 = 0; a0 < m; a0++){
            int x = in.nextInt();
            int y = in.nextInt();
            int w = in.nextInt();
                
            for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
            checks[i][j]=false;
            
            
            volcanoes[x][y]+=w;
            checks[x][y]=true;
            int i=1;
            w-=1;
            
            
            // Write Your Code Here
            while (w>0)    {
            for (int j=x-i;j<=x+i;j++)
                for (int k=y-i;k<=y+i;k++)
                {
                    if (k < 0 || k >= n || j < 0 || j >= n)
                        continue;
                    if (checks[j][k]==false){
                        volcanoes[j][k]+=w;
                        checks[j][k]=true;
                    }
                       
                }
            i+=1;
            w-=1;
            }
                
          
        }
        in.close();
        for (int i=0;i<n;i++)
            for (int j=0;j<n;j++)
                if (volcanoes[i][j]>max_)
                    max_=volcanoes[i][j];
        
    System.out.println(max_);
    }
    
}
