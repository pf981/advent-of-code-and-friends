package main

import "../../utils"
import "core:fmt"
import "core:log"
import "core:strconv"
import "core:strings"

Instruction :: struct {
	turn:   enum {
		Left,
		Right,
	},
	amount: int,
}

parse :: proc(input: string) -> []Instruction {
	instructions: [dynamic]Instruction
	for line in strings.split_lines(
		strings.trim_right(input, "\n"),
		allocator = context.temp_allocator,
	) {
		amount, ok := strconv.parse_int(line[1:])
		if !ok {
			panic(fmt.tprintfln("Unable to process line: %s", line))
		}

		append(&instructions, Instruction{.Right if line[0] == 'R' else .Left, amount})
	}
	return instructions[:]
}

part1 :: proc(input: []Instruction) -> int {
	result := 0
	p := 50
	for inst in input {
		fmt.println(inst)
		for _ in 0 ..< inst.amount {
			p = (p + (1 if inst.turn == .Right else -1)) % 100
		}
		if p == 0 {
			result += 1
		}
	}
	return result
}

part2 :: proc(input: []Instruction) -> int {
	result := 0
	p := 50
	for inst in input {
		fmt.println(inst)
		for _ in 0 ..< inst.amount {
			p = (p + (1 if inst.turn == .Right else -1)) % 100
			if p == 0 {
				result += 1
			}
		}
	}
	return result
}

main :: proc() {
	utils.run(year = 2025, day = 1, parse = parse, part1 = part1, part2 = part2)
}
