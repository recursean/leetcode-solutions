class Pr12 {
    public String intToRoman(int num) {
        String roman = "";
        
        while(num > 0) {
            if(num / 1000 > 0) {
                for(int i = 0; i < num / 1000; i++) {
                    roman += "M";
                }
                num -= 1000 * (num / 1000);
            }
            else if(num / 900 > 0) {
                for(int i = 0; i < num / 900; i++) {
                    roman += "CM";
                }
                num -= 900 * (num / 900);
            }
            else if(num / 500 > 0) {
                for(int i = 0; i < num / 500; i++) {
                    roman += "D";
                }
                num -= 500 * (num / 500);
            }
            else if(num / 400 > 0) {
                for(int i = 0; i < num / 400; i++) {
                    roman += "CD";
                }
                num -= 400 * (num / 400);
            }
            else if(num / 100 > 0) {
                for(int i = 0; i < num / 100; i++) {
                    roman += "C";
                }
                num -= 100 * (num / 100);
            }
            else if(num / 90 > 0) {
                for(int i = 0; i < num / 90; i++) {
                    roman += "XC";
                }
                num -= 90 * (num / 90);
            }
            else if(num / 50 > 0) {
                for(int i = 0; i < num / 50; i++) {
                    roman += "L";
                }
                num -= 50 * (num / 50);
            }
            else if(num / 40 > 0) {
                for(int i = 0; i < num / 40; i++) {
                    roman += "XL";
                }
                num -= 40 * (num / 40);
            }
            else if(num / 10 > 0) {
                for(int i = 0; i < num / 10; i++) {
                    roman += "X";
                }
                num -= 10 * (num / 10);
            }
            else if(num / 9 > 0) {
                for(int i = 0; i < num / 9; i++) {
                    roman += "IX";
                }
                num -= 9 * (num / 9);
            }
            else if(num / 5 > 0) {
                for(int i = 0; i < num / 5; i++) {
                    roman += "V";
                }
                num -= 5 * (num / 5);
            }
            else if(num / 4 > 0) {
                for(int i = 0; i < num / 4; i++) {
                    roman += "IV";
                }
                num -= 4 * (num / 4);
            }
            else if(num / 1 > 0) {
                for(int i = 0; i < num / 1; i++) {
                    roman += "I";
                }
                num -= 1 * (num / 1);
            }
        }

        return roman;
    }

    public static void main(String[] args) {
        System.out.println(new Pr12().intToRoman(1994));
    }
}