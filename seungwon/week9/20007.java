import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tk = new StringTokenizer(br.readLine());
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((x, y) -> x[0] - y[0]);
        
        int N = Integer.parseInt(tk.nextToken());
        int M = Integer.parseInt(tk.nextToken());
        int X = Integer.parseInt(tk.nextToken());
        int Y = Integer.parseInt(tk.nextToken());

        List<Integer[]>[] adjLi = new ArrayList[N];
        int[] distance = new int[N];
        Integer[] index = new Integer[N];
        
        for (int i = 0; i < N; i++) distance[i] = Integer.MAX_VALUE;
        distance[Y] = 0;
        for (int i = 0; i < N; i++) adjLi[i] = new ArrayList<>();
        for (int i = 0; i < N; i++) index[i] = i;

        for (int i = 0; i < M; i++) {
            tk = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(tk.nextToken());
            int B = Integer.parseInt(tk.nextToken());
            int C = Integer.parseInt(tk.nextToken());

            adjLi[A].add(new Integer[] {C, B});
            adjLi[B].add(new Integer[] {C, A});
        }
        
        for (Integer[] e : adjLi[Y]) {
            pq.add(e);
        }

        while (!pq.isEmpty()) {
            Integer[] e = pq.remove();
            int d = e[0];
            int p = e[1];

            if (distance[p] <= d) continue;
            
            distance[p] = d;

            for (Integer[] a : adjLi[p]) {
                pq.add(new Integer[] {d + a[0], a[1]});
            }
        }

        Arrays.sort(index, (x, y) -> distance[x] - distance[y]);

        int sum = 0;
        int result = 0;
        for (int idx : index) {
            if (distance[idx] > X) {
                System.out.println(-1);
                return;
            }

            sum += distance[idx];

            if (sum * 2 > X) {
                result++;
                sum = distance[idx];
            }
        }
        result++;
        
        System.out.println(result);
    }
}