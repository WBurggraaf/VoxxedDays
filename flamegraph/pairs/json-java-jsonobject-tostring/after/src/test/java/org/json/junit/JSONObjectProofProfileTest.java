package org.json.junit;

import static org.junit.Assert.assertTrue;

import org.json.JSONArray;
import org.json.JSONObject;
import org.junit.Test;

public class JSONObjectProofProfileTest {
    @Test
    public void profileToStringPath() {
        JSONObject template = new JSONObject();
        for (int i = 0; i < 48; i++) {
            JSONArray nested = new JSONArray();
            for (int j = 0; j < 12; j++) {
                nested.put("value-" + i + '-' + j);
            }
            template.put("key" + i, nested);
        }
        long total = 0L;
        for (int round = 0; round < 4000; round++) {
            String json = template.toString(2);
            total += json.length();
        }
        assertTrue(total > 0L);
    }
}
