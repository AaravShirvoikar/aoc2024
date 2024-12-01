mod solves;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = args.get(1).expect("enter the day");

    println!("day {} solution:", day);
    match day.as_str() {
        "1a" => solves::day01::part1(),
        "1b" => solves::day01::part2(),
        _ => println!("invalid day"),
    }
}
