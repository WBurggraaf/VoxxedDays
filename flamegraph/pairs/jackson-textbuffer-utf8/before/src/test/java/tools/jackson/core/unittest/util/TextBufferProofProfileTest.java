package tools.jackson.core.unittest.util;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.nio.charset.StandardCharsets;

import org.junit.jupiter.api.Test;

import tools.jackson.core.util.TextBuffer;

class TextBufferProofProfileTest {
    @Test
    void profileResetWithUtf8() throws Exception {
        byte[] bytes = makePayload().getBytes(StandardCharsets.UTF_8);
        TextBuffer buffer = new TextBuffer(null);
        long total = 0L;
        for (int i = 0; i < 20000; i++) {
            buffer.resetWithUTF8(bytes, 0, bytes.length);
            total += buffer.contentsAsString().length();
        }
        assertTrue(total > 0L);
    }

    private static String makePayload() {
        StringBuilder sb = new StringBuilder(128);
        for (int i = 0; i < 48; i++) {
            sb.append((char) ('a' + (i % 26)));
        }
        return sb.toString();
    }
}
