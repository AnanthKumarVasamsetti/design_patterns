class Knife {
    String name;

    Knife() {
        this.name = null;
    }

    public Knife SteakKnife() {
        Knife knife = new Knife();
        knife.name = "Steak knife";
        return knife;
    }
    public Knife ChefKnife() {
        Knife knife = new Knife();
        knife.name = "Chef knife";
        return knife;
    }

    public void sharpen() {
        System.out.println("Sharpening knife");
    }

    public void polish() {
        System.out.println("Polishing knife");
    }

    public void pack() {
        System.out.println("Packing knife");
    }
}

class KnifeFactory  extends Knife {
    public Knife createKnife(String name) {
        Knife knife = null;
        if(name.equals("steak")) {
            knife = SteakKnife();
        } 
        else if(name.equals("chef")) {
            knife = ChefKnife();
        }

        System.out.println("Created "+knife.name);
        return knife;
    }
}

 class KnifeStore {
     KnifeFactory factory;
     Knife knife;

     KnifeStore(KnifeFactory factory) {
         this.factory = factory;
     }

     public Knife orderKnife(String name) {
         Knife newKnife;

         newKnife = factory.createKnife(name);

         newKnife.sharpen();
         newKnife.polish();
         newKnife.pack();

         return knife;

     }
 }

 public class Factory {
     public static void main(String[] args) {
         KnifeStore store = new KnifeStore(new KnifeFactory());
         store.orderKnife("steak");
     }
 }