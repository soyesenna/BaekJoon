package p1149;

import java.io.*;
import java.util.*;
public class MainFail {

    //R G B
    public static List<List<Integer>> costs = new ArrayList<>();
    public static Map<String, Integer> dp = new HashMap<>();
    public static int N;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            List<Integer> tmp = new ArrayList<>();
            for (int j = 0; j < 3; j++) {
                tmp.add(Integer.parseInt(st.nextToken()));
            }
            costs.add(tmp);
        }
        dp.put("B", costs.get(0).get(2));
        dp.put("R", costs.get(0).get(0));
        dp.put("G", costs.get(0).get(1));

        dpFunc("R");
        dpFunc("G");
        dpFunc("B");

        System.out.println(dp.values().stream().min(Comparator.naturalOrder()));


    }

    public static int dpFunc(String s) {
        if (s.length() == N){
            return dp.get(s);
        }

        char last = s.charAt(s.length() - 1);
        int min = 0;
        String nowR;
        String nowG;
        String nowB;
        int resR;
        int resB;
        int resG;
        int dpNowR, dpNowG, dpNowB;
        switch (last) {
            case 'R':
                 nowG = s + "G";
                 resG = dp.get(s) + costs.get(s.length() - 1).get(1);
                dp.put(nowG, Math.min(resG, dp.getOrDefault(nowG, Integer.MAX_VALUE)));

                 nowB = s + "B";
                 resB = dp.get(s) + costs.get(s.length() - 1).get(2);
                dp.put(nowB, Math.min(resB, dp.getOrDefault(nowB, Integer.MAX_VALUE)));
                dpNowG = dpFunc(nowG);
                dpNowB = dpFunc(nowB);
                min = Math.min(dpFunc(nowG), dpFunc(nowB));

            case 'G':
                 nowR = s + "R";
                 resR = dp.get(s) + costs.get(s.length() - 1).get(0);
                dp.put(nowR, Math.min(resR, dp.getOrDefault(nowR, Integer.MAX_VALUE)));

                 nowB = s + "B";
                 resB = dp.get(s) + costs.get(s.length() - 1).get(2);
                dp.put(nowB, Math.min(resB, dp.getOrDefault(nowB, Integer.MAX_VALUE)));
                min = Math.min(dpFunc(nowR), dpFunc(nowB));

            case 'B':
                 nowG = s + "G";
                 resG = dp.get(s) + costs.get(s.length() - 1).get(1);
                dp.put(nowG, Math.min(resG, dp.getOrDefault(nowG, Integer.MAX_VALUE)));

                 nowR = s + "R";
                 resR = dp.get(s) + costs.get(s.length() - 1).get(0);
                dp.put(nowR, Math.min(resR, dp.getOrDefault(nowR, Integer.MAX_VALUE)));


                min = Math.min(dpFunc(nowG), dpFunc(nowR));

        }

        return min;
    }

}
