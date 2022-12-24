# Databricks notebook source
# MAGIC %md https://adventofcode.com/2020/day/21

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 21: Allergen Assessment ---</h2><p>You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.</p>
# MAGIC <p>You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you <em>do</em> understand. You should be able to use this information to determine which ingredient contains which allergen and <span title="I actually considered doing this once. I do not recommend it.">work out which foods are safe</span> to take with you on your trip.</p>
# MAGIC <p>You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's <em>ingredients list</em> followed by some or all of the allergens the food contains.</p>
# MAGIC <p>Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. <em>Allergens aren't always marked</em>; when they're listed (as in <code>(contains nuts, shellfish)</code> after an ingredients list), the ingredient that contains each listed allergen will be <em>somewhere in the corresponding ingredients list</em>. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.</p>
# MAGIC <p>For example, consider the following list of foods:</p>
# MAGIC <pre><code>mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# MAGIC trh fvjkl sbzzf mxmxvkd (contains dairy)
# MAGIC sqjhc fvjkl (contains soy)
# MAGIC sqjhc mxmxvkd sbzzf (contains fish)
# MAGIC </code></pre>
# MAGIC <p>The first food in the list has four ingredients (written in a language you don't understand): <code>mxmxvkd</code>, <code>kfcds</code>, <code>sqjhc</code>, and <code>nhms</code>. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: <code>dairy</code> and <code>fish</code>.</p>
# MAGIC <p>The first step is to determine which ingredients <em>can't possibly</em> contain any of the allergens in any food in your list. In the above example, none of the ingredients <code>kfcds</code>, <code>nhms</code>, <code>sbzzf</code>, or <code>trh</code> can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces <em><code>5</code></em>: they all appear once each except <code>sbzzf</code>, which appears twice.</p>
# MAGIC <p>Determine which ingredients cannot possibly contain any of the allergens in your list. <em>How many times do any of those ingredients appear?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''blmpt vrcd sffksrkn bkgxfl kgkct dpvnsd xjjc hjc frtfg dbfxfjd svbmv gblgkb tqv zfhz rnkbccd qmrps smpg bnv rqksl fkn zxdmj xrdtpr fvrplq gxdrk qjjss lptpdd qnvx btf smgnpc zxvfb gntfcf ldbcvh srxgh bttv cjjmhlmm knfsd qtsgr lbcfst mmpmmh mhgxm sppx vvfjj ksqp rqsnq grlg qngpn hcjtjd rpk cljf qsjszn cpxmpc xbnk lchxqhn xbggv gqhkxn bbknm chcb mhnlcxv kcxrlp fvdnrd nqhln dhzkcf dlzrg cbqgz kgjm rbld lnblbr tvcvnj (contains wheat)
mkrzt gblgkb mctcnf nqvxt mmpmmh sppx stgxzx rvj nfmqzmn zxvfb cnfp cvtbq cljf xrdtpr cpxmpc qmrps kmjrr kgjm hcjtjd djsq scqs ndzkc qzs brgkb khrgj bnv lchtjz rbs svbmv jpmvj qsjszn tvjnk rjfnqc srxgh vtk frtfg vvfjj rkfcbq lchxqhn gmxqpdgz hvnkk (contains soy)
qmrps qnvx tcnc cpxmpc mgnsdhl qzs brcnbqc tqv rqksl jbkbxgz hxkds hvnkk rjfnqc kvg kgjm dlzrg gmxqpdgz rvj xpqsj hlzl cgck gshhq ltxqk bbknm khrgj lsbmlsf grlg rbld kczx smpg dbfxfjd zfhz vvfjj pcppmnz zdpbx cljf sbxfxq vrcd cn sgnqbn pzglb qhssg hhdcqk jpmvj frtfg pdlgg lnblbr jjjs mmsr (contains soy, shellfish)
qnvx gvlcxv hvnkk qqdp pdlgg brgkb kzhjnft hlzl qlgzjf stgxzx nchklb frtfg hgcxmnf qngpn zfhz rbld tvjnk fkn qzs rbs qjmvq gxdrk bkgxfl qsjszn xpqsj jmhpt fkmj ntcpp tvcvnj gntfcf ctk zhz rkfcbq vrcd hlcxrd kvvfg sbpd ndzkc mmsr khrgj vvfjj ldbcvh qmrps mjgxc bncgmk pvqv lchtjz xbggv znkqb hcjtjd jkm cjlgz mhgxm rzxq btf cljf (contains dairy)
qnvx cpxmpc chcb nqhln ldbcvh qhssg xnxrs vrcd cnfp ncp gshhq bncgmk kvg qmrps pnzqt trvv mctcnf cljf cbqgz bbknm ddbnz mmsr mqv pdxtnh jmhpt fkn qsjszn jcp gntfcf xbnk mnlkx qjmvq bhfsr hgcxmnf stgxzx khrgj qpdjgp grlg rqsnq brgkb qlgzjf hlkvg hgdgpvg lsbmlsf ztlmjm sgnqbn vnhqd rpk rqxgs hcjtjd vvfjj gblgkb rlfnr kcxrlp vdr sppx thjh frtfg rmxrlf nfmqzmn jcn kmjrr zfhz rvj dbfxfjd tcnc cvtbq jllbgt qjcktn rbld lchxqhn pbvf phkq qzs xsljt hqqdr kgkct hjc zxvfb ksqp (contains fish, shellfish, wheat)
qmrps bncgmk gxdrk hxkds ddbnz qsjszn stgxzx nrkqg dbfxfjd khrgj fkmj ncp bkgxfl qqdp mhgxm hcjtjd cpxmpc svbmv djsq qzs pcppmnz ldbcvh vnhqd hhdcqk frtfg hvnkk cn qjmvq cjjkdc sffksrkn zjxssr qtsgr rlfnr hlcxrd knfsd rpk lptpdd jkm jcp brgkb rqsnq pvqv qzlp scqs blmpt sbxfxq vdr hgjjt kgjm fvrplq jcn fkn tvjnk rpmczd vvfjj zdpbx rjfnqc pdxtnh qlgzjf tcnc trvv zxvfb mctcnf kvvfg xjjc lchtjz xdsxbrx gntfcf brcnbqc rbld cnfp srxgh xbnk sbpd xhbzbt thd hjc kvg bttv qnvx rnkbccd zxdmj sgnqbn (contains shellfish, nuts, soy)
sbpd hvnkk ldbcvh smlp cjjkdc lsbmlsf rjfnqc qsjszn cn kzhjnft grlg kcxrlp skbms vnhqd kqtj qmrps ztlmjm fkn kvg vvfjj qpdjgp lnblbr frtfg hqqdr jcn phkq vtk chcb ltxqk gmxqpdgz hlcxrd pvqv bkgxfl srxgh sgvk tsvk khrgj cljf ddbnz zdpbx rqksl lchxqhn hlfg tvjnk jrtdg dbfxfjd cgnb vrcd ntcpp gxnv ncp qhssg jcp cpxmpc cvtbq hhdcqk hlzl rzxq vpjrmt xrdtpr hgjjt dlzrg (contains wheat, dairy, nuts)
tqv sbpd xtjfp jpmvj nfmqzmn chcb rbs bqsngs tvjnk xsljt frtfg ntcpp smgnpc mjgxc vvjvph jllbgt gntfcf rbld pvqv gshhq mqv cpxmpc ndzkc rmxrlf xrdtpr hlqknsf nqvxt btf cn xjjc sgnqbn rvj cjjkdc svbmv rpmczd qmrps zxdmj rjfnqc vvfjj mmsr sppx vpjrmt qgpgzkc jjjs qsjszn stgxzx qhssg zhz cbqgz jcp qzlp rqsnq hlkvg rzxq hvnkk vtk thjh mhgxm brgkb rpk skbms rnkbccd kvvfg jbkbxgz fkmj cljf ltxqk tcnc vrcd kgjm sbxfxq qzs pdxtnh zrtsxf (contains wheat, dairy)
qnvx gblgkb hlzl vvfjj cpxmpc hvnkk tqv zjxssr rqxgs frtfg gntfcf rqsnq ddbnz jrtdg qhssg rnkbccd brgkb qsjszn btf brcnbqc qngpn rlfnr hgcxmnf bncgmk bctkn lptpdd cn khrgj kmjrr cljf cbqgz xjjc hlkvg cjjmhlmm mhnlcxv vvjvph qgpgzkc zrtsxf fkmj fvrplq qtsgr srxgh xhbzbt qjmvq ctk pvqv vdr jkm pzglb xrdtpr kcxrlp mmsr jpmvj nqvxt hlfg djzm qpdjgp xnxrs rbs bsgvtrs jcp nqhln blvk sgnqbn pbvf rzxq mjgxc thjh nchklb trvv bhfsr lbcfst xbggv dhzkcf phkq jcn bttv hqqdr vpjrmt ltxqk cgnb kczx (contains fish)
gmxqpdgz mmsr rqxgs sbxfxq rbs stgxzx rkfcbq qhssg xbggv xbnk xhbzbt nchklb hlkvg cljf lsbmlsf kvvfg qnvx chcb lnblbr lbcfst qpdjgp kgkct qgpgzkc hcjtjd zhz sffksrkn nrkqg mctcnf blmpt tqv qmrps ztlmjm gvlcxv lchxqhn mkrzt thjh ltxqk pbvf qsjszn rjfnqc cpxmpc gblgkb hvnkk hgcxmnf cnfp scqs ntcpp srxgh rmxrlf vvfjj ksqp fkmj khrgj hxkds jkm zrtsxf tvcvnj cjlgz xpqsj cjjkdc grlg sppx zdpbx mhnlcxv nfmqzmn ndzkc qjmvq bncgmk (contains shellfish, dairy)
cnfp sbxfxq qtsgr nqhln pvqv rjfnqc smlp nfmqzmn svbmv rnkbccd pbvf rpmczd vpjrmt hcjtjd jpmvj qsjszn qmrps fvdnrd chcb ksqp thjh hvhfrsm kgkct hlqknsf jcp qgpgzkc hqqdr hjc cpxmpc lchtjz stgxzx kcxrlp brcnbqc djsq nrkqg gfjmzl hgjjt zxvfb qzs phkq vvfjj gntfcf dlzrg xpqsj cn smpg xjjc qlgzjf qnvx jbkbxgz vvjvph kmjrr qjgnp rqxgs dpvnsd khrgj frtfg cljf (contains nuts, eggs, soy)
kvvfg mjgxc xsljt rjfnqc rbld bctkn cjlgz cjjmhlmm znkqb rkfcbq phkq nchklb sppx qzlp djsq pvqv frtfg bbknm kgkct gvlcxv xbnk cnfp qnvx qncmm jkm blmpt gmxqpdgz cn hqqdr zxdmj fkn pcppmnz xpqsj lsbmlsf vdr gqhkxn lptpdd zrtsxf cgnb qjjss cljf mmsr qmrps hvhfrsm ntcpp bncgmk lchxqhn srxgh vvfjj pbvf qsjszn xdsxbrx qgpgzkc qzs tgxsld lnblbr qjmvq kqtj vnhqd jllbgt rmxrlf pdlgg cpxmpc kgjm lchtjz smpg hxkds gfjmzl (contains dairy)
zjxssr hqqdr hvnkk gblgkb gmxqpdgz qhssg pnzqt kgkct fkmj ntcpp cjjmhlmm cljf vpjrmt smgnpc qnvx xsljt qjgnp ltxqk xhbzbt rmxrlf qjcktn dpvnsd svbmv rqxgs vvfjj fvdnrd jcn kmjrr chcb znkqb qtsgr lbcfst kvg jbkbxgz lchxqhn sffksrkn qjmvq bsgvtrs bncgmk tvcvnj thjh zdpbx rpmczd zfhz gxnv dbfxfjd ncp lnblbr jllbgt hlqknsf pdxtnh knfsd ndzkc gvlcxv mhnlcxv hcjtjd rpk frtfg vvjvph pbvf tsvk smlp xbggv nchklb cpxmpc btf bkgxfl mmsr qmrps cbqgz (contains eggs, dairy)
kcxrlp cgnb vtk hgjjt ksqp cljf tqv qnvx mmsr bnv qlgzjf vrcd vpjrmt ndzkc stgxzx phkq ddbnz jllbgt zfhz mctcnf cjlgz jjjs qsjszn tvjnk gfjmzl gxnv ldbcvh bbknm vvfjj xhbzbt qgpgzkc rnkbccd srxgh zxdmj qmrps sffksrkn qngpn kzhjnft ctk smgnpc zhz blvk hvnkk frtfg jcp pvqv dpvnsd jrtdg (contains peanuts, wheat)
dlzrg bctkn vvfjj frtfg qmrps btf xnxrs zjxssr cljf hgcxmnf ksqp fvrplq rlfnr bttv cgnb xtjfp lbcfst gntfcf smlp nqhln rkfcbq qpdjgp cbqgz hlkvg bbknm jbkbxgz ncp zdpbx qhssg rnkbccd zfhz svbmv hvnkk ltxqk nfmqzmn kvvfg rbs zxvfb qnvx jllbgt qzlp trvv xsljt sgvk qsjszn xbnk jjjs qngpn kmjrr pcppmnz tcnc vrcd mkrzt (contains dairy, peanuts, fish)
pcppmnz xbnk fkmj ndzkc sgvk qjgnp gblgkb smpg sffksrkn jpmvj vpjrmt dhzkcf rpmczd qpdjgp qlgzjf vvfjj rjfnqc cpxmpc mqv skbms trvv tvjnk kmjrr xtjfp knfsd bhfsr frtfg rvj ntcpp qmrps mctcnf cnfp ctk ldbcvh gxdrk qjcktn sbpd tgxsld nfmqzmn cljf smlp hvnkk ksqp qtsgr bncgmk rzxq vtk qnvx pdxtnh rkfcbq hgcxmnf nchklb fvrplq qngpn fkn gshhq cbqgz nqhln hqqdr thjh brgkb pdlgg xpqsj kvg jjjs pzglb blvk bctkn kqtj qjjss (contains eggs)
xhbzbt vdr nrkqg lptpdd zxvfb cbqgz qjgnp kvvfg kmjrr cgck mmpmmh sbxfxq rqxgs mqv ctk cpxmpc hlkvg rkfcbq jjjs ksqp blvk kgjm hvnkk qmrps xnxrs tsvk xjjc dbfxfjd djzm lchxqhn cnfp mgnsdhl cljf knfsd tgxsld cgnb bttv mhnlcxv nqhln vvfjj frtfg trvv skbms gntfcf bncgmk hjc sppx jcp qzs hgjjt ndzkc zxdmj xbnk scqs khrgj sgnqbn qjmvq tvjnk fkn tqv hcjtjd ltxqk tvcvnj dhzkcf jcn qnvx rjfnqc rbs smlp kczx pdlgg jpmvj cvtbq mmsr qlgzjf qgpgzkc pvqv (contains nuts)
jbkbxgz knfsd vtk qnvx cgck gshhq ntcpp ndzkc vrcd qsjszn rvj vvfjj bhfsr hvnkk bqsngs hgcxmnf jcp sgnqbn cjlgz kmjrr hgdgpvg tgxsld mctcnf scqs tvjnk ldbcvh kgkct lsbmlsf cljf dbfxfjd pcppmnz frtfg cvtbq cbqgz thjh bttv qjgnp fvdnrd pvqv kqtj smgnpc gblgkb phkq rzxq brgkb gntfcf rbs zjxssr qmrps kvg btf blvk zxdmj nqhln thd cnfp smpg hcjtjd nqvxt mmsr lnblbr mgnsdhl stgxzx (contains wheat, dairy)
pdxtnh rpmczd vtk sbpd qnvx rbld xrdtpr mhnlcxv tvjnk nchklb ldbcvh bnv mctcnf smlp pcppmnz kmjrr cpxmpc ncp vdr jpmvj bsgvtrs rkfcbq mjgxc cljf zjxssr qqdp cvtbq ksqp sppx ztlmjm vrcd qsjszn gmxqpdgz dpvnsd rzxq gshhq pbvf kgkct gntfcf ltxqk kvvfg frtfg qmrps kgjm pnzqt xsljt hxkds hvnkk xjjc kzhjnft fvdnrd ndzkc smgnpc cnfp djsq gxdrk (contains shellfish, wheat, nuts)
qtsgr smpg nrkqg sffksrkn bqsngs cbqgz jmhpt vvjvph ltxqk cpxmpc rzxq cn grlg vtk thd qqdp qnvx cnfp cjjkdc chcb hlqknsf ksqp kgjm tgxsld stgxzx vvfjj rpk hgjjt zdpbx zfhz vdr sbpd mnlkx gntfcf ndzkc rqxgs qzs jllbgt hxkds djsq ddbnz nfmqzmn hgdgpvg qjgnp lsbmlsf rbld rbs qlgzjf hvhfrsm frtfg kqtj zxvfb hhdcqk bsgvtrs hvnkk pdxtnh qmrps qjmvq cljf (contains eggs)
tvcvnj mqv qmrps hgdgpvg qjjss jmhpt kzhjnft zhz rzxq lptpdd qtsgr xjjc cjjkdc mmsr jjjs brcnbqc lnblbr nrkqg kgkct qngpn cbqgz hcjtjd jbkbxgz sffksrkn xbggv qsjszn xsljt pcppmnz mctcnf hvnkk pdlgg lbcfst cjjmhlmm mgnsdhl gfjmzl cpxmpc pbvf rpk djsq gblgkb gxnv rlfnr kcxrlp ltxqk smpg frtfg mhgxm hlcxrd smgnpc bnv znkqb hvhfrsm hxkds ddbnz ctk jkm thjh vpjrmt kvvfg grlg srxgh qncmm rbld qnvx tqv rvj djzm hjc lchxqhn vrcd jllbgt vvfjj rqxgs (contains soy, nuts, wheat)
lnblbr jcp hvnkk vrcd mnlkx qmrps smpg gntfcf fvrplq sbpd cljf zrtsxf tsvk xtjfp qzs rjfnqc zfhz tvcvnj xnxrs ntcpp rbs vtk qngpn zxvfb frtfg blvk scqs gmxqpdgz sffksrkn qsjszn lbcfst jllbgt smlp rlfnr lchxqhn vnhqd xsljt hvhfrsm rmxrlf fkn cjlgz kvg jbkbxgz kgkct mkrzt srxgh zhz jrtdg hgcxmnf hlkvg gxnv gfjmzl dhzkcf vvfjj qnvx rkfcbq mjgxc ksqp kmjrr bsgvtrs mqv nchklb bqsngs ddbnz hxkds tvjnk phkq grlg zjxssr qgpgzkc brcnbqc bnv gvlcxv fvdnrd sbxfxq mhgxm rqsnq (contains fish, nuts)
lchtjz blmpt hvnkk pdxtnh xtjfp xbnk tgxsld rqxgs djzm nqvxt cjjkdc dhzkcf jcp hgdgpvg hxkds sgvk pcppmnz kmjrr rqksl hvhfrsm bhfsr jcn hlzl bctkn frtfg sbxfxq vvfjj cjjmhlmm tcnc lbcfst kczx scqs chcb vnhqd gqhkxn mqv lnblbr vpjrmt nchklb ltxqk qnvx xrdtpr zxvfb cbqgz kgjm dbfxfjd ddbnz cpxmpc qjgnp qqdp qsjszn kqtj mmsr rnkbccd btf zjxssr pvqv ksqp qgpgzkc gxdrk rzxq qncmm srxgh qpdjgp jpmvj cljf bncgmk (contains peanuts)
pvqv vvfjj gshhq kvvfg smgnpc qjcktn fvrplq cpxmpc brcnbqc pcppmnz mmsr stgxzx hvnkk smpg dlzrg rqksl hlcxrd hjc qjmvq ndzkc cjjmhlmm gxnv scqs rbs mhgxm nqhln lptpdd lchxqhn mctcnf znkqb hqqdr trvv qngpn qqdp qnvx cnfp jcn hcjtjd mgnsdhl brgkb sffksrkn qsjszn hxkds qncmm xrdtpr mmpmmh xsljt qtsgr xpqsj bnv bqsngs gqhkxn lnblbr ksqp frtfg cvtbq mjgxc srxgh kmjrr nrkqg vtk sgnqbn svbmv vdr qpdjgp vrcd ctk pnzqt zxvfb qmrps blmpt hlzl cjjkdc dhzkcf bhfsr jbkbxgz btf hgjjt sbxfxq rbld xtjfp zfhz (contains nuts)
lptpdd mkrzt frtfg pnzqt xbnk cjjmhlmm pdxtnh gxnv jcn hlfg qncmm sbxfxq tcnc qmrps pcppmnz qzlp rnkbccd xtjfp vnhqd vrcd hlqknsf sgvk vvfjj xrdtpr rvj jpmvj hqqdr hcjtjd scqs cbqgz fvdnrd qqdp cpxmpc nfmqzmn cn qhssg vvjvph qnvx ctk khrgj qngpn hhdcqk qjjss tqv kcxrlp rjfnqc cgnb rbld cvtbq hvnkk cjlgz cljf qpdjgp brcnbqc qzs fvrplq mctcnf (contains soy, fish)
cjjmhlmm rbld vpjrmt gmxqpdgz rpmczd rjfnqc ctk zfhz sffksrkn tcnc nrkqg qzs chcb kvg qgpgzkc mgnsdhl gntfcf kgkct hxkds djsq bncgmk brcnbqc qhssg fkn qsjszn cljf kgjm xbggv bhfsr hvhfrsm hcjtjd vvfjj qmrps qnvx tvcvnj ddbnz frtfg jkm xrdtpr zhz qqdp trvv cnfp rbs xsljt hvnkk qjcktn (contains eggs, wheat)
phkq dbfxfjd xjjc lbcfst bncgmk cljf qmrps tcnc bqsngs xbggv qlgzjf brgkb vrcd fkmj qqdp mhnlcxv btf xdsxbrx bhfsr rbs tsvk bctkn qncmm qsjszn trvv dlzrg jjjs kvvfg hqqdr hgdgpvg nrkqg hcjtjd sgvk jllbgt pvqv cnfp pzglb zxvfb qnvx rqxgs gqhkxn qtsgr lsbmlsf pcppmnz frtfg cpxmpc pbvf xnxrs scqs ddbnz gntfcf rlfnr hvnkk rkfcbq jmhpt chcb brcnbqc (contains eggs, wheat)
pnzqt fkmj hgdgpvg gvlcxv pvqv rpmczd grlg mctcnf xnxrs hvnkk cpxmpc zrtsxf cljf phkq sgnqbn djsq qmrps khrgj kgjm dhzkcf sbpd trvv pbvf ndzkc vvjvph znkqb thd chcb tcnc frtfg qzlp xtjfp srxgh qnvx bbknm hlfg qsjszn tsvk rbs nfmqzmn nrkqg xbggv cgnb cjjkdc jrtdg pdxtnh rqxgs cjlgz qjjss nqhln qzs vpjrmt (contains dairy, nuts, peanuts)
frtfg hgcxmnf cljf lsbmlsf srxgh kzhjnft vpjrmt knfsd qzlp qmrps kmjrr rmxrlf gxnv svbmv brcnbqc rjfnqc bkgxfl tgxsld gfjmzl kgkct sppx cpxmpc dlzrg rqsnq sbpd stgxzx vvfjj xsljt hhdcqk qpdjgp smpg dbfxfjd bsgvtrs gblgkb gxdrk bbknm vrcd qjmvq mhnlcxv sgvk kvvfg fvrplq trvv mqv hlzl rpk zxvfb qngpn rzxq vvjvph hgdgpvg zrtsxf lchtjz vdr xhbzbt ddbnz tsvk ltxqk ncp jmhpt pdlgg qnvx cbqgz hvnkk zxdmj xbnk nqhln vtk cjjkdc tcnc (contains dairy)
frtfg ntcpp sbpd fkn jllbgt djsq vvfjj cljf cjjmhlmm qnvx srxgh hvnkk pdlgg kvvfg skbms ncp mkrzt btf sgnqbn pdxtnh kmjrr hqqdr jkm dbfxfjd vnhqd rqsnq qmrps gfjmzl knfsd pvqv qsjszn jcn sbxfxq xsljt qtsgr hlcxrd zjxssr vvjvph gmxqpdgz qlgzjf sffksrkn khrgj mmpmmh (contains eggs, shellfish)
kvvfg rqsnq qzs cbqgz hvnkk ntcpp jcp nqvxt qncmm kmjrr jkm mjgxc jllbgt qnvx xbnk mqv xrdtpr rbs khrgj lchxqhn xsljt nchklb hcjtjd brgkb lchtjz vvfjj thd btf cjlgz xhbzbt zjxssr cjjkdc qsjszn nfmqzmn pzglb cpxmpc fvrplq hlcxrd pbvf pvqv qpdjgp pnzqt kvg sffksrkn svbmv sbxfxq mctcnf kgkct cljf tcnc ltxqk dpvnsd bncgmk cvtbq cjjmhlmm vtk ldbcvh qmrps djsq qjmvq pcppmnz vrcd dhzkcf qngpn gvlcxv ksqp gmxqpdgz tsvk zdpbx qqdp cgck dbfxfjd hqqdr mmsr lbcfst smpg fvdnrd hgjjt (contains nuts, wheat, dairy)
hlkvg ztlmjm ltxqk cljf chcb kczx qmrps gshhq qjjss sbpd trvv lnblbr tqv dpvnsd blmpt hgdgpvg jllbgt qngpn qjmvq rmxrlf vvfjj jkm hlcxrd frtfg zxdmj sbxfxq fkmj rnkbccd qsjszn cjjkdc zjxssr kmjrr svbmv cjjmhlmm xdsxbrx bsgvtrs xbnk bctkn tvcvnj qnvx ndzkc vvjvph cpxmpc mgnsdhl qzlp skbms vrcd (contains shellfish, wheat, dairy)
zhz xnxrs dhzkcf qgpgzkc cjjkdc qzs hjc mctcnf zrtsxf kvg sbpd mmpmmh lptpdd xjjc pdxtnh qjgnp gxnv xbnk blvk qncmm qhssg hlkvg skbms pzglb djzm smpg vdr mkrzt gvlcxv nfmqzmn hvhfrsm rqxgs mqv bhfsr gmxqpdgz smlp frtfg ksqp jllbgt fkn tcnc qmrps jpmvj gxdrk phkq cljf vvfjj qsjszn hvnkk zxvfb vtk hqqdr nrkqg vrcd tgxsld sppx qnvx xsljt ddbnz qqdp (contains nuts, peanuts, shellfish)
hhdcqk qnvx rqksl mctcnf vvjvph hvnkk sffksrkn qmrps gmxqpdgz brgkb gqhkxn kvg pdlgg chcb bqsngs kzhjnft qhssg bttv svbmv cjjkdc rzxq rpmczd brcnbqc smlp hjc lnblbr djzm vnhqd hxkds rnkbccd vdr phkq ldbcvh pzglb khrgj cpxmpc frtfg qsjszn xdsxbrx rmxrlf xnxrs bsgvtrs mhnlcxv hlkvg zrtsxf xtjfp jllbgt hlfg scqs zfhz kgkct mqv zxvfb cjjmhlmm ztlmjm hlzl qtsgr sbxfxq srxgh mnlkx cljf (contains wheat, soy, dairy)
cjjkdc ltxqk smpg qsjszn rjfnqc rnkbccd mhgxm qjgnp nchklb djsq sgnqbn qmrps djzm jllbgt jcn kvvfg bctkn kcxrlp zjxssr nqhln hcjtjd vnhqd tvcvnj dlzrg fkn qnvx qzlp frtfg hjc vvfjj rlfnr qjmvq qhssg sppx smlp hqqdr fkmj rzxq nrkqg hvnkk gmxqpdgz btf kmjrr srxgh rbs khrgj cljf thjh pnzqt rvj thd fvrplq gshhq (contains eggs)
cpxmpc xbggv svbmv dlzrg hlcxrd thjh qjjss cn pzglb qmrps zfhz qsjszn tsvk bsgvtrs hvnkk cjjkdc gvlcxv kmjrr cljf mqv znkqb qnvx btf qtsgr mjgxc sppx rmxrlf djsq vvfjj jkm bqsngs kgkct cgck smpg tvjnk bkgxfl rzxq cjjmhlmm cbqgz brgkb xrdtpr mctcnf cjlgz (contains wheat, peanuts, fish)
ctk bqsngs xtjfp frtfg kvvfg zrtsxf dlzrg zjxssr tvcvnj btf hqqdr qgpgzkc hvhfrsm svbmv pbvf tvjnk qnvx grlg vpjrmt phkq cjlgz rzxq xsljt cpxmpc sffksrkn srxgh sbpd qtsgr smpg fkmj qsjszn tgxsld hvnkk rpk lsbmlsf djzm mhnlcxv qmrps cn bsgvtrs fvdnrd mqv knfsd jcp rqksl jrtdg kgkct scqs bnv cgnb brcnbqc mgnsdhl mhgxm qjgnp mctcnf ztlmjm xpqsj znkqb cljf rvj qlgzjf cnfp gvlcxv (contains dairy)
jcn gvlcxv gntfcf kqtj bkgxfl hgjjt kgkct rvj smlp mctcnf cnfp mnlkx gshhq qsjszn xhbzbt bsgvtrs ddbnz sbpd hvnkk rqxgs pdlgg hgcxmnf knfsd mhnlcxv jcp pnzqt srxgh fkmj vvfjj zjxssr brcnbqc hcjtjd cpxmpc qjmvq kczx vtk mkrzt frtfg ndzkc qmrps gblgkb tvjnk vvjvph qtsgr ztlmjm ncp khrgj hvhfrsm qngpn kzhjnft fkn rbs xnxrs cljf rjfnqc gqhkxn hqqdr pzglb mhgxm qlgzjf vrcd vpjrmt lbcfst rqsnq cbqgz sgvk bnv cn lchtjz tqv tsvk grlg hlkvg pdxtnh cjjkdc qpdjgp qhssg rnkbccd xrdtpr lsbmlsf (contains wheat, dairy)
znkqb kgjm gvlcxv xrdtpr trvv xnxrs btf cgnb mkrzt kvg bqsngs qsjszn jpmvj xsljt hjc rvj hvnkk sgvk dhzkcf dlzrg qngpn qjmvq xjjc stgxzx vvfjj nfmqzmn qtsgr cn gqhkxn smlp fvrplq qmrps jrtdg lchxqhn rlfnr qpdjgp hqqdr vvjvph qzs tsvk rbs qjgnp frtfg cjjmhlmm rjfnqc gxnv sgnqbn cvtbq sppx cljf zxdmj tqv qhssg svbmv tvjnk jbkbxgz chcb hxkds hlqknsf nrkqg qnvx jjjs lptpdd tvcvnj rpmczd rnkbccd bsgvtrs kgkct jmhpt gblgkb tgxsld (contains wheat, nuts)
gblgkb hhdcqk rjfnqc xbggv dlzrg bsgvtrs gxdrk qmrps sbpd tcnc ldbcvh fvrplq fkmj qsjszn ksqp xjjc bnv jjjs hlqknsf zdpbx nqvxt ddbnz gshhq qnvx frtfg lsbmlsf xrdtpr rqsnq kmjrr lbcfst hvnkk tgxsld rmxrlf kgjm mkrzt tqv cljf lchxqhn rvj rpmczd znkqb rbld srxgh cpxmpc jkm vrcd qhssg rzxq tsvk (contains wheat, dairy, shellfish)
brcnbqc qtsgr vdr rnkbccd bqsngs nchklb kgjm pbvf knfsd kvg trvv xhbzbt hvnkk zfhz zjxssr xrdtpr rpmczd rzxq hqqdr rvj nqvxt mhgxm qsjszn smpg cn brgkb jrtdg jjjs mmpmmh hlcxrd ntcpp sgnqbn cpxmpc ldbcvh vvjvph qmrps djsq cjlgz bsgvtrs rqsnq btf pzglb qnvx sgvk vvfjj sppx xdsxbrx cgnb rqksl bnv khrgj smlp cjjmhlmm cljf mqv pvqv hlqknsf qpdjgp pnzqt ctk thjh xtjfp bkgxfl rpk kcxrlp fkmj lptpdd ddbnz ksqp xsljt vtk tqv hgjjt tsvk hlfg qjgnp qjjss qjcktn ltxqk (contains shellfish, wheat)'''

# COMMAND ----------

import re


foods = [tuple(frozenset(re.findall(r'[a-z]+', part)) for part in line.split('contains')) for line in inp.splitlines()]
all_ingredients, all_allergens = (frozenset.union(*part) for part in zip(*foods))

possible_allergens = {}
for ingredient in all_ingredients:
  possible_allergens[ingredient] = all_allergens
  for food_ingredients, food_allergens in foods:
    if ingredient in food_ingredients:
      continue
    possible_allergens[ingredient] -= food_allergens

non_allergen_ingredients = {ingredient for ingredient, candidate_allergens in possible_allergens.items() if not candidate_allergens}

answer = sum(non_allergen_ingredient in food_ingredients for food_ingredients, _ in foods for non_allergen_ingredient in non_allergen_ingredients)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.</p>
# MAGIC <p>In the above example:</p>
# MAGIC <ul>
# MAGIC <li><code>mxmxvkd</code> contains <code>dairy</code>.</li>
# MAGIC <li><code>sqjhc</code> contains <code>fish</code>.</li>
# MAGIC <li><code>fvjkl</code> contains <code>soy</code>.</li>
# MAGIC </ul>
# MAGIC <p>Arrange the ingredients <em>alphabetically by their allergen</em> and separate them by commas to produce your <em>canonical dangerous ingredient list</em>. (There should <em>not be any spaces</em> in your canonical dangerous ingredient list.) In the above example, this would be <em><code>mxmxvkd,sqjhc,fvjkl</code></em>.</p>
# MAGIC <p>Time to stock your raft with supplies. <em>What is your canonical dangerous ingredient list?</em></p>
# MAGIC </article>

# COMMAND ----------

for ingredient in non_allergen_ingredients:
  del possible_allergens[ingredient]

confirmed_allergens = {}
while possible_allergens:
  for ingredient, candidate_allergens in possible_allergens.items():
    if len(candidate_allergens) == 1:
      confirmed_allergen = next(iter(candidate_allergens))
      confirmed_allergens[ingredient] = confirmed_allergen
      del possible_allergens[ingredient]
      break
  
  for ingredient, candidate_allergens in possible_allergens.items():
    possible_allergens[ingredient] = candidate_allergens - {confirmed_allergen}

answer = ','.join(sorted(confirmed_allergens, key=confirmed_allergens.__getitem__))
print(answer)
