let parseQuery = queryString => queryString.split('&')
    .map(s => s.split('='))
    .reduce((root, [key, value]) => {
        root[decodeURIComponent(key)] = decodeURIComponent(value);
        return root;
    }, {});

class UriBuilder {
    constructor(url) {
        if (url.includes('?')) {
            let [u, query] = url.split('?');
            this.url = u;
            this.params = parseQuery(query);
        } else {
            this.url = url;
            this.params = {};
        }
    }

    build() {
        return this.url + (Object.keys(this.params).length === 0 ? '' : '?' +
                Object.entries(this.params).map(([k, v]) => encodeURI(k) + '=' + encodeURI(v)).join('&')
        );
    }
}