import java.io.*;
import java.util.*;
public class Main {

    private static List<Integer> ascending = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8));
    private static List<Integer> descending = new ArrayList<>(List.of(8, 7, 6, 5, 4, 3, 2, 1));


    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Integer> input = new ArrayList<>();

        while (st.hasMoreTokens()) {
            input.add(Integer.parseInt(st.nextToken()));
        }



        if (check(input, ascending)) {
            System.out.println("ascending");
        } else if (check(input, descending)) {
            System.out.println("descending");
        }else System.out.println("mixed");

    }

    private static boolean check(List<Integer> input, List<Integer> co) {
        boolean result = true;
        for (int i = 0; i < input.size(); i++) {
            if (!input.get(i).equals(co.get(i))) {
                result = false;
                break;
            }
        }

        return result;
    }
}
