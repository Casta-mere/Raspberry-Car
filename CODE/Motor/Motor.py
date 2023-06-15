#!/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

# 对使用的GPIO端口进行初始化
motor_a_in1_pin = 26
motor_a_in2_pin = 19
motor_b_in1_pin = 13
motor_b_in2_pin = 6

motor_c_in1_pin = 21
motor_c_in2_pin = 20
motor_d_in1_pin = 16
motor_d_in2_pin = 12

GPIO.setwarnings(False)  # 模块内置功能，一般要加上
GPIO.setmode(GPIO.BCM)  # 设置GPIO引脚为BCM编码模式
GPIO.setup(motor_a_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_a_in2_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_b_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_b_in2_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_c_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_c_in2_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_d_in1_pin, GPIO.OUT)  # 设置该端口为输出模式
GPIO.setup(motor_d_in2_pin, GPIO.OUT)  # 设置该端口为输出模式



count = 0
while True:
    time.sleep(1)
    GPIO.output(motor_a_in1_pin, GPIO.HIGH)
    GPIO.output(motor_a_in2_pin, GPIO.LOW)
    GPIO.output(motor_b_in1_pin, GPIO.HIGH)
    GPIO.output(motor_b_in2_pin, GPIO.LOW)
    GPIO.output(motor_c_in1_pin, GPIO.HIGH)
    GPIO.output(motor_c_in2_pin, GPIO.LOW)
    GPIO.output(motor_d_in1_pin, GPIO.HIGH)
    GPIO.output(motor_d_in2_pin, GPIO.LOW)


    time.sleep(1)
    GPIO.output(motor_a_in1_pin, GPIO.LOW)
    GPIO.output(motor_a_in2_pin, GPIO.HIGH)
    GPIO.output(motor_b_in1_pin, GPIO.LOW)
    GPIO.output(motor_b_in2_pin, GPIO.HIGH)
    GPIO.output(motor_c_in1_pin, GPIO.LOW)
    GPIO.output(motor_c_in2_pin, GPIO.HIGH)
    GPIO.output(motor_d_in1_pin, GPIO.LOW)
    GPIO.output(motor_d_in2_pin, GPIO.HIGH)