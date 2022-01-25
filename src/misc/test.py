import motordriver
import encoder


enc = encoder.Encoder(pyb.Pin.board.PB6, pyb.Pin.board.PB7, 4)
enc2 = encoder.Encoder(pyb.Pin.board.PC6, pyb.Pin.board.PC7, 8)
driver = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    
driver.set_duty_cycle(100)

while True:
    enc.update()
    enc2.update()
    

    
    print('enc1:',enc.read(), 'enc2:',enc2.read())
