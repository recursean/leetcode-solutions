class Pr1844 {
	public String replaceDigits(String s) {
		char[] c = s.toCharArray();
		for(int i = 1; i < c.length; i+=2) {
			if(i < c.length)
				c[i] = shift(c[i-1], Character.getNumericValue(c[i]));
		}
		return new String(c);
	}
	
	char shift(char c, int n) {
		return (char)((int)c + n);
	}
	
	public static void main(String[] args) {
		Pr1844 p = new Pr1844();
		if(args.length > 0) {
			System.out.println(args[0]);
			System.out.println(p.replaceDigits(args[0]));
		}
	}
}
