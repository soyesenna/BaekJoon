
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(arr);

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++){
            sb = new StringBuilder();
            sb.append(arr.get(i));
            sb.append("\n");
            bw.write(sb.toString());
            //bw.flush();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
