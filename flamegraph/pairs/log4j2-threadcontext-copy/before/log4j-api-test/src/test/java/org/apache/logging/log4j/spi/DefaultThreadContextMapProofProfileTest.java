package org.apache.logging.log4j.spi;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Map;

import org.junit.jupiter.api.Test;

class DefaultThreadContextMapProofProfileTest {
    @Test
    void profileGetCopyPath() {
        DefaultThreadContextMap map = new DefaultThreadContextMap();
        for (int i = 0; i < 24; i++) {
            map.put("key" + i, "value" + i);
        }
        long total = 0L;
        for (int i = 0; i < 30000; i++) {
            Map<String, String> copy = map.getCopy();
            total += copy.size();
        }
        assertEquals(24L * 30000L, total);
    }
}
