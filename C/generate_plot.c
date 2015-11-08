solve;

printf '' > 'transp2.dat';
for { i in I  } {
  for { j in J } {
    printf '%i "%s"', sum{k in I: k < i} 1, i >> 'transp2.dat';
    printf ' %i "%s"', sum{l in J: l < j} 1, j >> 'transp2.dat';
    printf ' %f', x[i,j] >> 'transp2.dat';
    printf '\n' >> 'transp2.dat';

    printf '%i "%s"', sum{k in I: k < i} 1, i >> 'transp2.dat';
    printf ' %i "%s"', sum{l in J: l <= j} 1, '' >> 'transp2.dat';
    printf ' %f', x[i,j] >> 'transp2.dat';
    printf '\n' >> 'transp2.dat';
    }
    printf '\n' >> 'transp2.dat';
  for { j in J } {
    printf '%i "%s"', sum{k in I: k <= i} 1, '' >> 'transp2.dat';
    printf ' %i "%s"', sum{l in J: l < j} 1, j >> 'transp2.dat';
    printf ' %f', x[i,j] >> 'transp2.dat';
    printf '\n' >> 'transp2.dat';

    printf '%i "%s"', sum{k in I: k <= i} 1, '' >> 'transp2.dat';
    printf ' %i "%s"', sum{l in J: l <= j} 1, '' >> 'transp2.dat';
    printf ' %f', x[i,j] >> 'transp2.dat';
    printf '\n' >> 'transp2.dat';
    }
    printf '\n' >> 'transp2.dat';
  }
data;

set I := San-Diego Seattle;

set J := Chicago New-York Topeka;
