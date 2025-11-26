import java.util.HashMap;
import java.util.Scanner;

public class Homework8 {
    public static void main(String[] args) {
        HashMap<String, String> idPw = new HashMap<>();

        idPw.put("myId", "myPass");
        idPw.put("myId2", "myPass2");
        idPw.put("myId3", "myPass3");

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("id와 password를 입력해주세요.");

            System.out.print("id : ");
            String id = sc.nextLine().trim();

            if (!idPw.containsKey(id)) {//pw가 없을때
                System.out.println("입력하신 id는 존재하지 않습니다. 다시 입력해주세요.\n");
                continue;
            }

            System.out.print("password : ");
            String pw = sc.nextLine().trim();

            if (idPw.get(id).equals(pw)) { //key를 입력하면 연결된 value가 나옴
                System.out.println("id와 비밀번호가 일치합니다.");
                break;
            } else {
                System.out.println("비밀번호가 일치하지 않습니다. 다시 입력해주세요.\n");
            }
        }

    }
}
