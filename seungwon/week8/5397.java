import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            List<Character> li = new LinkedList<>();
            ListIterator iter = li.listIterator();
            for (char c : br.readLine().toCharArray()) {
                if (c == '<') {
                    if (iter.hasPrevious()) iter.previous();
                } else if (c == '>') {
                    if (iter.hasNext()) iter.next();
                } else if (c == '-') {
                    if (iter.hasPrevious()) {
                        iter.previous();
                        iter.remove();
                    }
                } else {
                    iter.add(c);
                }
            }

            for (char c : li) bw.write(c);
            bw.newLine();
            bw.flush();
        }

        br.close();
        bw.close();
    }
}
