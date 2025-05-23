import java.security.*;
import javax.crypto.Cipher;
import java.util.Base64;

public class RSADemo {

    // Method untuk menghasilkan pasangan kunci RSA
    public static KeyPair generateKeyPair() throws Exception {
        KeyPairGenerator generator = KeyPairGenerator.getInstance("RSA");
        generator.initialize(2048); // Kunci 2048-bit
        return generator.generateKeyPair();
    }

    // Method untuk mengenkripsi pesan
    public static String encrypt(String plainText, PublicKey publicKey) throws Exception {
        Cipher encryptCipher = Cipher.getInstance("RSA");
        encryptCipher.init(Cipher.ENCRYPT_MODE, publicKey);

        byte[] encryptedBytes = encryptCipher.doFinal(plainText.getBytes("UTF-8"));
        return Base64.getEncoder().encodeToString(encryptedBytes);
    }

    // Method untuk mendekripsi pesan
    public static String decrypt(String encryptedText, PrivateKey privateKey) throws Exception {
        byte[] bytes = Base64.getDecoder().decode(encryptedText);

        Cipher decryptCipher = Cipher.getInstance("RSA");
        decryptCipher.init(Cipher.DECRYPT_MODE, privateKey);

        byte[] decryptedBytes = decryptCipher.doFinal(bytes);
        return new String(decryptedBytes, "UTF-8");
    }

    public static void main(String[] args) {
        try {
            // Generate kunci
            KeyPair keyPair = generateKeyPair();

            // Teks asli
            String message = "Ini pesan rahasia dari Christhio!";
            System.out.println("Pesan Asli: " + message);

            // Enkripsi
            String encrypted = encrypt(message, keyPair.getPublic());
            System.out.println("Pesan Terenkripsi: " + encrypted);

            // Dekripsi
            String decrypted = decrypt(encrypted, keyPair.getPrivate());
            System.out.println("Pesan Terdekripsi: " + decrypted);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
