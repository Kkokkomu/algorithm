import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        int len = 'z' - 'a' + 1;
        for (int i = 0; i < len; i++) {
            System.out.print(str.indexOf((char)(i+'a'))+" ");
        }
    }
}