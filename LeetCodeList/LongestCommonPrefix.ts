/* 14. Longest Common Prefix - JimmyKurui

Runtime 72 ms Beats 93.53%
Memory 45.1 MB Beats 22.81% */

function longestCommonPrefix(strs: string[]): string {
    let substring: string = "";
    let sample: string = strs.sort( (a,b) => a.length - b.length)[0];

    if(strs.length==1) return strs[0];
    for(let i:number=0; i<sample.length; i++)
    {
        substring += sample[i]; 
        let re = new RegExp('^'+substring);
        let matchString: string[] = strs.map( (a) => String(re.test(a)));
        if(matchString.indexOf('false') != -1) {
            return substring.slice(0,substring.length-1);
        }
    }
    return substring;

};