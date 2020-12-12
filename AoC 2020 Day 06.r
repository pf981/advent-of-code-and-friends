# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/6
# MAGIC 
# MAGIC <main>
# MAGIC <script>window.addEventListener('click', function(e,s,r){if(e.target.nodeName==='CODE'&&e.detail===3){s=window.getSelection();s.removeAllRanges();r=document.createRange();r.selectNodeContents(e.target);s.addRange(r);}});</script>
# MAGIC <article class="day-desc"><h2>--- Day 6: Custom Customs ---</h2><p>As your flight approaches the regional airport where you'll switch to a much larger plane, <a href="https://en.wikipedia.org/wiki/Customs_declaration" target="_blank">customs declaration forms</a> are distributed to the passengers.</p>
# MAGIC <p>The form asks a series of 26 yes-or-no questions marked <code>a</code> through <code>z</code>. All you need to do is identify the questions for which <em>anyone in your group</em> answers "yes". Since your group is just you, this doesn't take very long.</p>
# MAGIC <p>However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line.  For example:</p>
# MAGIC <pre><code>abcx
# MAGIC abcy
# MAGIC abcz
# MAGIC </code></pre>
# MAGIC <p>In this group, there are <em><code>6</code></em> questions to which anyone answered "yes": <code>a</code>, <code>b</code>, <code>c</code>, <code>x</code>, <code>y</code>, and <code>z</code>. (Duplicate answers to the same question don't count extra; each question counts at most once.)</p>
# MAGIC <p>Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:</p>
# MAGIC <pre><code>abc
# MAGIC 
# MAGIC a
# MAGIC b
# MAGIC c
# MAGIC 
# MAGIC ab
# MAGIC ac
# MAGIC 
# MAGIC a
# MAGIC a
# MAGIC a
# MAGIC a
# MAGIC 
# MAGIC b
# MAGIC </code></pre>
# MAGIC <p>This list represents answers from five groups:</p>
# MAGIC <ul>
# MAGIC <li>The first group contains one person who answered "yes" to <em><code>3</code></em> questions: <code>a</code>, <code>b</code>, and <code>c</code>.</li>
# MAGIC <li>The second group contains three people; combined, they answered "yes" to <em><code>3</code></em> questions: <code>a</code>, <code>b</code>, and <code>c</code>.</li>
# MAGIC <li>The third group contains two people; combined, they answered "yes" to <em><code>3</code></em> questions: <code>a</code>, <code>b</code>, and <code>c</code>.</li>
# MAGIC <li>The fourth group contains four people; combined, they answered "yes" to only <em><code>1</code></em> question, <code>a</code>.</li>
# MAGIC <li>The last group contains one person who answered "yes" to only <em><code>1</code></em> question, <code>b</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the sum of these counts is <code>3 + 3 + 3 + 1 + 1</code> = <em><code>11</code></em>.</p>
# MAGIC <p>For each group, count the number of questions to which anyone answered "yes". <em>What is the sum of those counts?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>6170</code>.</p><article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you finish the last group's customs declaration, you notice that <span title="Don't worry, nobody ever misreads just one word in real life.">you misread one word</span> in the instructions:</p>
# MAGIC <p>You don't need to identify the questions to which <em>anyone</em> answered "yes"; you need to identify the questions to which <em>everyone</em> answered "yes"!</p>
# MAGIC <p>Using the same  example as above:</p>
# MAGIC <pre><code>abc
# MAGIC 
# MAGIC a
# MAGIC b
# MAGIC c
# MAGIC 
# MAGIC ab
# MAGIC ac
# MAGIC 
# MAGIC a
# MAGIC a
# MAGIC a
# MAGIC a
# MAGIC 
# MAGIC b
# MAGIC </code></pre>
# MAGIC <p>This list represents answers from five groups:</p>
# MAGIC <ul>
# MAGIC <li>In the first group, everyone (all 1 person) answered "yes" to <em><code>3</code></em> questions: <code>a</code>, <code>b</code>, and <code>c</code>.</li>
# MAGIC <li>In the second group, there is <em>no</em> question to which everyone answered "yes".</li>
# MAGIC <li>In the third group, everyone answered yes to only <em><code>1</code></em> question, <code>a</code>. Since some people did not answer "yes" to <code>b</code> or <code>c</code>, they don't count.</li>
# MAGIC <li>In the fourth group, everyone answered yes to only <em><code>1</code></em> question, <code>a</code>.</li>
# MAGIC <li>In the fifth group, everyone (all 1 person) answered "yes" to <em><code>1</code></em> question, <code>b</code>.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the sum of these counts is <code>3 + 0 + 1 + 1 + 1</code> = <em><code>6</code></em>.</p>
# MAGIC <p>For each group, count the number of questions to which <em>everyone</em> answered "yes". <em>What is the sum of those counts?</em></p>
# MAGIC </article>
# MAGIC <p>Your puzzle answer was <code>2947</code>.</p><p class="day-success">Both parts of this puzzle are complete! They provide two gold stars: **</p>
# MAGIC <p>At this point, you should <a href="/2020">return to your Advent calendar</a> and try another puzzle.</p>
# MAGIC <p>If you still want to see it, you can <a href="6/input" target="_blank">get your puzzle input</a>.</p>
# MAGIC <p>You can also <span class="share">[Share<span class="share-content">on
# MAGIC   <a href="https://twitter.com/intent/tweet?text=I%27ve+completed+%22Custom+Customs%22+%2D+Day+6+%2D+Advent+of+Code+2020&amp;url=https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F6&amp;related=ericwastl&amp;hashtags=AdventOfCode" target="_blank">Twitter</a>
# MAGIC   <a href="javascript:void(0);" onclick="var mastodon_instance=prompt('Mastodon Instance / Server Name?'); if(typeof mastodon_instance==='string' &amp;&amp; mastodon_instance.length){this.href='https://'+mastodon_instance+'/share?text=I%27ve+completed+%22Custom+Customs%22+%2D+Day+6+%2D+Advent+of+Code+2020+%23AdventOfCode+https%3A%2F%2Fadventofcode%2Ecom%2F2020%2Fday%2F6'}else{return false;}" target="_blank">Mastodon</a></span>]</span> this puzzle.</p>
# MAGIC </main>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "jmcvr
marvj

doh
kdrmulsg
ypde
eyodf
d

gneqwlfbjxcmvpstoak
gsnmaweycokpxvtqjfl

wufimrzxltqke
iuflmwzrteqkxyga

outvl
tolvu
votul

tmfjpaxhricyld
ymjialfkxchprd
mljcxfhdgrapyi
myljhxfdcrpai
cxrhgmljdafpyi

cx
xc
cx

ncwxluvo
woybuiacmeqkrxzn
pchwtsxnuo
cnoutxgfvw
hfxcgouvnw

d
m
n

bovpilz
ovzlfib

cxnfyaelwvzq
bgrxhsl
juxiol
rijlxdt

iaxgdh
haigxd
ixhgda
haixdg
hiadxg

mnlizwedqrcg
ocmwragqdnfie
ecmwrqgind

vgzhujaqcptlfosnkyewmb
yoxlacmnwkqvpsjehgtzufb
ynlpbztwqcvaghksfdmjeiou

eai
ielk
hoiemtg
kexi
ine

xwcsyrvjanhltfqpmuoikgd
gonhrmdixykztjucwqlfpsa
tjalfyhudsmknqrocwgxpi

qefnjlradtyiwugmhkcxpzsb
ybrwdukzgeqhsmxpcaniojflt
kqsndcybemrgfwxiuaztjplh

zmpuyef
zepfumc
ufepmz
uzenpmf
mefzpu

nouftsgkayw
unoaswykfmteg
gnypwskafqtu

cqfatlhduwbv
wvabclqufdt
vqawbtudoecfl
tuvlawbdfcq

kjhvutrgoblpmdy
gkbrmpvydljoau
luiwndrmsvkzyjog

xcj
hbnmc
uvpclterk
cyinmzj
qcs

vywm
m
m
m

wpajrnoudxyhs
wuoxdayljnhrps
boxjpnwhusaerdtfkvyzm
qhndgocpasrixjwuy

rjwmt
twxj
tjw
wjt
twj

uwcebltnksazfd
dyeunsfavkzwc
gxiszcamdfnkuh
pkuqajozcnfsdr

l
l
l

ekxmjsyh
jymkhexv

phkw
whkrp
wkph
phkw
khwp

hzyaj
atyzvg

xpu
mp

wcetozfsjlbvdmig
cnapwmlgzk
mwynhugclzq

xcrhvnwsikul
bdlnrswivuxc

ecv
evp
ev
yuvie
pcve

sycbzvkjhiupxgtq
xuycqhptvkzbsjig
vgzcitubshqyjkpx

tasdmoy
masjly
qmfsyj
hsmoy
umzgskcbiprywn

rustblckdfjx
ftrujcbdxslk

frswhgvtj
gmitfnuhpwkyqx
wzfajgchet
hwbtcgflr

l
myczv
l
h

bjymhok
ngadmt

fbcxnwavutjzipglqe
ablzgeuivnqfptwcjx
ubgqzjwnavctfpliex

ghemp
qmpxgh

jdh
dhju
ude
drsgtkp

hlsivanjo
losnuhmziva
zlhnovias

l
x

sw
sw
gws
sw

fpgu
pufg

f
f
cn

gvbxjldm
dhlmbjv
mnbdvlj
bmdjrlv

lhvujbgno
ngluhojv
hivuwlnjogk
lhvgubjonc

v
p
c
i
r

e
e

ucoiyhwem
hoiueqap
vreozgntbu

pqykxjsmuact
fseonvdrgzbw

tuckf
kftuc
uftck
cufkt
ctkuf

cexirwftagusbhpzlodkyj
ugtyorbcaejwhixlfskzd
ebijclzodrxykawstgufh
jcksbdholmatzyfwnvigreux

uyczsapqhvfltxbwgn
jumxibzwhoprvqtfdsg

psun
sdaxtkchn
musn
sn
qsumnwg

i
ic
id
jic

qgcdivwhxs
zyoltm

deixqu
toflkep
hbaze
yjsgcxveam

wqbjkmluyos
jfwtsgkbvorquhy

xoj
foxjl
oxj
uxjo
jox

pqmnoyrwgk
porqtkwygmz
wqksmgpnoyer
qmxocfauprigykw

ivox
voxi

veh
hve
hve

pfqgzoelmyawuc
goszuamnfxecyqp
eucpazlgjmyof
eazgycdmufop
ativbhzkeogfycpmur

fzlonc
fonzlc
lonzfc
lfoncz

sucrahnjglmzfikevoxqp
fnlaimqjpsruhvzkgoecx

ouvyz
quh
ljecsb

vbnzfcpduytlei
boipnfytulvcz
vuzgtficlhbyp
fipbmwzjslvtruayxc
plzybituokqgnvfc

tcyfbkaw
tfyakw
wekynatf
twafyk

n
ojn
s
n

i
ih
bsi
in

qrihgluedspjycb
puhjlbceirqsdgy
iudrqejcbpylsgh
eygcpbudrqhljsi
lheiscrjqdyupgb

nw
nw
nw
nw
wn

urxsya
bycij
ynk
nyqvatr
vytao

gvoszuwxfa
hzxruaqwgvdfs
gxzfaosvlwu
fgvwpezsau
amvruzgfsw

nkplwreoy
aoe
cjmvohs

kznwvygbjtmsxochrfliuq
flgqmctuwkshvrbnx
twugqmxkcsvbnfelahr

donptruvijqzx
cpqfuiodrjeznx

azwxpnqisodcbue
bdaxoypgnzwui

pvmaybqceh
yajvshgnifk

tqzernishxmgaodfvwpj
xobwgtpejqsrdhz
rhqpgejwsltdoxbz
wqodztgjsehxpr

whqvmejckfiudnrsgapy
ikfhcyqavdsrjwulegpnm
niskxmuapwgbdqrycetfjh
eqrkyumgndcwpifhasj
jgudwyamprikqcesfnh

vxmeapndjq
elkbqxdaz
ogaeyxdq

fjrmydqwp
wydmjprq
dyrwpmjuqb
mjwydqpr
pqyjfmrdw

oms
osma

fevzlpstd
efvlcgdtsn

jlhcexfdtbgrwykznuo
zvkdhbyojlgfxtnwurce
gbhklxjndzyeiproftwcu
etuldfygkzwnhbxcovjr

kznbxcadpgqerwmoyfslv
yveqanzpskdoxwclgbmfr
cfaqdwbxemgvynkrozspl
ypeqlszdbafrvnxkcwmog
bronewmgpfszvklyxcqda

w
w
w

cpi
c
c
c
c

pxltifng
anlsvgx
dbwlrmgonz
xglniuh

jfhelnqtipadxwr
dwthfarexijnpl
hrewiglfjxnapdt
nwpfvlixarjhtde

nb
r
r

ixafewbtzrkqsd
pdconufaxhlkvgy

juieosrl
cijgferulswo

qhfsedblari
gyphvxzwmtc

rpo
o
vow
vno
wvo

iptoy
piuo
pio

tueioxzyhnjkfbg
bxhgufiokzney
xzgfkboyneuhi
gbknuyxhifeoz

qhkyrvdtaln
aztsbjwquxokri
afrcklqt

nc
dehsrf
wp

v
v

dkzwixqjbthmurvca
pjvcwgbszlefxyn

obxijc
bofcjx
xbjco

mhktbrljyg
nirlg
zrgql
gaplr
iqsrvgl

cadtpqvo
pctvqago
paqovtc
apcotvq

balcxuhpiseg
knistcxue

qejnfmbska
imdqnsjfabe
nfbmaesjq
sgoqmnbjfae

jxy
ibjyd
vygj

ojuzcadpxw
zpradwglyien
ztdxapwbq
dpzqukawx
dsfbopawhz

cwuzitmfbxejlyk
xmynf
dfamyxgp
fgymxq

kovdtmebspcwurxq
vwmdrjueoqntgbcpsi
tsbvrpuodemqcnw
prcuwdqbmieotvsf
tdqrawulobepsmvchz

ikufnxbywva
zhgetmqcdaprls

vtsi
vits
stiv
tivs
stvi

ikgsf
kfros
skf

qxnyg
on
wnrzhevli
njyxap
stn

lyza
zeyal
yahzlo
zayl

pyaglvdjf
njsceglwtbdp
jlvgdp

ceswvfxldjahpzutk
simfjdlzavohywucpx

bknvsezl
eslnbvkz
vnkselzb
semlkznvb
sekzblvn

qpxcy
ljqbcp

lfaqkwpizu
pduzsychgja
ntqupawmz
uoaqzfp

tu
ut
tfmluv

hbelrdkapxmvsqgfin
mdhnaflgbsxerpkq
nrxedfqbmghlakspt
nqkarfbehplxsgdm

jtbfzhxd
zcfjtbx
vxhbztjef
lfkijotuqzxba
zfjxtb

o
o
t

qhd
h
h

pdvikgrwust
gpurwkdtias
tuplksgiwdr
swqkptudgir

vfct
qbgyjelp
ct

vxonbisrjlquyktwp
osxqitjblyndwurkfp

kzfjuybwdx
dzbexpfijwk
wkbxqjfdz

dqkrwf
rfkdqw
rwfqdk
rfdwkq
drqfwk

frexstackzgnjwh
uvbzyqlpm

wijxztecbpqylrsof
xpltqsrnebocijwfz
pzwdhreoxlicqsbftj
lewspjczrqfbtiaox
eivbswtxqrpzcgfljo

ghtcljxsiazkuqmnfvwyop
jwulpndxyeibztgsamrqkoc

xi
yx
qx
xw

mups
mpsxu

vtszwo
ltvzrow
zwsdtov

kuoipzvlcsjmdfebxw
fnebckrizujtwpxq

ldqxcn
jlzuicagxh
ilmctaxo

ivnyeut
utiyev
vtiuey

qodp
hqn
q

tr
rt
rt
lztbijwr
tur

gad
ad
ad
ad
tda

lusvnkcpgryjixz
jgkzrisyucxpnvl
xnusyvjciklgprz
gkvsiulypjxcznr

kvneghodfrct
kgrlnqvhcx
khnvlrxqpugc
gcnkhyvr
gmhvcnrk

orjdfaptbcvl
tlavrdfucpbjo

zqompunrfeiy
pqyomzurif
forujzmpqvtxiy
cufzrlomypikqd

qpwsajvfxndbtm
qfsjdnbtmpxvaw
sphdjvwaqfgixtnbm
qfmtezvojpwscardbxn
afdbmxtspnqvjwg

khgsmvwad
wokymraphszg
asmbgkhw

eulncr
crnul
luvnrcj

icb
suyt
lr
wqbgz

sucnh
nhucs
unhsc

ivhrypsx
yhvsrpxi
syriphxv

abfvpxwrymksi
yrbkxswanivpm
aimysrbpxvkw
iapwkrbmvsxy
kxbpgicsavmywer

ujefblv
bfja
fbj
jbf

fpoviwdk
zpusja
rsgmape

geukt
sdqy
vysq

smigbkfvrnyw
zkgqyvfwhd

skw
qswk
wks
mksw

wsz
sjgwz

cldthxb
xdlqchtb
bchldtxp
hbxtdlcq

klbywtef
iktfpcy
fkty
kfxtyva

xczosruim
xmsiczo
symzncxtilo
mjxoicsdzq
eojmusdcixz

kcqzyibsdw
zcyqlidksu
cmzqjhfsdyik

f
f
f
f

fiskzwaundyom
inosdyuakmwzf
iatdnwzfyosukm
oszaydinkmfuw

flicgakhrpxjbentwyuzq
lduxhqbsarcvejtnwmkyof

gkcmzqpiuv
vcuzqegkmjip

ehdyguo
autprsky
rayuwcf
iksuy
uy

gpyifovl
yfvxlpg
gpflvy

eidr
ierd
drei
ride

dirp
jg

qz
zpq
qzynvp
qzvg
ztmdq

kbdsmpqngith
gkinbdthmrqsp
mthrpbidngsqk
fwsktgmbcinhdpqa

lxa
alx
alx
lxkamn

bykfv
ykbvfg

hdxkgbierszqplvtyujcfawnmo
dgzkebvxnarwosihpjflqmyu
gpluehrvkbjmowyfzsnxiqda

ijpskconavfy
jopvyskbfidh
rxgwsvloyetupqmkjfzi

b
b
w
e
x

docfzlgmuktbrnaphvieyqsjxw
dmokthecrbpsfyqjlaznwvxuig

hw
whu

fhrwdejnxb
wyvbhkezjcumn

vnoks
nsk
ksatnw
nplsky

ihpdyrkwlvmfaocuzj
chkoymzwelpjf
lmkyjwhfzcop

ajyuhqxn
xyauqjhn
haqnxuy
xqznauohyc
hxajyuqvn

fztsvm
jvfmzt
wzvdhpotumf

ewyclrsztqmxhbkudi
elsijdmcfgvnrpbkqao

evgmapfjhwlzby
plhgjyvbmeazfw
yzudbaogjnqvlemfhpwk
xsbeawmgfjvhiyzlp
vpfbglywjmzeah

qubejn
nujqbe
juqnbe
nuqejb
qnjebu

ysjxvl
svlnpjy

w
w
bwq
w

pxw
wxroh
hxdt
pxvf
yknisujcbxlegq

ckwi
kwfvi
ivkw
wki

bqowsjpxzkdeura
szceuorpkdxaq
zoparqsuhdgxke

anm
ln

p
fds
w
i

qgswozixebydaurpj
xvmwuianrsygpzoedqjb
aeiruopfwdysjqbxgz
dbwxiyuazjetogrqsp

kfpajbghmoqw
qceawob
owbxqa
oqvlabw
boqaxiw

baxlpkydhmwn
kyactupsxdmnw

exrjugtcynwvdb
twgbjzvcdunre
ucjtebdwyrvng
rbweudvxcgjnt

zheoun
hulzxe
hloauz
hzsfu
zlaudhr

tminpflavgkxrsdyzq
dykpgsxqnltzvmfiar
smzirgqnvyktdlapfx

xpguove
vxupegio
pougevx
pogvxue

co
cios
poc

u
u
u
u

xgszykfjp
jayxzpgbsfc
tyxszpjgf

sqiyvnec
eyscniqbv
vnieqysc

qwtbhva
whtqbsv
pwjcqvhtrb
twbhvql
qvhwtb

epvfcbjsdo
gpti
qylpkw
phnizyq
zrpaxu

igemwkru
xsktwbgh

smbfakwglvz
olmswfv
lmwsfv
vwselufm
lfswmvhd

flzivx
vrxfw
meoxqgyadnt

iyrsqaxkdeuzbfpolt
xcosekyipavrutqldfgzb
abiklworzpsqhyjxfdteu

uh
x
pgfy

dulxercoykfzs
ezxyrqnljd
lyrhmxajbzde

oxnuafhesi
poaxnshfieu

xhnqbv
axkgvzq
svnzkxq
iqtbvxj
fmvqxdryo

qxocdfn
gqocndxf
onxcfqd
bqxcondf
dqxocfn

xyf
fyx
fxy

xibzdsefv
zxvbifsde
svxfzeibd

tqwcehgrindmj
tdniwmzrgfcjhyq
htrjngqiwkdcm
gmhnqtilwjdcre

yivbdgcqa
bdaycvgi

egmtkosihblnpdvaufcrq
arbznlpgsovktfumhdiceq
vmdeqlbiuftnpahoscrkg
oamfnpbcsltdrqivhkegu

vniomyberucg
fxslzatq

xiapqy
pya
ytsap
ayp

sirtykxd
sicktrd
isrkdt
sdixtrkb
mpustkrdzi

nxkitjzs
kinjbytzsx
ntkjxzis
ijtwkxnszd
iktnzsjrx

grjvys
ujvsgx

kqxg
gxkq
gxqok
gqkx
qxgk

bcilrdpauxmq
jcfogkyvlzhxsbp

kpgwvfex
pgenidbvx
gevdxspn
egpxtvsb

zeud
dzue
ezud

kwyuvpamheb
zplya
laiyp

uxdsnziv
ixvszdun
zdsvnixu
igfsnuvzxdp
dsvuixzn

ngfdlqmrxwtuv
vuxezkhoigncla

hv
rfhev

mscweilzq
wqrmksze
qskzumwex
hjmswnzeytgfdq
zwbermusq

nlbxzcpayri
rxlanbcyizp
npdqcylxzubria
cazxrwilbpyn
axylibrcznp

jbxtrnshwmqafczdugo
rsowfqnmugbjazdhtxc
yowcuzgraqtdhbmsjxfn

pzjlbxchewutsnogmk
smpyhbntzxakufloge

rfjwd
gdfwexr
drwfexa
wfkdrlp
mtidzvcfwrhy

dwva
vwad
wdxza
gwad
aspcwdl

xcfr
lhxbfr
xdrmcwf
rcxyfio
fxrodn

uaw
u
u

qrijuhlztegmvyc
htjeulzcgryqvmi
rgvemljiyzqcthu
jcmuvygtirqzlhe
jvtgyeulczhrwqmi

cywvfe
fwevxc
xecfvw

mfwoznta
wifn
xdsk

pzdfjcombvthquls
pfxslgrayvkui

uoyqkrhievabmfwxntlc
dqylwmixtahcekrov
yzicmeqwopklrsajvgtx

tlbzcfpgw
ehgj
uydoixaqsvg
zckgnm

t
t
u
t
t

frsqwpyhmx
spxqhryw
qyhewsxrp

wfde
wuesonzy
faew
hawjfe
ejwp

psq
qp

kts
skt
skt

q
r

rndjegh
ndhrejg
jdrgehn

ti
afchje
lxkmypv
ehrjd

vszy
szyv
zvsy
hzyvs
svxozy

vygnmbzxqlt
bmtzqvxyjg
qcmxvbzjgdoit
rezkmbvuxatgq
yqixtpwvmbgnz

bqeuzkdrln
qlvybjtsmdekpxor
zulrhkbdqaec
qkbhrazedli

cxznrlvhdo
ondvrzwuxi
drpsvyoknxa

zmovqcpygfsiuxklwhejrdab
ydiuvjxrbzehkwplcfmosqga
fhclwsrozjgkqvaxyieumbpd
qxfoljagpdsmbvchuiykzerw

n
n
nx

oebwgshp
wbgspieh
xbgepwvsh
whsgbjpte

sbge
esbg
sbeg
begs
esgb

niwhmy
nwiymj
isnyldqxwc
yiwn

vsn
veamr

voafu
keo
voz
ndhgtqmpo
vo

hkmwvrtxbejz
xztwbfgjvr
bzvtwxjr
vtrxjzbw
zjvfrxiwtb

cvhljyr
ycrhljv
rcjlyvh
rvhljfyuzc

igt
agoitu
tlgih
togai
tigu

aozudhmnv
lpkvrjzifegbt
wzhdqaxcvy

ej
e
enc
e

xgcfkjdntsuilayhqzwre
xgukfyhbezriqlajdtwn
geinwdtqrfxhlaykuzj
xkyfrznwlqidauhtgje

d
kv
m
d

d
dqch
i
mc
zywa

crik
iecfh
lirgczph
sjvxcmibqaydonw

hurdm
umhrd
rhdum

ermio
rem
emr
mre
rme

dchmwyfk
whcymkfd
dkhwcmyf
ywfmkhdc

m
ih

bzfdtrce

dizlgksopctuyrf
ofzyjktgsnvrpiul

fctgjmhzaknpsd
hgjavckztxse
cjksnahgut
bagjhliyqstrocw

hvu
f
u
niwjx
vf

nuozebjagkhdqrwt
fgrnhkadtbquoejz
cneirbqhdjoygztuxka
grdojebkatuhnqz
ugztqojabredkhn

rxeyi
rbxsie
ijlxuhe

azrlemjgcdqwhnfbtuo
jhcavrizqtflyepok

oxynmtsgkv
gqnomxyk
fnxqgmylok
giyrbckhxnwm

jzqupkynsrxaifeg
ugcbyrpnwxkeioatvhlfd

kxzphoyladfwm
dlmkaxwfyzoph
lxudmakocwfpzsy
foxmydwlzpka

ehsxl
dyiehx

grvdmsbtxucpqwyj
bprqygvmsdxukwjt

symnihotjdglxuwqvf
sdvunxgzojfrbalw

rudnjfeymbhcoqs
xqonmwytfudgrjspb

lfezcvyumpokhdriq
pdirafkuocveqmylz
xiczmotupdeavylfqrk
pbdecmzyusjinqfrklgov

ux
rx
px
uxo

gqcpldoxukinarezjsfmwty
wxijftmzlsenpcoqrdybukg

kszg
k
k

qlu
q
qm
q
mq

zixsykjfgmqrw
ztmnfsqrkxgi
zgqseixrmkdf

hzasq
bylsqz
tsgqz
zshqf

yglczv
hvclyug
lcvgy
cvlwyge

rjxwahkfqybcsnm
lnpygfhirmkbawqxjc
jasnrhfkwyxmdcqb
ahqxcdfbjwyzknrm

rnumlkzyxhsqv
klxmonyuvrhsqzp
iunymsrhqlzvxk
kmquyhnlxzvsr

zsegylqmhjapvwtb
azvheoqmrpgwjblts
ptsjblwhaqzvegym

i
uf
kb
l
wl

zjx
xdtjroe
jfca
mynsvluwb

dcrxnvw
nxwdprc
ldxnwycrp
nxcrdw

gfljwsonki
ydxaecbqvr
upfmhtsz

mrephsjynzlku
yloxaetzhjfusikm

bsfqnlocdv
vdxfuqcolsz
wehgsfarqyvopmt

ulcyihg
lcvug
gulc

jxwopchkgf
hwgpkjuo
gjhpuokwn

miqsvpoegzknxj
sjzwveifogaquykcm

t
rnkaqm
kpa
sdjlv

wolpetm
omutwlq
odwtm
twoipm
motzw

opvwc
cpvw

zunej
vzjqfikme
xlzegjac
zlnjge

vjpznxu
uxeyovpj
rxjkwpvu
jbvpmux
pxjwvu

xvfqhmzwnkudciogp
hbqpcxdonwmugzfikv
xkvfgonizcwpdqumh
qpzfomginkwvduchx

o
o

yaihsrozcb
zyuicoharb
cyiarhzob
ychborazi

hcpefysokwnt
jlcwnpqxkfehy
zpfvahrmunbwgedi

eqkcmtaj
gvzuiwdhbspx
tykcq

dm
md

vgpbiofdeynalk
nvfgkbleyiopda
bfndkevaogliyp

xmtgyovfqhlszdbecirp
swutolzmcixyvgqnhr
vlqxcjzgtaiyhmsor

ixv
irv
vri
vi
lvi

nwac
nac
anocgx
cna

r
dr
rv

tzlxd
xwqpibztulad
mjxltyfsz
hzlxet
zxlt

u
u
u
u

drqztbxkyajfnwgovslhmui
oivcrkxqbdtunamflhwygjsz
falhroiudgszvkytjxwbnqm

qnihelxaus
xsieavhqld

hybtifmsalgwq
tywkxqszgfprmo

m
m
hm

imjxcnz
jxznpw
bjzxougye

mpbytfl
tujhimgws

hnlpwedivbuqrf
xqwjrnahgbyu

gzyvowjxchiarlksb
amepscroidgkwhvzxyjl
ryxzcasljivokghw

n
n
n

yvgiotm
gviytmo
imtyov
oitmyvuj

euanslzqvgfxipbo
iudlbnjwvcythmrpe

wktbvufdamyenjsclzxqhgpi
aivtwmgczybnsxdkhplque
phuxzyctembvqgraksinlwd

nbht
hntb
thbn
nhbt
rthnb

yvr
gvy
ryv
vry

bhocmeravgznykujf
nmvgeboafkpuz
egvafobumknz

zklgbcevfojhwriq
zjqflxokvhgeicbwr
kcioelrbjhfzvwgq

vux
uv

rsnpdmklh
lxrqczu
joiaegvyb

tp
ipt
paexwtu

v
sej
xiv

l
w
l
cj
l

marvbhizesfugdnpclqkwxyj
nxkyrdwzflgbjqsaecpiuhm

vzl
z

ztey
ytez
ezty
eytz
tyez

kdnocrgm
mdngokc
socfkndiglamj
nkdecmgo

pdiazkqeju
idulkeqjpazf
peazkindquj

pwdimugxeh
hzpbwudxmegi
gemhpwixdu
ixwdhmegup

dxp
qpdcx
dxp
fxdowkps
dxvbghyp

a
a
aj

pf
fp
pf

ghzxa
xvdzjy
xnzrabf
lzfknbxqas

b
u
b

pmgjysxhkw
zpbfaqh

bqltrv
fzt
umtc

tvaylxdmfr
rzgibpqjlhcky

rcmkjw
zrjm
jtmfr
mjr

oji
ijw
oij
qijc

togbvkacqjrnsdm
qbvandscrtmfojg
vnomkqrjcdgbsat

fxm
mf
mf

labnifyw
nwibyfjs
faidyb
bsuixy
cbermhptokvgizqy

jaoei
auogj
naglo
zuaoxj
hsdcykwovftarq

vfqa
vqa
aqv
iqav

xsbpdzu
lbunzwrqdsgvxp
dtbfapxuizjys
ksgrvzbwpxdue

edxwayiz
jgpfqkm
zvewc

odxts
cedxpost
xotsdi
qtdoxs

ysqxkzdcbuergwjfivtoph
zafthripqcdeoumjyxlnvkgws

hfrujsmvckxwniepdy
jwaeprnxdylsucfkimv

vdapyuqzsxbk
gvicztrjqmf

dlmjakb
iwabdjk

q
q

wk
wk
wk
kw
kw

uwbkfojtazpvsygxqnhmiel
cbfuoxewakqmrpnzt

pcbye
pebyc
beucyp
padygebw
ebpy

imtqugjanrwpexl
ianpcluewjrg
lgjeiyopnwuar

idjahpnsfyvokzctmr
jfcshiradvpozlyutnk

cyvapdrqtgzksnm
vjylmgcusotzpqdna

lwgqftpameshzcxjvio
denobxsjhawukyq

nilbuswmv
cuwqsl
sxulw

ikano
vtrzxyqeulw

isugbhaxowyzd
yhuasbzdgwoxi
gihodusxwaytzb

ucdtwxjqbozv
vtdxbzjqwcu
bvjdqwyxzcut
dcvbxzwtjqu
jqtcbzvwudx

k
k
k

zpvou
uoxavznp
pouva
opyjqivlhuebg

hr
vr
lcne

csngfr
gsn
nsg
ngs
gsn

gtfpwms
swt
wtls
etwzs

sdnurw
cnldptvwrsg
ibjrxmzofnadehk

moizkgtebyscwf
okgcqwsifrybtez
iefxohlsjykabtgcu
oygcfkbtised
eowipvcygfbknst

bktuncgwoimd
utdocihgkmbwn
kbomndicwgtu
gowmcbdnutki

kchguwafroy
uhkocrjeqaxwbg

flvhgjzbcd
cdbygeztf
bghqzcmf
gpcrbkzsufi

xkzfocvps
vlhofui
jbrfmanov
pvsjdfrzow

os
s
ds
os
s

abldotguwpcivn
boaqpwxlvg
bymzhfgwseovl

bhz
zbh
hzb

xb
bx
bx
bxn

c
co
icy

ydilw
ylwdih
lwydi
gydwilt
cldwiy

hr
h
rh
h
he

lhbpo
flbho
hbol
ihkrjbol
lvbhqo

l
l
l
ls
gl

o
h
jr
so
dbf

wljmryca
mlgjcr
cljrm
rljmcz
rcplmjg

ayhfznrgoub
kfzgmoynlwbjt

tadlv
vduat
vadlht

xlkngoz
sxbwply

fkutnyrvsxpqcmzw
pjwltkoymruvzfxcsq
vkzmqdtsfxchyuwr
kmyfzaexcswvurtqi

epirjxhtngblam
selbxmgnrthiacvf
elnmtrhxpbagi
xrenthmilbgad
mlbxantpehgri

mjilctopnk
ltjnxkcmip
pkijcsmdetln
tjincphkml

hbufxmodlyeqj
mwzhjbefdupxqolayg
notqhbdlefjmxuy
lyqobxdeuhfjm
lefdmhoqxcujyibr

hktjbxf
zurltvgfbhy
bitpoknhfesa

xwlpniufjtbesdkhzv
sdhilwvxjfpzubekt
bxaejlktihosdpfuzvw
xhudtfezbnwjlpsikv

juxwcq
wqjxf
qwjx
xjqw

dqesyxulowh
xtoswqyehidl
qslhxcyeodw

codpb
daljbpoc
moczdbp

idpuf
jdcfu
uzdgfhto

rgknle
glkren
eglknr

xplkswhuqtozn
bamjdvgie

dqvapsmu
toyfnw
zbhgjlrko

kxenarljymgfoqwic
eikoygxcarqfnwmjl

rmvfd
rdfm
dfrm
mwdrf

ipedzvkoabrtfynmgjhqcl
hpzdcbyiorklfangmeqvtj
vpacthzroeilydqbngfkmj
ocylkvpimjbdqrnegaftzh
lvpmzaoicnrghtkdjfyqeb

mniubl
lumnbi

twvodzl
ipbcmnxfhsy
jgvedu

ykhpfrnig
aktiyrfhgpnv
ipgyrnhfk
ghnyifrpk

bhsrjdm
mjrsbdh
djrsmbh
rsjdbxqmh

wvuocghaikszrt
qhxtucpmjzgowisbdlf
wcoutishgz

nmfuwei
wtnrmieu

ykgtrsvpiq
lmxdcwuehzfb

txlqnp
xlqpnt
qxpulnt
qpxltn

uyrqhei
laqwuihxe
clgeqiydbhk
fgqiupeh
oqimzshenjvt

bkvz
kvzb
okvztb
kvbz
kbvz

g
g
g
g

z
s
s
z
e

hrvinjdwbtl
dlivwhjtrb
dbwvlojrhctiq

ilyrdmqjgb
ydubicflm

idkpzwqbvatocu
ubdqawekipovxct
mgvebcadfwtkquxrio
dotvnsqkubacwyijh
ultikvoqwcdpab

w
wd
w

pvbouylkhdtrgxnifajwmec
actuxymjbfidhloewpgqr
hxzeaorwtpiludbjqmgcyf

csjyebmigpdl
prysedgbumjc

pkitmzfu
puikeqf

yafwqrdhpn
bxoevlstjm

iohkjpefsmvadgcu
plhbiucsgjtwaovfm
gjmpuvifchqasko
msvxhogjiuafcp
icvoujazphgmfs"

# COMMAND ----------

answers <-
  input %>%
  str_split("\n\n") %>%
  map(str_split, "\n") %>%
  first() %>%
  enframe(name = "group", value = "answer") %>%
  unnest(answer)

answers %>%
  group_by(group) %>%
  summarise(
    yes_questions = answer %>%
      str_split("") %>%
      unlist() %>%
      unique() %>%
      length()
  ) %>%
  pull(yes_questions) %>%
  sum()
#> [1] 6170

# COMMAND ----------

# MAGIC %md ## Part 2

# COMMAND ----------

answers %>%
  group_by(group) %>%
  summarise(
    yes_questions = list(
      answer %>%
        str_split("") %>%
        reduce(intersect)
    )
  ) %>%
  unnest(yes_questions) %>%
  count(group) %>%
  pull(n) %>%
  sum()
#> [1] 2947