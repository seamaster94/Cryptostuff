__author__ = 'Sascha'

import operator
import re
import base64


#
#coinc = dict()
#nice_try = dict()

knacknuss = """W yzrqc az o ghcu ivbe avi Jshkiedhbho. Yzrqcwu ova kvrpr xlsx yzcjw.
Nhwfstwadxrdf 3 amhzwrr cspfw kt yoszhlb ens adhr whql usou. Xuwf ova gcoh gzycycv cxx gzl Bipvsupnfkg. E hofji csyh sb hvh qnjrsx eg trv ggbfmoh gryiwuwvo. Vcziiwy gsis Rxxpz wsslzs, seelpqyhofoc ssyaing, advxwa uenrsqiek hbh cofgiawyg wpwzo arsy hlaa trv rnlfczom xwr. Gbhwers wlr lvivegh lrqmzhvu, yzrqcwu qej ps ishfk pioh wq pbuhz xkcz vlbhz orz uouhrf jsrpsfv.
Xuw afezwhlsass oph-kcrhrf Kixyv qostk ooza pshr bxmwgeozoc nujfizwhhh nk zojahm vlbwz kmpv hki PW tovg obg gnf dwxdghdrq ssasoh oqc cwusxnohlsa auqpqrwqk fzhft kpxhggk hbh ycbfialyoxar ofmqk. Aviu ofh eplbophm gdjrj avej ghhiyuhdtar dusgwjhmrs gksrk pb wkas fmeubawpobfif, sz hla kcrh pjhqoo fowlrj avej rsqxf au sbpfspi nujwhabhv, eydvkmju sdwl jlasroz rj gzl qpku oqh aga qsjhwqyrv wfiogiui bf avi pcsv fl los (izus rj) gzl gxasz qsfw.Zcqa ct wlr Vbhgd ozvs pgugmzsf zinjpbk yzcjw nk ismju vheylom jkf hki jwhfing' thig.
Auhinsgwmay mogp, hvh oygtd mo ozvs ewsoxar hr xuw dcvz goesgsns. Xds Tuiauo ksnr trv xdvat eg gdfbl. Mfijqv zseclfw svc ziew ysthoqhh oq togdwbhw gzycaar o npbew wr pvs pepzpbi pc puinc ph.
Cki sdvawk msqfghps los jefgw tnja cj pvs ipny: lpGPT{62o"""

plaidCTF20 = "fvoxoxfvwdepagxmwxfpukleofxhwevefuygzepfvexwfvufgeyfryedojhwffoyhxcwgmlxeylawfxfurwfvoxecfezfvwbecpfpeejuygoyfefvwxfpwwfxojumwuxfuffvwawuxflecaazubwjwoyfvwyepfvwuxfhwfjlopwckaohvfjlzopwoaahevupgwpfvuywjoywjdwyfufjupouvbuaajwuaoupkecygjwoyfvwuxxdofvyeacmwbvuzoyhlecpwzcbroyhdofvfvwgcgwdveheffvwrwlxfelecpxuzwuygfvexwfvufbuyfgempoyhxcofxbplfelecpcybawxujfexwffawgoxkcfwxfvechvflecgfubrawfvoxdofvuaoffawjepwfubfmcffvwyuhuoyzcghwkubrwpxogeyfryediubroxvwgufwupwswplfojwofvoyrezaorxuyhmcfxvofjuyfvwlpwubepkepufoeyuygojukwpxeyozobufoeyezzpwwgejzepuaaleczoaagebrwfxaorwfvufxubeybwkfzepwohyfeluaadvoawaudlwpxjcggldufwpuygfpexxfuaaecfezmcxoywxxoxiuoazepjwuyglecpwxcoyhjwbosoaalwnvomoffvoxoyfvwbecpfpeejheeygeofogupwlecbeyhpufcaufoeyxfvwzauhoxxoybwywdbplkfejohvfvuswyxumubrgeepxocxweagbplkfe"

def count_letters(text):
    """ Counts all occuring letters in a string-"""
    alphabet = dict()
    distribution = dict()
    for e in text:
        if e in alphabet:
            alphabet[e] += 1
        else:
            alphabet[e] = 1
    sorted_alphabet = sorted(alphabet.items(), key=lambda x: x[1])
    print("Länge des Textes: " + str(len(text)))
    for element in sorted_alphabet:
        print(float(element[1]))
        distribution[str(element)] = str(((float(element[1]) / len(text)) *100))[:4]
    print(distribution)
    return sorted_alphabet

print(count_letters(plaidCTF20))

def count_splits(text, letters):
    """Counts, how many words occur with 2 up to 'letters' letters. """
    res = dict()
    #pattern = re.compile(r'\b.{2,letters}\b')
    for e in text.split():
        if len(e) >= 2 and len(e) <= letters:
            if len(e) in res:
                res[len(e)] .append(e)
            else:
                res[len(e)] = []
    return res

print(count_splits(plaidCTF20, 3))
#print(count_splits(plaidCTF20, 7)[4])

translator = {"f": "t", "w": "e", "e": "a", "u": "i", "x": "s", "y": "n", "v": "h", "p": "r", "a": "d", "c": "l",
              "g": "c", "b": "u", "l": "m", "j": "w", "h": "f", "z": "g", "r": "y", "d": "p", "m": "b", "k": "v",
              "s": "k", "q": "k", "n": "j", "o": "i"}
def substitution(text, translator):
    """ Takes a text and a dictionairy as a input, and returns a string, with all letters corresponding to the keys of
    the translator replaced by the values of translator[key]
    """
    nice_try = ''
    for letter in text:
        if letter in translator:
            letter = '['+ translator[letter]+ ']'
        nice_try += letter
    return(nice_try)

print(substitution(plaidCTF20, translator))

def base64_to_ascii(text):
    """ converts a base64-encoded text into a ascii-encoded text."""
    binarytext = base64.b64decode(text)


#
#6bit_translator = {'A': bin(0), 'B': bin(1), 'C': bin(2), }
#0	A	16	Q	32	g	48	w
#1	B	17	R	33	h	49	x
#2	C	18	S	34	i	50	y
#3	D	19	T	35	j	51	z
#4	E	20	U	36	k	52	0
#5	F	21	V	37	l	53	1
#6	G	22	W	38	m	54	2
#7	H	23	X	39	n	55	3
#8	I	24	Y	40	o	56	4
#9	J	25	Z	41	p	57	5
#10	K	26	a	42	q	58	6
#11	L	27	b	43	r	59	7
#12	M	28	c	44	s	60	8
#13	N	29	d	45	t	61	9
#14	O	30	e	46	u	62	+
#15	P	31	f	47	v	63	/


