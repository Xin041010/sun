from time import sleep
from loongpio import TonalBuzzer
from loongpio import PWMLED
from loongpio.pins import *
import random


led1 = PWMLED(PWM1)
led2 = PWMLED(PWM2)
led3 = PWMLED(PWM3)
buzzer = TonalBuzzer(PWM0)
note = 'G'
A = 15
B = 30
i = 0
while(i < 60):t = random.randint(0,40)
print(t)
if t <= A:
led2.value = 1
elif t > A and t <= B:
led1.value = 1
elif t > B:
led3.value = 1
buzzer.play(note)
sleep(1)
led1.value = 0
led2.value = 0
led3.value = 0
buzzer.stop()
i = i + 1



# 假设PWM模块的函数如下：
# pwm_export(pin) - 导出PWM引脚
# pwm_unexport(pin) - 取消导出PWM引脚
# pwm_enable(pin) - 启用PWM引脚
# pwm_config(pin, period, duty_cycle) - 配置PWM参数

# 这里定义PWM引脚和周期
pwm_pins = [0, 1, 2, 3]
period = 10000  # 周期



# 初始化PWM引脚
for pwm_pin in pwm_pins:
    pwm_export(pwm_pin)
    pwm_enable(pwm_pin)

try:
    for i in range(10):
        # 随机生成一个0到40之间的整数
        t = random.randint(0, 40)
        print(t)

        # 根据随机数配置PWM
        if t < 15:
            pwm_config(pwm_pins[2], period, 10000)  # 启用pwm2
        elif t >= 15 and t < 30:
            pwm_config(pwm_pins[1], period, 10000)  # 启用pwm1
        elif t >= 30:
            pwm_config(pwm_pins[3], period, 10000)  # 启用pwm3

        sleep(1)  # 等待1秒

finally:
    for pwm_pin in pwm_pins:
        pwm_unexport(pwm_pin)
    else:
        pwm_config(pwm_pins[2], period, 10000)
        pwm_config(pwm_pins[1], period, 10000)
        pwm_config(pwm_pins[3], period, 10000)


