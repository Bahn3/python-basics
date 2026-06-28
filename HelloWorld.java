public class HelloWorld {
    public static void addNumbers(int num1, int num2){ 
        return num1 + num2;
    }
    public static void main(String[] args){
        int result = addNumbers(7,20);
        System.out.println("The result is: " + result);
    }
}