/**
 * @param {string[]} words
 * @return {string}
 */

 function isPalindrome(str){
    if(str.length === 0 || str.length === 1) return true;
    return str[0]===str[str.length-1] && isPalindrome(str.slice(1,str.length-1))
 }
var firstPalindrome = function(words) {
    
    for(i=0;i<words.length;i++){
        
        if(isPalindrome(words[i])) return words[i]
    }
    return ""
};