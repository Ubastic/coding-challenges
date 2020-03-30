package kata;

public class NaturalNumber {

    public static final NaturalNumber ZERO = new NaturalNumber();
    private NaturalNumber parent = ZERO;

    public NaturalNumber() {}

    public NaturalNumber(NaturalNumber parent) {
        this.parent = parent;
    }

    public NaturalNumber succ() {
        return new NaturalNumber(this);
    }

    public NaturalNumber pred() {
        return parent;
    }

    public NaturalNumber add(NaturalNumber o) {
        return o == ZERO ? this : this.succ().add(o.pred());
    }

    public NaturalNumber subtract(NaturalNumber o) {
        return o == ZERO ? this : this.pred().subtract(o.pred());
    }

    public NaturalNumber multiply(NaturalNumber o) {
        return o == ZERO ? ZERO : this.add(this.multiply(o.pred()));
    }

    public NaturalNumber modulo(NaturalNumber o) {
        return this.resolve() < o.resolve() ? this : this.subtract(o).modulo(o);
    }

    public int resolve() {
        return this == ZERO ? 0 : 1 + this.pred().resolve();
    }

    public boolean equals(Object o) {
        return o instanceof NaturalNumber && this.resolve() == ((NaturalNumber) o).resolve();
    }
}