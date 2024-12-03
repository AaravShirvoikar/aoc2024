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
    let re1 = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();
    let re2 = Regex::new(r"do\(\)").unwrap();
    let re3 = Regex::new(r"don't\(\)").unwrap();

    let mut enabled = true;
    let sum: i32 = re1.captures_iter(&input).fold(0, |acc, c| {
        let p = c.get(0).unwrap().start();
        let p1 = re2.find_iter(&input).filter(|m| m.start() < p).last();
        let p2 = re3.find_iter(&input).filter(|m| m.start() < p).last();

        enabled = match (p1, p2) {
            (Some(re2), Some(re3)) => re2.start() > re3.start(),
            (Some(_), None) => true,
            (None, Some(_)) => false,
            _ => true,
        };

        if enabled {
            let x = c[1].parse::<i32>().unwrap_or(0);
            let y = c[2].parse::<i32>().unwrap_or(0);
            acc + (x * y)
        } else {
            acc
        }
    });

    println!("{}", sum);
}
