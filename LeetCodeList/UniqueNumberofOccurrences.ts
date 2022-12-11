/* 1207. Unique Number of Occurrences

Runtime 126 ms Beats 10.62%
Memory 49.5 MB Beats 5.42% */

function uniqueOccurrences(arr: number[]): boolean {
    let counter: object = {};
    
    for(let i=0; i<arr.length; i++) {
        if( (<any>Object).keys(counter).includes(String(arr[i])) ) {
            continue;
        }
        let count: number = 0;

        for(let j = 0; j < arr.length; j++) {
            if (arr[j] == arr[i]) {
                 count++;
            }
        }
        if( (<any>Object).values(counter).includes(count) ) {
            return false;
        }
        else {
            counter[arr[i]] = count;
        }
    } 
    return true;
}