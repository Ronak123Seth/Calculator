class p2 
{
    word(const s ,const w1)
    {
        let c = 0;
        let w = ''
        let l = s.length;
        for(let i = 0;i < l;i++)
        {
            let ch = s[i];
            if(ch !== ' ')
            w + = ch;
            else
            {
                if(w === w1)
                ++c;
                w=''
            }
        }
        console.log("The word "+w1+"is present "+c+"times")
    }
}
const obj = new p2("He is a good and is a bad man is he ","is");
