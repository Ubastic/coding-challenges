function nouveau (f, ...args) {
  let proto = Object(f.prototype) === f.prototype ? f.prototype : Object.prototype;
  let obj = Object.create(proto);
  let ret = f.apply(obj, args);
  return Object(ret) === ret ? ret : obj;  
}