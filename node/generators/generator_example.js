function* generator_basic() {
	yield 1;
	yield 2;
	yield 3;
}

const gen0 = generator_basic(); // "Generator { }"

console.log(gen0.next()); // 1
console.log(gen0.next()); // 2
console.log(gen0.next()); // 3
console.log(gen0.return());     // { value: undefined, done: true }
console.log(gen0.return(50));
console.log(gen0.next()); // undefined


console.log("====================================")



function* generator() {
	let y = 1;
  	while (true) {
        yield y++;
    }
}

const gen = generator(); // "Generator { }"

console.log(gen.next()); // 1
console.log(gen.next()); // 2
console.log(gen.next()); // 3
console.log(gen.return());     // { value: undefined, done: true }
console.log(gen.return(50));
console.log(gen.next()); // undefined


console.log("====================================")


function* Add(x) {
   yield x + 1;
   var y = yield(null);
   y = 6
   return x + y;
}

var gen2 = Add(5);

console.log(gen2.next()); // 6
console.log(gen2.next()); // null
console.log(gen2.next()); // 11
console.log(gen2.next()); // undefined