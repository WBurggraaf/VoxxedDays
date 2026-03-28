package tools.jackson.core.unittest.read;

import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.StringWriter;
import java.io.Writer;

import org.junit.jupiter.api.Test;

import tools.jackson.core.JsonParser;
import tools.jackson.core.JsonToken;
import tools.jackson.core.json.JsonFactory;

class ReadStringProofProfileTest {
    private static final JsonFactory JSON_FACTORY = new JsonFactory();

    @Test
    void profileReadStringPath() throws Exception {
        String payload = makePayload();
        long total = 0L;
        for (int i = 0; i < 1200; i++) {
            try (JsonParser parser = JSON_FACTORY.createParser(payload)) {
                parser.nextToken();
                parser.nextToken();
                Writer writer = new StringWriter();
                total += parser.readString(writer);
                if (parser.currentToken() == JsonToken.VALUE_STRING) {
                    parser.finishToken();
                }
            }
        }
        assertTrue(total > 0L);
    }

    private static String makePayload() {
        StringBuilder sb = new StringBuilder(14000);
        sb.append('[').append('"');
        for (int i = 0; i < 6000; i++) {
            sb.append((char) ('a' + (i % 26)));
        }
        sb.append('"').append(']');
        return sb.toString();
    }
}
