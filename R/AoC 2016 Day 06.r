# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 6: Signals and Noise ---</h2><p>Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple <a href="https://en.wikipedia.org/wiki/Repetition_code">repetition code</a> to get the message through.</p>
# MAGIC <p>In this model, the same message is sent repeatedly.  You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. <em>Almost</em>.</p>
# MAGIC <p>All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:</p>
# MAGIC <pre><code>eedadn
# MAGIC drvtee
# MAGIC eandsr
# MAGIC raavrd
# MAGIC atevrs
# MAGIC tsrnev
# MAGIC sdttsa
# MAGIC rasrtv
# MAGIC nssdts
# MAGIC ntnada
# MAGIC svetve
# MAGIC tesnvt
# MAGIC vntsnd
# MAGIC vrdear
# MAGIC dvrsen
# MAGIC enarar
# MAGIC </code></pre>
# MAGIC <p>The most common character in the first column is <code>e</code>; in the second, <code>a</code>; in the third, <code>s</code>, and so on. Combining these characters returns the error-corrected message, <code>easter</code>.</p>
# MAGIC <p>Given the recording in your puzzle input, <em>what is the error-corrected version</em> of the message being sent?</p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "uzmnhwye
jvyyfmhr
eiwokyzj
rghqvfsx
pqjbfqey
ceqkjgny
kbpuzvof
epyeucto
bqhqvbef
tqduwleg
ysadziyj
onvxrwcl
dwbhjkmx
qvgqewkr
qazepxhd
bqtuexvi
vieyforp
kizhadeh
ofpraxry
xamrsokr
jrrottpf
gweaulph
gyctgzpo
mkddcnuk
llbxmhbt
mghoubct
arhrpksk
hzeshlue
loygkukn
asakqobo
vwvjnarb
pmqcgzkj
soucxjes
szsuqdss
hyjyxtyi
qjsjwjuf
cvkuyeit
qvlmnzih
distpoga
dtlpvlub
fszspsdu
zkpxuozx
yumhqgty
wetfiqij
ozpmcegi
ylpbjbru
rqksydxz
ifayduog
xqlhyrhl
wrolqshx
cliyrafn
jtuerdyy
damyknzr
olbtisgv
sdlvkpjg
tvfvrshv
ugywkitq
idjjqpzc
eeowwemi
npplofdm
ouzjrlph
foawnibc
xcdcepzd
irqsuacz
xtnmuzqp
sgsxsjoj
qhkpbuvq
tsvwtvtz
lgqaycod
adttxkwp
kjcyqgoc
bfkxbgxq
iiszhwbf
cgnihihb
gsgvjypz
lgcgjccw
rdkltabk
wnymgwbv
jdfqdvis
yxtuyupx
nsvafgfo
ztmbgjux
axugvumx
tstqlnye
eeyqirow
ovaityku
cdqyjdkz
vuhkumlu
rwebkmlj
prncgnbt
ftuhvnow
lhmnkhmy
unyaizoz
ezshlifw
bllzrnar
uxblibez
fpkclnns
zqocayvl
umoistgi
skmgbxls
jgtlmsux
nulmpeow
rxeyoiwy
xpqouwhq
ogepecdf
paeqseqk
auntemaj
kyorwfkl
tnvbjicg
xazuvzok
noiksasa
tvgkzpcl
jqzwlyvl
zcbzkese
notfmgol
vceqbfbg
qfeabvhv
hejfluqw
yoxvxdes
pbgiqytr
tntrwezn
duadnppa
nqnwslev
okmdpmyr
eljfthrk
fymbhtes
cdyjpcnd
qmaihzyz
cifmitdm
ksjznrxd
jdcmoqpo
caicyvmw
zhgsnmcv
idxndssh
ppykgzto
hvkjejgz
dezkqhas
ddfpqxfu
zabdhasf
qkhgknfl
gqrzmfdv
lnzrgbwm
wrytspbl
bsjzukak
kfpcoyua
zzbpiifh
ygrhxtug
zedbugkr
sienwiyq
vpophmnv
kvrgegtp
azpkkojs
jgwlwtjo
azwbmxgy
wblpgwvu
jwkustki
fmjixbct
ghkclypp
erczaojx
iqmhmlkf
yfqnajza
vhpadprc
hjicylfh
mwbavklg
txhtbhbm
pufqjjei
zazwoxia
yhzexooi
vuqtvkuv
mppianmz
tscbvqrg
hajzaamg
urqizitm
ircgrvlo
jgzcpbjo
erpiqxlw
xvnqbjqc
xauztetw
bcytezdp
sqwrbgjb
tinldoyz
rdkbfbew
kkpmcqid
fjiztfcy
ybdoeafy
burdrehw
uyredvvm
bwvobekv
fniozvjr
ifaoxink
zaoujdun
bykdovxw
wasdjrzy
uxokzwlb
votizlio
leoxtnlc
ymcesetp
mibahaht
ldgfbbar
aaegvpyn
etgdecrd
cbqerkil
myldihga
aycsmksz
sbdprnva
ytlllxsq
shxuxktj
otxymese
hygjpofa
lozdcvfn
ulrvezsj
elflfepx
xtyqbbaz
wombapna
uesqfrfo
amagopph
tdipmqwo
qlfhnwxp
qycwncct
haofnvsq
bwiyooof
fdftgidb
xzntthfa
ouzddcqt
fywssrae
ywmmvhut
gphtugjk
qxfymjuh
dbnxhxac
mvwunqfa
tfrrjcnr
lycvubak
pfxofasn
xiacctnn
vrlncgrn
wjkeqsav
vskxlpkf
iaknsppj
kzexhdzd
jesglqmn
lkqtzgzd
wnwksqbf
htqrcgyq
jjynwudx
lawnwevw
cfewlcwu
ledcrfvq
zlfpilwv
jckvhaly
xhggozqd
hrnuxzwq
ajominjf
bkoaxnil
zcjslwqq
vgexcqtl
ddfannml
ufbfceuh
vuibklnx
tmrtgqxx
izxwfael
njtzahxu
bzwyyycr
ggxoqbvo
oysvzvoi
ejxxjhjl
unwkfzyr
nwycafcu
lfqieudu
natvibge
qzrnpxew
mqjbtpmh
ixdsjywf
nmilafsn
tfwubeot
ccmrtlfs
uajfiusi
jhinkyxm
qwcvvimb
wlbhjanf
vdcedtkw
uiibfsbh
hkgxmybs
lsqlrxll
ihvodcrb
ewrfalkm
kelnqkcd
vroxnjwh
jeneowpg
ozivuper
fxatuncj
dchmobvr
oyxqiszo
uuyxgshp
sxcbjmhu
dorsqxgt
urygoghb
lolotlqh
ytaalnkv
bcspchnq
wbdululm
vzqwkjix
hinyyoag
qkyqkdit
lolhbfkp
zlwjxdoa
yudtkctc
xcvazkiu
ttvfuzxr
rqfrdkcm
rihwltdh
qcpjwsjz
bazpmmmx
grxiwhag
cbljykhx
weooldcv
lumfsfwj
kiunrfgy
fafbvyjx
acpzgmgh
pdyhmtvq
ssismufm
pdlzydrn
sxxbtkqi
gnuxwgui
wcuguqju
jkjkdkph
prpmfknq
csuabssx
khymlrkm
muavohgo
sqgzadar
svzwomsw
zfscsyyh
rhuwuqij
otxcyjya
ftecgqvj
nbdrbipz
sppapkeb
xxysrbxg
pkvvzfwx
mpadytha
iqbdgpwm
aqisvbnk
ipckdhwl
rkivzxzk
tkiykice
jmpfxvqq
shrwhvwl
uxlgxmgf
nhjjylml
ujvjqgao
yekgzrqv
ujbnxfya
pmtovthi
hsazctam
hhmesojw
vgxomjtg
ucudhxze
kzgkdvlj
vtjkjgrj
fticzjct
dwulyubi
fyfiwbkt
orcuggcq
kvxqcwfz
vvjeoumv
xsyobzop
iszghxbl
kxxvtiuf
klwsferz
emzmpfvt
gnsxgbib
nnrmtcdj
qqnfngkm
lkdxvyxe
vkeaswre
kfvpnnpd
mozumbpg
omwjojxc
sjmkijsk
fivvusjy
esmktnbm
mbkizlzq
mscagsvf
twpwpsbj
okwrcirc
hcexoyjh
tzhxxmkr
zfhzgnoe
soldpmdf
ejikyuba
cudjzzmg
xfwpcilo
vpjqpuyk
oprtpooj
djzadomw
shuqtulp
rlspstxi
gxbfmsqv
qoojsatd
rvupwphy
zfgqbrwb
ninnufxt
annvdtct
phwyfyjt
qxwfsujq
bwrbuwxs
ihwlqjbr
zylvjunv
bmmsjzxk
rvfidswe
fjgovnmk
mogllpfx
ddsefzqd
wrssovrq
yaqhesmy
cvvcswup
kpmipygw
xrjtbhze
nqucxgea
kpbbhdhz
fhdsgcdm
pmjidvmk
szbhczpa
tchjtqzu
qzorzcpu
mfnvijyy
wuutyddc
ysupoemc
dunwqmbn
mocewxzi
qiwracmo
rmbbhvud
cltnmdiy
ruutdaeo
wihpnryn
mgajpkys
iahfwmuw
vuocxwiu
mbygminp
kmkjaead
hxnztxbh
flnxmtbj
nkbrfcqg
blkvlojl
ppdielzk
ssclzhip
qvvymayo
cthwrgfx
rjqdlnep
hccjexgw
cbclqcga
cxjjdgvu
puthjawq
gvvzvjac
wtxxtwef
retdqdpn
hifhvrbd
jctkaclz
bftzisge
wofmrtss
fvojyyar
cbnhtlqp
jqozxhny
ybgsemfv
ooaqxove
gqvrbkqy
ppdcrmte
clfxucnu
toenbwtd
jzmywsup
inqsaqid
aehpaztz
gragbfrw
dlrjyzmu
sblqqwsb
gzruigwt
aplpzlui
wmrpyrjm
xyxwaeog
bhkpwzvo
egdpnujd
hbbdjlws
mbphcthb
bykhifcd
rrwkidpm
iztrhfnf
nydlpqze
dgulsfzt
eludirwj
iyvbrttp
aerocrzf
ejaearsc
dxruknqe
zmhbnkls
qnsykqvu
gotmslog
nbprjbxc
gtlykrzb
egethaib
flomperi
xcamglue
zceleqek
cnvgfdwf
dchfyogi
ygtzquvk
xxxunqji
amqehkhx
lsacrdtm
ybnapfyu
aiukmmqc
pepgjpqa
uermcxac
kapeodph
ozdanagr
pdjfzxdb
ioospvis
uhxuoyrd
jnnlwvdv
gnxaqkly
zsiucnpt
gtveajfy
tudfnxqg
pwugrcdu
obeeyadl
yhybzygs
enbwkfwn
iiziwmrj
rmldlsrp
wfqifmcn
aehofonk
bvxavoez
fwelvohr
eviaivqh
yjwslphn
wjdocdoc
dqgiuhli
geinepsk
npaemvap
ngnqfbvw
pobgwlhb
zufxdrkb
ggfdeuts
defhitoc
ndzvtils
oysmqhnq
tdmsbwqi
wwfvshad
btkerpuz
gwqvhvto
nflozwyk
tbiexdrg
okshetxm
mbgrhojh
eluzaxsb
hwqtiqwr
yrsddclj
wrsfnbdb
klfmnoqq
ztmkgmgg
xnkrekxs
qmdwfeuo
jwzfwhkv
nxjlnbiy
vdhnrrxi
smgjcxcp
aphleuvc
ljbadhdn
jkbnkinm
mjtovsxa
xpjsorxu
gicuerdc
azrhkarl
hpgwlzge
bweruitv
vnoglwep
pjwqtqdb
myvyrjye
xiqzlwfn
zqpnhjnn
hkzycpkb
fmoryqng
dfembrgo
dvguwian
rwgwffsn
ixgfpslt
rkxnxyff
ljankcms
kksozyit
cncygufc
agsevmlz
ectijrxs
rhvtaplx
hxddxhda
mpvfoaim
rtxkcevq
qythgaev
lnhqdrzc
"

# COMMAND ----------

input <- "eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
"

# COMMAND ----------

answer <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  bind_cols() %>%
  t() %>%
  apply(MARGIN = 2, FUN = function(x) {
    table(x) %>%
      sort(decreasing = TRUE) %>%
      names() %>%
      first()
  }) %>%
  str_c(collapse = "")
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Of course, that <em>would</em> be the message - if you hadn't agreed to use a <em>modified repetition code</em> instead.</p>
# MAGIC <p>In this <span title="*Please* don't try this at home.">modified code</span>, the sender instead transmits what looks like random data, but for each character, the character they actually want to send is <em>slightly less likely</em> than the others. Even after signal-jamming noise, you can look at the letter distributions in each column and choose the <em>least common</em> letter to reconstruct the original message.</p>
# MAGIC <p>In the above example, the least common character in the first column is <code>a</code>; in the second, <code>d</code>, and so on. Repeating this process for the remaining characters produces the original message, <code>advent</code>.</p>
# MAGIC <p>Given the recording in your puzzle input and this new decoding methodology, <em>what is the original message</em> that Santa is trying to send?</p>
# MAGIC </article>

# COMMAND ----------

answer <-
  input %>%
  read_lines() %>%
  str_split("") %>%
  bind_cols() %>%
  t() %>%
  apply(MARGIN = 2, FUN = function(x) {
    table(x) %>%
      sort(decreasing = TRUE) %>%
      names() %>%
      last()
  }) %>%
  str_c(collapse = "")
answer
