library(tidyverse)



ip_register <- read_lines(input, n_max = 1) %>% str_extract("\\d+") %>% parse_integer()
ip_register

instructions <-
  read_lines(input, skip = 1) %>%
  str_split(" ") %>%
  map_dfr(set_names, c("op", "a", "b", "output_register")) %>%
  mutate_at(vars(-op), parse_integer)
instructions

Rcpp::cppFunction('
std::vector<int64_t> find_halt_values() {
  std::set<int64_t> halt_values_s;
  std::vector<int64_t> halt_values;

  int64_t result;
  int r0 = 0, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
K:	r4 = r3 | 65536;
	r3 = 1107552;
J:	r5 = r4 & 255;
	r3 += r5;
	r3 &= 16777215;
	r3 *= 65899;
	r3 &= 16777215;
	;
	if (256 > r4) goto D;
	;
B:	;
C:	r5 = 0;
I:	r1 = r5 + 1;
	r1 *= 256;
	;
	if (r1 > r4) goto G;
	;
E:	;
F:	r5++;
	goto I;
G:	r4 = r5;
	goto J;
D:	;

    // START NEW CODE
    if (halt_values_s.find(r3) != halt_values_s.end()) return halt_values; 
	halt_values_s.insert(r3);
	halt_values.push_back(r3);
    // END NEW CODE

	goto K;
}
')

halt_values <- find_halt_values()
answer <- first(halt_values)
answer

answer <- last(halt_values)
answer
