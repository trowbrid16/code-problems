import java.util.*;

class Solution{

	public int solution(String s){
		Stack stack = new Stack();
		
		for(int i = 0; i < s.length(); i++)
		{
			// get ascii value of character at i
			int value = (int)s.charAt(i);

			switch(value) 
			{
				case 48:
				case 49:
				case 50:
				case 51:
				case 52:
				case 53:
				case 54:
				case 55:
				case 56:
				case 57:
					//push the numeric value to the stack
					stack.push(Character.getNumericValue(s.charAt(i)));
					break;

				case 42:
					//multiplication
					int a = (int)stack.pop();
					int b = (int)stack.pop();
					int mult = a * b;

					if(mult/4096 >= 1)
					{//overflow
						System.out.println("Overflow from multiplication.");
						return -1;
					}

					//push result
					stack.push(mult);
					System.out.println("Mult pushed\n" + stack);

					break;

				case 43:
					//addition
					int c = (int)stack.pop();
					int d = (int)stack.pop();
					int sum = c + d;

					if(sum/4096 >= 1)
					{
						System.out.println("Overflow from addition.");
						return -1;
					}

					stack.push(sum);
					System.out.println("Sum pushed\n" + stack);

					break;

				default:
					//unrecognized character
					System.out.println("unrecognized character " + value + " " + s.charAt(i));
					System.out.println(stack);
					return -1;
			}
		}

		return (int)stack.pop();
	}

	public static void main(String args[]){
		Solution sol = new Solution();


		String test = "99*9*9*9*9*";
		System.out.println(sol.solution(test));
	}
}




