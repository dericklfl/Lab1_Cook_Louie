from motordriver import MotorDriver

def main():
    driver = MotorDriver(pyb.Pin.board.PA10, pyb.Pin.board.PB4, pyb.Pin.board.PB5, 3)
    driver.set_duty_cycle(100)
    
if __name__ == '__main__':
    main()   