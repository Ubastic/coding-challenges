using namespace std;

enum Direction {
    DirectionUp,
    DirectionLeft,
    DirectionNone,
    DirectionDown,
    DirectionRight
};

pair<int, int> next(Direction d, int row, int column) {
    switch (d) {
        case DirectionUp:
            return {row - 1, column};
        case DirectionDown:
            return {row + 1, column};
        case DirectionLeft:
            return {row, column - 1};
        case DirectionRight:
            return {row, column + 1};
        default:
            return {-1, -1};
    }
}

pair<int, int> normalize(Direction d, int row, int column, int rows, int columns) {
    switch (d) {
        case DirectionUp:
            return {rows - 1, column};
        case DirectionDown:
            return {0, column};
        case DirectionLeft:
            return {row, columns - 1};
        case DirectionRight:
            return {row, 0};
        default:
            return {-1, -1};
    }
}


template<typename T>
class Table {
public:
    class iterator : public std::iterator<input_iterator_tag, T> {
    public:
        iterator(Table<T> &table, Direction d0 = DirectionNone, Direction d1 = DirectionNone, int r = 0, int c = 0)
                : table(table), d0(d0), d1(d1), row(r), column(c) {
            for (auto d : {d0, d1})
                tie(row, column) = normalize(d, row, column, rows(), columns());
        }

        void operator++() {
            auto[r, c] = next(d0, row, column);

            if (!is_valid(r, c)) {
                tie(r, c) = next(d1, row, column);
                tie(r, c) = normalize(d0, r, c, rows(), columns());

                if (!is_valid(r, c))
                    tie(r, c) = next(DirectionNone, row, column);
            }

            row = r;
            column = c;
        }

        T &operator*() {
            return table.mData[row][column];
        }

        bool operator!=(iterator other) {
            return !(row == other.row && column == other.column);
        }

        int rows() {
            return this->table.mData.size();
        }

        int columns() {
            return this->table.mData[0].size();
        }

        bool is_valid(int r, int c) {
            return 0 <= r && r < rows() && 0 <= c && c < columns();
        }

    private:
        Table<T> &table;
        Direction d0;
        Direction d1;
        int row;
        int column;
    };

    void push_back(const vector<T> &row) {
        mData.push_back(row);
    }

    iterator end() {
        return iterator(*this);
    }

    iterator begin(Direction d0, Direction d1) {
        return iterator(*this, d0, d1);
    }

private:
    vector<vector<T>> mData;
};
