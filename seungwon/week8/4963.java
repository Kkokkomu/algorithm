import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

class Main {
    static boolean[][] isVisited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] di = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dj = {-1, 0, 1, -1, 1, -1, 0, 1};

        while (true) {
            int w, h;
            w = sc.nextInt();
            h = sc.nextInt();
            if (w == 0 && h == 0) break;

            int[][] map = new int[h + 2][w + 2];
            isVisited = new boolean[h + 2][w + 2];

            for (int i = 1; i < h + 1; i++) {
                for (int j = 1; j < w + 1; j++) {
                    map[i][j] = sc.nextInt();
                }
            }

            int answer = 0;
            for (int i = 1; i < h + 1; i++) {
                for (int j = 1; j < w + 1; j++) {
                    if (isVisited[i][j] || map[i][j] == 0) continue;

                    answer++;
                    Deque<Integer[]> deque = new ArrayDeque<>();
                    deque.add(new Integer[]{i, j});

                    while (!deque.isEmpty()) {
                        Integer[] coordinate = deque.remove();
                        int curI = coordinate[0];
                        int curJ = coordinate[1];

                        if (isVisited[curI][curJ]) continue;

                        isVisited[curI][curJ] = true;

                        for (int k = 0; k < 8; k++) {
                            int nextI = curI + di[k];
                            int nextJ = curJ + dj[k];

                            if (map[nextI][nextJ] == 1 && !isVisited[nextI][nextJ]) {
                                deque.add(new Integer[]{nextI, nextJ});
                            }
                        }
                    }
                }
            }

            System.out.println(answer);
        }
    }
}