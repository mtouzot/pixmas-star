from gpiozero import LEDBoard, Device
from gpiozero.pins.rpigpio import RPiGPIOFactory


class Star(LEDBoard):
    def __init__(self, pwm=False, initial_value=False, pin_factory=None):
        # Use the RPiGPIOFactory if pin_factory is not provided
        if pin_factory is None:
            pin_factory = RPiGPIOFactory()  # Set to RPi.GPIO pin factory

        super(Star, self).__init__(
            outer=LEDBoard(
                A=8,B=7,C=12,D=21,E=20,F=16,G=26,H=19,I=13,J=6,K=5,L=11,M=9,
                N=10,O=22,P=27,Q=17,R=4,S=3,T=14,U=23,V=18,W=15,X=24,Y=25,
                pwm=pwm, initial_value=initial_value,
                _order=('A','B','C','D','E','F','G','H','I','J','K','L',
                        'M','N','O','P','Q','R','S','T','U','V','W','X','Y'),
                pin_factory=pin_factory),
            inner=2,
            pwm=pwm, initial_value=initial_value,
            _order=('inner','outer'),
            pin_factory=pin_factory
            )
        self.off()
