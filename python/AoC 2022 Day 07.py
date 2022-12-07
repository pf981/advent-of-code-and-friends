# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/7

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 7: No Space Left On Device ---</h2><p>You can hear birds chirping and raindrops hitting leaves as the expedition proceeds. Occasionally, you can even hear much louder sounds in the distance; how big do the animals get out here, anyway?</p>
# MAGIC <p>The device the Elves gave you has problems with more than just its communication system. You try to run a system update:</p>
# MAGIC <pre><code>$ system-update --please --pretty-please-with-sugar-on-top
# MAGIC <span title="E099 PROGRAMMER IS OVERLY POLITE">Error</span>: No space left on device
# MAGIC </code></pre>
# MAGIC <p>Perhaps you can delete some files to make space for the update?</p>
# MAGIC <p>You browse around the filesystem to assess the situation and save the resulting terminal output (your puzzle input). For example:</p>
# MAGIC <pre><code>$ cd /
# MAGIC $ ls
# MAGIC dir a
# MAGIC 14848514 b.txt
# MAGIC 8504156 c.dat
# MAGIC dir d
# MAGIC $ cd a
# MAGIC $ ls
# MAGIC dir e
# MAGIC 29116 f
# MAGIC 2557 g
# MAGIC 62596 h.lst
# MAGIC $ cd e
# MAGIC $ ls
# MAGIC 584 i
# MAGIC $ cd ..
# MAGIC $ cd ..
# MAGIC $ cd d
# MAGIC $ ls
# MAGIC 4060174 j
# MAGIC 8033020 d.log
# MAGIC 5626152 d.ext
# MAGIC 7214296 k
# MAGIC </code></pre>
# MAGIC <p>The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called <code>/</code>. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.</p>
# MAGIC <p>Within the terminal output, lines that begin with <code>$</code> are <em>commands you executed</em>, very much like some modern computers:</p>
# MAGIC <ul>
# MAGIC <li><code>cd</code> means <em>change directory</em>. This changes which directory is the current directory, but the specific result depends on the argument:
# MAGIC   <ul>
# MAGIC   <li><code>cd x</code> moves <em>in</em> one level: it looks in the current directory for the directory named <code>x</code> and makes it the current directory.</li>
# MAGIC   <li><code>cd ..</code> moves <em>out</em> one level: it finds the directory that contains the current directory, then makes that directory the current directory.</li>
# MAGIC   <li><code>cd /</code> switches the current directory to the outermost directory, <code>/</code>.</li>
# MAGIC   </ul>
# MAGIC </li>
# MAGIC <li><code>ls</code> means <em>list</em>. It prints out all of the files and directories immediately contained by the current directory:
# MAGIC   <ul>
# MAGIC   <li><code>123 abc</code> means that the current directory contains a file named <code>abc</code> with size <code>123</code>.</li>
# MAGIC   <li><code>dir xyz</code> means that the current directory contains a directory named <code>xyz</code>.</li>
# MAGIC   </ul>
# MAGIC </li>
# MAGIC </ul>
# MAGIC <p>Given the commands and output in the example above, you can determine that the filesystem looks visually like this:</p>
# MAGIC <pre><code>- / (dir)
# MAGIC   - a (dir)
# MAGIC     - e (dir)
# MAGIC       - i (file, size=584)
# MAGIC     - f (file, size=29116)
# MAGIC     - g (file, size=2557)
# MAGIC     - h.lst (file, size=62596)
# MAGIC   - b.txt (file, size=14848514)
# MAGIC   - c.dat (file, size=8504156)
# MAGIC   - d (dir)
# MAGIC     - j (file, size=4060174)
# MAGIC     - d.log (file, size=8033020)
# MAGIC     - d.ext (file, size=5626152)
# MAGIC     - k (file, size=7214296)
# MAGIC </code></pre>
# MAGIC <p>Here, there are four directories: <code>/</code> (the outermost directory), <code>a</code> and <code>d</code> (which are in <code>/</code>), and <code>e</code> (which is in <code>a</code>). These directories also contain files of various sizes.</p>
# MAGIC <p>Since the disk is full, your first step should probably be to find directories that are good candidates for deletion. To do this, you need to determine the <em>total size</em> of each directory. The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly. (Directories themselves do not count as having any intrinsic size.)</p>
# MAGIC <p>The total sizes of the directories above can be found as follows:</p>
# MAGIC <ul>
# MAGIC <li>The total size of directory <code>e</code> is <em>584</em> because it contains a single file <code>i</code> of size 584 and no other directories.</li>
# MAGIC <li>The directory <code>a</code> has total size <em>94853</em> because it contains files <code>f</code> (size 29116), <code>g</code> (size 2557), and <code>h.lst</code> (size 62596), plus file <code>i</code> indirectly (<code>a</code> contains <code>e</code> which contains <code>i</code>).</li>
# MAGIC <li>Directory <code>d</code> has total size <em>24933642</em>.</li>
# MAGIC <li>As the outermost directory, <code>/</code> contains every file. Its total size is <em>48381165</em>, the sum of the size of every file.</li>
# MAGIC </ul>
# MAGIC <p>To begin, find all of the directories with a total size of <em>at most 100000</em>, then calculate the sum of their total sizes. In the example above, these directories are <code>a</code> and <code>e</code>; the sum of their total sizes is <code><em>95437</em></code> (94853 + 584). (As in this example, this process can count files more than once!)</p>
# MAGIC <p>Find all of the directories with a total size of at most 100000. <em>What is the sum of the total sizes of those directories?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''$ cd /
$ ls
dir drblq
133789 fjf
dir jpfrhmw
dir jqfwd
dir ncgffsr
12962 ntnr.lrq
dir qnbq
dir rqdngnrq
dir shcvnqq
dir vsd
dir vtzvf
$ cd drblq
$ ls
133843 bglzqdd
dir brfnfhj
268201 fbqjmp.jzv
80676 shcvnqq
$ cd brfnfhj
$ ls
150447 jlcg.dsg
dir nhvgrzs
$ cd nhvgrzs
$ ls
282889 jlcg.dsg
19004 ncgffsr.gwr
dir vbzr
6338 vpsgdph.gbh
dir wdcn
$ cd vbzr
$ ls
225101 fbqjmp
243277 vbzr
$ cd ..
$ cd wdcn
$ ls
154089 dlmpbbf.psv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jpfrhmw
$ ls
87622 cffdsj.jzf
26165 qnbq.sbm
dir vbzr
$ cd vbzr
$ ls
dir blhstw
16919 nttftcts
dir rgdp
116477 shcvnqq
242592 tmjrnqbz.chq
dir vbzr
dir wmct
$ cd blhstw
$ ls
98023 jwdv.qct
$ cd ..
$ cd rgdp
$ ls
dir gcb
141507 shcvnqq
dir ssvzm
$ cd gcb
$ ls
189016 ncgffsr.rbq
$ cd ..
$ cd ssvzm
$ ls
82667 shcvnqq.zjq
$ cd ..
$ cd ..
$ cd vbzr
$ ls
120202 jlcg.dsg
86205 vbzr.jtr
$ cd ..
$ cd wmct
$ ls
dir fbsfcgph
155709 hpsftv
13636 lztgs
273353 ncgffsr.jsg
dir pvwhpfp
$ cd fbsfcgph
$ ls
139944 ncgffsr.gpf
$ cd ..
$ cd pvwhpfp
$ ls
111230 bscrjpzh.glp
dir dgjsddgq
37234 lwd
107139 lztgs
258111 mgtwwvwz
117638 qpdvnfb.gnf
dir szrplcdw
dir vzsl
dir wsmf
$ cd dgjsddgq
$ ls
dir qnbq
$ cd qnbq
$ ls
199119 jlcg.dsg
$ cd ..
$ cd ..
$ cd szrplcdw
$ ls
122236 qclr.cpf
269638 qnbq
$ cd ..
$ cd vzsl
$ ls
233006 twpz.tdm
$ cd ..
$ cd wsmf
$ ls
dir wcnptvtz
$ cd wcnptvtz
$ ls
183952 shcvnqq.lwt
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jqfwd
$ ls
dir hqb
285121 jqffsjbs.jrm
dir nhpqpdn
dir qnbq
dir qtrv
dir wspztvjr
$ cd hqb
$ ls
253786 jwdv.qct
dir vbzr
$ cd vbzr
$ ls
153 gbh
dir gqpqqrgl
dir jzncgd
36914 nvdnsnls.mpd
$ cd gqpqqrgl
$ ls
206691 dmdgcwm.bgh
$ cd ..
$ cd jzncgd
$ ls
122640 vrgmf.tnp
$ cd ..
$ cd ..
$ cd ..
$ cd nhpqpdn
$ ls
86329 ntnr.lrq
$ cd ..
$ cd qnbq
$ ls
76269 fbqjmp.lbd
118968 fbqjmp.msg
190416 gfwhsb.dpc
dir lhgjrmj
dir pbv
173541 pfl
141842 srrmt.ssj
$ cd lhgjrmj
$ ls
dir ghccnw
180420 ldzcj.rwz
149356 lztgs
61792 ncgffsr
dir spmbcjhc
$ cd ghccnw
$ ls
253233 lztgs
56439 ntnr.lrq
19225 ntrmjf.gdb
31628 pdhhzjhm.lbd
$ cd ..
$ cd spmbcjhc
$ ls
dir shcvnqq
$ cd shcvnqq
$ ls
122334 drjbh
$ cd ..
$ cd ..
$ cd ..
$ cd pbv
$ ls
69436 cctsjqh.wqr
285573 ljtqddz
$ cd ..
$ cd ..
$ cd qtrv
$ ls
234568 dmwqfbwd
dir pwwsrjc
245046 qmcr
159151 qtvdjncm.rdb
dir swhzds
178915 vbzr.vgn
dir vcgv
$ cd pwwsrjc
$ ls
173975 bgdj.jnw
202714 jwdv.qct
270702 wggrgcvw.rtp
$ cd ..
$ cd swhzds
$ ls
114686 jwdv.qct
$ cd ..
$ cd vcgv
$ ls
dir fbqjmp
dir qlsgtfhf
dir vbzr
$ cd fbqjmp
$ ls
73065 fbqjmp.jfb
dir shcvnqq
$ cd shcvnqq
$ ls
231428 shcvnqq
$ cd ..
$ cd ..
$ cd qlsgtfhf
$ ls
75227 ntnr.lrq
$ cd ..
$ cd vbzr
$ ls
128050 ncgffsr.gsj
187649 vbzr
$ cd ..
$ cd ..
$ cd ..
$ cd wspztvjr
$ ls
dir pntrhtwh
dir qnbq
dir zfdzvv
$ cd pntrhtwh
$ ls
237258 cffhtr
$ cd ..
$ cd qnbq
$ ls
dir qnbq
$ cd qnbq
$ ls
dir ccwmftsj
$ cd ccwmftsj
$ ls
dir mfc
dir shcvnqq
12262 smpjmn
$ cd mfc
$ ls
198047 fbqjmp.cgh
dir gghsht
205411 wlclz
$ cd gghsht
$ ls
31767 vbzr.lmb
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir lgrghwf
$ cd lgrghwf
$ ls
114786 shcvnqq.vrz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zfdzvv
$ ls
54298 sjp
60303 tcmhrll.htm
$ cd ..
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
dir fqqsqmpr
dir gfznw
dir ncdft
dir pwmppt
dir shcvnqq
196969 vbzr
214841 vzgvr
$ cd fqqsqmpr
$ ls
dir mcdjcntr
$ cd mcdjcntr
$ ls
281856 ncgffsr.lbm
$ cd ..
$ cd ..
$ cd gfznw
$ ls
255657 fzrctbsj.lgf
dir ltfsndpd
175434 qnbq
31794 qnbq.zhd
13366 shcvnqq.wld
dir vcspqgn
235199 wmnjjd.bnh
dir wqpnp
$ cd ltfsndpd
$ ls
dir ncgffsr
dir zpzvdhb
$ cd ncgffsr
$ ls
9898 jjbsnj.gcg
$ cd ..
$ cd zpzvdhb
$ ls
106139 lnp
$ cd ..
$ cd ..
$ cd vcspqgn
$ ls
25386 dgsmmqj
$ cd ..
$ cd wqpnp
$ ls
65905 wjtbfvjp.fmd
$ cd ..
$ cd ..
$ cd ncdft
$ ls
34616 bzlpmsqc
59863 jlcg.dsg
64629 zpzjcl.fmp
$ cd ..
$ cd pwmppt
$ ls
dir dwnqgrzm
80901 vbzr.vsg
89557 vbzr.zlz
$ cd dwnqgrzm
$ ls
184770 jwdv.qct
dir vbzr
$ cd vbzr
$ ls
210329 jlcg.dsg
62272 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
128433 gbh
30208 hjbw
200071 jlcg.dsg
dir sgcz
25045 tbhlwfqg.hts
$ cd sgcz
$ ls
193481 gbh
96461 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd qnbq
$ ls
236171 shcvnqq
$ cd ..
$ cd rqdngnrq
$ ls
dir cprnb
280135 hshsfqwm
dir hwhm
245626 qnbq
145502 qspgdz
114231 rctg.tgt
dir zgn
$ cd cprnb
$ ls
115025 twwgmmp.wbb
$ cd ..
$ cd hwhm
$ ls
229849 cvm
190622 jwdv.qct
dir mscztz
dir ncgffsr
$ cd mscztz
$ ls
59743 bzgpzn.bds
75184 pbdgv
181089 shcvnqq.dhq
dir zqgtr
$ cd zqgtr
$ ls
189142 ffnznfs.nct
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
dir dphrnjl
dir zzfztql
$ cd dphrnjl
$ ls
117317 vbzr
$ cd ..
$ cd zzfztql
$ ls
51096 lztgs
$ cd ..
$ cd ..
$ cd ..
$ cd zgn
$ ls
dir bpbzwgz
dir gqnw
75631 ljptj
283351 ljzhsw.rbs
131158 lztgs
dir ncgffsr
3136 nnpl.swf
dir shcvnqq
dir vbzr
$ cd bpbzwgz
$ ls
29659 jlcg.dsg
15547 shcvnqq
117389 zprhsdfv
$ cd ..
$ cd gqnw
$ ls
117091 brqwhst.jgb
88406 nzjmbrrm.hmh
$ cd ..
$ cd ncgffsr
$ ls
195821 gbh
dir lbzgc
226692 llqqr.spq
247989 lztgs
231909 vnctc
157973 wqnggh
$ cd lbzgc
$ ls
251414 ffmsbscc.dqg
46840 lztgs
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir dvvmhzcq
dir ncgffsr
dir sqzzllv
$ cd dvvmhzcq
$ ls
dir qnbq
70226 qvvm.rpp
dir shcvnqq
$ cd qnbq
$ ls
103994 bfcjrmvr.ltq
dir fbqjmp
dir fcs
177152 gjghvvw.bzg
dir lbfjqh
78412 ntnr.lrq
dir sgjtm
286995 shcvnqq
51750 wmq.vjj
$ cd fbqjmp
$ ls
267212 qhhb.zvg
$ cd ..
$ cd fcs
$ ls
272051 znhsswwh.mjj
$ cd ..
$ cd lbfjqh
$ ls
261487 jlcg.dsg
$ cd ..
$ cd sgjtm
$ ls
dir dnznpj
dir jzsntnbs
dir nqgcbd
dir vdg
$ cd dnznpj
$ ls
173938 hrp.cjq
180485 qnbq.thj
215400 ztvt.wnt
$ cd ..
$ cd jzsntnbs
$ ls
67448 gpvgh.psg
$ cd ..
$ cd nqgcbd
$ ls
196250 fbqjmp.qcv
198482 jlcg.dsg
$ cd ..
$ cd vdg
$ ls
257343 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
156769 fbqjmp.hdb
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
205473 fbqjmp
113067 gsvznzz.qtv
$ cd ..
$ cd sqzzllv
$ ls
146018 ddvjgswr.gsq
$ cd ..
$ cd ..
$ cd vbzr
$ ls
dir vbzr
$ cd vbzr
$ ls
266721 mhlfqpbs.pwr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir slnvdd
$ cd slnvdd
$ ls
90875 pzqv.gnv
207484 rbrj.vcr
$ cd ..
$ cd ..
$ cd vsd
$ ls
dir dfb
dir fqqnsph
dir gbwdhjr
18837 jwdv.qct
dir ncgffsr
dir qnbq
dir rjzjrbvs
$ cd dfb
$ ls
dir bpst
66174 jwdv.qct
dir lcwhfzjw
$ cd bpst
$ ls
dir nqftnn
dir pcvgnvnp
$ cd nqftnn
$ ls
dir bbrsg
dir gjfc
dir hfql
dir shcvnqq
139226 shcvnqq.sbd
dir ssnjqbg
$ cd bbrsg
$ ls
73382 vjcf
$ cd ..
$ cd gjfc
$ ls
164310 gbh
126316 mmqnrc
133899 ntnr.lrq
102615 rgfhrt
$ cd ..
$ cd hfql
$ ls
14685 jwdv.qct
$ cd ..
$ cd shcvnqq
$ ls
119597 lztgs
34165 shcvnqq.zcg
$ cd ..
$ cd ssnjqbg
$ ls
77678 gqdfbqj.tmj
$ cd ..
$ cd ..
$ cd pcvgnvnp
$ ls
21250 lhq
266619 qps.crp
$ cd ..
$ cd ..
$ cd lcwhfzjw
$ ls
dir bhdnnbvm
dir fdnsvfh
12002 jlcg.dsg
dir lfdbzfl
46488 ncgffsr
233704 nthcv.pnc
204660 ntnr.lrq
172482 shcvnqq
dir tlw
$ cd bhdnnbvm
$ ls
37204 fwrdjw.zvv
3248 ntnr.lrq
$ cd ..
$ cd fdnsvfh
$ ls
20765 jlfgnwb.szl
$ cd ..
$ cd lfdbzfl
$ ls
dir fspntmld
183925 jlcg.dsg
$ cd fspntmld
$ ls
251568 lztgs
146785 ncgffsr.mmj
$ cd ..
$ cd ..
$ cd tlw
$ ls
dir qqn
$ cd qqn
$ ls
39232 lprqfwf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fqqnsph
$ ls
132318 lztgs
103863 ntnr.lrq
18793 tngbs
$ cd ..
$ cd gbwdhjr
$ ls
253798 jwdv.qct
$ cd ..
$ cd ncgffsr
$ ls
110767 blctz.tqz
dir csfssn
dir dbbfz
dir hjgm
dir hwd
249139 rgcz.gnz
dir wgw
$ cd csfssn
$ ls
dir dlcw
dir jqspd
119066 mlwlc.mql
dir ncgffsr
203475 nwnbsc
143071 qnbq
116623 qvw.gjz
83637 whm.cdg
$ cd dlcw
$ ls
232066 gqllsd.qpl
1046 mfsh
$ cd ..
$ cd jqspd
$ ls
251070 mthmm.bmh
$ cd ..
$ cd ncgffsr
$ ls
83639 ntnr.lrq
$ cd ..
$ cd ..
$ cd dbbfz
$ ls
112576 jgqf.qmj
148549 jlcg.dsg
144811 jwdv.qct
23726 ntnr.lrq
123802 pgdjchrf.vnm
dir vzfbzbcp
$ cd vzfbzbcp
$ ls
39375 fbqq
31914 jwdv.qct
165999 lztgs
$ cd ..
$ cd ..
$ cd hjgm
$ ls
dir ljqjtdmf
100534 mdw
219057 qnbq
97164 rzjwmvdw.vlv
dir shcvnqq
83034 vbzr
$ cd ljqjtdmf
$ ls
23716 dmslzv.qns
159519 gbh
dir hlvbmpg
dir nlqqshp
247315 vqt
dir wlsjnthg
$ cd hlvbmpg
$ ls
54421 jlcg.dsg
$ cd ..
$ cd nlqqshp
$ ls
dir rvzprwhp
$ cd rvzprwhp
$ ls
35024 lztgs
$ cd ..
$ cd ..
$ cd wlsjnthg
$ ls
29178 gnrlgb.bgh
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
150311 nvrd
$ cd ..
$ cd ..
$ cd hwd
$ ls
dir jzqtmm
$ cd jzqtmm
$ ls
103547 jtvdt.jtn
$ cd ..
$ cd ..
$ cd wgw
$ ls
dir mmhlt
$ cd mmhlt
$ ls
dir cmwjh
$ cd cmwjh
$ ls
243844 qnbq.shn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qnbq
$ ls
dir dhfng
dir fbqjmp
16855 rgrszmrh.lbl
dir rqjs
dir shcvnqq
38322 vhvrmq
$ cd dhfng
$ ls
132537 gwngz.hpt
dir lbccc
182221 ntnr.lrq
$ cd lbccc
$ ls
282448 fbqjmp.njj
267049 gbh
dir jtj
dir ntnn
dir vbfgmmvw
128500 vbzr
$ cd jtj
$ ls
dir hvmlh
$ cd hvmlh
$ ls
131886 dmww.sqc
$ cd ..
$ cd ..
$ cd ntnn
$ ls
109064 lgh.bbf
dir wfgdd
53862 wflv.ngc
$ cd wfgdd
$ ls
58756 gbh
dir lgzlndn
dir qnbq
$ cd lgzlndn
$ ls
190415 dwsqvczd
$ cd ..
$ cd qnbq
$ ls
240922 znjhmhp.ngt
$ cd ..
$ cd ..
$ cd ..
$ cd vbfgmmvw
$ ls
271827 vbzr.dfl
$ cd ..
$ cd ..
$ cd ..
$ cd fbqjmp
$ ls
144993 gvpnf
150786 jwdv.qct
49025 pdcwwtt.grs
$ cd ..
$ cd rqjs
$ ls
dir bwnzs
119390 jlcg.dsg
172042 vjzg
$ cd bwnzs
$ ls
108537 hzzgm.zrn
38699 qgfqbfr
dir vhvcfhvr
$ cd vhvcfhvr
$ ls
2783 jwdv.qct
209933 mgj.nvj
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
257312 fbqjmp
193792 msdqtrpn.grn
98165 rgm
$ cd ..
$ cd ..
$ cd rjzjrbvs
$ ls
dir ftrlfg
dir mtrnl
dir rdpbbd
dir shcvnqq
dir vztnr
$ cd ftrlfg
$ ls
196590 cjjvwjb
dir ffsvh
70123 ldnbc
dir lwnfc
106499 lztgs
dir ncgffsr
dir tfdctq
dir vgthdbf
80852 zndjt.wtl
$ cd ffsvh
$ ls
20370 dvdftpvb.qcj
$ cd ..
$ cd lwnfc
$ ls
dir fgmd
dir gmdjt
274331 hmgjmq.vbz
9726 qjfdqbf.dfj
dir ssnncn
$ cd fgmd
$ ls
280608 jwdv.qct
201912 rqtbw.shd
$ cd ..
$ cd gmdjt
$ ls
202107 jwdv.qct
$ cd ..
$ cd ssnncn
$ ls
140697 jwdv.qct
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
227389 fpdfqp.fzl
164141 hzhrrvpm.hlf
$ cd ..
$ cd tfdctq
$ ls
dir cttmzlw
dir ntvtm
257094 qnbq.zjm
284928 shcvnqq
$ cd cttmzlw
$ ls
142651 rptschdv.mgv
$ cd ..
$ cd ntvtm
$ ls
176269 dhpj
88278 gbh
$ cd ..
$ cd ..
$ cd vgthdbf
$ ls
130998 ncgffsr.mnf
$ cd ..
$ cd ..
$ cd mtrnl
$ ls
86144 djwnvdj
122600 gsdpwh.cmb
$ cd ..
$ cd rdpbbd
$ ls
177384 gbh
dir gstfdm
dir qnbq
dir qtj
260302 vbzr.dhq
$ cd gstfdm
$ ls
23734 mnwzrm.hzr
$ cd ..
$ cd qnbq
$ ls
51705 gmt
205537 ntnr.lrq
94469 vbzr.bvj
$ cd ..
$ cd qtj
$ ls
dir tls
dir zvpcfhg
$ cd tls
$ ls
dir chvgwnt
dir jvgnmfjw
$ cd chvgwnt
$ ls
dir rbw
dir srhj
$ cd rbw
$ ls
174372 btjd.bvv
272995 cnqqh.dfc
$ cd ..
$ cd srhj
$ ls
134054 qwzpr
$ cd ..
$ cd ..
$ cd jvgnmfjw
$ ls
dir hdcwbwgm
236775 sdc
$ cd hdcwbwgm
$ ls
113707 ntnr.lrq
$ cd ..
$ cd ..
$ cd ..
$ cd zvpcfhg
$ ls
dir lsq
$ cd lsq
$ ls
220331 jlcg.dsg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir cmwrqgfq
258731 fbqjmp.fvn
277895 gbh
64973 jlcg.dsg
77978 jwdv.qct
dir lttjrdn
dir sqgnhc
$ cd cmwrqgfq
$ ls
81199 gbh
$ cd ..
$ cd lttjrdn
$ ls
23355 gbh
148263 hcgfqdw
57338 hjwr
166510 jbvnmcj
$ cd ..
$ cd sqgnhc
$ ls
dir glswqrdp
dir qnbq
$ cd glswqrdp
$ ls
225761 ncgffsr.vct
$ cd ..
$ cd qnbq
$ ls
62861 pdqz.wzs
$ cd ..
$ cd ..
$ cd ..
$ cd vztnr
$ ls
189943 wvtlfsp
$ cd ..
$ cd ..
$ cd ..
$ cd vtzvf
$ ls
43248 jwdv.qct'''

# COMMAND ----------

import functools


def process(i, lines):
  args = lines[i].split(' ')[1:]
  output = []
  i += 1
  while i < len(lines) and not lines[i].startswith('$'):
    output.append(lines[i])
    i += 1
  
  return i, args, output


@functools.cache
def get_size(path):
  if isinstance(path, int):
    return path
  return sum(get_size(obj) for obj in objects[path])


lines = inp.splitlines()
wd = tuple()
objects = {}
i = 0
while i < len(lines):
  i, args, output = process(i, lines)
  if args[0] == 'cd':
    if args[1] == '/':
      wd = tuple()
    elif args[1] == '..':
      wd = wd[:-1]
    else:
      wd += (args[1],)
  elif args[0] == 'ls':
    objects[wd] = objects.get(wd, [])
    for out in output:
      if out.startswith('dir'):
        out = wd + (out.split(' ')[1],)
      else:
        out = int(out.split(' ')[0])
      
      objects[tuple(wd)].append(out)
      

answer = 0
for path in objects:
  size = get_size(path)
  if size <= 100000:
    answer += size
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>Now, you're ready to choose a directory to delete.</p>
# MAGIC <p>The total disk space available to the filesystem is <code><em>70000000</em></code>. To run the update, you need unused space of at least <code><em>30000000</em></code>. You need to find a directory you can delete that will <em>free up enough space</em> to run the update.</p>
# MAGIC <p>In the example above, the total size of the outermost directory (and thus the total amount of used space) is <code>48381165</code>; this means that the size of the <em>unused</em> space must currently be <code>21618835</code>, which isn't quite the <code>30000000</code> required by the update. Therefore, the update still requires a directory with total size of at least <code>8381165</code> to be deleted before it can run.</p>
# MAGIC <p>To achieve this, you have the following options:</p>
# MAGIC <ul>
# MAGIC <li>Delete directory <code>e</code>, which would increase unused space by <code>584</code>.</li>
# MAGIC <li>Delete directory <code>a</code>, which would increase unused space by <code>94853</code>.</li>
# MAGIC <li>Delete directory <code>d</code>, which would increase unused space by <code>24933642</code>.</li>
# MAGIC <li>Delete directory <code>/</code>, which would increase unused space by <code>48381165</code>.</li>
# MAGIC </ul>
# MAGIC <p>Directories <code>e</code> and <code>a</code> are both too small; deleting them would not free up enough space. However, directories <code>d</code> and <code>/</code> are both big enough! Between these, choose the <em>smallest</em>: <code>d</code>, increasing unused space by <code><em>24933642</em></code>.</p>
# MAGIC <p>Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. <em>What is the total size of that directory?</em></p>
# MAGIC </article>

# COMMAND ----------

unused = 70000000 - get_size(tuple())
need = 30000000 - unused

answer = float('inf')
for path in objects:
  size = get_size(path)
  if size >= need:
    answer = min(answer, size)

print(answer)
