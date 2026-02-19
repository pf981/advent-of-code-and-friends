package utils

Solution :: struct($T: typeid, $Out: typeid) where Out == int || Out == string {
	year:  int,
	day:   int,
	parse: proc(input: string) -> T,
	part1: proc(input: T) -> Out,
	part2: proc(input: T) -> Out,
}
