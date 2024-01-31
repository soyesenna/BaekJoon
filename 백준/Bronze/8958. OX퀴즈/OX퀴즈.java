import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int round = Integer.parseInt(br.readLine());

        for (int i = 0; i < round; i++) {
            String quiz = br.readLine();

            int Ocount = 1;
            int score = 0;

            for (char c : quiz.toCharArray()) {
                if (c == 'O') {
                    score += Ocount;
                    Ocount++;
                }else Ocount = 1;
            }

            System.out.println(score);
        }
    }
}
