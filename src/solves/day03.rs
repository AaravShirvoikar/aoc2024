use regex::Regex;
use std::fs;

pub fn part1() {
    let input = fs::read_to_string("./inputs/input03").expect("no file");
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let sum: i32 = re
        .captures_iter(&input)
        .map(|c| {
            let x = c[1].parse::<i32>().unwrap_or(0);
            let y = c[2].parse::<i32>().unwrap_or(0);
            x * y
        })
        .sum();

    println!("{}", sum);
}

pub fn part2() {
    let input = fs::read_to_string("./inputs/input03").expect("no file");
    let re = Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)").unwrap();

    let mut mul = true;
    let sum: i32 = re
        .captures_iter(&input)
        .filter_map(|c| match c.get(0).map(|m| m.as_str()) {
            Some("do()") => {
                mul = true;
                None
            }
            Some("don't()") => {
                mul = false;
                None
            }
            Some(_) if mul => {
                let x = c[1].parse::<i32>().unwrap_or(0);
                let y = c[2].parse::<i32>().unwrap_or(0);
                Some(x * y)
            }
            _ => None,
        })
        .sum();

    println!("{}", sum);
}
