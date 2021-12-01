import java.net.Inet6Address;
import java.net.InetAddress;
import java.util.*;

public class Baekjoon_3107{
     public static void main(String []args){
         Scanner sc=new Scanner(System.in);
         String ipv6addr = sc.next();
         try {
             InetAddress ip1 = Inet6Address.getByName(ipv6addr);
             byte[] addr = ip1.getAddress();
             System.out.printf("%02x%02x", addr[0], addr[1]);
             for (int i = 2; i < addr.length; i += 2 ) {
                 System.out.printf(":%02x%02x", addr[i], addr[i+1]);
             }
         }
         catch (Exception e) {
            
         }
     }
}
