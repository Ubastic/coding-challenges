let solution = (s, m) => s.replace(RegExp(`\\s*[${m.join("")}].*`, 'gm'),"",);