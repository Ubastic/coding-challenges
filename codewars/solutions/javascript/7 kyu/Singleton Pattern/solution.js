let instance = null;

let Singleton = function(){
  instance = instance || this;
  return instance;
};
