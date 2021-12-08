# Databricks notebook source
# MAGIC %md <article class="day-desc"><h2>--- Day 8: Seven Segment Search ---</h2><p>You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.</p>
# MAGIC <p>As your submarine slowly makes its way through the cave system, you notice that the four-digit <a href="https://en.wikipedia.org/wiki/Seven-segment_display" target="_blank">seven-segment displays</a> in your submarine are malfunctioning; <span title="Yes, just the four-digit seven-segment ones. Whole batch must have been faulty.">they must have been damaged</span> during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.</p>
# MAGIC <p>Each digit of a seven-segment display is rendered by turning on or off any of seven segments named <code>a</code> through <code>g</code>:</p>
# MAGIC <pre><code>  0:      1:      2:      3:      4:
# MAGIC  <em>aaaa</em>    ....    <em>aaaa    aaaa</em>    ....
# MAGIC <em>b    c</em>  .    <em>c</em>  .    <em>c</em>  .    <em>c  b    c</em>
# MAGIC <em>b    c</em>  .    <em>c</em>  .    <em>c</em>  .    <em>c  b    c</em>
# MAGIC  ....    ....    <em>dddd    dddd    dddd</em>
# MAGIC <em>e    f</em>  .    <em>f  e</em>    .  .    <em>f</em>  .    <em>f</em>
# MAGIC <em>e    f</em>  .    <em>f  e</em>    .  .    <em>f</em>  .    <em>f</em>
# MAGIC  <em>gggg</em>    ....    <em>gggg    gggg</em>    ....
# MAGIC 
# MAGIC   5:      6:      7:      8:      9:
# MAGIC  <em>aaaa    aaaa    aaaa    aaaa    aaaa</em>
# MAGIC <em>b</em>    .  <em>b</em>    .  .    <em>c  b    c  b    c</em>
# MAGIC <em>b</em>    .  <em>b</em>    .  .    <em>c  b    c  b    c</em>
# MAGIC  <em>dddd    dddd</em>    ....    <em>dddd    dddd</em>
# MAGIC .    <em>f  e    f</em>  .    <em>f  e    f</em>  .    <em>f</em>
# MAGIC .    <em>f  e    f</em>  .    <em>f  e    f</em>  .    <em>f</em>
# MAGIC  <em>gggg    gggg</em>    ....    <em>gggg    gggg</em>
# MAGIC </code></pre>
# MAGIC <p>So, to render a <code>1</code>, only segments <code>c</code> and <code>f</code> would be turned on; the rest would be off. To render a <code>7</code>, only segments <code>a</code>, <code>c</code>, and <code>f</code> would be turned on.</p>
# MAGIC <p>The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires <code>a</code> through <code>g</code>, but those wires are connected to segments <em>randomly</em>. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits <em>within</em> a display use the same connections, though.)</p>
# MAGIC <p>So, you might know that only signal wires <code>b</code> and <code>g</code> are turned on, but that doesn't mean <em>segments</em> <code>b</code> and <code>g</code> are turned on: the only digit that uses two segments is <code>1</code>, so it must mean segments <code>c</code> and <code>f</code> are meant to be on. With just that information, you still can't tell which wire (<code>b</code>/<code>g</code>) goes to which segment (<code>c</code>/<code>f</code>). For that, you'll need to collect more information.</p>
# MAGIC <p>For each display, you watch the changing signals for a while, make a note of <em>all ten unique signal patterns</em> you see, and then write down a single <em>four digit output value</em> (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.</p>
# MAGIC <p>For example, here is what you might see in a single entry in your notes:</p>
# MAGIC <pre><code>acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# MAGIC cdfeb fcadb cdfeb cdbaf</code></pre>
# MAGIC <p>(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)</p>
# MAGIC <p>Each entry consists of ten <em>unique signal patterns</em>, a <code>|</code> delimiter, and finally the <em>four digit output value</em>. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because <code>7</code> is the only digit that uses three segments, <code>dab</code> in the above example means that to render a <code>7</code>, signal lines <code>d</code>, <code>a</code>, and <code>b</code> are on. Because <code>4</code> is the only digit that uses four segments, <code>eafb</code> means that to render a <code>4</code>, signal lines <code>e</code>, <code>a</code>, <code>f</code>, and <code>b</code> are on.</p>
# MAGIC <p>Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (<code>cdfeb fcadb cdfeb cdbaf</code>) use five segments and are more difficult to deduce.</p>
# MAGIC <p>For now, <em>focus on the easy digits</em>. Consider this larger example:</p>
# MAGIC <pre><code>be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
# MAGIC <em>fdgacbe</em> cefdb cefbgd <em>gcbe</em>
# MAGIC edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
# MAGIC fcgedb <em>cgb</em> <em>dgebacf</em> <em>gc</em>
# MAGIC fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
# MAGIC <em>cg</em> <em>cg</em> fdcagb <em>cbg</em>
# MAGIC fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
# MAGIC efabcd cedba gadfec <em>cb</em>
# MAGIC aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
# MAGIC <em>gecf</em> <em>egdcabf</em> <em>bgf</em> bfgea
# MAGIC fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
# MAGIC <em>gebdcfa</em> <em>ecba</em> <em>ca</em> <em>fadegcb</em>
# MAGIC dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
# MAGIC <em>cefg</em> dcbef <em>fcge</em> <em>gbcadfe</em>
# MAGIC bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
# MAGIC <em>ed</em> bcgafe cdgba cbgef
# MAGIC egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
# MAGIC <em>gbdfcae</em> <em>bgc</em> <em>cg</em> <em>cgb</em>
# MAGIC gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
# MAGIC <em>fgae</em> cfgab <em>fg</em> bagce
# MAGIC </code></pre>
# MAGIC <p>Because the digits <code>1</code>, <code>4</code>, <code>7</code>, and <code>8</code> each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting <em>only digits in the output values</em> (the part after <code>|</code> on each line), in the above example, there are <code><em>26</em></code> instances of digits that use a unique number of segments (highlighted above).</p>
# MAGIC <p><em>In the output values, how many times do digits <code>1</code>, <code>4</code>, <code>7</code>, or <code>8</code> appear?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''cgaed gcdbfa gcfaed gfcde gadfceb cdbfeg acg eacf eabgd ca | agc efcgbd cag eacf
ga ega edgfa cafed gabd cefagdb begfad ebdgf fcbega cbgdfe | bgdef fdgeb dgabfe gea
ged eg acfgd fdceb cdbefa dgcfe cebfdg edcbga egbf ceadfbg | dfcge dacegbf gcdbaef fdceg
cbefg fedbcg bfdg abgedc fgced edcagf caefb gb fedcbga beg | bdfg cbeaf cfdebg gbe
gecdab gbafd geabdcf ecfa dbcfge cfb afgbc efgbac cf cgbae | fbc fbc cfebgad cf
cbdef febdga fba ba fadecb cgfea adbc cbafe fbedcag egcfbd | dfgbae fdcageb adcefbg efbdc
gecdba ecafbg ecabg bgacfd gecaf feba aedbfgc fca gdfec af | fac af cfa eafbgc
geab adgfc gacef acgefdb gecfba eg dbfgec beacf afedbc ecg | baeg fgadc fagbce edfgbca
gebcfad dafceg gdcaf bdfgea ab befgc gfbca bdca gab dgabcf | bga fgceb bag gfeabd
efgcdb egd gceaf dabgcf ed acegd gdbaefc dabe dgacb adcebg | afecg ed de egcfabd
eb efb eafgbd bgce adcfe fbcgd fgdbac bdefcg fcdbe fcebadg | ecgb bcdagef bcge egfcbad
cafgbde aced gfdaec defgbc ce gec gfdca bfgacd afgeb cegaf | cafegdb efabg cfbged eafgdcb
gcedba dgbe eba ecadgf bcfda bfegca eb gfecadb abcde egcad | eb be bea aeb
fgcd bcf edfbg dbgeafc fc efdbc fcdbeg beacd adgebf aebfcg | cf dgcf cf dceab
decag bade ad gda gadceb fgcbae adfgcb dfecg gceab edfgcab | adg gbcae gda da
adbgfe fd dbgf gdeaf agfeb agcde gedabcf afcedb gbceaf daf | afdeg bagefc afd bagfecd
cgeabfd efbgac dgcfba gbfd dcageb dga gd bgcaf fgadc aecfd | fbdg agd fgcbade gdfb
efdgc gfdb cegbfd bdefcga bcgef bacdge eafcd afgecb cdg dg | gd dgfce dg dcg
edgabc cgaf gdbfa cafdgeb dbfacg gdc adfebg fgbcd gc bcdef | bgacfd cdg ebfdc cafg
bcdfage ebgdac dcb adce cd acdgb bcfedg gbace dbfag fgceab | dcebfga caed eacd bgceda
fd gafcdb feadcgb dacefb gdfab fagcbe gcdf bdf edagb gacfb | dfb gcfabe bgdaf bfd
daefcb cg gfdea ceg ecfabg beafc gecdafb eafcg bcfg abdcge | gec egafc eabcf edbgac
degafbc fgeac gb acbeg bcead dcafge bcfg gbe bcgefa edafgb | fbaecgd bcgf beg bg
adeg ga agfcbde gadefc fbcged acg gefdc gcbeaf acdbf acgfd | cebgfda cag cfegab gac
bfegda eag dbcafg gfedabc fegcab afgbd ae faed dbaeg bdecg | fadgcb afed bgadcfe ecgabfd
bcdga bgd cdfag dbaec dcfgeab cadfeg gb cdgbfa fdcebg gbfa | bdg bg adcefbg efagbcd
acfgbed eagdcf cgdb db gdcbfa acbdf cbefa gadfc gbadfe bfd | bfd acfbd db gfdeac
agbed geaf cfbgaed dae ae deafcb fbcdeg dgefb dgcab fbegad | defabg cbdafeg febdcga acbgd
bcade fdecba bgceaf acg ecdfg adbg cgfdbae bcgead ga eacgd | cga afdceb cdgbea ga
agcefb cbfdaeg fabce eg dcgfb bcadfe gace bedagf gbefc beg | fegabd ceag ge dbeafc
efbgc ebgfa dacegfb daegf bcfgea dbcgef abfc agbecd ba bag | ab ab dcegbf cbaf
aebf fed fdbacg fe gdeacf egdfb ecgfabd gcdbe fbaedg fabdg | def aebf fe ef
adf cgabfd daegf af edfgc egbcfad gcbdae ebaf gbeda faedgb | feba eafb feba abgcdf
gab gcfb cgbdae defab afbdg acefdg bfgdac bg eafcbdg cagfd | bfgc fdbgeac cbaegd cfbg
eagfbd fcbgd baceg dba bcdgfe facgbd da dafc cgafedb bcdga | fdca afdc cbfegd gebfdac
feacgb gbfac dag dbac cdfgea gfebacd gfdeb gdfba da dfgcab | dga aedgfbc ad cdba
cfdabg ecag ecgadb eg ebg faebd dgbea dacfegb gbdca bgfecd | dgcefb baedg ecbafdg bge
bfdec fgdbce debga adecfb fa face dgfabec bfdae gacbfd bfa | afec af fa cfea
fcbad ecd fbagecd deabg gaedbc fgbdae ec adbce aecg ebfcdg | ec gcea ced ec
dg efbcgd cfdbaeg cfdga adeg bagcfe caefgd gdf feacg cdfab | gaedcbf abcfd dg dfegca
fdgbe gbc egfcdb cbdeg dcbf ecgad bc gcbafe beadfg bgdface | bfcd bfdc gcebfda bc
gace gcefb cgdebf ac cfa fbeac fgcdeba ebafd bagcdf gfacbe | ac feacdgb bcfea gafbdce
fcbega dfgcab gacbedf fgeca cbeg gc fegdba gac ecfda egabf | cbge ebgc gdebacf gc
cbga bdceaf bgfdec ba efgab aeb efcbga gdaef egbcf abgcdef | bacfde cgafbe dbcgaef fcgebda
fdcba bgfcd fdbaecg fcgaeb cegd bfgdae dgefb dfcgeb gc gbc | degc cgb cegd gdbaefc
caedgf bge dacbg be dbfecag cgbefa eagfc ebaf ecbag fdcbeg | beg eb agceb egfdac
dacgbef gebdfa bdcfga cgd adfgec cd cdba cdfbg ebcgf fdgab | defcga bcda acbd bgefc
fdgac cebf baedc dceaf adfcbe bfedga edgcba fe fed edabfgc | adcfg dagefbc egbcda fdceba
dagfbc fceabd fgbc edbcafg bdf bf bdgae afgcd fbdga gaefdc | gdcbfa bf bf fbcg
dgfcb abdfe fgadbc cfbgae gadfb afg cdgbefa cagd fcgdbe ag | gaf dabegfc fadgb ebacdfg
gbedc faced dfb fbegadc fcdbe fcdgab bf bdafce beaf edfacg | bf fb bf dfb
aegcfb dacgbfe fc ebcag acgebd acef cfbag cgf cbedfg fagdb | acgeb cbega bfdcgea debfgac
dgcfabe bgad eab agedc befcg cbaegd cefabd gaecb dceagf ab | bagd agdfce bea ba
fgbde fgba efb bf fcdgae afdeg afbecd becgd efdcbga dfegab | bgaf fb bf gefad
fb acgefb egafd baf adefb dcageb bdafce aefgdcb decab cbdf | dfcb afb fb begfadc
edcaf dgabfe ceb bgdc cb gaefcb fdgceb ecdfgba begdf bdcfe | cb gfdceab dbcfe bc
gedfcba bcdaeg dgae gca gdcbe afbdgc gfdcbe agcbe eafcb ag | gcbeafd agc bdegafc daebcg
aebcfg fagdc fcgea fgdebca ecabf ge feg bcge fgadeb cdebaf | fgeca ecgb eg gcafedb
aegcf becgdaf cbfag bafcd gcb cfgbde abdfce acdgfb bg dgba | egfcabd gb abdg gfcae
egcab adfegb gc febgac dbcea fgce bgafcde cdgbaf fbgea cgb | fgce bgc gc cg
cabfe dfa agdec df aecdfb cfbadg fagceb befd cfade dbaefgc | bcfgad faebcg df df
gcab fbeadcg badcf ag fgaced gfabdc dgbfa fag bgfed afdbec | fabcd cdbfgea cgefdba gaf
ae bdefac dacbf ecabd afdecgb feacbg eba aedf bcgde dfgcab | bae edaf ae ea
fdgba bdgeca cgb fdgec gbcadef dgabef bcagdf bc fbac gbcfd | cbg bc cfbgd dfcagb
afdgbce geac egfdca acbedf fgdce faced eg efg dgbaef bdcgf | dcfbeag afbegcd ge cega
daf fdaeb df dbfg dbeca egfab cegabf cfeadg cbdaefg dfbaeg | fda agfbe dfgb afd
gdcabe bfc dgbefca fc aebgc dcabfe efbgac fbcga agbfd efgc | bacdeg bfc cf bcgdeaf
cf fgdbe deacfg dbcea efdcb bfcg fdebcg fdc befdag gebdfca | cf cgbf fdegabc defbgac
gdfba fceadg cb fbcgd cgeb cdefg cdb bdfcae fgdcbe gbedfca | dbc cb fgbdc dfcagbe
dbgcaef dbfc eafgb fd dgbaec bcdag daf dfcaeg bdgfa bfcagd | adf fd df cdaefg
cd cfedb cgadebf efbgc abdfec edfab cadefg abcd dcf gbeadf | dc debcf fdc fbagcde
cgdfbae fe gecfd defb adcgeb caefgb fge dcgeb cgedfb cdfga | fe fge befgac fedb
egadb bdfge gcebdf ga cfdgabe edabc gdfa beafgd abg bacgef | fdga fbcdeg fedagbc bag
gbdea bfaeg fba gabcdf gadbec bf dbef egabdfc cfeag dfbgea | fb bacegfd dfeb bf
ebdac becfda bd bedfga edgcafb bed aecdg ebafcg dbcf abfec | cdfeab dbe cdfb ecabfd
gfbac dcage dfgace abgfed fgcdaeb fd agcebd defc gafdc gdf | ebdagfc gdf cdef dfg
bcfdeg dgceaf cea fecgb cbafe ea geab adcfb bdfgcae gcefab | egbcfa geba gdecaf caebf
gd agebc fgcd dbg fdgecb egfbda fbdgaec fcdeab bfdce bcdeg | caefdbg cagfebd debcfga cdgf
edc acged fcea ce dgecaf ebgdfc bcafgd fdcga acbgedf aegbd | gbfadce gbdefc ce afec
gfebd agbcfd acdbf caefdb abgefc gbfadce abe eacd ae dafeb | ae dbcfgea ea edac
aebcf dea gdacfe gfad adcgbfe caedf gbdeca ad dgcbef cfdeg | ade fdecga ad eda
eabgcd gdaeb faebgcd gaedf fdcbea efd ef efgb fgcad daefgb | gfbedac fecabgd fceabd dbfaec
cbeaf bafceg bfeg bcf bdcfag cdeaf fb edbcag bgeac cbgefad | abceg fb ebdafgc bf
ced aecgfdb fdecgb gcefa agde ed efdca abfcd begafc agdfce | gead bdacf abfdegc decfa
cda gdcaeb cadfe ebcagf cbefa dfabce gfdae cdfb cadgebf cd | dca cd bfdace aefdg
gacfbde bg degcaf gfbce aefgcb cbdef egcfa acgb bge gfaedb | cagebdf dfaegc ebgfac bagc
aefcd dfgea dfc cf fedcga cbdea adgefb adbgcf gecf gcbefad | cf dfagec fdc edfcbag
gefbd adgf eafdb gd gecfb fedgba bgd acbfde cdfageb adgbec | fbdgaec dg gdb aecbdfg
cdfabe cfga cg dcefa gce eagbd agced fcdeag gcefbd bdaefcg | gaedfc ecadgf gcfa dbega
dgcea cfgebda dagb fgcaed bcg bg bcaef cedabg bcaeg cegfdb | cgbade bfdecag aedgc gfcbdae
dbcfg cdfeg dbf befagc debfac agbd dgbcfa dbfgace db facgb | bd fbd bd bd
dbefga efcadb cgdab cdbfa gad fdcbgea gbaec dg fcdg acfdgb | dg dgcba fgcd dg
ebag gbafed fbdgac eb bdfag bef dfbge abegdcf fedcg acbdef | fgbade gabe edgbf fgcbdea
deg bcgfad efdagb fedagcb eg ebcg cdafe decfg dgcfb dfcbge | cdbgf cgfedba bcge eagbdf
egbdc efbgdc aec bagfecd eagcbd gbface ae adbe fadcg gcead | eac eca egbadc eac
acedb fdcgea degabf ebcafd eb fceb agdbfec deb cgbad feacd | eb edb agbcdef cdabe
gcdbfae eadb feacg ad dbcef dac bcedgf dbacgf cfdea bdafce | fdcbe dca fdebc caefg
edfba cedf cebad ecdfab decabgf acgbe cgabfd ebgdfa adc dc | cad adc baecdf efabd
caeg dbefg egdba afgbcd fbdcea cdgafeb ag agb bdecga adecb | ga gdaefbc ag dbeacg
bf bagdcf gbfa dgaecf gdfcb fdgbcae fdb bfcdea gcebd cdfga | febcda bagf fb fgba
cgbdef begfa agebd bdac da bgeacd ecdgb aed defacg cdbgfea | cbgdef da dbca ad
aebfdg aegbdcf cdebg ebgcdf ef cbef dgbcae gfe gfcda gfedc | gcdbe fge efcdgba fe
befad bcdf fce bgcaefd gaefdb dacfe cbefag gaecd caefbd cf | fce fc fdbc fc
gecab gfeca eafdbcg bgcdae fdcgeb gbc dceafb gb dabg abedc | agbd gafce gcaeb cdbgea
deabf dfg fcedgba bfgc fg cbdeag fedcga fbcadg cbgda afdbg | gbcf bgcad gdbca cgfb
bcafgd gefba acg abec decgf gbacef ca gafdbe cafeg bgecafd | afgec fgecdba gbadfc bgcadfe
febcgda ebga dgbecf efadbg ceafd eb edb bdgfac fbade fgabd | fdgba edb egab fdbga
dgb dbce faebcg bd gfbdac fecgb gbfcade bdgef bgfdce edgaf | bd db dbg bcdgefa
fdaeg afebgc dcf gcafbed cbfge dc dbcg bcfegd cbdefa edgcf | bcafge bagcfe agedf bgdc
cgfb bacgdfe bdfeg fdebcg cb cdb edgfab edfca becdf gebacd | cdefb acdegb bc afdbeg
gbdcaf gfbad gfdabce abfdce debagf gcfad ac gfced fca agbc | fca agcb egfdab gdcabf
cedbagf edagc bge bcdge gbad gb bgefac aecfgd bdfec cegdba | gbefadc febgadc ebg cagde
dfecga cdagbfe aegcd cdfg fegab bcfaed egafc cbegda fc fac | cdfg gdfbcae caf fc
gecdf agdfe dga cfda cegbda bafeg ad caefgd dfagceb bfgdec | dag gefdca cdfbgea afbgdec
deabf gdea bcaedf agdfeb dfg gd dcfabeg ecfbg edbfg bgdfac | gdf ecfgabd badgfc fgd
gfabc gafce adeg bgdfce dabgefc eacdfg ea dfcge ebcafd afe | agcedf fcgedb fcdaeb becgfd
dcbgeaf dbafec cafde beagdc gd dafg cfbge dge fegcda fgedc | dagf dgefc gd agdf
egcbdf dafe dfbge adbgefc eadbg egabc gcfdba abgedf dba ad | begdf efabcgd eafd edaf
cegd bcfde gfbcdea efdab dbcfg cef efbcdg ce abcfgd aecfbg | bedfc bfeda egcd dbefa
abdceg acedg efbcg ab bcad gcabe bdfage afdgce agebdcf gba | gadbcfe gbeac bdgeacf fbgec
dfba fcebad afgebc dbcea fcgdaeb befcd ebf gcdef fb eabgdc | bf efb bef agbfec
cfgde geadb fgdbec gfcb fbd bcfade egdbf adcefg bedcagf bf | bf fcbg bdf gdcefba
edf fgdbce agcfbe efbdga dafge beda de cbgfeda cdagf gafbe | ed gfead fed gcafd
ebdg fcbedg cdbagf de fbedca fecag daegfcb cbgfd cedfg dec | fbedcg cde ecd bgefacd
fbecgd gefca bcefa fgbeda deabgcf gc adgef cgad gfc gcefad | gc gc cfdega fcg
cgefab afb abgfde gadfcbe fbgced dcbga fa gebdf gfbda efad | cegbfa fbegda edgbf baf
dcbfg adce cegbd ed egcdbfa befagd bgace bcfaeg bdacge egd | fgdbeac geabdc begcadf acgefbd
ebgfac dabcfe fea bdafcg ea defbg aecg fcagb cafebgd abfge | gcfab gbfea afe efa
fdb beadfc decgb fd acdf dafbegc cfbed fcbaeg cabfe agfbde | fdb dcegb eabcf efcgdba
cbad dae dcbge feabg da gcbdef gaedb dbcegaf edagbc dgecfa | ade ade da adcb
fbe dcbefg fe adfbce gebdacf fbadcg baceg bdacf fead fceab | debfgc ef ef bcaeg
ab cbgdfae cbdagf dceabg ebad bag gdbce edfbcg cefga ebcag | dabe ba fagdebc gcbde
cdagbf fcadbe gac acgbd bgcde cgbafe eabgcfd ga adgf cbafd | ag agfd adfg cbgafd
edca eagcfbd dbgae dge ed bgcad bdcfga fagbe gbcaed gebdfc | cead gde deg fcdgbe
edb abfgecd edgf fgaeb bdage cadgb fdcbea de fbedga abfceg | eadfcb bedgcfa bed dbe
faedgbc cfebad dbecf afeb ab afdcg dba adbfc aedgcb ebfcgd | dab fcgad dbgefca dcfga
aedc dagbcf afbdce gfbed cd efbac acefgb dcefgba cfebd dcf | fbcagde eadbfcg cd bedfg
agedbc egdcb eb bgea bedfac dbgca cgfde edgabfc cbe dbfcga | ecdgb fdcge bega dfebca
dfbeac gcdefa cf fbcea ebadf efc gdfaeb abgce ebfcdag fdcb | ecf bgeac fc fcbd
gacdef dbeaf dgaefb fc dcafgeb ebcdfa gbecd bcdfe cdf abfc | cdf fdc egfbdca cf
ecfdba be bgce fcedag abdfg gbfed acgdfbe cefdbg cefgd dbe | deb be dfbag cgeb
bfgac acbfgd fga dgbca gbaefd efgcb cdefbga dgeacb af fdca | fadcebg fa adfgbec fa
dbgeac gd decg dabegfc dbeacf eadcb fdbega adgbc gbfac dbg | cdeg dabgc ecdba agcdbe
daebg ecgfd cbfeadg eabf degcba fgbdca afg gfaedb gfaed af | dcabge baef agf feab
edcgab dfcbage bfga becgfa gca efdca gfbdec ga becgf fecga | ebagcf gfba bgaf ebfcgd
bdfeag dcbfeag eg cdge afbec gea ecgaf fgadbc fcgeda fgdac | eg eagfc cdeg egcd
gdbeacf dfcgba ebafd ag bgaecf bcfgd afg gdafb bedgfc dacg | dgac gdca gfa gefbca
afbedc bfd gdbce bedafg gdfeb bf eacbfgd gefad agdefc bgaf | feagd bafdge fbag bdcafe
cae becgad gdabe ac cagb cgafde ebdac fcbde abcdfge degbaf | dbefga adcbge dgfeba fegbdac
caedb adb ecfgdab gdaec gbdeca ab cgdefa fgdcab dcbef eagb | gfaedc ba ba bcgafd
dcefa gcd agdfc bgeadc dg fgceabd dfgaec dfeg gbcaf dbfeac | bcgead fgacebd gcbaed bagcf
adbgce cd cdeg adc bcedgaf fbeac bdace ebdga afbged cbdagf | dac gedc cda dc
ad dfbce cdabf fgbca edbcga fead ebdgcaf bgfedc dac bcfade | eafd ad fgcab fbaecd
bfgdae baegf cbfeagd ebdaf fedca dabg dbe efbcgd db abgfec | bdfeag egbaf db gbda
gcfea eafdb eabgcfd egafb gadfeb gb fdgb bdafec ebg egabdc | decabf acdgfbe dbfg bfgd
gebaf cedgbf acbeg cbagdfe fbe acbf gaefd gcbdae fb gecfba | agfdceb bf bfca acbf
cegabfd fc gaefbd cbdea fadec fecg afc gecadf cbgdaf dgefa | cfbgda fac dfeca abgdcef
ab gdfea egba afegdc fdbae cfedb bad aefdbcg dgfcab egdbaf | facgdb abfedgc ab ba
af fgbeadc ceadg cfeagb fgdbae efa egfad efgdb fdab begdfc | dbfeg fa af bafd
dfgecb cgabf cdaefbg adbcge dabeg bec ec aecbg febdag aced | aebgfcd fgedba aedcgb adecbgf
bcadef cbfgd dcagbf dfe febg befcgd degfc degac bfagced fe | fde efdbgca gcbfdae fgbe
fgd edfc fgedca gafdebc febga agedf eadcg gdebca dacbfg df | cdef dgeca bdcfga efdc
aedcfbg dfceba eb caegdb begca fbacg bea egdb ecagd dgcafe | eba gdeac abe bgde
cg fcdg deacbgf cdgbaf fbcea abfgd gac badceg facgb dbfage | dfcg fabedg gc cgebda
bdgae eg defba gcedab bgadc dbfcag egbc ged gafcde cfbagde | geafbdc bfead ged bgead
agefc cgdef cgfdea ca fcdabg fecdgba aedc bgfae fac dgcbfe | fgecd agefc gafdec ceafg
ca cagbfd efbdc fac afecd aebc cadbef gfaedbc dbgefc feagd | ac dfgcabe defbc cdafbg
cdb ecfab gbcaed cafdg gbfd db adbcf cdagef afgcdb cfdebga | db bcdgae dbc db
begfcd ag cgaebf gfbcdea bdgeaf gead bgadf agf fdgeb acdbf | gfbad ag fadcb ga
ad gbced dab bcfage adbge afegb fcagdeb fbdaeg dagf acbdfe | fadcgeb bedga gdfa gdbeaf
begfdc fgdcb fgadbe caebg cagfdb efg edcf ebcgf ef efbdgca | degafb gef fagbcd feg
ecfdg gfbed gdac acgbfe cdafe bafdgce gec dfecga cg afcdbe | cg gc abcdfge ceg
deabg gea egdfcab bgcda gbfe fdbgae efcdag fadbe eg efadcb | gafbcde ega gfeb dfgbcae
ef gecadb adbeg defbg fcbgd fgae feb efgabd bedfca facbdeg | efb bef ef agef
cefga cfd fcebdg ceagbd bfdg bfdeac gcbde gfdce agcdfbe fd | faedgcb fdc dcgfbe cdf
dfce cgbfa gbadef df bfd gaecdb ebdgcf cgbde gdcfb acgbdef | fbd fd cgfba fdb
dca da bdfgc cadbef ebfacdg eadb bfeac fdcgae bfcad fgecab | adeb abcfegd gbfcea ad
gcedaf gfdecb gb caefg cebga fgacbe fabg dcabe agbfced bcg | agfb begca dcgeabf bg
dbgac cdf fagde fedbacg fgdabc acdbge dfgca ecafdb gcbf fc | bcgf cfbg ebgcdaf bdagc
ed fedag dge gceaf dfabg dcfe afdegcb aebfgc dgbaec dagecf | acgefb de afdeg gcdeba
dca fcbdg fgecab ad adbcg debfgca ecbdag gceba facged edab | acefgb ad gfebdca fcdaegb
edaf gfeab ebfgda dfbga dacgb gfbceda bgeacf df gfd bcdgfe | df fdg aegfdb feabg
bcfagde dgabfc beafc geca fgcaeb fdbec ac fca gabfe gfdaeb | gcfbead fca gebfa caf
aecbg cfeagd cadfbe dgceb cgfae edacfgb fecbag ba abc gfba | ab bca bca fbag
bdc aebgc db cdgef dagb geabcf ebgacd gdebc aedcbf gadfbce | befacdg abgced dbc bdceg
egbacfd dabgfc beagfd ef dbef dgbaf fge gcfade cgbea eafbg | dgcafe befd feg fedb
faebd cbdaf edfgab fdcbeg dfgbe ae dagfce bedgafc ead beag | dea ae abcdfge fgedbac
gfabd fagcde cdbefa gaebdf ecfdbga gaefd fab aebg cgbfd ab | ebga fdbeagc fba gadfec
bfa cfga acbfe edcfbga fa fagebd bdcfe aecfgb ebdacg geacb | gfca bgace gafceb gcaf
dgbae dcfegb bgdfc fagbcd gca dafc ca dabgfce cgbda agbecf | cafd ac cag cga
fcag egdca gc agedb cgd adefc bcfged cbefad egcfad efcagdb | cg dcg cgd cgd
ea fdeacb eab bgdefc adgcefb bfdga face cbdfe bedaf dcgaeb | gcbfdae ecdgbfa bea bae
acbe ecd feacdb ec egafd eadcf cbdaf fgcdba cfbagde efcbgd | dgcabfe ce bgfedc egdbfac
cdageb badf gbfcad fcgab fgadebc gecfd bd eacfbg dbg bgfcd | febcdag bd fadb fdba
adgcbef bef cgedba fbecag efbca baegc bf gcdbfe bfga acefd | agfb bgfa gbaf bef
bcfade agcde acd edcbg feagcd gdaf dbeacgf ad eafcgb fcega | cad gdcefab dgaf ebdgfca
df abfce degbc cfd acgfed gbdf bacfegd efdcb badceg egfcbd | cebgd bgdf bceaf df
bfdc eabdf ebcad fgead bcdeag fba bf bcedgfa cdebfa bcegaf | defba cfbd bdcf fabceg
dbaefcg ec aec dfgbea cafeg aedcbg gacedf egadf gfcba cfde | eac efcd ec egcfda
ecgfdab gcefb bcfa af cgfdbe aegbf ebadg eacgfd gbecaf afg | aedbg bafc acfb dgfbace'''

# COMMAND ----------

import re

displ = [
    [
        [frozenset(s) for s in re.findall(r'[a-g]+', part)]
        for part in line.split(' | ')
    ]
    for line in inp.splitlines()
]

answer = sum(len(word) in [2, 4, 3, 7] for _, output in displ for word in output)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Through a little deduction, you should now be able to determine the remaining digits. Consider again the first example above:</p>
# MAGIC <pre><code>acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# MAGIC cdfeb fcadb cdfeb cdbaf</code></pre>
# MAGIC <p>After some careful analysis, the mapping between signal wires and segments only make sense in the following configuration:</p>
# MAGIC <pre><code> dddd
# MAGIC e    a
# MAGIC e    a
# MAGIC  ffff
# MAGIC g    b
# MAGIC g    b
# MAGIC  cccc
# MAGIC </code></pre>
# MAGIC <p>So, the unique signal patterns would correspond to the following digits:</p>
# MAGIC <ul>
# MAGIC <li><code>acedgfb</code>: <code>8</code></li>
# MAGIC <li><code>cdfbe</code>: <code>5</code></li>
# MAGIC <li><code>gcdfa</code>: <code>2</code></li>
# MAGIC <li><code>fbcad</code>: <code>3</code></li>
# MAGIC <li><code>dab</code>: <code>7</code></li>
# MAGIC <li><code>cefabd</code>: <code>9</code></li>
# MAGIC <li><code>cdfgeb</code>: <code>6</code></li>
# MAGIC <li><code>eafb</code>: <code>4</code></li>
# MAGIC <li><code>cagedb</code>: <code>0</code></li>
# MAGIC <li><code>ab</code>: <code>1</code></li>
# MAGIC </ul>
# MAGIC <p>Then, the four digits of the output value can be decoded:</p>
# MAGIC <ul>
# MAGIC <li><code>cdfeb</code>: <code><em>5</em></code></li>
# MAGIC <li><code>fcadb</code>: <code><em>3</em></code></li>
# MAGIC <li><code>cdfeb</code>: <code><em>5</em></code></li>
# MAGIC <li><code>cdbaf</code>: <code><em>3</em></code></li>
# MAGIC </ul>
# MAGIC <p>Therefore, the output value for this entry is <code><em>5353</em></code>.</p>
# MAGIC <p>Following this same process for each entry in the second, larger example above, the output value of each entry can be determined:</p>
# MAGIC <ul>
# MAGIC <li><code>fdgacbe cefdb cefbgd gcbe</code>: <code>8394</code></li>
# MAGIC <li><code>fcgedb cgb dgebacf gc</code>: <code>9781</code></li>
# MAGIC <li><code>cg cg fdcagb cbg</code>: <code>1197</code></li>
# MAGIC <li><code>efabcd cedba gadfec cb</code>: <code>9361</code></li>
# MAGIC <li><code>gecf egdcabf bgf bfgea</code>: <code>4873</code></li>
# MAGIC <li><code>gebdcfa ecba ca fadegcb</code>: <code>8418</code></li>
# MAGIC <li><code>cefg dcbef fcge gbcadfe</code>: <code>4548</code></li>
# MAGIC <li><code>ed bcgafe cdgba cbgef</code>: <code>1625</code></li>
# MAGIC <li><code>gbdfcae bgc cg cgb</code>: <code>8717</code></li>
# MAGIC <li><code>fgae cfgab fg bagce</code>: <code>4315</code></li>
# MAGIC </ul>
# MAGIC <p>Adding all of the output values in this larger example produces <code><em>61229</em></code>.</p>
# MAGIC <p>For each entry, determine all of the wire/segment connections and decode the four-digit output values. <em>What do you get if you add up all of the output values?</em></p>
# MAGIC </article>

# COMMAND ----------

import itertools

def map_segments(segments, mapping):
  return [frozenset(mapping[c] for c in s) for s in segments]

base_mapping = {
  frozenset('acedgfb'): 8,
  frozenset('cdfbe'): 5,
  frozenset('gcdfa'): 2,
  frozenset('fbcad'): 3,
  frozenset('dab'): 7,
  frozenset('cefabd'): 9,
  frozenset('cdfgeb'): 6,
  frozenset('eafb'): 4,
  frozenset('cagedb'): 0,
  frozenset('ab'): 1
}

output_total = 0
for segments_in, segments_out in displ:
  strings = set(segments_in + segments_out)
  
  for replacement_letters in itertools.permutations('abcdefg', 7):
    mapping = {k: v for k, v in zip('abcdefg', replacement_letters)}
    new_strings = map_segments(strings, mapping)
    
    if all(new_string in base_mapping for new_string in new_strings):
      new_output_strings = map_segments(segments_out, mapping)
      output_total += int(''.join(str(base_mapping[s]) for s in new_output_strings))
      break

answer = output_total
print(answer)
