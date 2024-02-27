function mergeAlternately(word1, word2) {
    let resutl = "";
    const regex = /./;

    if (word1.length > word2.length) {
        word2 = word2.padEnd(word1.length, " ");
    }
    else if (word2.length > word1.length) {
        word1 = word1.padEnd(word2.length, " ");
    }

    for (let i = 0; i < word1.length; i++) {
        resutl += word1[i];
        resutl += word2[i];
    }

    return resutl.replace(/\s/g, "");
};


function test(word1, word2, test) {
    if (mergeAlternately(word1, word2) !== test) {
        throw console.error("");
    }
}

const word1 = "abcd";
const word2 = "pq";
const wordTest = "apbqcd";

console.log(mergeAlternately(word1, word2));
test(word1, word2, wordTest);
