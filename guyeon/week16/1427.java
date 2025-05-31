import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] str = br.readLine().split("");
        ArrayList<Integer> arr = new ArrayList<>();

        for(int i=0; i<str.length ; i++){
            arr.add(Integer.parseInt(str[i]));
        }

        Collections.sort(arr, Collections.reverseOrder());

        for(int i=0; i<str.length ; i++){
            sb.append(arr.get(i));
        }

        System.out.println(sb);
    }
}