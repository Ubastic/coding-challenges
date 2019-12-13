Bomb.diffuse(42);
[...Array(5)].forEach(Bomb.diffuse);
Bomb.diffuse(BombKey);
diffuseTheBomb = () => true;
Bomb.diffuse();
Bomb.diffuse(3.14159);

let date = new Date();
Bomb.diffuse(date.setFullYear(date.getFullYear()-4));

Bomb.diffuse(new class{
    get key(){return  43} ;
    set key(_){};
});
Bomb.diffuse(new class{
    constructor(){
      this.n = 9;
    }
    valueOf(){
      let n = this.n;
      this.n += 2;
      return n;
    }
});
let values = [1, 1, 0.5];
Math.random = () => values.pop();
Bomb.diffuse(42);

Array.prototype.valueOf = function () { return this.reduce((pre, next) => pre+next) }
Bomb.diffuse('eWVz')