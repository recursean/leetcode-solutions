class Pr13 {
    public int romanToInt(String s) {
        int num = 0;
        char prev = ' ';

        for(char c: s.toCharArray()) {
            if(c == 'I') {
                num += 1;
            }

            else if(c == 'V') {
                if(prev == 'I') {
                    // IV = 4, but already added 1
                    num += 3;
                }

                else {
                    num += 5;
                }
            }

            else if(c == 'X') {
                if(prev == 'I') {
                    // IX = 9, but already added 1
                    num += 8;
                }

                else {
                    num += 10;
                }
            }

            else if(c == 'L') {
                if(prev == 'X') {
                    // XL = 40, but already added 10
                    num += 30;
                }

                else {
                    num += 50;
                }
            }

            else if(c == 'C') {
                if(prev == 'X') {
                    // XC = 90, but already added 10
                    num += 80;
                }

                else {
                    num += 100;
                }
            }

            else if(c == 'D') {
                if(prev == 'C') {
                    // CD = 400, but already added 100
                    num += 300;
                }

                else {
                    num += 500;
                }
            }

            else if(c == 'M') {
                if(prev == 'C') {
                    // CM = 900, but already added 100
                    num += 800;
                }

                else {
                    num += 1000;
                }
            }

            prev = c;
        }

        return num;
    }

    public static void main(String[] args) {
        System.out.println(new Pr13().romanToInt("MCMXCIV"));
    }
}