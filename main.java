//Single & Multilevel Inheritance

class Animal {
    protected String name;

    public void eat() {
        System.out.println(name + " is eating...");
    }
}

class Dog extends Animal {
    public Dog(String name) {
        this.name = name;
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy");
        dog.eat();
    }
}