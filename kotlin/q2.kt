/*
    ANSWER

    class Solution {
    public:
    vector<int> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        for(int i=0;i*4<=tomatoSlices;i++){
        int j=(tomatoSlices-i*4)/2;
        if(i*4+j*2==tomatoSlices&&i+j==cheeseSlices)
            return vector<int>({i,j});
        }
        return {};
    }
    };
    */

fun numOfBurgers(tomatoSlices: Int, cheeseSlices: Int): List<Int> {
    var jum = 0
    var sml = 0

    var tom = tomatoSlices
    var chs = cheeseSlices

    while(tom >= 2 && chs >= 1) {
        sml++

        tom -= 2
        chs -= 1
    }

    var tmp = tom / 2
    jum += tmp
    sml -= tmp
    tom -= tmp * 4
    /* while((tom != 0 || chs != 0) && sml >= 1) {
        println(sml)
        println(jum)
        println(tom)
        println(chs)
        println() 
        sml--
        tom += 2
        chs += 1

        if(tom >= 4) {
            jum++
            tom -= 4
            chs -= 1
        }
    }*/

    if(tom == 0 && chs == 0) {
        return listOf(jum, sml)
    }
    else {
        return listOf()
    }
}

fun main() {
    var ans = numOfBurgers(193862, 69739)

    for(an in ans) {
        println(an)
    }
}