import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String name[] = new String[n];
        for(int i = 0; i < n; i++){
            String str = br.readLine();
            System.out.println(str.substring(0,1) + str.substring(str.length()-1, str.length()));

        }
    }
}