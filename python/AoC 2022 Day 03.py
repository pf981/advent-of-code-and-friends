# Databricks notebook source
# MAGIC %md https://adventofcode.com/2022/day/3

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 3: Rucksack Reorganization ---</h2><p>One Elf has the important job of loading all of the <a href="https://en.wikipedia.org/wiki/Rucksack" target="_blank">rucksacks</a> with supplies for the <span title="Where there's jungle, there's hijinxs.">jungle</span> journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.</p>
# MAGIC <p>Each rucksack has two large <em>compartments</em>. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.</p>
# MAGIC <p>The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, <code>a</code> and <code>A</code> refer to different types of items).</p>
# MAGIC <p>The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.</p>
# MAGIC <p>For example, suppose you have the following list of contents from six rucksacks:</p>
# MAGIC <pre><code>vJrwpWtwJgWrhcsFMMfFFhFp
# MAGIC jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# MAGIC PmmdzqPrVvPwwTWBwg
# MAGIC wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# MAGIC ttgJtRGJQctTZtZT
# MAGIC CrZsJsPPZsGzwwsLwLmpwMDw
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li>The first rucksack contains the items <code>vJrwpWtwJgWrhcsFMMfFFhFp</code>, which means its first compartment contains the items <code>vJrwpWtwJgWr</code>, while the second compartment contains the items <code>hcsFMMfFFhFp</code>. The only item type that appears in both compartments is lowercase <code><em>p</em></code>.</li>
# MAGIC <li>The second rucksack's compartments contain <code>jqHRNqRjqzjGDLGL</code> and <code>rsFMfFZSrLrFZsSL</code>. The only item type that appears in both compartments is uppercase <code><em>L</em></code>.</li>
# MAGIC <li>The third rucksack's compartments contain <code>PmmdzqPrV</code> and <code>vPwwTWBwg</code>; the only common item type is uppercase <code><em>P</em></code>.</li>
# MAGIC <li>The fourth rucksack's compartments only share item type <code><em>v</em></code>.</li>
# MAGIC <li>The fifth rucksack's compartments only share item type <code><em>t</em></code>.</li>
# MAGIC <li>The sixth rucksack's compartments only share item type <code><em>s</em></code>.</li>
# MAGIC </ul>
# MAGIC <p>To help prioritize item rearrangement, every item type can be converted to a <em>priority</em>:</p>
# MAGIC <ul>
# MAGIC <li>Lowercase item types <code>a</code> through <code>z</code> have priorities 1 through 26.</li>
# MAGIC <li>Uppercase item types <code>A</code> through <code>Z</code> have priorities 27 through 52.</li>
# MAGIC </ul>
# MAGIC <p>In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (<code>p</code>), 38 (<code>L</code>), 42 (<code>P</code>), 22 (<code>v</code>), 20 (<code>t</code>), and 19 (<code>s</code>); the sum of these is <code><em>157</em></code>.</p>
# MAGIC <p>Find the item type that appears in both compartments of each rucksack. <em>What is the sum of the priorities of those item types?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''dWlhclDHdFvDCCDfFq
mGdZBZBwRGjZMFgvTvgtvv
jwwJrzdzGdSbGGnNlzWczHzPHPhn
cczcbMBszhzzDBTBPPPGjtvtlt
LqJLfpwdLnvQLRGQjGtj
gSgnSJJCGSGpGSrwgfhchmmmHzcrHDmbrmMm
bVjstCsSstCLCrbSLnMpdMndcLddcqcpHR
wPZJQJwtBfJZmgBwPTcpTdcnfHMppcGMdG
gmFJzwPJJtszvNhCNC
DmjZDMZWDqGRqqRpHmmRLTTNTPTfCQJQQLJHTClc
FtzfvrfFwVgtzztgBLJNcNlTcTVNNQLN
vgsdbzzrwtqWfWRpZDdZ
rJhqRhLHhdcQqdHqfQGfPGstgGPlWttM
DzCpDDmnNCmBZBZnVBmZzBGPfsbglfNPwgPGPMWsWWft
BZFnlmpBpBzDzVZmhFHFrrrchhRqTdrc
DWCCWFNqdGFdPVcb
HllttQsTRlJlsblrHlhdmPLVcVcTccndLvPLmL
HSlstHgJltghhRrzNBNDzSwMjNZwNb
dzGSHCWSsGVVSdHVHHWWVVDCgJDpQqLTTRJpgmTLRmJTTpTR
BvNjMPZMBtBBMvvNMNttlhLQqCJpLmhTRQqQJgRJLQQg
llNncBlMCwwMnwPZrGsVHzcfFGdHGFGs
JfZhphMMQmFzDTDjSdrQjQ
sqHCbCwBVtbqbCqtrWdjzlSJTlrTSWBn
bHcwbGCGRssNscwtHNbwvmRFvpFFJFvLZMmPLFfv
qBCrzznVmDCmMMDNgrgcrvHHcgbQcW
TTTsdJRTRhhlsgbvbdCFdbWvbQ
JhGGlfRlJsnCMDMqjmfV
rqLLvDLtStDLQhQDQrQhhNdsmWdmmjjnssPnTMnTzfTsWT
ZRFFpgCgppcBcnjTsjTMTfPFMP
GCZpGlwJwBgGHcJhSSHLDDrNqrMtNq
FsPFqsDNZFNnZrcBmWfWWQ
lSnRlRTvgrWtctTmft
SMbGbbvnGlnSDwGqLwNCqNVD
dPQDcBwJJDgDTPgGgQTBVjSsmLhLTrLmjSLpjSLh
MvvZRHtMtbCNvCNCNtNvbRfBSMSrjmLpjnjmVhrVSLsnnmSh
qHZtbBZfRztbHbCzNRHPQgJPJgGgglFPPFqdQD
MsBsVDspRPfPlhMl
zWnCFzHbSCwqNmPSjmGlsmfN
FnHnFbFzsHHCCgzCzbBptVppgvvVgVrpBrJt
pTLntptZjQLfVDjQTDlVJCSWNCPSCCsSNmFlNslm
BBHbqGHHqgwSWSCCWwZWWZ
qRzbhhbzzrHdRRHhRHvzZjfrVTrppVQttDfcQTfp
DHsdHPHHsHMsRmhMZZQBtljgZGtC
NFnCbFznLVJbVrjhQthjGBLZBjGL
wNrfFJJbCpNnfbdwDSDHsvsHmsmH
jLZRjnMMjJhJnvtQbdHfHZbvHQ
mBzwptCWlcFCwsHSTpQfQHQfrpTb
mNltzmsCNmFzGwCBllGRgRgqjgLMnGqjnPjV
ZqqcqmVVtbcBMFfFMcQfgphJ
HLWLDvWjjLwTWzzvGLThQQshQllgJDJgfbffJQ
vHzLvrwwzGzTRGzzLLRPRwRdSVdnBBdSbBSVStbNmnrmZS
TWVVvPSgwWSqcRgRwbRRcqshsfFzzzChTGNHzHhhhCsG
njZrjMLlpmDmGfSGtrNttzCF
ZQBmZdDBZRRPRSBgcb
TpntvdpnZDptnbnTDGtSFSlFmzCzzmSFRjqlZj
MWrNcWRMlgqzMjzq
NPwsPNrBNcVHNNcJHBNBcJwwttDvGVnDptVRtbnTtGvVGtGG
tsbbvvSfnqvzQLLBjfMLdd
gJRmRNmJNchgmmrFJhFgWJQMwBnjwrMBVQwQTBdLdVQj
GcGpGGRGJgqstvpbnCqb
rsHcrbZHBTTtLtNSwwHLLJ
mFqhWVsjsVCjQlNJGMwMlMMGMh
QggzffQRCfgVFWzzCQffqfZpZDcRvTTBTvvZnsdnddcn
bPFMFFBpMlFfMZMpHGNSrNctJcPSSchJchPt
zCgwnmgzQDnQgdWWQRgqSrqLSqSgssLNJhgJ
rQCQQTrRRmDBFfbHBFHZbT
fzfPQsGrrMMjtHtBHs
SwNNDqwhWpVTwbDGGDmwSVhZRZHdbCtgBjCRjMtbBHtRMd
vVTGvVGNvPPvQvfncJ
cwzMJbclHDPqfJQPfq
rrqjjTBrqqBjRCgTjrRjNrsGPDhDFGCfWGfPFfFPGWfD
BZTTSTZgjbSwVptvpq
PPPPJpvpJsJwPHHPsJdTNZRZZZjTFFmRRRNjZd
qbWVfChDCDnVVDGfnSFNNjRLmNfBNLQjLjmBRm
DhFDhbnWCDhGcbJPPwrsrMwrvlvc
lFSDTwHTSwlTNwFFlwNcFFpjLZvZqvnqLPnnWbgngbbncqbZ
rzQfMzRGrRGJCffBMGdGsJZWWnqWVqdPPgNvvVZWPWWn
RJrttBtNQCsNzTpShhHFDwFlth
QNzQFjNFrQPNbmPpqTTDGswWmB
ggHRcSlcCVCSzMVqDGwgqTWpsmqwqG
cltzCZtLClHRRtMZZLQjfNvtrJfhvrddvNNd
mcfWHffBFnQRQlTFdv
wssSLVbbzDVbzbggzSzNshNMnvnljRdvQRlMBjvQdnCj
bhDzVSSJDDJhDLBwtbDzzbbWppfpcmWGmprqqGtqprcHPp
rpVFrZpgHWSZrFPqhzwcqPwmcVBD
vMTnQJjQLCbljvvQzTMbTjPNdBLwwDhmhNNqPwmmhhBh
jvGjjQJnrspGHgFz
sjssjtZlcphZHwWvcrHTwWJH
qDdzzrFNNNDGdFDzzVBVVvfWJPfgPmgWPgvwVH
nqMQGDrnLGnqqLNqjtCZZjsMhZhCMbtl
JJJsLFmzsrFlSpzPscjgHhnRnmvcjqRvvj
fCMQbCbTjjqTGhjc
bfdbWdCddfBbtCfbfbqVWQQpPlBrJLJJSSLwppFssFzLzp
pdbbzlffWtJbgQwhcphQcCCg
vHvLFvVLvSfFRLnRFRNHjPjggcssQcjjsnwhsPCC
vGVGGFFVHLTvDRHDmBbTzfZWMdJZlfMm
wjCbjQgjTQhNNzgWQCWrDFMZmZDZDCrrMDpLpL
czGSPznnRGGJGGlVVRVBGGlBmDDcMDFDDZLqfffZFrrZqFpZ
JPGlvBSJHVGnVsjvQjjzwdwjzd
MFlWQHDTpnpsFNNQllWFWlhzjGgrgDzGGhGGjvmZDZrh
PtTPcTLbBCVPTRVcvhjmmhVhSZGGgvZg
JLPfCwPbTbBPJCfblplMpqWsMpMwWHQn
QbHVBBzWtzHBNtBwQSgqhqSbFgRLjhmqqj
ZnCnMcdsDnJTncggFJwRmSwgRFmL
sTMZpGDvsZcMpcvTCPHwzrfzrpzHpWBrWz
PMdJWwJWHFWJnNzbDlfbCfMvbl
rZgttrFptFFcBtccbbCDvgfbGCGGgGDz
QsZBmsrFscrVrjQJjJQRJWWLwq
GwNNJwwRThwrWfhh
SmQqmzsjHssQzCbvsmSSzsQTjWpFTTfFfThchhFTBBfppB
mmbHbmtmCzzQZzQRdZJhNMdMlRMglh
rrsPbncQvvgnnrTdGDVcCdpZHHZp
RwwwhjLLqtJFwjzwtwmwwGpDZVdGDVdZBZDFHdHZCp
zhzwLhhfffLtjNChgWbbrbnMvPrMrrfv
tQMtQtTSBFtSmQSttMggMtbtnTnPrZvrnzNNTGZvrZZdLdnL
HqhwDpDcwlHqpVrrFzvFGpZrrzrP
RwlhhjwRCjVfjDbMtFWBWJMgWjWm
WpWVlWzsGlBJpspNclNlhhhmgzrdtzQMQttzMmtt
RfnPRLTPDHRdPbwvvntnSrFgmvnmtm
CwqRDCCwqCwbCTqJcJBNcZqdVcBlpJ
tpfnNBsGGNRppRCgfgRRCRQJGMPPWdwMJdWFFwjVzGPJ
chLSchLTbLqvqcZLlvvLqbmldMzFFWdzVSFWFMzQVJwjQjdM
rLqqcjDrcvhRsDfHDtNNnN
DjZjvTTDqrtTZZSMcdRdmRJrcJNc
HWgPGVhFPgnSVtnJcdMs
FPLfBwCWGPfCwfLHCCDBZlbDpBjvqTtDzzDj
FJNqNFgNFssqGGqBsTlMVcgVrCwLwlhcrw
fRZzDmDZvvDdZbtdpDZmbrThrLMCvcChwwlSTrvMSr
zmfZmtZmpDmbfWRDDZdqFljqnNQjGWnsjFqGsG
rMdMWddmJmvdSdmWfWMddpVRqRFVHRRqMRRPQMRqRq
tDGtGGhLjLLZNLjjNgNthGtqHTVqRVVpPDRpHHVRQVRPPR
ZlLtzNjgsZZlssLgtjNpfWfJvlJrrvCJfBmBfn
hqpWvFJsJFNHhqMWNhWvWRmmDcDMLcwZnjcwnjRnjn
LdrlgCCrSSTrTnwRjmwRQZwdwG
PVlfClrLlLlfggtBPzHHhHFbWzJNbvqJFNqF
TbbQtnDtbGGjGlGsGHpJJmFWFJJrBWWFlWrS
CZzzNzzhddNchhMhhRVjpCBwBrCvJvpmSCvrwJ
fhZZhddRjRgZzMZRzPjPTsLGQtHLTHTbDPQTtqPT
nHnWsQNQQWTWQshwjBJJJmHwFBwm
VZZpfbffZVvbSbGfBhSwmtmmJlmjJFJJ
bpphpMfMvMzDbMGZgQNrrngzdTsNqWdd
VPNddVTPPmdnVcPVZcdTmcDbQTFjMpjtFzbMtFjzsFTssT
lJCllWCrgvRlgwlJfRRvSzjSjQpbzMHpbwMQpszM
fRhGBBJJCgrNLsNPNVVhNq
pLrVDgbNbjVplpsltHBqWSqhSQcHDttH
MCdCwCGTmnTmmmvTTCwCqNhHQhRWcwHWBRHSqSQH
TNTFFPfffTvFTJvTPCPTFfGdzVjspVLZglJbsbZpVblrzjlb
cdPzFrldgcdCrnlznPzrBNRssLLBbVNVZsLHRHdm
wTQQwvvtqwqcGvTZmVHBbVLLBbRV
GWJSGfJWcjQwhQQWjqJhhGfgpMnMzDnpMlPpMnDlMrzl
pMhqTTsSpdBPpNBshsdMMTQFvFlQtQWCRQlCllVFqVqG
dfcbnmrnjzRFvGQQGvfv
mDrjLLLcJjLhpZSSJMdpph
NGZNwqFqZhhcFSCfRzwdzRfCzVRw
QTTmBTsWQWJPPCvzvpHPzdvVFR
bsmWTBbQDbmbLQQMsWWQchgqLqhGGGGZLhSFjhqS
HgmGlgsvBBDgBGCdHHvHwCGwhZJWhTjSdhTSFFFhJtSJTJhT
RQfVrfQNszMQfpMzpNnfLbtjhtSbWJWFWtFFtFJtFSZq
PNzLfnLnBCPHgsgC
mTZGgCdNSNmCQLLpPnDhRlGhpV
vWJHWFsfHMWBBFbBsjfjHrFfLRRLPPnpLthttRVPLSnhSPbS
fzMrBjWfBrzsZCZmSTgQzcNN
mgmCZCMgmnZmZgBZpgpJfbQfwSQPDTdfdwSDfwhn
sHhcrWLcFlzHcHRNNFvNFcFPwDDTWdddDdqWbSTWDPTTQS
RNsslsRrNcRNvNRFFNvVsghZBJtVCCtCtGghjhGBGG
gchrcRRdnRwPPnvQ
CVCCSrDjFHjVDbBLFGGBSvwnwNMnMsPPNsNPvwPQVM
lHLCTHGDCbbjFTTzdWlpcqfgcrdzZg
fRDPsDsqqJttttJSzPDgJWQCbQQbGMWCCnGGPVGVQQ
rTTBvZhrvBnWWDWCbZWW
cwLlTLpjTwBFLLhgfRRfmRqRDmRdjq
sprGGPTrJTsGPzszqGzNtTtpfbQddQSQSDFDFvvbZvwFbbfN
LWWCMVmwMmgWFQfFDDvZDgdF
mlMmRVCWVMmmHRjVCmjHWRhMzpTtlrlPzrtzwlsGPrpwtrJp
tsfwwfjfdfrtrClfvwvvLnTHNmvLHcNccRNcvNWH
qQSqZqFQRBzghDFncHgmccHNmWcNmM
SQJphFJzRDSsdpVlllrCrw
vGQqLQFvBvLvdNnvjnvNDc
TRJwmWmZWlCCmzznbNhhbDhRgj
CCTtDTlmDTWTmDmZZlVLLsFfstfFFLsBLQfF
cfWflMmWWlWfPWBhBlQtLmmvrrrvCLjvRTjLLwwr
gSgbsbgHdsjzHbqbdVDLZLvTZwLTvSrZrFvZLw
sdbJqDNdjJNdsJBpBWpJlMcfcB
FHlMHPqDLlPctgHSnttCSC
zhrmBrTwJTjBmQcSQvQqbtwGvg
jBjmBmJjjjRZTBzhhrBJLDdZqfpDMdfWWlDDLMlV
zPVdbsBzZdwqJGhrLTvNNJqH
tmmCgCPCDDnptHDjNvGvhrDvLv
pRWRlpSpPllClnpbQVQwFFVSQFVBZz
nDrCvmvMnMSmsCvblBzzCZplbJlTbZ
FNRtFWRfcGqFGQbzlZTQqQTBbd
GRwFfNtwFRNFGMvBsnnwMMMBjn
LVTBjjlJCDrnJzJNQR
GsGGsggGpfhgpchgdqzbMzzhzQRnnMRrNzzR
PwWFqFGpwWpdWgfsGggdmjCVHPHlCCCVZNCjVmVj
qVTsCWwbCsPlCVfcbvfPDgLzbzDDhrzRrjgZghgr
ntmHmNpSQNGtntNttmSdSdBdjrrDLQZQLLhRrFFFRDTFZhDF
mtMtBNTSNBpNJStMGSdHppNcVWPsWvqVcsVJfwwqlqWqlc
vvWzLvvdpZDvhTpcrLcTTLpdwSPnCfJwCMnQSMwSnCGJrnwr
ttHVmVNNsHBBRsHbMMwwnjnjBfjJwCMP
tsVllgNVqbRlfplldDvDWT
mLjLsQqLQqsBRvvlRBLRlT
bhgtDDhCtmptmTTS
nfmdbggwGWrfsPzfWq
JpWDcSGJpGzsHPSSlbbd
wVRqVZwwRwPDwbDddH
VtVVVLthLVtVgfQLRTNtqDcCcJBmmWMWWprpFrcBJWNp
dhhhDtmLdttdPlslGlRFjfzBBpzzRpGJ
QMrVMwbVrrbvVVCrvcnqQQrrSMBJfpjFSzfjJFMFRWSpjjFG
cwvbHHbCqVchRDHgDsPTdt
CgVNCtDsDtJGZZGqMMGhDq
cLRnSHgWcRdLHWSSRLjQdlHBTTPcPwwhzqzTMBPTwhPPwP
HnnnglnWWgdRjlmQNsNFmJCFJFvsJsNN
hfccLbjhfSRbfDZjFRJzrlvlwwlnnFrWwzqr
TCsPLNtQdpdQQVtVNvJNJWlzJzwlrvJl
pHtPsPtPtCQfbRHHDHhMLh
nWRWgLtWnfTcZNNsscfd
JMGzMVJwMVTvzVQFGHMMmPdddsPsCjldlHPcScNPsP
vGrMQQmmvTQzMJpghWRWgpbbBqLbLR
WSbhFbPTpRfTfPdhpfbhSbfPQLzlQlzlHvtQsvlltlsgHdgQ
pZcGJDZNGcVrJwrDrrnvtNvlNzsgtgzvvsgt
qmJZZJcBqwrMJcVbWfSPPWpmpjmSCF
jHVjjCcpNrDgjsfB
ndqllRvJQtqlQQTRWllFNDrsMZBfDBLvNMNDfsbZ
qTFnWJqdWRdqWRlnTRnQGnTmwwSHCzpcGNmHNcPVcHGmCz
pZCpBhDfvgBVZQGMMVZVlq
sLsLTTSssjPnTNbFGRGFPVHqMMRF
TsNSccnjLdcsLjdmjWvWvBhfmvWpCGhGhD
VWFFFPMpPVSMbTppHTnHTbRH
DtvfNdBNddDNSLjsvDTTHnzzHwrTrwsrwqbT
dgBLNffdgjjtfBQSvgNjNDlvMcQJmJJmZCMmVVVZFPFcPMGG
VWsQLHMVVSNRShWLhNSNLjbbbddbpDZDddcbZdDRztpd
FPlhhgPvThGFJndnnCCnJzzdCp
qrTfmllGvfvGqwNMMMsffsQsNh
NsmFqNlmnQRbCFsmJgSffpPcbvSfrVvpgS
LhZGDZhhwtDHMwDdHGhDjDpTzzPdzgTvcPvpSSpPrdrv
jgHMjBLhwtZMHMHmJNNJNFlBqlBJNn
bznSQggscgMcSTTfJbSQzQFwClMhmCmthClvMwFLwhZL
BRWBPBVVPjPNVHpVqlqrvtwFqmmLqltZmL
WDVddNHNvRgccgsDsgbT
sNgnQLtLLLPPnsPpqdqjBclpGWjcWjBG
rVCChSZhVrrwqVDVHSHmMjldGfJGfHddJGJlfGjGJj
CVZmDvZCmmhFVVrCgTNbbnQFgbsqNqNQ
WmMmSSfJNRRPfJRMRMtllCgdStgbgttgCdDd
QGBrvzwBczlgqCtDbvDq
QQpBGFrLQjQzGVVRNjPmNNWMbW
gGljnJhnJtllpNVCHWcccdTdjdmB
bLfSQDSMSHmBnwCB
LFMDrbFfFQZQRzLZnbgtlsRGtltpgNhgPpPG
cRThZZchCThtgTRhZTRtjWFjWNwqCjGmwFjqqffC
DPDPGzPMHDbrpqjfwrjqmjmp
JVHHDdVdVbvGMdnVdQVdDbHcRZllhRtgStRLThRSTcBTvc
lQWPSBrrPZGgPglGssDfHnWsfDFHHvHh
TDCqpttptJNLtwNpbwTqzqHshsvsMMFnmHMNfssmvmvf
JCjqVpDtrBjQjrlj
wFGWGpFLvCczNSWWsz
tlfgtftjlbtHHlDBsBzmQQnsQDQsCn
gjfrsVqVgPlfqhvLdvdwZhGq
pHpZHBSvRvRCBBZCTMngRnWndnRmWcgg
jsfrfrjJFDwDDMMggMCGWGcfmG
qbCszCjtCjQsQrtZVBHBHvBvqLZvlp
scFzsPScNgNPNgQzpttlCBCwpLrMLCrDdljLwq
TjfGZZjVwMZwMLwr
vnGbWTvTmFRjQFQPsb
bVLrzqrzJVgJbbtVrWJVgppcBCzBvdzwBCCBHDcBvc
hflPQnMQmQSRlQMPNRTHwwHHHqpHpdfwdBCp
hFhZMhqSNMNbrZgWWGWJjZ
NJsgNjJlMHQrwnRgSRPwrP
tqpQtTFpFvbGpzTTWSrnSbrhwChCnRfrCf
GtcvGqQpttzcqdFzWppDsZMJjBBsBJcBNmBjMsLJ
lGfZGZhFfhdSWqmFFWSS
wDRDPLcDnjtWbSmqrSCSLC
MPwmtVnVMjztznHPgQhQfJfvvHHGggQZ
llTspLllCHmLHHndldqHdlLQQPSBQczZSFDDQZSNGcGG
jMhwvVrRjbRhFBZNGPcGNN
wVtrrtRwrfrwftjVjwWvMrRpsqsnsHsBglslCmTsdWdHTd
vPvmTGgDPRvGpDPGPqGHQnWJQJMBBzJBlBQWlHWl
bfbwNsmwFdLjbfrrLsSfLNQtMllznBzJQZMQtMlZZnnF
frssSscssNfScCjfSCwjsDmRDpGmDRDvvvVcvRDvRp
LtlPZPjBTbWsWJVJVzdT
nnprqhrqmzfrSrphqfCChVVGVDJWgSHHWgWsRDVHWd
nrmppNqhcCrfMchcMCncqbzPZvlvlwbBNjPjtNjZjL
FPWsFdSspVbbbtWVvl
CCHnnfHHvCwtVMhzlzDllC
LrGnjGfgfvcwfgrLrBjrBLgwdBTSRBFsRZdRsSqFFSFSSPPp
whGCLqsrjgGhhGFqrCCFGCGzTRTZJcNnzlLTnznNHcnzTH
ddvVmbfvdvVbDVQdvvdSzpNcnJzlzSRHNJpnJcSc
BPdvfQdWtPDDPfDvDQVVPmbhssCGGMqgFCFMqGMWgMjrRw
PSLbGmWPSPLQbMTPWGFWltthdDdrmBDHhdDdczzDRh
VfCngVfgsZwCftrZdhcZrdNDzz
CjVJJJqnJwQhWPPLQlGj
ntnnQmTQTQGVWGNGNNlClG
jDffjMSvqjHzHHzwNVwNVcCddPVNdD
ZszJsrrZMjsHqqvZJLRQCbTRQbJmThbt
BgLHgFDsJNWgQgflWd
mnVVcCHnCGRcVnZSjmlthftMQddlfhQctNfW
qbSGqmHSTFprvpvTTL
dvdTMvvpdLpTcSLvdLLMmhfFBftwCNhRwRNjtCTRCf
lshQWgsgrHHqlFfRqFjRFfFwCB
rsgHQbJbrsGHHlgQHgJrlHrPZdhdpMZGDSDpdPLcZhdvhZ'''

# COMMAND ----------

import string

items = inp.splitlines()
alphabet = '0' + string.ascii_letters

total = 0
for line in items:
  half = len(line) // 2
  a = set(line[:half])
  b = set(line[half:])
  intersection = a.intersection(b)
  total += alphabet.index(next(iter(intersection)))

answer = total
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you finish identifying the misplaced items, the Elves come to you with another issue.</p>
# MAGIC <p>For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the <em>only item type carried by all three Elves</em>. That is, if a group's badge is item type <code>B</code>, then all three Elves will have item type <code>B</code> somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.</p>
# MAGIC <p>The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.</p>
# MAGIC <p>Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is <em>common between all three Elves</em> in each group.</p>
# MAGIC <p>Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:</p>
# MAGIC <pre><code>vJrwpWtwJgWrhcsFMMfFFhFp
# MAGIC jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# MAGIC PmmdzqPrVvPwwTWBwg
# MAGIC </code></pre>
# MAGIC <p>And the second group's rucksacks are the next three lines:</p>
# MAGIC <pre><code>wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# MAGIC ttgJtRGJQctTZtZT
# MAGIC CrZsJsPPZsGzwwsLwLmpwMDw
# MAGIC </code></pre>
# MAGIC <p>In the first group, the only item type that appears in all three rucksacks is lowercase <code>r</code>; this must be their badges. In the second group, their badge item type must be <code>Z</code>.</p>
# MAGIC <p>Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (<code>r</code>) for the first group and 52 (<code>Z</code>) for the second group. The sum of these is <code><em>70</em></code>.</p>
# MAGIC <p>Find the item type that corresponds to the badges of each three-Elf group. <em>What is the sum of the priorities of those item types?</em></p>
# MAGIC </article>

# COMMAND ----------

total = 0
for i in range(0, len(items), 3):
  a, b, c = (set(s) for s in items[i:i+3])
  intersection = a.intersection(b).intersection(c)
  total += alphabet.index(next(iter(intersection)))

answer = total
print(answer)
