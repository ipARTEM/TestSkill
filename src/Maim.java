public class Maim
{
    public static void main (String[] args) throws java.lang.Exception
    {
        System.out.println("Система расчёта штрафов");

        System.out.println(76+54*279);

        int carSpeed=225;

        int fineFor20to40=500;
        int fineFor40to60=1000;
        int fineFor60to80=2000;
        int fineFor80andMore=5000;

        int townSpeed=60;

        int overSpeed=carSpeed-townSpeed;

        System.out.println(carSpeed);

        if(overSpeed<20)
        {
            System.out.println("Скорость не превышена или превышена незначительно");
        }

        else if(overSpeed>=20&&overSpeed<40)
        {
            System.out.println("Штраф: "+fineFor20to40);
        }

        else	if(overSpeed>=40&&overSpeed<60)
        {
            System.out.println("Штраф: "+fineFor40to60);
        }

        else	if(overSpeed>=60&&overSpeed<80)
        {
            System.out.println("Штраф: "+fineFor60to80);
        }

        else	if(overSpeed>=80)
        {
            System.out.println("Штраф: "+fineFor80andMore);
        }
    }
}
