# Databricks notebook source
# MAGIC %md https://adventofcode.com/2023/day/20

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 20: Pulse Propagation ---</h2><p>With your help, the Elves manage to find the right parts and fix all of the machines. Now, they just need to send the command to boot up the machines and get the sand flowing again.</p>
# MAGIC <p>The machines are far apart and wired together with long <em>cables</em>. The cables don't connect to the machines directly, but rather to communication <em>modules</em> attached to the machines that perform various initialization tasks and also act as communication relays.</p>
# MAGIC <p>Modules communicate using <em>pulses</em>. Each pulse is either a <em>high pulse</em> or a <em>low pulse</em>. When a module sends a pulse, it sends that type of pulse to each module in its list of <em>destination modules</em>.</p>
# MAGIC <p>There are several different types of modules:</p>
# MAGIC <p><em>Flip-flop</em> modules (prefix <code>%</code>) are either <em>on</em> or <em>off</em>; they are initially <em>off</em>. If a flip-flop module receives a high pulse, it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it <em>flips between on and off</em>. If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.</p>
# MAGIC <p><em>Conjunction</em> modules (prefix <code>&amp;</code>) <em>remember</em> the type of the most recent pulse received from <em>each</em> of their connected input modules; they initially default to remembering a <em>low pulse</em> for each input. When a pulse is received, the conjunction module first updates its memory for that input. Then, if it remembers <em>high pulses</em> for all inputs, it sends a <em>low pulse</em>; otherwise, it sends a <em>high pulse</em>.</p>
# MAGIC <p>There is a single <em>broadcast module</em> (named <code>broadcaster</code>). When it receives a pulse, it sends the same pulse to all of its destination modules.</p>
# MAGIC <p>Here at Desert Machine Headquarters, there is a module with a single button on it called, aptly, the <em>button module</em>. When you push the button, a single <em>low pulse</em> is sent directly to the <code>broadcaster</code> module.</p>
# MAGIC <p>After pushing the button, you must wait until all pulses have been delivered and fully handled before pushing it again. Never push the button if modules are still processing pulses.</p>
# MAGIC <p>Pulses are always processed <em>in the order they are sent</em>. So, if a pulse is sent to modules <code>a</code>, <code>b</code>, and <code>c</code>, and then module <code>a</code> processes its pulse and sends more pulses, the pulses sent to modules <code>b</code> and <code>c</code> would have to be handled first.</p>
# MAGIC <p>The module configuration (your puzzle input) lists each module. The name of the module is preceded by a symbol identifying its type, if any. The name is then followed by an arrow and a list of its destination modules. For example:</p>
# MAGIC <pre><code>broadcaster -&gt; a, b, c
# MAGIC %a -&gt; b
# MAGIC %b -&gt; c
# MAGIC %c -&gt; inv
# MAGIC &amp;inv -&gt; a
# MAGIC </code></pre>
# MAGIC <p>In this module configuration, the broadcaster has three destination modules named <code>a</code>, <code>b</code>, and <code>c</code>. Each of these modules is a flip-flop module (as indicated by the <code>%</code> prefix). <code>a</code> outputs to <code>b</code> which outputs to <code>c</code> which outputs to another module named <code>inv</code>. <code>inv</code> is a conjunction module (as indicated by the <code>&amp;</code> prefix) which, because it has only one input, acts like an <span title="This puzzle originally had a separate inverter module type until I realized it was just a worse conjunction module.">inverter</span> (it sends the opposite of the pulse type it receives); it outputs to <code>a</code>.</p>
# MAGIC <p>By pushing the button once, the following pulses are sent:</p>
# MAGIC <pre><code>button -low-&gt; broadcaster
# MAGIC broadcaster -low-&gt; a
# MAGIC broadcaster -low-&gt; b
# MAGIC broadcaster -low-&gt; c
# MAGIC a -high-&gt; b
# MAGIC b -high-&gt; c
# MAGIC c -high-&gt; inv
# MAGIC inv -low-&gt; a
# MAGIC a -low-&gt; b
# MAGIC b -low-&gt; c
# MAGIC c -low-&gt; inv
# MAGIC inv -high-&gt; a
# MAGIC </code></pre>
# MAGIC <p>After this sequence, the flip-flop modules all end up <em>off</em>, so pushing the button again repeats the same sequence.</p>
# MAGIC <p>Here's a more interesting example:</p>
# MAGIC <pre><code>broadcaster -&gt; a
# MAGIC %a -&gt; inv, con
# MAGIC &amp;inv -&gt; b
# MAGIC %b -&gt; con
# MAGIC &amp;con -&gt; output
# MAGIC </code></pre>
# MAGIC <p>This module configuration includes the <code>broadcaster</code>, two flip-flops (named <code>a</code> and <code>b</code>), a single-input conjunction module (<code>inv</code>), a multi-input conjunction module (<code>con</code>), and an untyped module named <code>output</code> (for testing purposes). The multi-input conjunction module <code>con</code> watches the two flip-flop modules and, if they're both on, sends a <em>low pulse</em> to the <code>output</code> module.</p>
# MAGIC <p>Here's what happens if you push the button once:</p>
# MAGIC <pre><code>button -low-&gt; broadcaster
# MAGIC broadcaster -low-&gt; a
# MAGIC a -high-&gt; inv
# MAGIC a -high-&gt; con
# MAGIC inv -low-&gt; b
# MAGIC con -high-&gt; output
# MAGIC b -high-&gt; con
# MAGIC con -low-&gt; output
# MAGIC </code></pre>
# MAGIC <p>Both flip-flops turn on and a low pulse is sent to <code>output</code>! However, now that both flip-flops are on and <code>con</code> remembers a high pulse from each of its two inputs, pushing the button a second time does something different:</p>
# MAGIC <pre><code>button -low-&gt; broadcaster
# MAGIC broadcaster -low-&gt; a
# MAGIC a -low-&gt; inv
# MAGIC a -low-&gt; con
# MAGIC inv -high-&gt; b
# MAGIC con -high-&gt; output
# MAGIC </code></pre>
# MAGIC <p>Flip-flop <code>a</code> turns off! Now, <code>con</code> remembers a low pulse from module <code>a</code>, and so it sends only a high pulse to <code>output</code>.</p>
# MAGIC <p>Push the button a third time:</p>
# MAGIC <pre><code>button -low-&gt; broadcaster
# MAGIC broadcaster -low-&gt; a
# MAGIC a -high-&gt; inv
# MAGIC a -high-&gt; con
# MAGIC inv -low-&gt; b
# MAGIC con -low-&gt; output
# MAGIC b -low-&gt; con
# MAGIC con -high-&gt; output
# MAGIC </code></pre>
# MAGIC <p>This time, flip-flop <code>a</code> turns on, then flip-flop <code>b</code> turns off. However, before <code>b</code> can turn off, the pulse sent to <code>con</code> is handled first, so it <em>briefly remembers all high pulses</em> for its inputs and sends a low pulse to <code>output</code>. After that, flip-flop <code>b</code> turns off, which causes <code>con</code> to update its state and send a high pulse to <code>output</code>.</p>
# MAGIC <p>Finally, with <code>a</code> on and <code>b</code> off, push the button a fourth time:</p>
# MAGIC <pre><code>button -low-&gt; broadcaster
# MAGIC broadcaster -low-&gt; a
# MAGIC a -low-&gt; inv
# MAGIC a -low-&gt; con
# MAGIC inv -high-&gt; b
# MAGIC con -high-&gt; output
# MAGIC </code></pre>
# MAGIC <p>This completes the cycle: <code>a</code> turns off, causing <code>con</code> to remember only low pulses and restoring all modules to their original states.</p>
# MAGIC <p>To get the cables warmed up, the Elves have pushed the button <code>1000</code> times. How many pulses got sent as a result (including the pulses sent by the button itself)?</p>
# MAGIC <p>In the first example, the same thing happens every time the button is pushed: <code>8</code> low pulses and <code>4</code> high pulses are sent. So, after pushing the button <code>1000</code> times, <code>8000</code> low pulses and <code>4000</code> high pulses are sent. Multiplying these together gives <code><em>32000000</em></code>.</p>
# MAGIC <p>In the second example, after pushing the button <code>1000</code> times, <code>4250</code> low pulses and <code>2750</code> high pulses are sent. Multiplying these together gives <code><em>11687500</em></code>.</p>
# MAGIC <p>Consult your module configuration; determine the number of low pulses and high pulses that would be sent after pushing the button <code>1000</code> times, waiting for all pulses to be fully handled after each push of the button. <em>What do you get if you multiply the total number of low pulses sent by the total number of high pulses sent?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''%jr -> mq, xn
%zl -> tz, cm
&lh -> nr
%hx -> jx, tz
%cm -> tz, ls
&fk -> nr
broadcaster -> sj, pf, kh, cn
%gz -> mq, lq
%gb -> xf, kr
%zc -> rq
%ln -> qj, xf
%gq -> pp
%fb -> xf
%pf -> tg, nv
%bc -> cf
&tz -> cn, fk, ls
%cq -> fb, xf
%rq -> tg, dx
%km -> gq
&mq -> gq, xn, fv, km, lh, xv, sj
%zp -> mq, xv
%jx -> tz, np
&tg -> mm, rp, zc, pf, bc
%cv -> sq, xf
%nv -> ht, tg
%sq -> gb
%kr -> ln
%dk -> cv
%xn -> zp
%sx -> xf, cq
%zt -> tz, fq
%dx -> tg, qn
&ff -> nr
%bn -> hx, tz
%fj -> zt, tz
%ht -> rr, tg
%fq -> tz, bn
%kh -> dk, xf
%sj -> mq, fv
%vm -> zl, tz
&mm -> nr
%rp -> bc
%fh -> sx
%ls -> fj
%xz -> mq, gz
%fv -> km
&nr -> rx
%lq -> mq
%xv -> xz
%cn -> tz, vm
%pp -> jr, mq
%hn -> tg
%qn -> hn, tg
%rr -> rp, tg
%cf -> tg, zc
%qj -> fh, xf
&xf -> sq, dk, fh, ff, kh, kr
%np -> tz
'''

# COMMAND ----------

import collections


def initialise_conjunction_inputs(m):
  conjunction_inputs = collections.defaultdict(dict)
  for name, parts in m.items():
    for part in parts:
      if f'&{part}' in m:
        conjunction_inputs[f'&{part}'][name] = 'low'
  return conjunction_inputs


def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()
    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      if signal == 'high':
        continue

      if cur in on_flipflops:
        on_flipflops.remove(cur)
      else:
        on_flipflops.add(cur)
      
      output = 'high' if cur in on_flipflops else 'low'
    
    if cur[0] == '&':
      conjunction_inputs[cur][parent] = signal
      output = 'low' if all(sig == 'high' for sig in conjunction_inputs[cur].values()) else 'high'
      
    for nxt in m[cur]:
      if f'%{nxt}' in m:
        nxt = f'%{nxt}'
      else:
        nxt = f'&{nxt}'
      q.append((nxt, output, cur))


m = {name: tuple(parts.split(', ')) for name, parts in [line.split(' -> ') for line in inp.splitlines()]}
conjunction_inputs = initialise_conjunction_inputs(m)

pulses = {'high': 0, 'low': 0}
on_flipflops = set()
for _ in range(1000):
  push_button()

answer = pulses['low'] * pulses['high']
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The final machine responsible for moving the sand down to Island Island has a module attached named <code>rx</code>. The machine turns on when a <em>single low pulse</em> is sent to <code>rx</code>.</p>
# MAGIC <p>Reset all modules to their default states. Waiting for all pulses to be fully handled after each button press, <em>what is the fewest number of button presses required to deliver a single low pulse to the module named <code>rx</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

# Export it to Draw.io
#   Arrange -> Insert -> Advanced -> From Text... -> Diagram
#   Arrange -> Layout -> Vertical Tree
for name, parts in m.items():
  for part in parts:
    if f'&{part}' in m:
      part = f'&{part}'
    if f'%{part}' in m:
      part = f'%{part}'
    print(f'{name}->{part}')

# COMMAND ----------

import collections
import itertools
import math


def push_button():
  q = collections.deque([('broadcaster', 'low', 'button')])
  while q:
    cur, signal, parent = q.popleft()

    if cur in required_lows_periods and signal == 'low':
      required_lows_periods[cur] = presses

    pulses[signal] += 1

    if cur not in m:
      continue

    output = 'low'

    if cur[0] == '%':
      if signal == 'high':
        continue

      if cur in on_flipflops:
        on_flipflops.remove(cur)
      else:
        on_flipflops.add(cur)
      
      output = 'high' if cur in on_flipflops else 'low'
    
    if cur[0] == '&':
      conjunction_inputs[cur][parent] = signal
      output = 'low' if all(sig == 'high' for sig in conjunction_inputs[cur].values()) else 'high'
      
    for nxt in m[cur]:
      if f'%{nxt}' in m:
        nxt = f'%{nxt}'
      else:
        nxt = f'&{nxt}'
      q.append((nxt, output, cur))


conjunction_inputs = initialise_conjunction_inputs(m)
on_flipflops = set()

# From the graph, `rx` receives a low pulse when all of the inputs of `&nr` receive a low pulse.
# The required number of presses is the lowest common multiple of the periods
required_lows_periods = {name: None for name in conjunction_inputs['&nr']}

for presses in itertools.count(1):
  push_button()

  if all(required_lows_periods.values()):
   break

answer = math.lcm(*required_lows_periods.values())
print(answer)
