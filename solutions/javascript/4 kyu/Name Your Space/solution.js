    function namespace(root, path, value) {
        let paths = path.split('.');
        let holder = root;

        if (value === undefined) {
            for (let attr of paths) {
                if (!(attr in holder)) {
                    return undefined;
                }
                holder = holder[attr];
            }
            return holder;
        } else {
            for (let attr of paths.slice(0, paths.length - 1)) {
                if (!(attr in holder)) {
                    let obj = {};
                    holder[attr] = obj;
                    holder = obj;
                } else {
                    holder = holder[attr];
                }
            }

            holder[paths[paths.length - 1]] = value;
        }
    }