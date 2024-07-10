import serial
from loongpio import DHT11
from loongpio import GPIO
from loongpio import PWMLED
from time import sleep




def led():
    led1 = PWMLED(PWM0)
    ser = serial.Serial('/dev/ttyS1', 115200, timeout=5)
    print("open")
    sleep(3)
    i = 0
    while (i < 6):
        # 检查串行端口是否有数据
        if ser.in_waiting > 0:
            try:
                # 读取数据
                data = ser.readline().decode('utf-8').strip()
                print(data)
                if data == 'turn on':
                    led1.value = 1  # LED全亮
                elif data == 'turn off':
                    led1.value = 0  # LED关闭
                elif data == 'turn flash':
                    # 闪烁LED
                    for _ in range(10):  # 假设闪烁10次
                        led1.value = 1
                        sleep(0.5)
                        led1.value = 0
                        sleep(0.5)
                        break
                        break
                        sleep(1)
                        i=i+1
                        ser.close()
            except serial.SerialException as e:
                print("Serial error:", e)

# LED


def gpio():
    gpio1 = GPIO(GPIO39)
    while True:
        gpio1.value = 0  # 初始状态设置为关闭蜂鸣器
        # 检查是否满足报警条件
        if tem >= 20 or hum >= 70:
            for _ in range(10):  # 假设报警持续10秒
                gpio1.value = 1  # 打开蜂鸣器
                sleep(0.5)  # 蜂鸣器响0.5秒
                gpio1.value = 0  # 关闭蜂鸣器
                sleep(0.5)  # 等待0.5秒再次响起
        else:
            sleep(1)  # 如果不满足条件，等待1秒再次检查

#蜂鸣器






if __name__ == "__main__":
    sensor1 = DHT11(4)
    while True:
        tem = sensor1.getTemperature()
        hum = sensor1.getHumidity()
        print('当前温度为' + str(tem) + '摄氏度')
        print('当前的相对湿度为' + str(hum) + '%')
        sleep(5)
        led()
        gpio()

    #蜂鸣器