import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] blocks = new int[W];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            blocks[i] = Integer.parseInt(st.nextToken());
        }

        // 각 위치에서 왼쪽의 최대 높이를 계산
        int[] leftMaxes = new int[W];
        int leftMax = 0;
        for (int i = 0; i < W; i++) {
            leftMax = Math.max(leftMax, blocks[i]);
            leftMaxes[i] = leftMax;
        }

        // 각 위치에서 오른쪽의 최대 높이를 계산
        int[] rightMaxes = new int[W];
        int rightMax = 0;
        for (int i = W - 1; i >= 0; i--) {
            rightMax = Math.max(rightMax, blocks[i]);
            rightMaxes[i] = rightMax;
        }

        // 각 위치에서 고일 수 있는 빗물의 양을 계산
        int water = 0;
        for (int i = 0; i < W; i++) {
            water += Math.min(leftMaxes[i], rightMaxes[i]) - blocks[i];
        }

        System.out.println(water);
    }
}
