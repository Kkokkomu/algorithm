import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int D = sc.nextInt();
        int P = sc.nextInt();
        int[][] arr = new int[P][2];
        int[] dp = new int[D + 1];
        dp[0] = Integer.MAX_VALUE;
        for (int i = 1; i < D + 1; i++) dp[i] = -1;

        for (int i = 0; i < P; i++) {
            int L = sc.nextInt();
            int C = sc.nextInt();
            arr[i] = new int[]{L, C};
        }

        Arrays.sort(arr, (x, y) -> x[0] - y[0]);

        for (int[] pipe : arr) {
            int l = pipe[0];
            int c = pipe[1];
            boolean[] isReplaced = new boolean[D + 1];
            int[] originalDP = new int[D + 1];

            int i = 0;
            while (i + l < D + 1) {
                if (dp[i] == -1) {
                    i++;
                    continue;
                } else if (isReplaced[i]) {
                    originalDP[i + l] = dp[i + l];
                    dp[i + l] = Math.max(dp[i + l], Math.min(originalDP[i], c));
                    isReplaced[i + l] = true;
                    i++;
                    continue;
                }

                originalDP[i + l] = dp[i + l];
                dp[i + l] = Math.max(dp[i + l], Math.min(dp[i], c));
                isReplaced[i + l] = true;
                i++;
            }
        }

        System.out.println(dp[D]);
    }
}