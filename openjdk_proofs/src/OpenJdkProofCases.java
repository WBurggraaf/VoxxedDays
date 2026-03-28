import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.atomic.AtomicLong;

public final class OpenJdkProofCases {
    private OpenJdkProofCases() {
    }

    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.err.println("Usage: OpenJdkProofCases <case> <iterations> [threads]");
            System.exit(2);
        }

        String caseName = args[0];
        int iterations = Integer.parseInt(args[1]);
        int threads = args.length >= 3 ? Integer.parseInt(args[2]) : 16;

        switch (caseName) {
            case "threadmxbean-current-user-time" -> runThreadMxBean(iterations, threads);
            case "formatter-simple-fastpath" -> runFormatterSimple(iterations);
            case "formatter-localized-numbers" -> runFormatterLocalized(iterations);
            case "collections-bulk-copy" -> runCollectionsBulk(iterations);
            default -> {
                System.err.println("Unknown case: " + caseName);
                System.exit(3);
            }
        }
    }

    private static void runThreadMxBean(int iterations, int threads) throws Exception {
        ThreadMXBean bean = ManagementFactory.getThreadMXBean();
        warmupThreadMxBean(bean, iterations / 10, threads);

        AtomicLong sink = new AtomicLong();
        CountDownLatch ready = new CountDownLatch(threads);
        CountDownLatch start = new CountDownLatch(1);
        CountDownLatch done = new CountDownLatch(threads);

        long begin = System.nanoTime();
        for (int i = 0; i < threads; i++) {
            Thread t = new Thread(() -> {
                ready.countDown();
                try {
                    start.await();
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                long local = 0L;
                for (int j = 0; j < iterations; j++) {
                    local ^= bean.getCurrentThreadUserTime();
                }
                sink.addAndGet(local);
                done.countDown();
            }, "proof-thread-" + i);
            t.start();
        }

        ready.await();
        begin = System.nanoTime();
        start.countDown();
        done.await();
        long elapsed = System.nanoTime() - begin;
        long ops = (long) iterations * threads;
        printResult("threadmxbean-current-user-time", elapsed, ops, sink.get(), threads);
    }

    private static void warmupThreadMxBean(ThreadMXBean bean, int iterations, int threads) throws Exception {
        int warmupIterations = Math.max(50_000, iterations);
        CountDownLatch done = new CountDownLatch(threads);
        for (int i = 0; i < threads; i++) {
            Thread t = new Thread(() -> {
                long local = 0L;
                for (int j = 0; j < warmupIterations; j++) {
                    local ^= bean.getCurrentThreadUserTime();
                }
                if (local == Long.MIN_VALUE) {
                    System.out.println("impossible");
                }
                done.countDown();
            });
            t.start();
        }
        done.await();
    }

    private static void runFormatterSimple(int iterations) {
        int warmup = Math.max(50_000, iterations / 10);
        long sink = 0L;
        for (int i = 0; i < warmup; i++) {
            sink += simpleFormatBody(i);
        }

        long begin = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            sink += simpleFormatBody(i);
        }
        long elapsed = System.nanoTime() - begin;
        long ops = (long) iterations * 3;
        printResult("formatter-simple-fastpath", elapsed, ops, sink, 1);
    }

    private static int simpleFormatBody(int i) {
        String a = String.format("A:%s", "value-" + (i & 31));
        String b = String.format("B:%08d", i);
        String c = String.format("C:%12s-%04d", "text", i & 1023);
        return a.length() + b.length() + c.length();
    }

    private static void runFormatterLocalized(int iterations) {
        NumberFormat warmupFmt = NumberFormat.getInstance(Locale.GERMANY);
        warmupFmt.setGroupingUsed(true);
        warmupFmt.setMaximumFractionDigits(2);
        warmupFmt.setMinimumFractionDigits(2);

        int warmup = Math.max(20_000, iterations / 10);
        long sink = 0L;
        for (int i = 0; i < warmup; i++) {
            sink += localizedFormatBody(i);
            sink += warmupFmt.format(i * 1.03125d).length();
        }

        long begin = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            sink += localizedFormatBody(i);
        }
        long elapsed = System.nanoTime() - begin;
        long ops = (long) iterations * 3;
        printResult("formatter-localized-numbers", elapsed, ops, sink, 1);
    }

    private static int localizedFormatBody(int i) {
        String a = String.format(Locale.GERMANY, "%,.2f", i * 1.03125d);
        String b = String.format(Locale.GERMANY, "%,.2f", (i + 7) * 11.25d);
        String c = String.format(Locale.GERMANY, "%,.2f", (i + 13) * 0.125d);
        return a.length() + b.length() + c.length();
    }

    private static void runCollectionsBulk(int iterations) {
        List<String> source = new ArrayList<>();
        for (int i = 0; i < 75; i++) {
            source.add("key-" + i);
        }
        List<String> singleton = Collections.singletonList("only");

        int warmup = Math.max(50_000, iterations / 10);
        long sink = 0L;
        for (int i = 0; i < warmup; i++) {
            sink += collectionsBody(source, singleton);
        }

        long begin = System.nanoTime();
        for (int i = 0; i < iterations; i++) {
            sink += collectionsBody(source, singleton);
        }
        long elapsed = System.nanoTime() - begin;
        long ops = (long) iterations * 2;
        printResult("collections-bulk-copy", elapsed, ops, sink, 1);
    }

    private static int collectionsBody(List<String> source, List<String> singleton) {
        ArrayList<String> dst = new ArrayList<>(source.size() + 1);
        dst.addAll(source);
        ArrayList<String> dst2 = new ArrayList<>(1);
        dst2.addAll(singleton);
        return dst.size() + dst2.size();
    }

    private static void printResult(String caseName, long elapsedNs, long ops, long sink, int threads) {
        double nsPerOp = ops == 0 ? 0.0d : (double) elapsedNs / (double) ops;
        System.out.println("CASE=" + caseName);
        System.out.println("ELAPSED_NS=" + elapsedNs);
        System.out.println("OPS=" + ops);
        System.out.println("NS_PER_OP=" + String.format(Locale.ROOT, "%.3f", nsPerOp));
        System.out.println("THREADS=" + threads);
        System.out.println("SINK=" + sink);
    }
}
