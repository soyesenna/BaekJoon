package p1003;

import java.io.*;
import java.util.*;
public class Main {

    public static int T;
    public static List<List<Integer>> table = new ArrayList<>();

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        List<String> result = new ArrayList<>();

        while (T > 0) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0){
                result.add("1 0");
                T--;
                continue;
            }else if(n == 1){
                result.add("0 1");
                T--;
                continue;
            }

            table = new ArrayList<>();

            table.add(new ArrayList<>(List.of(1, 0)));
            table.add(new ArrayList<>(List.of(0, 1)));

            for (int i = 2; i < n + 1; i++) {
                table.add(new ArrayList<>(List.of(-1, -1)));
            }

            List<Integer> now = fibonacci(n);
            result.add(now.get(0) + " " + now.get(1));
            T--;
        }
        for (String s : result) {
            System.out.println(s);
        }
    }

    public static List<Integer> fibonacci(int n) {

        List<Integer> n1 = table.get(n - 1);
        if (n1.get(0) == -1) n1 = fibonacci(n - 1);

        List<Integer> n2 = table.get(n - 2);
        if (n2.get(0) == -1) n2 = fibonacci(n - 2);

        table.get(n).set(0, n1.get(0) + n2.get(0));
        table.get(n).set(1, n1.get(1) + n2.get(1));

        return table.get(n);
    }
}
