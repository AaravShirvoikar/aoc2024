use std::fs;

pub fn part1() {
    let input = fs::read_to_string("./inputs/input02").expect("no file");
    let reports: Vec<Vec<i32>> = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|n| n.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let sum = reports
        .iter()
        .filter(|r| {
            let mut inc = None;
            r.windows(2).all(|l| {
                if (l[1] - l[0]).abs() > 3 {
                    return false;
                }

                if l[1] > l[0] {
                    if let Some(false) = inc {
                        return false;
                    }
                    inc = Some(true);
                } else if l[1] < l[0] {
                    if let Some(true) = inc {
                        return false;
                    }
                    inc = Some(false);
                } else {
                    return false;
                }

                true
            })
        })
        .count();

    println!("{}", sum);
}

pub fn part2() {
    let input = fs::read_to_string("./inputs/input02").expect("no file");
    let reports: Vec<Vec<i32>> = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|n| n.parse::<i32>().unwrap())
                .collect()
        })
        .collect();

    let sum = reports
        .iter()
        .filter(|r| {
            let mut inc = None;
            let mut tol = false;
            r.windows(2).all(|l| {
                if (l[1] - l[0]).abs() > 3 {
                    if tol == true {
                        return false;
                    }
                    tol = true;
                }
                if l[1] > l[0] {
                    if let Some(false) = inc {
                        if tol == true {
                            return false;
                        }
                        tol = true;
                    }
                    inc = Some(true);
                } else if l[1] < l[0] {
                    if let Some(true) = inc {
                        if tol == true {
                            return false;
                        }
                        tol = true;
                    }
                    inc = Some(false);
                } else {
                    if tol == true {
                        return false;
                    }
                    tol = true;
                }
                true
            })
        })
        .count();

    println!("{}", sum);
}
