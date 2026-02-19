package main

import "core:c/libc"
import "core:fmt"
import "core:log"
import "core:mem"
import "core:os"
import "core:time"

import "solutions"
import "utils"

solns := [1]utils.Solution{solutions.y2025_d01}

timer :: proc(f: proc(input: string) -> string, input: string) -> (string, f64) {
	stopwatch: time.Stopwatch

	time.stopwatch_reset(&stopwatch)
	time.stopwatch_start(&stopwatch)

	result := f(input)

	time.stopwatch_stop(&stopwatch)
	ms := time.duration_milliseconds(time.stopwatch_duration(stopwatch))
	return result, ms
}

run :: proc(soln: Solution) {
	fmt.printfln("\nRunning solution year=%d day=%d", soln.year, soln.day)

	filename := fmt.tprintf("input/%d_%02d.txt", soln.year, soln.day)
	input, ok := os.read_entire_file(filename, context.temp_allocator)
	if !ok {
		log.error(fmt.tprintfln("Unable to read file: %s", filename))
		free_all(context.temp_allocator)
		return
	}

	parsed_input, parse_time_ms := timer(soln.funcs[.Parse], string(input))
	part_1_result, part_1_time_ms := timer(soln.funcs[.Part1], parsed_input)
	part_2_result, part_2_time_ms := timer(soln.funcs[.Part2], parsed_input)

	fmt.printfln("Parsed input in %f ms", parse_time_ms)
	fmt.printfln("Part 1: %s (took %f ms)", part_1_result, part_1_time_ms)
	fmt.printfln("Part 2: %s (took %f ms)", part_2_result, part_2_time_ms)

	free_all(context.temp_allocator)
}

main :: proc() {
	context.logger = log.create_console_logger()

	default_allocator := context.allocator
	tracking_allocator: mem.Tracking_Allocator
	mem.tracking_allocator_init(&tracking_allocator, default_allocator)
	context.allocator = mem.tracking_allocator(&tracking_allocator)
	defer {
		if len(tracking_allocator.allocation_map) > 0 {
			log.error(
				fmt.tprintf(
					"=== %v allocations not freed: ===\n",
					len(tracking_allocator.allocation_map),
				),
			)
			for _, entry in tracking_allocator.allocation_map {
				log.error(fmt.tprintf("- %v bytes @ %v\n", entry.size, entry.location))
			}
		}
		mem.tracking_allocator_destroy(&tracking_allocator)
	}

	for soln in solns {
		run(soln)
	}
}
