import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<String>> arr = new ArrayList<>();
        StringTokenizer st;
        for (int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine(), " ");
            String age = st.nextToken();
            String name = st.nextToken();

            arr.add(new ArrayList<>(Arrays.asList(age, name)));
        }

        arr.sort((a1,a2) -> 
            Integer.compare(Integer.parseInt(a1.get(0)),Integer.parseInt(a2.get(0)))
        );

        StringBuilder sb = new StringBuilder();
        for (int i=0; i<N; i++){
            sb.append(arr.get(i).get(0) + " " + arr.get(i).get(1) + "\n");
        }

        System.out.println(sb);
    }
}