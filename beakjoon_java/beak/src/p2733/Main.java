package p2733;

import java.io.*;
import java.text.StringCharacterIterator;
import java.util.*;

public class Main {

    public static int T;

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        int nowProgram = 1;
        while (T > 1) {
            System.out.println("PROGRAM #" + nowProgram + ":");
            nowProgram++;
            String s = br.readLine();
            List<Character> order = new ArrayList<>();
            List<Integer> byteArray = new ArrayList<>();
            for (int i = 0; i < 32768; i++) byteArray.add(0);

            int nowPointer = 0;
            // [ 가 없으면 false, 있으면 true
            boolean correctFlag = false;
            boolean good = true;
            while (!s.contentEquals("end") && good) {
                for (int i = 0; i < s.length(); i++) {
                    char c = s.charAt(i);
                    if (correctChar(c)) {
                        if (c == '['){
                            if (correctFlag) {
                                good = false;
                                break;
                            }else correctFlag = true;
                        }else if (c == ']'){
                            if (!correctFlag) {
                                good = false;
                                break;
                            }else correctFlag = false;
                        }
                        order.add(c);
                    }
                    else if (c == '%') break;
                }
                s = br.readLine();
            }
            if (!good) {
                System.out.println("COMPILE ERROR");
                continue;
            }
            //System.out.println(order);
            int idx = 0;
            while (idx < order.size()){
                char o = order.get(idx);
                switch (o){
                    case '>':
                        nowPointer++;
                        if (nowPointer == 32768) nowPointer = 0;
                        break;
                    case '<':
                        nowPointer--;
                        if (nowPointer == -1) nowPointer = 32767;
                        break;
                    case '+':
                        if (byteArray.get(nowPointer) == 255) byteArray.set(nowPointer, 0);
                        else byteArray.set(nowPointer, byteArray.get(nowPointer) + 1);
                        break;
                    case '-':
                        if (byteArray.get(nowPointer) == 0) byteArray.set(nowPointer, 255);
                        else byteArray.set(nowPointer, byteArray.get(nowPointer) - 1);
                        break;
                    case '.':
                        System.out.print((char)byteArray.get(nowPointer).intValue());
                        break;
                    case '[':
                        if (byteArray.get(nowPointer) == 0) {
                            while (order.get(++idx) != ']');
                        }
                        break;
                    case ']':
                        if (byteArray.get(nowPointer) != 0){
                            while (order.get(--idx) != '[');
                        }
                        break;
                }
                idx++;
            }
            System.out.println();
            T--;
        }

    }


    public static boolean correctChar(char c) {
        char[] correct = "<>+-.[]".toCharArray();
        for (char co : correct) {
            if (co == c) return true;
        }
        return false;
    }
}
