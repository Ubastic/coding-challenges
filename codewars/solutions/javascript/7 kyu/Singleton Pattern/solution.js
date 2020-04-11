let instance = null;

let Singleton = function(){
  if (!instance)
     instance = this;
  return instance;
};
