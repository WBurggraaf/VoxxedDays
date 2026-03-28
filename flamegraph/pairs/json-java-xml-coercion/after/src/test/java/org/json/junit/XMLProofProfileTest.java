package org.json.junit;

import static org.junit.Assert.assertTrue;

import org.json.JSONObject;
import org.json.XML;
import org.junit.Test;

public class XMLProofProfileTest {
    @Test
    public void profileStringToValuePath() {
        String xml = "<root>"
                + "<item enabled='true' count='42' ratio='12.50'>12345</item>"
                + "<item enabled='false' count='7' ratio='2.75'>67890</item>"
                + "<item enabled='true' count='19' ratio='4.25'>24680</item>"
                + "</root>";
        long total = 0L;
        for (int i = 0; i < 5000; i++) {
            JSONObject object = XML.toJSONObject(xml);
            total += object.toString().length();
        }
        assertTrue(total > 0L);
    }
}
