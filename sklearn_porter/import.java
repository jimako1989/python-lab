// $ javac import.java
// $ java -Xmx128M -Xms16M Brain 1 2 3 4
// $ 1
// $ java -Xmx128M -Xms16M Brain 1 2 32 500
// $ 2

class Brain {

    public static int predict(float[] atts) {
        if (atts.length != 4) { return -1; }
        int[] classes = new int[3];
            
        if (atts[3] <= 0.80000001192092896) {
            classes[0] = 50; 
            classes[1] = 0; 
            classes[2] = 0; 
        } else {
            if (atts[3] <= 1.75) {
                if (atts[2] <= 4.9499998092651367) {
                    if (atts[3] <= 1.6500000953674316) {
                        classes[0] = 0; 
                        classes[1] = 47; 
                        classes[2] = 0; 
                    } else {
                        classes[0] = 0; 
                        classes[1] = 0; 
                        classes[2] = 1; 
                    }
                } else {
                    if (atts[3] <= 1.5499999523162842) {
                        classes[0] = 0; 
                        classes[1] = 0; 
                        classes[2] = 3; 
                    } else {
                        if (atts[0] <= 6.9499998092651367) {
                            classes[0] = 0; 
                            classes[1] = 2; 
                            classes[2] = 0; 
                        } else {
                            classes[0] = 0; 
                            classes[1] = 0; 
                            classes[2] = 1; 
                        }
                    }
                }
            } else {
                if (atts[2] <= 4.8500003814697266) {
                    if (atts[0] <= 5.9499998092651367) {
                        classes[0] = 0; 
                        classes[1] = 1; 
                        classes[2] = 0; 
                    } else {
                        classes[0] = 0; 
                        classes[1] = 0; 
                        classes[2] = 2; 
                    }
                } else {
                    classes[0] = 0; 
                    classes[1] = 0; 
                    classes[2] = 43; 
                }
            }
        }
    
        int class_idx = 0;
        int class_val = classes[0];
        for (int i = 1; i < 3; i++) {
            if (classes[i] > class_val) {
                class_idx = i;
                class_val = classes[i];
            }
        }
        return class_idx;
    }

    public static void main(String[] args) {
        if (args.length == 4) {
            float[] atts = new float[args.length];
            for (int i = 0, l = args.length; i < l; i++) {
                atts[i] = Float.parseFloat(args[i]);
            }
            System.out.println(Brain.predict(atts));
        }
    }
}