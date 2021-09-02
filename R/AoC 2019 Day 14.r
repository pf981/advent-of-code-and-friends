# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/14

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 14: Space Stoichiometry ---</h2><p>As you approach the rings of Saturn, your ship's <em>low fuel</em> indicator turns on.  There isn't any fuel here, but the rings have plenty of raw material.  Perhaps your ship's <span title="Yes, the acronym is intentional.">Inter-Stellar Refinery Union</span> brand <em>nanofactory</em> can turn these raw materials into fuel.</p>
# MAGIC <p>You ask the nanofactory to produce a list of the <em>reactions</em> it can perform that are relevant to this process (your puzzle input). Every reaction turns some quantities of specific <em>input chemicals</em> into some quantity of an <em>output chemical</em>. Almost every <em>chemical</em> is produced by exactly one reaction; the only exception, <code>ORE</code>, is the raw material input to the entire process and is not produced by a reaction.</p>
# MAGIC <p>You just need to know how much <code><em>ORE</em></code> you'll need to collect before you can produce one unit of <code><em>FUEL</em></code>.</p>
# MAGIC <p>Each reaction gives specific quantities for its inputs and output; reactions cannot be partially run, so only whole integer multiples of these quantities can be used.  (It's okay to have leftover chemicals when you're done, though.) For example, the reaction <code>1 A, 2 B, 3 C =&gt; 2 D</code> means that exactly 2 units of chemical <code>D</code> can be produced by consuming exactly 1 <code>A</code>, 2 <code>B</code> and 3 <code>C</code>.  You can run the full reaction as many times as necessary; for example, you could produce 10 <code>D</code> by consuming 5 <code>A</code>, 10 <code>B</code>, and 15 <code>C</code>.</p>
# MAGIC <p>Suppose your nanofactory produces the following list of reactions:</p>
# MAGIC <pre><code>10 ORE =&gt; 10 A
# MAGIC 1 ORE =&gt; 1 B
# MAGIC 7 A, 1 B =&gt; 1 C
# MAGIC 7 A, 1 C =&gt; 1 D
# MAGIC 7 A, 1 D =&gt; 1 E
# MAGIC 7 A, 1 E =&gt; 1 FUEL
# MAGIC </code></pre>
# MAGIC <p>The first two reactions use only <code>ORE</code> as inputs; they indicate that you can produce as much of chemical <code>A</code> as you want (in increments of 10 units, each 10 costing 10 <code>ORE</code>) and as much of chemical <code>B</code> as you want (each costing 1 <code>ORE</code>).  To produce 1 <code>FUEL</code>, a total of <em>31</em> <code>ORE</code> is required: 1 <code>ORE</code> to produce 1 <code>B</code>, then 30 more <code>ORE</code> to produce the 7 + 7 + 7 + 7 = 28 <code>A</code> (with 2 extra <code>A</code> wasted) required in the reactions to convert the <code>B</code> into <code>C</code>, <code>C</code> into <code>D</code>, <code>D</code> into <code>E</code>, and finally <code>E</code> into <code>FUEL</code>. (30 <code>A</code> is produced because its reaction requires that it is created in increments of 10.)</p>
# MAGIC <p>Or, suppose you have the following list of reactions:</p>
# MAGIC <pre><code>9 ORE =&gt; 2 A
# MAGIC 8 ORE =&gt; 3 B
# MAGIC 7 ORE =&gt; 5 C
# MAGIC 3 A, 4 B =&gt; 1 AB
# MAGIC 5 B, 7 C =&gt; 1 BC
# MAGIC 4 C, 1 A =&gt; 1 CA
# MAGIC 2 AB, 3 BC, 4 CA =&gt; 1 FUEL
# MAGIC </code></pre>
# MAGIC <p>The above list of reactions requires <em>165</em> <code>ORE</code> to produce 1 <code>FUEL</code>:</p>
# MAGIC <ul>
# MAGIC <li>Consume 45 <code>ORE</code> to produce 10 <code>A</code>.</li>
# MAGIC <li>Consume 64 <code>ORE</code> to produce 24 <code>B</code>.</li>
# MAGIC <li>Consume 56 <code>ORE</code> to produce 40 <code>C</code>.</li>
# MAGIC <li>Consume 6 <code>A</code>, 8 <code>B</code> to produce 2 <code>AB</code>.</li>
# MAGIC <li>Consume 15 <code>B</code>, 21 <code>C</code> to produce 3 <code>BC</code>.</li>
# MAGIC <li>Consume 16 <code>C</code>, 4 <code>A</code> to produce 4 <code>CA</code>.</li>
# MAGIC <li>Consume 2 <code>AB</code>, 3 <code>BC</code>, 4 <code>CA</code> to produce 1 <code>FUEL</code>.</li>
# MAGIC </ul>
# MAGIC <p>Here are some larger examples:</p>
# MAGIC <ul>
# MAGIC <li><p><em>13312</em> <code>ORE</code> for 1 <code>FUEL</code>:</p>
# MAGIC <pre><code>157 ORE =&gt; 5 NZVS
# MAGIC 165 ORE =&gt; 6 DCFZ
# MAGIC 44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ =&gt; 1 FUEL
# MAGIC 12 HKGWZ, 1 GPVTF, 8 PSHF =&gt; 9 QDVJ
# MAGIC 179 ORE =&gt; 7 PSHF
# MAGIC 177 ORE =&gt; 5 HKGWZ
# MAGIC 7 DCFZ, 7 PSHF =&gt; 2 XJWVT
# MAGIC 165 ORE =&gt; 2 GPVTF
# MAGIC 3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF =&gt; 8 KHKGT
# MAGIC </code></pre></li>
# MAGIC <li><p><em>180697</em> <code>ORE</code> for 1 <code>FUEL</code>:</p>
# MAGIC <pre><code>2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX =&gt; 1 STKFG
# MAGIC 17 NVRVD, 3 JNWZP =&gt; 8 VPVL
# MAGIC 53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV =&gt; 1 FUEL
# MAGIC 22 VJHF, 37 MNCFX =&gt; 5 FWMGM
# MAGIC 139 ORE =&gt; 4 NVRVD
# MAGIC 144 ORE =&gt; 7 JNWZP
# MAGIC 5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF =&gt; 3 HVMC
# MAGIC 5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF =&gt; 6 GNMV
# MAGIC 145 ORE =&gt; 6 MNCFX
# MAGIC 1 NVRVD =&gt; 8 CXFTF
# MAGIC 1 VJHF, 6 MNCFX =&gt; 4 RFSQX
# MAGIC 176 ORE =&gt; 6 VJHF
# MAGIC </code></pre></li>
# MAGIC <li><p><em>2210736</em> <code>ORE</code> for 1 <code>FUEL</code>:</p>
# MAGIC <pre><code>171 ORE =&gt; 8 CNZTR
# MAGIC 7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP =&gt; 4 PLWSL
# MAGIC 114 ORE =&gt; 4 BHXH
# MAGIC 14 VRPVC =&gt; 6 BMBT
# MAGIC 6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW =&gt; 1 FUEL
# MAGIC 6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP =&gt; 6 FHTLT
# MAGIC 15 XDBXC, 2 LTCX, 1 VRPVC =&gt; 6 ZLQW
# MAGIC 13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW =&gt; 1 ZDVW
# MAGIC 5 BMBT =&gt; 4 WPTQ
# MAGIC 189 ORE =&gt; 9 KTJDG
# MAGIC 1 MZWV, 17 XDBXC, 3 XCVML =&gt; 2 XMNCP
# MAGIC 12 VRPVC, 27 CNZTR =&gt; 2 XDBXC
# MAGIC 15 KTJDG, 12 BHXH =&gt; 5 XCVML
# MAGIC 3 BHXH, 2 VRPVC =&gt; 7 MZWV
# MAGIC 121 ORE =&gt; 7 VRPVC
# MAGIC 7 XCVML =&gt; 6 RJRHP
# MAGIC 5 BHXH, 4 VRPVC =&gt; 5 LTCX
# MAGIC </code></pre></li>
# MAGIC </ul>
# MAGIC <p>Given the list of reactions in your puzzle input, <em>what is the minimum amount of <code>ORE</code> required to produce exactly 1 <code>FUEL</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

library(tidyverse)

# COMMAND ----------

input <- "2 JNLZG => 7 SJTKF
1 BDCJZ, 3 NWCRL => 5 PMQS
1 TNRBS => 2 LHNGR
7 TWHBV => 6 FLQSP
4 DNLQF, 3 DRFL, 4 RSHRF => 6 HXJFS
5 VHSLS => 7 DZDQN
11 STPXT, 16 XRTW => 1 CTZFK
5 BXWD => 2 RVNR
1 XRTW, 2 SJTKF => 2 FPKWZ
1 JMGDP, 3 TJLKW => 7 FNLF
26 DTQTB, 16 TWHBV => 3 JMGDP
1 DFRNL, 1 LHNGR => 9 NWCRL
2 NWPC, 2 LHNGR, 3 QCHC => 8 HPBP
10 CSKJQ => 4 QRSD
8 FVLQ => 6 WMBVF
11 NPVB, 12 QRFV => 6 STPXT
3 SJTKF, 1 NPVB => 7 GWHG
4 DKPKX, 1 SJPWK => 5 DTQTB
1 RVNR => 8 XRTW
67 KGVR, 1 ZLJR, 4 TBPB, 19 KPJZM, 8 QSWQ, 12 DTQTB, 15 QRSD, 4 FPKWZ => 1 FUEL
20 LHNGR, 6 DNLQF, 9 TWHBV => 8 SJPWK
1 QRSD, 11 HZWS => 5 KGVR
2 CTZFK, 1 DRFL, 1 TNRBS => 5 DKPKX
14 FVFTN, 2 VLKQ, 12 STPXT => 4 TWHBV
1 FXWRB, 1 BXWD => 8 FVFTN
12 NPVB, 2 KJWC, 1 JNLZG => 3 NDNZP
13 NPVB, 7 HZLKM => 3 ZRMQC
2 HXJFS, 14 PDGB, 2 FNLF => 1 FVLQ
7 QRFV, 10 QRSD, 6 FVFTN => 5 DNLQF
4 XQDC, 2 VHSLS => 1 BDCJZ
9 HZLKM, 1 NDNZP => 6 DRFL
147 ORE => 4 BXWD
6 DNLQF => 5 VCBFZ
1 FVFTN => 8 TNRBS
1 RSHRF, 2 PDGB, 1 MKWH, 4 QRSD, 11 DNLQF, 7 WMBVF, 1 HJHM => 8 QSWQ
6 PMQS, 2 HNTS => 1 WNVGC
4 RVNR, 6 GWHG => 2 VLKQ
11 DRFL, 1 PDGB => 6 DFRNL
3 WNVGC, 28 PFZN, 14 HNTS, 2 WMBVF, 18 VCBFZ, 2 HPBP, 2 PDGB => 6 TBPB
2 XQDC => 6 HZWS
7 JNLZG, 1 BXWD, 7 FXWRB => 5 KJWC
9 KJWC, 7 NDNZP => 4 CSKJQ
194 ORE => 9 FXWRB
2 VHSLS, 12 MKWH, 2 FWBL, 6 TJLKW, 9 HZWS, 11 ZQGXM => 5 ZLJR
139 ORE => 2 JNLZG
2 TNRBS => 2 QCHC
7 DRFL, 10 STPXT, 1 QRSD => 6 MKWH
9 JNLZG => 8 NPVB
3 RSHRF => 6 FWBL
7 NDNZP => 5 PDGB
2 FVFTN => 6 QRFV
1 QRSD, 22 XQDC => 3 VHSLS
2 FVFTN => 3 HZLKM
6 ZRMQC => 2 PFZN
12 QRFV, 6 HZLKM => 6 XQDC
12 JMGDP, 1 KPJZM, 10 ZPKP => 5 HJHM
23 JNLZG => 2 ZQGXM
1 TJLKW => 9 HNTS
1 HZLKM, 12 PMQS => 5 KPJZM
7 DNLQF => 9 NWPC
1 FLQSP => 6 ZPKP
5 VLKQ => 7 RSHRF
6 TNRBS, 4 DZDQN, 6 TWHBV => 6 TJLKW
"

# COMMAND ----------

df <-
  read_lines(input) %>%
  str_split(" => ") %>%
  map_dfr(set_names, c("lhs", "rhs")) %>%
  mutate(
    chemical_out = str_extract(rhs, "[A-Z]+$"),
    n_out = str_extract(rhs, "\\d+"),
    chemical_in = str_extract_all(lhs, "[A-Z]+"),
    n_in = str_extract_all(lhs, "\\d+")
  ) %>%
  unnest(chemical_in, n_in) %>%
  mutate(
    n_in = as.integer(n_in),
    n_out = as.integer(n_out)
  ) %>%
  select(-lhs, -rhs)
df

# COMMAND ----------

zero_if_invalid <- function(x) {
  if (is.null(x) || is.na(x)) return(0)
  x
}

solve <- function(df, targets = c(FUEL = 1)) {
  leftovers <- c()
  total_ore <- 0
  
  while (length(targets) > 0) {
    target_chemical <- names(targets)[1]
    target_n <- targets[1]
    targets <- targets[-1]
    recipes <- df[df$chemical_out == target_chemical,]
   
    # Take output from leftovers
    if (zero_if_invalid(leftovers[target_chemical]) > 0) {
      n_out_taken_from_leftovers <- min(leftovers[target_chemical], target_n)
      target_n <- target_n - n_out_taken_from_leftovers
      leftovers[target_chemical] <- leftovers[target_chemical] - n_out_taken_from_leftovers
    }
    if (target_n <= 0) next
    
    n_batches <- ceiling(target_n / recipes$n_out[1])
    n_out_created <- n_batches * recipes$n_out[1]
    n_out_leftover <- n_out_created - target_n
    
    # Store the leftovers from the output
    if (n_out_leftover > 0) {
      leftovers[target_chemical] <- zero_if_invalid(leftovers[target_chemical]) + n_out_leftover
    }
    
    for (i in seq_len(nrow(recipes))) {
      n_in_needed <- n_batches * recipes$n_in[i]

      # Take input from leftovers
      if (zero_if_invalid(leftovers[recipes$chemical_in[i]]) > 0) {
        n_in_taken_from_leftovers <- min(leftovers[recipes$chemical_in[i]], n_in_needed)
        n_in_needed <- n_in_needed - n_in_taken_from_leftovers
        leftovers[recipes$chemical_in[i]] <- leftovers[recipes$chemical_in[i]] - n_in_taken_from_leftovers
      }
      
      if (n_in_needed <= 0) next
      
      if (recipes$chemical_in[i] == "ORE") {
        total_ore <- total_ore + n_in_needed
        next
      }
      
      targets[recipes$chemical_in[i]] <- zero_if_invalid(targets[recipes$chemical_in[i]]) + n_in_needed
    }
  }
  unname(total_ore)
}

# COMMAND ----------

answer <- solve(df)
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>After collecting <code>ORE</code> for a while, you check your cargo hold: <em>1 trillion</em> (<em>1000000000000</em>) units of <code>ORE</code>.</p>
# MAGIC <p><em>With that much ore</em>, given the examples above:</p>
# MAGIC <ul>
# MAGIC <li>The 13312 <code>ORE</code>-per-<code>FUEL</code> example could produce <em>82892753</em> <code>FUEL</code>.</li>
# MAGIC <li>The 180697 <code>ORE</code>-per-<code>FUEL</code> example could produce <em>5586022</em> <code>FUEL</code>.</li>
# MAGIC <li>The 2210736 <code>ORE</code>-per-<code>FUEL</code> example could produce <em>460664</em> <code>FUEL</code>.</li>
# MAGIC </ul>
# MAGIC <p>Given 1 trillion <code>ORE</code>, <em>what is the maximum amount of <code>FUEL</code> you can produce?</em></p>
# MAGIC </article>

# COMMAND ----------

target <- 1000000000000
low <- 1
high <- Inf
while (low < high - 1) {
  if (is.infinite(high)) {
    mid <- low * 10
  } else {
    mid <- floor((low + high) / 2)
  }
  
  result <- solve(df, targets = c(FUEL = mid))
  
  if (result < target) {
    low <- mid
  } else if (result > target) {
    high <- mid
  } else {
    low <- mid
    break
  }
}
answer <- low
answer
