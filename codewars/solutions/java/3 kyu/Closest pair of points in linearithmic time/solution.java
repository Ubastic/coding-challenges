import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Kata {

    private Point best1, best2;
    private double bestDistance = Double.POSITIVE_INFINITY;

    public static class Point2D extends Point implements Comparable<Point2D> {
        public Point2D(Point p) {
            this.x = p.x;
            this.y = p.y;
        }

        @Override
        public int compareTo(Kata.Point2D that) {
            if (this.y < that.y) return -1;
            if (this.y > that.y) return +1;
            if (this.x < that.x) return -1;
            if (this.x > that.x) return +1;
            return 0;
        }
    }

    public Kata(Point2D[] points) {
        init(points);
    }

    private void init(Point2D[] points) {
        int n = points.length;
        if (n <= 1) return;

        Point2D[] pointsByX = new Point2D[n];
        System.arraycopy(points, 0, pointsByX, 0, n);
        Arrays.sort(pointsByX, Comparator.comparingDouble(p -> p.x));

        for (int i = 0; i < n - 1; i++) {
            if (pointsByX[i].equals(pointsByX[i + 1])) {
                bestDistance = 0.0;
                best1 = pointsByX[i];
                best2 = pointsByX[i + 1];
                return;
            }
        }

        Point2D[] pointsByY = new Point2D[n];
        System.arraycopy(pointsByX, 0, pointsByY, 0, n);

        Point2D[] aux = new Point2D[n];
        closest(pointsByX, pointsByY, aux, 0, n - 1);
    }


    public static double distance(Point a, Point b) {
        return Math.sqrt(Math.pow(a.x - b.x, 2) + Math.pow(a.y - b.y, 2));
    }

    private static boolean less(Comparable v, Comparable w) {
        return v.compareTo(w) < 0;
    }

    private static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {
        if (hi + 1 - lo >= 0) {
            System.arraycopy(a, lo, aux, lo, hi + 1 - lo);
        }

        int i = lo, j = mid + 1;
        for (int k = lo; k <= hi; k++) {
            if (i > mid) a[k] = aux[j++];
            else if (j > hi) a[k] = aux[i++];
            else if (less(aux[j], aux[i])) a[k] = aux[j++];
            else a[k] = aux[i++];
        }
    }

    private double closest(Point2D[] pointsByX, Point2D[] pointsByY, Point2D[] aux, int lo, int hi) {
        if (hi <= lo) return Double.POSITIVE_INFINITY;

        int mid = lo + (hi - lo) / 2;
        Point2D median = pointsByX[mid];

        double delta1 = closest(pointsByX, pointsByY, aux, lo, mid);
        double delta2 = closest(pointsByX, pointsByY, aux, mid + 1, hi);
        double delta = Math.min(delta1, delta2);

        merge(pointsByY, aux, lo, mid, hi);

        int m = 0;
        for (int i = lo; i <= hi; i++) {
            if (Math.abs(pointsByY[i].x - median.x) < delta)
                aux[m++] = pointsByY[i];
        }

        for (int i = 0; i < m; i++) {
            for (int j = i + 1; (j < m) && (aux[j].y - aux[i].y < delta); j++) {
                double distance = distance(aux[i], aux[j]);

                if (distance < delta) {
                    delta = distance;
                    if (distance < bestDistance) {
                        bestDistance = delta;
                        best1 = aux[i];
                        best2 = aux[j];
                    }
                }
            }
        }
        return delta;
    }

    public static List<Point> closestPair(List<Point> points) {
        Kata kata = new Kata(points.stream().map(Point2D::new).toArray(Point2D[]::new));
        return Arrays.asList(kata.best1, kata.best2);
    }

}