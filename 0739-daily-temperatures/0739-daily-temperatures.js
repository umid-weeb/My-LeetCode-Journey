/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {
    let res = new Array(temperatures.length).fill(0);
    stack=[]
    for( let i=0; i<=temperatures.length; i++){
        while( stack.length >0 && temperatures[i]> temperatures[stack.at(-1)]){
            let index = stack.pop()
            res[index] = i- index
        }
        stack.push(i)
    }
    return res
};