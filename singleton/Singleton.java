// Singleton restricts the creation of only one object of a given class

public class Singleton {
    public static Singleton uniqueInstance = null;

    // Constructor is made private so that when ever the class object is called it doesn't the constructor
    private Singleton() {
    }

    public static Singleton getInstance() {
        if(uniqueInstance == null) {
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

}