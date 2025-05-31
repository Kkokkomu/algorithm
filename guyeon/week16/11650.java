import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            arr.add(new ArrayList<>(Arrays.asList(a,b)));
        }

        Collections.sort(arr, (e1, e2) -> {
            if (e1.get(0) == e2.get(0)){
                return e1.get(1) - e2.get(1);
            } else {
                return e1.get(0) - e2.get(0);
            }
        });

        for (int i = 0; i < N; i++) {
            sb.append(arr.get(i).get(0)).append(" ").append(arr.get(i).get(1)).append("\n");
        }
        System.out.println(sb);
    }
}