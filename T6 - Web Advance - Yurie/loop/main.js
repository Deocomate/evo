// Ctrl + ?
// console.log("Hello, Lesson 2 about javaScript loops!");
// for loop: 1 -> 2 -> 3 -> 4 -> 5 -> 6
// for (let i = 2; i < 10; i++) {
//     console.log("For Loop iteration number: " + i);
// }
// 2 -> 4 -> 6 -> 8 -> 10

// Write a for loop that prints even numbers from 2 to 10
// 2, 4, 6, 8, 10

// for (let i = 2; i <= 10; i++) {
//     if (i % 2 == 0) {
//         console.log(i);
//     }
// }
// let sum = "Hi";
// sum += " there"; 
// console.log(sum); 

//

// console.log(document);

// let ulElement = document.getElementById("list-of-number")

// let html = ""

// for (let i = 1; i <= 10; i++) {
//     html += `<li>I love you ${i}</li>`;
// }

// console.log(html);

// ulElement.innerHTML = html;

// let allH1Elements = document.getElementsByTagName("h1");

// console.log(allH1Elements);

let inputNumberElement = document.getElementById("input-number");
let buttonElement = document.getElementById("button");
let ulElement = document.getElementById("list-of-number");

buttonElement.onclick = function() {
    let value = Number(inputNumberElement.value)

    let html = ""

    for (let i = 1; i <= value; i++) {
        html += `<li>I love you ${i}</li>`;
    }

    ulElement.innerHTML = html;
    
}

// I want you 





