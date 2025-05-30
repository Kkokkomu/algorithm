import java.util.*;
import java.io.*;

public class Main{
    public static boolean check(String str){
        int len = str.length();
        int prev = 0;
        boolean[] apb = new boolean[26];

        for(int i = 0; i < len; i++){
            int now = str.charAt(i);

            if(prev != now){
                if(apb[now - 'a'] == false) {
                    apb[now - 'a'] = true;
                    prev = now;
                } else {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int res = 0;

        for(int i = 0; i<N;i ++){
            if (check(br.readLine())) res++;
        }

        System.out.println(res);
    }
}