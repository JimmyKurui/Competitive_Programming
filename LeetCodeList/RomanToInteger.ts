/* 13. Roman to Integer

Runtime 147 ms Beats 83.59%
Memory 51 MB Beats 11.96% */

function romanToInt(s: string): number {
    let numerals = {'I':1, 'V':5, 'X':10, 'L':50,  'C':100, 'D':500, 'M':1000};
    let sum = 0;

    for(let count = 0; count< s.length; count++)
    {
        if( numerals[s[count+1]]- numerals[s[count]]  == 4 ||
            numerals[s[count+1]]- numerals[s[count]]  == 9 ||
            numerals[s[count+1]]- numerals[s[count]]  == 40 ||
            numerals[s[count+1]]- numerals[s[count]]  == 90 ||
            numerals[s[count+1]]- numerals[s[count]]  == 400 ||
            numerals[s[count+1]]- numerals[s[count]]  == 900 
        ) {
            sum += (numerals[s[count+1]]- numerals[s[count]]);
            count++;
            continue;
        }
        sum += numerals[ s[count] ];  
    }

    return sum;
};

