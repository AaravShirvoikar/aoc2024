use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::fs;

pub fn part1() {
    let input = fs::read_to_string("./inputs/input01").expect("no file");
    let (l1, l2): (Vec<i32>, Vec<i32>) = input
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip();

    let mut h1: BinaryHeap<Reverse<i32>> = l1.into_iter().map(Reverse).collect();
    let mut h2: BinaryHeap<Reverse<i32>> = l2.into_iter().map(Reverse).collect();

    let mut sum = 0;
    while h1.len() != 0 {
        let Reverse(n1) = h1.pop().unwrap();
        let Reverse(n2) = h2.pop().unwrap();
        sum += (n1 - n2).abs();
    }

    println!("{}", sum);
}

pub fn part2() {
    let input = fs::read_to_string("./inputs/input01").expect("no file");
    let (l1, l2): (Vec<i32>, Vec<i32>) = input
        .lines()
        .map(|line| {
            let mut nums = line.split_whitespace().map(|n| n.parse::<i32>().unwrap());
            (nums.next().unwrap(), nums.next().unwrap())
        })
        .unzip();

    let counts = l2.iter().fold(HashMap::new(), |mut acc, &item| {
        *acc.entry(item).or_insert(0) += 1;
        acc
    });

    let sum: i32 = l1.iter().map(|n| n * counts.get(n).unwrap_or(&0)).sum();
    println!("{}", sum);
}
